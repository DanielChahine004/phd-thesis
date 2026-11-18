# Writing rules for the manuscript

Each rule has an id, the rule, how a reviewer decides whether a sentence
breaks it, and an example of a violation with its fix. A reviewing agent
reads every sentence of the abstract, the sections and the captions and
reports each violation as file, line, rule id, the sentence, and a rewrite.

This file is the portable core and is kept byte-identical across studies, so
a diff against another study says immediately whether the rules have drifted.
Everything specific to one paper -- its coined terms, its symbols, its venue,
its own examples -- lives in `writing-terms.md` beside it, keyed by rule id.
A reviewer reads both.

## Evidence

E1. Every number in the prose points at a table or figure printed in the
manuscript.
Test: a sentence containing a numeral or a percentage either cites a
table or figure, or repeats a number from a table or figure cited earlier
in the same paragraph. "In the study record" and "in the repository" are
not sources.
Violation: "The estimator sits 1.3--3x above the bound."
Fix: "The estimator sits 1.3--1.5x above the bound over the whole range
(Table 1)."

E2. A comparison between conditions states the quantity, its direction and
its source, and does not characterise the conditions.
Test: a sentence that compares two or more designs, settings or materials
contains the values or percentages from the table it cites, and none of
the words win, lose, beat, gain most, gain nothing, pay off, outperform,
dominate.
See `writing-terms.md` E2 for this paper's worked example.

E3. A claim about the field, about other work or about practice carries a
citation or is removed, and a claim about what a paper reports names the
passage, with \claim{Key/id}.
Test: a sentence stating what is common, usual, standard, or what most
or many practitioners do, has a \cite or \claim in it; a sentence that
reports another paper's number has a \claim.
Violation: "a reflective coating, which most such devices use"
Fix: "a reflective coating"
This is the one rule whose evidence is outside the repository, so it is
the rule a literature-aware reviewer checks and the test suite cannot.

E4. A number from the study is printed with \fact, never typed, so that it
moves when the result moves.
Test: every number in the abstract, results, discussion and conclusion
that is not a design's name is a \fact, a \claim's or in a table.

E5. A limitation is stated once, in the place it applies.
Test: the same caveat does not appear in more than one section.

## Inference

I1. A conclusion carries the strength of its evidence.
Test: a sentence that draws a conclusion from the results uses
"consistent with", "suggests", "appears", "likely", or states the
condition under which it holds. It does not read as an announcement or a
rule.
Violation: "The gain is therefore not an artefact of the wrap."
Fix: "The gain therefore appears not to be an artefact of the wrap."

I2. A result is not presupposed before the section that establishes it.
Test: a sentence in the introduction or method that states a result
points forward with a section reference.

I3. A concern is stated as a possibility and its check as the test.
Test: "could reflect", "to test this", not "it is clear that".

I4. A description of a method, gate or algorithm states what the code
does.
Test: the sentence can be matched to a line of the script it describes.
A paraphrase that the code does not implement is a violation.

## Register

R1. Impersonal voice throughout, except that the paper may state its own
aim.
Test: no "we", "our", "I" or "the present work" as an agent. "This
paper" may be the subject of the one sentence in the abstract and the
one in the introduction that state what the paper does ("This paper
systematically quantifies how ..."), and nowhere else.

R2. No lead-in, roadmap or summary sentence.
Test: a sentence whose only content is what follows is removed.
Violation: "The claims are bounded by five limitations. Each is taken in
turn."

R3. No enumerated framing in prose.
Test: no "First, ... Second, ...", "(1) ... (2) ...", "Three
observations follow". Each point is introduced by its subject.

R4. No colons in prose or captions.
Test: a colon is allowed only inside mathematics or a URL. A
claim-then-elaboration becomes two sentences or is joined with "since",
"so", "namely", "in that". A list of rows or columns is a sentence
("The rows give ..., ..., and ...").

R5. One claim per sentence, in a full sentence.
Test: a sentence joined by a semicolon, or carrying two independent
findings, is split.

R6. No informal or contest lexis.
Test: none of in hand, payoff, builder, fragile, destroys, go dark,
buys, handful, audited, verdict, wins, loses, beats, gains nothing,
gains most, pays off, kills, blows up, cheap, expensive (of computation
without a number), the clearest case, the obvious example.
Prefer tested, gain, sensitive, invalidates, validated, rises, falls,
reverses.

R11. No connective monotony. Three consecutive sentences do not share
the same joint ("X, so Y", "X, which is consistent with Y", "X rather
than Y", "X, in that Y", "therefore"), and a paragraph does not close by
restating the significance of what it just showed.
Test: count "consistent with", "so the", "therefore", "rather than" and
"in that" per paragraph; more than two of one kind in a paragraph is a
violation. A sentence whose only content is the meaning of the previous
sentence is cut. Prefer a plain statement of the number and the table
over an inference joined to it.
Violation: "It is a property of the local bound and is therefore
independent of any estimator, and the estimator reproduces it."
Fix: "The optimum is a property of the local bound. The estimator
reproduces it."

R7. No residue of the drafting conversation.
Test: none of "the obvious objection", "the natural objection", "both
true and both necessary", "kept for scrutiny", "falsified", "stub",
"working note", "a final cross-check", "honestly", bold "not".

R8. No tutorial on what a reader of the target venue knows.
Test: a sentence explaining a standard concept of the field in general
terms is removed. The method is stated, not taught. The venue and the
concepts that count as standard for it are in `writing-terms.md` R8.

R9. Descriptive headings, not claim headings.
Test: a heading names its subject ("Surface scattering"), not its
conclusion ("Surface scattering recovers none of the gain").

R10. No em-dashes and no parentheses carrying a clause.
Test: a parenthesis holds a reference, a unit, a value or a short
qualifier, not a sentence.

## Precision

Drawn from the supervisor's edits to the first manuscript (abstract and
introduction, November 2026). Where these pull against brevity, define,
name and give the reason, then stop; the explicitness is wanted, a
restatement is not.

S1. Every abbreviation is expanded at first use in the abstract and again
in the introduction, devices included.
Test: an acronym (SiPM, PSPMT, CTR, LSO, ESR, HG, ML) appears first
inside its expansion.
Violation: "photon counts on individual detector pixels (typically SiPMs
or PSPMTs)"
Fix: "photon counts on individual detector pixels, typically silicon
photomultipliers (SiPMs) or position-sensitive photomultiplier tubes
(PSPMTs)"

