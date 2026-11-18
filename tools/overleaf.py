"""The thesis on Overleaf: the project holds src/thesis/ at its root and nothing else.

    python tools/overleaf.py pull    # Overleaf's edits since the last sync, applied under src/thesis/ and committed
    python tools/overleaf.py push    # src/thesis/ as of HEAD, committed onto Overleaf's tip and pushed

A push commits src/thesis/'s tree on top of Overleaf's own history and records the commit
it came from (Repository-Commit: <sha>), so the repository's tools, environment and notes
never reach Overleaf. A pull takes the difference between the last state of Overleaf this
repository has (its last push, or its last pull) and Overleaf's tip, applies it under
src/thesis/ with a three-way merge, and commits it as "Pull thesis edits from Overleaf
(<sha>)". A push refuses while Overleaf holds edits not pulled yet. sync.sh and sync.ps1
call both; run them by hand only to sync Overleaf alone.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "src/thesis"
REMOTE, BRANCH = "overleaf", "main"
TRAILER = "Repository-Commit"
PULLED = re.compile(r"Pull thesis edits from Overleaf \(([0-9a-f]{40})\)")


def git(*a, input=None):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, input=input)
    if r.returncode:
        sys.exit(f"git {' '.join(a)} failed:\n{r.stderr.decode(errors='replace')}")
    return r.stdout.decode(errors="replace").strip()


def is_ancestor(a, b):
    return subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", a, b]).returncode == 0


def synced(tip):
    """The newest Overleaf commit this repository already has: its last push or its last pull.
    None while Overleaf still carries the old whole-repository layout."""
    have = []
    for sha, body in (c.split("\x00", 1) for c in git("log", "--format=%H%x00%B%x01", tip).split("\x01") if "\x00" in c):
        if f"{TRAILER}:" in body:
            have.append(sha.strip())
            break
    have += [s for s in PULLED.findall(git("log", "--format=%B", "HEAD")) if subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "-e", s], capture_output=True).returncode == 0 and is_ancestor(s, tip)]
    return max(have, key=lambda s: int(git("rev-list", "--count", s)), default=None)


def pull():
    git("fetch", "-q", REMOTE)
    tip = git("rev-parse", f"{REMOTE}/{BRANCH}")
    base = synced(tip)
    if base is None:
        if is_ancestor(tip, "HEAD"):            # the old layout, already merged by the old sync
            print("overleaf: nothing to pull (old layout, already merged)")
            return
        sys.exit("overleaf: Overleaf has edits in the old whole-repository layout; merge them by hand first")
    if base == tip:
        print("overleaf: nothing to pull")
        return
    patch = subprocess.run(["git", "-C", str(ROOT), "diff", "--binary", base, tip], capture_output=True).stdout
    if patch.strip():
        r = subprocess.run(["git", "-C", str(ROOT), "apply", "--3way", "--index", f"--directory={PREFIX}"],
                           input=patch, capture_output=True)
        if r.returncode:
            sys.exit("overleaf: Overleaf's edits did not apply cleanly; resolve the conflicts under "
                     f"{PREFIX}/, commit with the message 'Pull thesis edits from Overleaf ({tip})', then sync again\n"
                     + r.stderr.decode(errors="replace"))
    git("commit", "-q", "--allow-empty", "-m", f"Pull thesis edits from Overleaf ({tip})")
    print(f"overleaf: pulled {len(git('diff', '--name-only', base, tip).splitlines())} file(s), committed")


def push():
    git("fetch", "-q", REMOTE)
    tip = git("rev-parse", f"{REMOTE}/{BRANCH}")
    base = synced(tip)
    if base is None and not is_ancestor(tip, "HEAD"):
        sys.exit("overleaf: Overleaf has edits not merged yet; pull first")
    if base is not None and base != tip:
        sys.exit("overleaf: Overleaf has edits since the last sync; pull first")
    tree = git("rev-parse", f"HEAD:{PREFIX}")
    if tree == git("rev-parse", f"{tip}^{{tree}}"):
        print("overleaf: already up to date")
        return
    head = git("rev-parse", "HEAD")
    msg = f"{git('log', '-1', '--format=%s', head)}\n\n{TRAILER}: {head}\n"
    commit = git("commit-tree", tree, "-p", tip, "-m", msg)
    git("push", "-q", REMOTE, f"{commit}:refs/heads/{BRANCH}")
    print(f"overleaf: pushed {PREFIX}/ of {head[:7]} as {commit[:7]}")


if __name__ == "__main__":
    {"pull": pull, "push": push}[sys.argv[1]]()
