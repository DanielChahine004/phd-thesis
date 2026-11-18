# Writing terms for the thesis

The thesis annex to `writing-rules.md` (the portable core shared with the study
papers), keyed by rule id. A reviewer reads both. Where this file says a rule
reads differently for a thesis, this file wins.

## The venue

A PhD thesis at the University of Technology Sydney, read by examiners who know
PET instrumentation but read each chapter on its own.

## Rules that read differently in a thesis

R1. "This thesis" and "this chapter" may be the subject of the sentence that states
what the thesis or the chapter does, and nowhere else. No "we" or "our".

R2. The introduction ends with an outline of the chapters, and each chapter opens
with one paragraph saying what it covers and why. Examiners expect both. Anywhere
else a sentence whose only content is what follows is removed.

R8. The literature review (Chapter 2) may explain the background the thesis builds
on, for an examiner from a neighbouring field; it does not explain what every PET
physicist knows (the Cramér-Rao bound in general terms, Poisson statistics, how a
photomultiplier works) at more length than the argument needs.

E1, E4. The thesis has no \fact mechanism yet. A number from the literature carries
its citation; a missing source is marked `\needcite{...}`, never left bare. A number
from the thesis's own work will come from its study repository when that chapter is
written.

R10. No em-dashes in prose. This replaces the old house style that set `---`.

S1. Abbreviations are listed in `src/thesis/acronyms.tex` and printed in the front
matter, and each is still spelled out at its first use in every chapter, since
examiners read chapters on their own. Software names (GATE, Geant4, STIR,
CASToR) are named, not expanded.

Units. `\keV{511}` and the other `units.tex` shorthands, or a number joined to its
unit by `\,` or `~`; never a plain space.

## D1 -- terms that must be defined at first use

    monolithic detector, depth of interaction (DOI), time of flight (TOF),
    coincidence time resolution (CTR), line of response (LOR), light sharing,
    Anger logic, list mode

## E3 -- claims about the field that need a citation

Every historical date, every quoted performance figure (resolution, sensitivity,
cost), and every statement of what scanners or groups "typically" do.