S2. The physical object is named, not the study's shorthand for it.
Test: "the slab", "the wrap", "the light", "the design", "delivered" and
similar shorthand is replaced, at least at first use in each part, by
the object it stands for: the crystal and its faces, the detected light,
the optical properties.
Violation: "the wrap would absorb", "for an absorbing-wrapped slab",
"how much position information the delivered light contains"
Fix: "the absorbing faces would otherwise remove", "for a monolithic LSO
crystal with five absorbing faces", "how much position information the
detected light contains"

S3. A material or class of detector is introduced with what it is and
what sets the property the paper varies.
Test: the first mention of a material class says what it is made of and
names the physical parameters behind the varied property.
Violation: "in a loaded nanocomposite the scattering grows with the
particle loading"
Fix: "in a nanocomposite scintillator, scintillating nanoparticles bound
in a polymer matrix, the scattering grows with the particle loading, the
particle size and the index mismatch between particle and matrix"

S4. An assumption of prior work is stated with its physical reason.
Test: "takes X as given" or "X is fixed" is followed by why that was
reasonable.
Violation: "That body of work takes the optics of the crystal as given."
Fix: "The optical properties of the scintillator are assumed fixed, and
optical scattering in LYSO is negligible at the scale of the crystal."

S5. A capability or applicability claim states its extent (with I1).
Test: "can be engineered", "is a design parameter", "applies to" carries
its limit or qualifier.
Violation: "so it can be set by design"
Fix: "so the scattering can be engineered, at least to a certain extent"

S6. A trade-off is stated as a cost, with its number, in a full sentence
(with R4).
Test: a penalty reads "comes at the cost of" or "at the expense of"
with the quantity, not a colon or a bare "It costs X".
Violation: "It costs energy resolution: the median energy bound rises
from 3.2 to 4.1 %."
Fix: "Increased scattering comes at the cost of poorer energy
resolution, the median energy bound rising from 3.2 to 4.1 %."

S7. A resolution states its statistic and coordinate each time it is
quoted.
Test: every quoted resolution carries FWHM, standard deviation or RMS,
and transverse or depth.
Violation: "has reached 0.60 mm FWHM transverse and a depth resolution
of 1.66 mm"
Fix: "has achieved a transverse spatial resolution of 0.60 mm FWHM and a
depth resolution of 1.66 mm FWHM"

