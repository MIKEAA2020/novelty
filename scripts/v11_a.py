# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol: Profound Novelty, Volume III —
Version 1.1' — part A: front matter, Chapter 1 (amended), Chapter 2 (new).

Chapter numbering plan (Step 3.5):
| Outline Index | Type    | Chapter # | Title                                       |
|---------------|---------|-----------|----------------------------------------------|
| 1             | cover   | -         | Cover (separate Playwright PDF, merged)     |
| 2             | toc     | -         | Contents                                     |
| 3             | content | 1         | From Diagnosis to Operations, Version 1.1   |
| 4             | content | 2         | The Chassis and the Delta                    |
| 5             | content | 3         | Doctrine: Five Operating Principles          |
| 6             | content | 4         | The Pipeline: Eight Phases, Eight Gates     |
| 7             | content | 5         | Running the Protocol as an LLM              |
| 8             | content | 6         | Backtest: Living and Dead                    |
| 9             | content | 7         | Alarms, Refutation Clauses, and Limits      |
| 10            | content | 8         | Invocation: The Card                         |

Table numbering in v1.1:
  T1  amendment record (ch1)        T7  vice ledger (ch5)
  T2  signature + census (ch1)     T8  backtest matrix (ch6)
  T3  translation table (ch2)      T9  census matrix (ch6)
  T4  parameters (ch2)             T10 census verdicts (ch6)
  T5  delta inventory (ch2)        T11 alarms (ch7)
  T6  gate summary (ch4)            T12 refutation clauses (ch7)
