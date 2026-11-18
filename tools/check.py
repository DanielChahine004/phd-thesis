"""The thesis held to its writing rules wherever a pattern can decide (docs/writing-rules.md
and its thesis annex, docs/writing-terms.md); everything else is for a reader.

    pixi run check        # after pixi run build; exits 1 if anything is found

- the build log: no undefined reference or citation, no line more than 1 pt into the margin;
- units: a number joined to its unit by a units.tex shorthand (\\keV{511}), \\, or ~, never
  a plain space;
- R10: no em-dash in prose;
- the rules: docs/writing-rules.md is the pinned study-kit's core;
- S1: each abbreviation in acronyms.tex spelled out at its first use in every chapter,
  "positron emission tomography (PET)"; software names in NAMES are exempt.

Comments, \\topics{...} plans and math are not prose and are skipped.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THESIS = ROOT / "src" / "thesis"
LOG = ROOT / "build" / "thesis" / "main.log"
NAMES = {"GATE", "STIR", "CASToR", "GEANT", "Geant4", "SIRF", "NiftyPET", "QETIR", "OSEM"}
UNIT = re.compile(r"(?<![{\d.])\d*\.?\d( ?)(mm|cm|nm|um|m|ps|ns|keV|MeV|GeV|eV|kHz|MHz|GHz|Hz|MBq|Bq|mSv|Sv)(?!\w)")


def strip_group(text, command):
    """text with every \\command{...} removed, nested braces included."""
    out, i = [], 0
    while True:
        j = text.find(command + "{", i)
        if j < 0:
            return "".join(out) + text[i:]
        out.append(text[i:j])
        depth, k = 0, j + len(command)
        while k < len(text):
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            k += 1
            if depth == 0:
                break
        i = k


def prose(tex):
    """One string per source line: no comments, plans, citations, references or math."""
    tex = re.sub(r"(?<!\\)%[^\n]*", "", tex)
    tex = strip_group(tex, "\\topics")
    tex = re.sub(r"\\(?:cite[a-z]*|ref|eqref|autoref|label|needcite|input|includegraphics|begin|end)\*?"
                 r"(?:\[[^\]]*\])*\{[^}]*\}", " ", tex)
    tex = re.sub(r"\$[^$]*\$", " ", tex)
    return tex


def build_log():
    if not LOG.exists():
        return ["build log: none; run `pixi run build` first"]
    log = LOG.read_text(errors="replace")
    bad = sorted(set(re.findall(r"LaTeX Warning: (?:Reference|Citation) `[^']+' on page \d+ undefined", log)))
    bad += [f"{float(w):.1f} pt into the margin {where}" for w, where in
            re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\) (in [^\n]*)", log) if float(w) > 1.0]
    return [f"build log: {b}" for b in bad]


def chapters():
    return sorted((THESIS / "chapters").glob("*.tex"))


def units_and_dashes():
    bad = []
    for f in chapters():
        for i, line in enumerate(prose(f.read_text(encoding="utf-8-sig")).split("\n"), 1):
            for m in UNIT.finditer(line):
                bad.append(f"{f.name}:{i}: unit not joined to its number: {line[max(0, m.start() - 20):m.end()].strip()}")
            if "---" in line:
                bad.append(f"{f.name}:{i}: em-dash (R10): {line[max(0, line.index('---') - 30):line.index('---') + 30].strip()}")
    return bad


def abbreviations():
    acr = re.findall(r"\\acr\{([^}]+)\}", (THESIS / "acronyms.tex").read_text(encoding="utf-8-sig"))
    acr = sorted({a for a in acr if a not in NAMES and re.fullmatch(r"[\w-]+", a)})
    bad = []
    for f in chapters():
        text = re.sub(r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\{[^}]*\}", " ",
                      prose(f.read_text(encoding="utf-8-sig")))   # spelled out in the text, not the heading
        for a in acr:
            m = re.search(rf"(?<![\w-]){re.escape(a)}s?(?![\w])", text)
            if m and text[m.start() - 1:m.start()] != "(":
                line = text.count("\n", 0, m.start()) + 1
                bad.append(f"{f.name}:{line}: {a} used before it is spelled out in this chapter (S1)")
    return bad


def rules_copy():
    """docs/writing-rules.md is the installed study-kit's core; `pixi run kit-update` refreshes it."""
    try:
        from studykit import rules
    except ImportError:
        return ["rules: study-kit is not installed here (pixi install)"]
    copy = ROOT / "docs" / "writing-rules.md"
    same = copy.exists() and copy.read_text(encoding="utf-8").replace("\r\n", "\n") == rules.core()
    return [] if same else ["rules: docs/writing-rules.md is not the kit's core: run `pixi run kit-update`"]


if __name__ == "__main__":
    found = build_log() + units_and_dashes() + abbreviations() + rules_copy()
    print("\n".join(found) if found else "check: clean")
    sys.exit(1 if found else 0)