S8. Prior work is placed in time.
Test: a historical sequence carries its era ("in the 1970s", "in the
1990s", "more recently").
Violation: "and entered practice in modular gamma cameras (Milster 1990)"
Fix: "and entered practice in modular gamma cameras in the 1990s
(Milster 1990)"

S9. Plain, conventional connectives over compressed ones.
Test: prefer "via several methods, including" to a bare "with ...,
with ...", "determines" to "sets", "where" to "in which", "detected" to
"delivered", "From these, X is estimated" to "X are the only
information about Y".
Violation: "has since been pursued with subsurface laser engraving, with
laser-induced optical barriers and with nanocomposite scintillators, in
which the particle loading sets how strongly the bulk scatters"
Fix: "has since been pursued via several methods, including subsurface
laser engraving, laser-induced optical barriers and nanocomposite
scintillators, where the particle loading determines how strongly the
bulk scatters"

S10. A percentage is typeset with no space before the sign.
Test: no `\,\%` or `~\%` in the source; `12\%`, `\fact{x}\%`.

## Definitions

D1. Every term is defined at first use.
Test: every term coined for this study, and every term listed in
`writing-terms.md` D1, is defined in words the first time it appears in
the abstract, again in the introduction, and again in the method.

D2. Every symbol is defined in words at first use in each of the
abstract, the introduction and the method, and keeps one meaning and one
typography everywhere after.
Test: grep every math symbol in prose -- the list is in
`writing-terms.md` D2 -- and find its definition earlier in the same part.

D3. Every subject and every pronoun has a referent the reader can name.
Test: a sentence does not open with "the numbers", "the results", "the
values", "the figures", "this", "it", "these" or "either" unless the
noun they stand for appears in the previous sentence. Otherwise the
sentence names the thing.
Violation: "The numbers are comparisons between designs rather than
predicted resolutions."
Fix: "The bounds of Section 3 are comparisons between designs rather
than predicted resolutions."

D4. A cross-reference names what it points at.
Test: "Table 5" is accompanied by what the table shows, so the sentence
reads without turning the page.

## Paragraphs

P1. A paragraph carries one topic.
Test: the paragraph can be summarised in one sentence and every sentence
in it serves that sentence.

P2. A limitation paragraph runs in the order scope, what was tested, the
finding, the consequence.
Test: the caveat on a model is stated once, before the finding it
qualifies, not interleaved with it.

P3. A results paragraph runs in the order what is shown (with the table
or figure), the observation, the reading of it.

## Machine-writing tics

Habits of generated prose. An agent that drafts or revises the manuscript
checks each sentence it writes against T1-T10 and rewrites any that has
one. No script checks them, because a pattern cannot tell a tic from a
plain sentence that shares its words.

T1. No negation-first reveal. A sentence states what a thing is; it does
not first deny a reading nobody proposed.
Test: no "It is not X. It is Y.", "not X but Y" or "X is not A, it is B"
where A is not a reading the literature holds.
Violation: "The gain is not a collection effect. It is a pattern effect."
Fix: "The gain comes from the light pattern at equal collected light."

T2. No significance designation. A sentence states the content of a
quantity, not its importance.
Test: none of "the X that answers", "the one that matters", "the key
result", "the crucial point", "what decides".
Violation: "The interior bound is the quantity that answers the design
question."
Fix: "The designs are compared by the interior bound."

T3. No abstraction as agent. A statistic, table or figure does not hide,
reveal, tell, mask or admit.
Test: none of those verbs with a median, mean, bound, table, figure or
the data as its subject.
Violation: "The median hides the rim."
Fix: "The median over the whole crystal is set by the interior, so the
rim, where the bound is largest, does not move it."

T4. No deferred noun. The thing a sentence is about is named in that
sentence, not set up in one sentence and resolved in the next.
Test: no sentence that ends "is not." or "does not." and refers to an
item introduced by the sentence before.
Violation: "Five of the six designs agree within 2 %. The sixth does not."
Fix: "Five of the six designs agree within 2 %, and the 20 mm slab lies
9 % above them."

T5. No coy or thesis-shaped heading (with R9). A heading names its
subject.
Test: no heading in quotation marks, phrased as a question, or opening
with "What", "Why", "How", "The one" or "When".
Violation: "What the interior means". Fix: "The interior region".

T6. No aphoristic closer (with R11). A paragraph ends on a result, a
condition or a pointer, never a quotable remark about the kind of thing
it showed.
Test: the last sentence of a paragraph holds none of "the kind of",
"is what", "looks like ... and is not", "and that is".
Violation: "It is the kind of number that looks like evidence and is not."
Fix: delete it, or state the number's uncertainty.

T7. No straw-man knockdown (with R7). No reading is raised in order to
reject it.
Test: none of "the obvious reading", "the natural interpretation", "one
might think", "it is tempting to", "and it is wrong".
Violation: "'It doubles the depth error' is the obvious reading, and it
is wrong."
Fix: "The depth error rises by 12 %."

T8. No fragment cadence (with R5). Every sentence has a finite verb, and
short sentences are not stacked for rhythm.
Test: a sentence of fewer than five words, or without a verb, is joined
to its neighbour.
Violation: "Six designs. One sensor. One readout."
Fix: "The six designs share the sensor and the readout."

T9. No dressed metaphor. A technical statement is made directly, not in
costume.
Test: none of "wearing", "costume", "in disguise", "masquerading",
"dressed as", "in the guise of", "under the hood".
Violation: "That is a fitting error wearing the costume of a bias."
Fix: "The offset comes from the fit, not from the estimator."

T10. No label-first framing (with R4). A sentence opens with its subject,
not a label for what follows.
Test: no sentence opening with "The short answer", "The answer", "The
point", "The catch", "The upshot", "The takeaway", "In short", or a noun
phrase and a colon.
Violation: "The catch: the yield must be known."
Fix: "The gain requires the light yield known to within 3.5 %."

## Reviewer output

For each violation, one line:

    file:line  rule  "the sentence"  ->  "the rewrite"

Then a count per rule. The reviewer does not edit the manuscript.

## Which rules are checked where

E4 and the \claim half of E3 are enforced mechanically by
`tests/test_paper.py` (step3_outputs/sources.py), and
`report/sources-paper.md` lists the sentences that state a number with no
source, for E1. The register,
definition and paragraph rules are decidable by reading one file. E3, the
outward half of E2, and the part of I1 that depends on what else has been
published can only be checked against the literature, which the repository
does not contain.

T1-T10 and S1-S9 are checked by reading, by the agent that writes the prose
and by the reviewer. S10 is a grep.