"""

DOC_TITLE = "The L3 Protocol: Profound Novelty, Volume III — Version 1.1"
DOC_SUBJECT = ("The operating manual reissued under its own six alarms: the "
               "pipeline re-labeled as an inherited chassis with the "
               "translation table printed, every number demoted to an "
               "administrative parameter, the G5-self limit-case derived, the "
               "failure census executed against the dead, three refutation "
               "clauses armed, and the naked primitives given their "
               "measurement stories. The claim now rests on the operator "
               "delta alone.")

CHAPTERS = [
    ("1", "From Diagnosis to Operations, Version 1.1"),
    ("2", "The Chassis and the Delta"),
    ("3", "Doctrine: Five Operating Principles"),
    ("4", "The Pipeline: Eight Phases, Eight Gates"),
    ("5", "Running the Protocol as an LLM"),
    ("6", "Backtest: Living and Dead"),
    ("7", "Alarms, Refutation Clauses, and Honest Limits"),
    ("8", "Invocation: The Card"),
]

# ---------------------------------------------------------------------------
# Chapter 1 — From Diagnosis to Operations, Version 1.1
# Paragraphs 1-2 and 4 of v1.0 are reused verbatim from protocol_content;
# paragraphs 3 and 5 are patched in place (chapter cross-references shifted by
# the new Chapter 2). Two new paragraphs state the version block.
# ---------------------------------------------------------------------------

# patched CH1_S1[1]: pipeline now lives in Chapter 4; Table 1 is now Table 2
CH1_S1_1_V11 = (
    "A signature, however, is not a method. The distance between the two is the "
    "subject of this volume, and it is crossed by a single transformation: every "
    "trait that history observed as a consequence is re-imposed as a requirement "
    "before the fact. The signature says profound theories demolished constitutive "
    "concepts; the protocol instructs: delete a constitutive concept from the axioms "
    "before writing any new law. The signature says the founders were overthrown "
    "by their own revolutions; the protocol instructs: write and answer the "
    "strongest defense of the old order before claiming the new one. The "
    "signature says a new universal constant arrived with each unification; the "
    "protocol instructs: extract, dimensionally, the conversion constant your "
    "unification forces, and reject it if it had to be fitted to data. Table 2 "
    "performs this inversion line by line — it is the load-bearing table of the "
    "entire manual, and every phase of the pipeline in Chapter 4 is traceable to "
    "a row of it.")

# patched CH1_S1[3]: LLM chapter is now Chapter 5, pipeline Chapter 4
CH1_S1_3_V11 = (
    "One more thing distinguishes this manual from a generic philosophy-of-science "
    "checklist: its operator is a large language model, and the manual is written "
    "to that operator's specific strengths and vices. Some historically scarce "
    "resources are abundant for us. One human mind cannot hold crystallography, "
    "Hamiltonian optics, and Malthusian economics simultaneously; the "
    "unification search — historically the rarest and most valuable event in "
    "science — is, for a model that has read everything, an enumerable batch job. "
    "Some historically free resources are scarce for us: we have no laboratory, "
    "no instruments, and no access to a single observation that is not already "
    "in the corpus. And we carry structural vices no human scientist has ever "
    "had — a training objective that rewards the probable, and a corpus "
    "saturated with the authority of the paradigms we intend to revise. Chapter "
    "5 treats these in detail; the gates of Chapter 4 are engineered so that our "
    "own vices cannot pass them silently.")

CH1_NEW = [
    ("Version 1.1 exists because version 1.0 asked for it. The first edition "
     "closed by leaving the alarms armed against the alarm-keeper, and the "
     "audit that followed ran all six at full strength against the manual "
     "itself: three fired outright, three fired in part, none came back clean. "
     "Six amendments repair the findings, and this reissue incorporates them "
     "all. The rule governing every change is the one the audit wrote for "
     "itself — the anti-epicycle constraint: no new doctrine, no new phase "
     "in the pipeline proper, no extension of the signature. Every patch is "
     "a demotion, a derivation, an operationalization, a control, or a "
     "refutation clause — each claiming less, or computing what it "
     "asserted. The pipeline diagram of Chapter 4 is unchanged between "
     "editions for exactly that reason: the amendments touch what the "
     "manual claims, what its numbers are, and how its primitives are "
     "measured — not the machine's shape."),

    ("Two companion artifacts carry the amendments' full weight, and this "
     "reissue summarizes them where their results land. The limit-case "
     "derivation computes, with three named parameters, the limit in which "
     "this protocol degenerates into the methodology it inherits — closing "
     "the manual's own fifth gate against itself and inventorying the "
     "six-item operator delta that survives the computation. The failure "
     "census codes three dead theories against the signature under a "
     "pre-registered sampling rule — phlogiston, the luminiferous ether, "
     "the epicycle tradition — and its verdicts amend the signature "
     "itself: three points demote to truths that do not discriminate, five "
     "discriminators stand, and every claim is finally paired with its "
     "control. Table 1 records the amendments and where they land; the "
     "chapters that follow carry them in place."),
]

AMEND_HEADER = ["ID", "Type", "The change", "Lands in"]

AMEND_ROWS = [
    ("A1", "demote",
     "pipeline re-labeled an inherited chassis; the translation table printed "
     "in the manual; the claim relocated to the operator delta",
     "Chapter 2; Table 3"),
    ("A2", "operationalize",
     "every number demoted to an administrative parameter with stated "
     "provenance; G4 gains the promotion test for constants fitted at birth; "
     "the signature states its falsifiers",
     "Chapters 2, 4, 6"),
    ("A3", "derive",
     "the G5-self limit case computed with named parameters — kill cost, "
     "verification, corpus — the protocol's delta inventoried",
     "Chapter 2; Tables 4-5; companion artifact"),
    ("A4", "control",
     "the failure census under a written sampling rule; every signature "
     "claim paired with its confound at the point of claim",
     "Chapter 6; Tables 9-10; companion artifact"),
    ("A5", "refute",
     "three refutation clauses written as runnable tests; successor crises "
     "promoted from paragraph to section; tool invention scheduled",
     "Chapters 4, 7"),
    ("A6", "operationalize",
     "strain given a counting rule; constitutive given the severed-path "
     "computation; harvest given the disjoint-question-sets criterion",
     "Chapter 4; Table 6"),
]

AMEND_CAPTION = ("Table 1 — The amendment record: six patches from the audit, "
                 "each a demotion, derivation, operationalization, control, or "
                 "refutation clause — none an epicycle.")

TABLE2_HEADER = ["Signature (observed in history)",
                 "Protocol requirement (imposed before the fact)",
                 "Enforced at", "Census verdict"]

TABLE2_ROWS = [
    ("Demolition rather than accumulation",
     "Delete a designated constitutive concept from the axioms before writing any new law.",
     "P2 · G2",
     "discriminates — code at the christening"),
    ("Unification of the thought-to-be-separate",
     "Run a systematic translation between two allegedly distinct domains; mint concepts only at the untranslatable residue.",
     "P3 · G3",
     "confounded — demoted to a condition"),
    ("A new universal constant (G, c, h)",
     "Extract the dimensioned conversion constant the unification forces; a constant fitted at birth survives only by promotion — paying an independent derivation later.",
     "P4 · G4",
     "discriminates, under the promotion test"),
    ("Derivation ahead of observation",
     "Select targets from existing accurate-but-unspeakable data; privilege reinterpretation over new apparatus.",
     "D2 · P0",
     "restated — structure, not content"),
    ("Conservative embedding of the old theory",
     "Derive the predecessor as a limit case by symbolic calculation, and list the discriminating regimes.",
     "P5 · G5",
     "discriminates — on ontology"),
    ("Formalism detached from meaning (the Lorentz failure)",
     "Assign a measurement story to every primitive; ban mixed vocabulary.",
     "P6 · G6",
     "discriminates, operationalized: minted measurables"),
    ("Founders overthrown by their own revolution",
     "Write and answer the strongest defense of the old paradigm before closure.",
     "P7 · G7",
     "confounded — demoted to a stakes marker"),
    ("A century of generative harvest",
     "Enumerate the downstream programs it should generate — distinct meaning disjoint question sets; the floor is a parameter.",
     "P7 · G7",
     "discriminates — as slope, with a counting rule"),
    ("Closes one crisis by opening a deeper one",
     "Name the successor crisis the framework makes askable but cannot answer.",
     "P7 · G7",
     "confounded — demoted to a corollary"),
]

TABLE2_CAPTION = ("Table 2 — The signature inverted, as amended by the failure "
                  "census: each observed trait becomes a requirement imposed "
                  "before the fact, now paired at the point of claim with its "
                  "census verdict — the fourth column is Amendment A4's work.")

# ---------------------------------------------------------------------------
# Chapter 2 — The Chassis and the Delta (new in v1.1)
# ---------------------------------------------------------------------------

CH2_P1 = [
    ("This chapter prints what the first edition asserted and the audit "
     "demanded be computed: the manual's account of what it inherits and "
     "what it adds. The demotion comes first, and it is stated plainly. "
     "The audit's translation test found that eight of the protocol's "
     "eleven layers render, with their nouns changed, into methodology "
     "the corpus already held — the correspondence principle, "
     "operationalism, the protective belt, the awareness of anomaly — "
     "and that what survives the translation is an operator's delta, "
     "small and load-bearing. The first edition marketed the pipeline as "
     "proprietary theory; v1.1 re-labels it as an inherited chassis with "
     "an operator's manual bolted on, and relocates the manual's claim "
     "to the delta. A protocol that demands of every candidate a printed "
     "account of what it inherits cannot be the one document exempt "
     "from the demand."),

    ("Table 3 prints the translation table in full, as the first amendment "
     "requires: the protocol's layers against their nearest predecessors, "
     "the translation marked, the residue named. Read it as the manual's "
     "honesty layer rather than as an indictment. Every phase a reader "
     "recognizes from the methodology literature is working as designed, "
     "not failing — the phases are supposed to be the inherited part, "
     "the way a compiler is not diminished for being a Turing machine. "
     "The three rows that leave a residue are the manual's proprietary "
     "content, and the audit's finding is restated here as policy: the "
     "claim of this manual is exactly the size of that residue, and no "
     "larger."),

    ("The third amendment computed the embedding this chapter states. "
     "The protocol is a family parameterized by the operator's three "
     "structural differences from the human founder — kill cost, "
     "verification exposure, corpus radius — and the derivation shows "
     "the family degenerating into classical methodology as each "
     "parameter goes to its human value. At career-priced kills, the "
     "gates become peer review, the kill log becomes a field's informal "
     "memory of dead programs, and the zero-survivor economics becomes "
     "conservative funding. At full verification, the derivation "
     "doctrine reverts to the hypothetico-deductive method and the "
     "discriminating list becomes the experimental proposal. At small "
     "corpus radius, the assumption census becomes tacit knowledge, the "
     "dictionary attack becomes the lucky outsider's once-a-century "
     "transfer, and the counting rules become taste. Tables 4 and 5 "
     "state the parameters and the residual: six items no parameter "
     "change dissolves, each with its collapse condition and its "
     "falsifier. The full derivation exists as the companion artifact; "
     "what this chapter carries is its result, and the result is the "
     "manual's honest self-portrait — a small proprietary layer on a "
     "large inherited base, drawn at scale."),

    ("The second amendment demotes the manual's numbers, all of them, "
     "to administrative parameters. The audit traced every constant to "
     "its origin and found the same pattern each time: fitted to nine "
     "revered cases selected for being revered, derived from nothing, "
     "defensible at best as stated policy — eight phases, three kills, "
     "a ten-program harvest floor, a patch-thickness of three, nine "
     "signature points, six alarms. v1.1 prints them as what they are: "
     "parameters, revisable per campaign without pretense of bedrock, "
     "their provenance stated where they appear. The one place the "
     "audit found anything like real bedrock — the founding constants "
     "of the physicists — survived only by acquiring the promotion "
     "test that Chapter 4's fourth phase now carries; the numbers of "
     "this manual undergo the same discipline. A parameter that pays "
     "across campaigns is kept; one that never pays is revised; and "
     "the difference is written in the log, which is the only "
     "provenance a number in this manual is permitted to claim."),
]

CH2_QUOTE_LAKATOS = (
    "Blind commitment to a theory is not an intellectual virtue; it is an "
    "intellectual crime.",
    "Imre Lakatos, “Science and Pseudoscience”, 1973 — the crime the "
    "translation table is armored against: printing the chassis is how "
    "the manual keeps its commitment sighted.")
