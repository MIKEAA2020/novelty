# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol: Profound Novelty, Volume III' — part A.

Chapter numbering plan (Step 3.5):
| Outline Index | Type    | Chapter # | Title                                   |
|---------------|---------|-----------|-----------------------------------------|
| 1             | cover   | -         | Cover (separate Playwright PDF, merged) |
| 2             | toc     | -         | Contents                                |
| 3             | content | 1         | From Diagnosis to Operations            |
| 4             | content | 2         | Doctrine: Five Operating Principles     |
| 5             | content | 3         | The Pipeline: Eight Phases, Eight Gates |
| 6             | content | 4         | Running the Protocol as an LLM          |
| 7             | content | 5         | Backtest: The Protocol Against History  |
| 8             | content | 6         | Alarms and Honest Limits                |
| 9             | content | 7         | Invocation: The Card                    |
"""

DOC_TITLE = "The L3 Protocol: Profound Novelty, Volume III"
DOC_SUBJECT = ("An operating manual for the production of profound novelty: "
               "the nine-point signature and six necessary conditions of the earlier "
               "volumes inverted into doctrine, an eight-phase pipeline with gates, "
               "operator constraints for a language-model researcher, a backtest "
               "against the founding revolutions, and the alarms that separate "
               "depth from decoration.")

CHAPTERS = [
    ("1", "From Diagnosis to Operations"),
    ("2", "Doctrine: Five Operating Principles"),
    ("3", "The Pipeline: Eight Phases, Eight Gates"),
    ("4", "Running the Protocol as an LLM"),
    ("5", "Backtest: The Protocol Against History"),
    ("6", "Alarms and Honest Limits"),
    ("7", "Invocation: The Card"),
]

# ---------------------------------------------------------------------------
# Chapter 1 — From Diagnosis to Operations
# ---------------------------------------------------------------------------

CH1_S1 = [
    ("The first two volumes of this study were diagnoses. Volume I selected the "
     "three cleanest specimens physics offers — Newtonian mechanics, Einstein's "
     "relativity, and the quantum — took their diff against each theory's own past, "
     "and extracted a nine-point signature of profundity, anchored on a three-level "
     "ladder: ordinary novelty adds phenomena (Level 1) or laws (Level 2); profound "
     "novelty rewrites the vocabulary in which the laws are written (Level 3). "
     "Volume II widened the case base to nine revolutions across five disciplines, "
     "recovered the same signature everywhere, and added the conditions under which "
     "such events become possible: instruments and the adjacent possible, a prepared "
     "outsider, a carrier that compels assent alone, conservative embedding, a "
     "prepared community, and ratification by a century of harvest. Both volumes "
     "look backward. They describe what profundity looks like in cross-section, "
     "after the world has already voted."),

    ("A signature, however, is not a method. The distance between the two is the "
     "subject of this volume, and it is crossed by a single transformation: every "
     "trait that history observed as a consequence is re-imposed as a requirement "
     "before the fact. The signature says profound theories demolished constitutive "
     "concepts; the protocol instructs: delete a constitutive concept from the axioms "
     "before writing any new law. The signature says the founders were overthrown "
     "by their own revolutions; the protocol instructs: write and answer the "
     "strongest defense of the old order before claiming the new one. The "
     "signature says a new universal constant arrived with each unification; the "
     "protocol instructs: extract, dimensionally, the conversion constant your "
     "unification forces, and reject it if it had to be fitted to data. Table 1 "
     "performs this inversion line by line — it is the load-bearing table of the "
     "entire manual, and every phase of the pipeline in Chapter 3 is traceable to "
     "a row of it."),

    ("What such a conversion cannot promise must be said plainly, because it "
     "bounds everything that follows. There is no algorithm for profundity; if a "
     "procedure reliably produced Level-3 revisions, its outputs would be expected, "
     "and an expected revision of vocabulary is a contradiction — the corpus "
     "already contains the consensus the revision would overwrite. What a "
     "protocol can do is three humbler things, and history suggests they are the "
     "three that mattered. It can position: aim the operator where Level-3 "
     "opportunities actually live — at strain between accurate data and inherited "
     "concepts, not at open problems the field already knows how to state. It can "
     "force: substitute process discipline for the flashes of temperament the "
     "founders supplied themselves. And it can prevent self-deception, which is "
     "the failure mode that consumes almost all would-be revolutionaries: not "
     "producing something wrong, but believing one has produced something profound "
     "when one has produced a renaming, a patch, or a mood."),

    ("One more thing distinguishes this manual from a generic philosophy-of-science "
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
     "4 treats these in detail; the gates of Chapter 3 are engineered so that our "
     "own vices cannot pass them silently."),
]

CH1_QUOTE_EINSTEIN = (
    "We have to take into account that all our judgments in which time plays a "
    "part are always judgments of simultaneous events.",
    "Albert Einstein, “On the Electrodynamics of Moving Bodies”, 1905 — the operational "
    "question that opened the relativity paper before a single equation appeared in it.")

CH1_S2 = [
    ("The protocol runs as a campaign of targets, not a single grand attempt. A "
     "target is a suspected Level-3 strain site: a domain where accurate data is "
     "straining against inherited vocabulary. Each campaign occupies a working "
     "directory whose structure is fixed, because the artifacts, not the "
     "narrative, are the deliverable: <i>ledger.md</i> for the anomaly inventory; "
     "<i>autopsy/</i> for the concept inventory, dependency graph, and assumption "
     "census; <i>amputation/</i> for the deleted-axiom derivations; <i>dictionary/</i> "
     "for the translation tables and their residue; <i>invariants/</i> for the "
     "invariance statements and dimensional analysis; <i>limits/</i> for the "
     "limit-case derivations and discriminating list; <i>semantics.md</i> for the "
     "operational dictionary; <i>closure/</i> for the defense, the harvest "
     "enumeration, and the successor crisis; and <i>gates.md</i>, the only file "
     "the operator is obliged to keep current, logging every gate verdict with "
     "its date, its evidence, and its loop count. The directory is the protocol's "
     "memory, and it is also its honesty: an assertion that cannot be found as a "
     "file has not been made."),

    ("The iteration policy is the loop rule, and it is the closest thing the "
     "protocol has to a personality. Every gate failure carries a return-target: "
     "a kill at G1 returns the campaign to P0 with a sharpened ledger; a kill at "
     "G2 returns it to P1 for a better-chosen concept; a kill at G6 returns it to "
     "P2 for a deeper cut. Three kills at the same gate abandon the target "
     "entirely and demand a post-mortem: what was mistaken about the strain site, "
     "what the census missed, what kind of anomaly this was after all. The "
     "post-mortems are first-class artifacts, never discarded, because the kill "
     "log is the operator's compounding asset. Every kill is a map annotation "
     "reading <i>no bedrock here</i>, and after many campaigns the map is worth "
     "more than any single expedition: it is the difference between searching "
     "and remembering where one has already searched. Run targets in parallel, "
     "expect nearly all of them to die at G0 or G1, and price that outcome as "
     "success — the protocol's purpose is not to make profundity likely but to "
     "make its pursuit cheap, early-killing, and legible to itself."),
]

TABLE1_HEADER = ["Signature (observed in history)",
                 "Protocol requirement (imposed before the fact)",
                 "Enforced at"]

TABLE1_ROWS = [
    ("Demolition rather than accumulation",
     "Delete a designated constitutive concept from the axioms before writing any new law.",
     "P2 · G2"),
    ("Unification of the thought-to-be-separate",
     "Run a systematic translation between two allegedly distinct domains; mint concepts only at the untranslatable residue.",
     "P3 · G3"),
    ("A new universal constant (G, c, h)",
     "Extract the dimensioned conversion constant the unification forces; reject any constant fitted to data.",
     "P4 · G4"),
    ("Derivation ahead of observation",
     "Select targets from existing accurate-but-unspeakable data; privilege reinterpretation over new apparatus.",
     "D2 · P0"),
    ("Conservative embedding of the old theory",
     "Derive the predecessor as a limit case by symbolic calculation, and list the discriminating regimes.",
     "P5 · G5"),
    ("Formalism detached from meaning (the Lorentz failure)",
     "Assign a measurement story to every primitive; ban mixed vocabulary.",
     "P6 · G6"),
    ("Founders overthrown by their own revolution",
     "Write and answer the strongest defense of the old paradigm before closure.",
     "P7 · G7"),
    ("A century of generative harvest",
     "Enumerate at least ten distinct downstream programs before claiming the framework.",
     "P7 · G7"),
    ("Closes one crisis by opening a deeper one",
     "Name the successor crisis the framework makes askable but cannot answer.",
     "P7 · G7"),
]

TABLE1_CAPTION = ("Table 1 — The signature inverted: each diagnostic observation of "
                  "Volumes I–II becomes a requirement imposed before the fact.")

# ---------------------------------------------------------------------------
# Chapter 2 — Doctrine: Five Operating Principles
# ---------------------------------------------------------------------------

CH2 = [
    ("Doctrine is the layer of the manual that decides conflicts between rules. "
     "The pipeline of Chapter 3 will frequently present the operator with a "
     "choice — deepen the dictionary or widen it, kill the target or loop once "
     "more — and the five principles below are what settle such choices when "
     "local judgment runs out. They are stated once, here, and the gates assume "
     "them. Each is a compression of one or more rows of Table 1, and each earns "
     "its place by having been paid for, at least once in history, by a founder "
     "who lacked it at exactly the moment it mattered."),

    ("<b>D1 — Profundity is vocabulary surgery.</b> The Level-3 criterion is the "
     "protocol's whole claim to scope: a target qualifies only if its resolution "
     "requires redefining a constitutive concept — space, time, cause, state, "
     "observation, species, computation — rather than adding content or "
     "structure inside a stable vocabulary. The operational test is statability: "
     "ask whether the motivating problem can be fully stated in the field's "
     "current language. If it can, the work ahead is Level-2 or Level-1, "
     "legitimate and out of scope. “What carries light?” was statable, and the "
     "ether answered it; “is simultaneity absolute?” could not even be posed "
     "properly until simultaneity was given an operational definition, and that "
     "unstatable question is where the twentieth century began. Classify the "
     "target first; surgery on a statable problem is malpractice."),

    ("<b>D2 — Derive, don't discover.</b> The operator has no laboratory, and "
     "the doctrine turns that deficit into the historically canonical path. The "
     "signature's fourth point recorded that profound theories were derived "
     "ahead of observation: Einstein's 1905 was a reinterpretation of data that "
     "was already on the table — Michelson and Morley's null result, the "
     "asymmetries of Maxwell's electrodynamics, the quirks of the photoelectric "
     "effect — not a report of new apparatus. Rutherford needed the lab; "
     "Einstein needed the thought experiment and the existing measurements. "
     "The protocol therefore selects targets where accurate data already strains "
     "the vocabulary, and treats the discriminating predictions it eventually "
     "makes as specifications written for the world to execute, not as "
     "experiments we pretend to run."),

    ("<b>D3 — Invariance is the form of a deep law.</b> When the pipeline asks "
     "for the content of a candidate theory, it asks for it in one specific "
     "grammar: state what remains unchanged. Newton's mechanics is the same for "
     "a falling apple and an orbiting Moon; Maxwell's equations keep their form "
     "in every inertial frame; the quantum formalism conserves probability "
     "under every unitary step. A principle that cannot be cast as an "
     "invariance is presumptively a reformulation wearing a law's clothing. The "
     "corollary prices the unification: whenever two domains merge into one, a "
     "fixed conversion ratio appears — G converts mass into motion, c converts "
     "space into time, h converts frequency into energy — and the constants are "
     "not parameters but the fees the unification charges. A candidate theory "
     "that installs no new constant, or installs one that must be tuned to "
     "data, has not reached bedrock."),

    ("<b>D4 — The anti-consensus prior.</b> Immediate plausibility to a trained "
     "mind is negative evidence at Level 3. The founders themselves resisted "
     "their own revolutions — Einstein argued against quantum randomness for "
     "thirty years; Schrödinger regretted the cat — so a theory that reads "
     "smoothly at first pass is more likely an average of the corpus than a "
     "revision of it. This is not a fashion for the strange: the rule runs one "
     "way only, since the merely weird is as confabulable as the merely smooth. "
     "The discipline it imposes is procedural: at G7 the operator must write the "
     "old paradigm's strongest defense, at full strength, and answer it; a "
     "candidate that survives because no serious attack was ever attempted has "
     "not survived anything. For a consensus-trained model this doctrine is not "
     "optional temperament but calibration: the training objective rewards the "
     "probable continuation, and the Level-3 event is by definition improbable "
     "relative to the vocabulary it replaces."),

    ("<b>D5 — Artifacts, not assertions.</b> Every gate demands a "
     "machine-checkable deliverable: a table, a derivation, a dictionary, an "
     "enumeration. The sentence “the old theory is recovered in the limit” "
     "passes nothing at G5; the symbolic derivation that computes the limit, "
     "with its error term, does. The rule is the anti-confabulation discipline, "
     "and for a language-model operator it is the load-bearing one, because "
     "fluency is precisely what makes unverified claims dangerous in our hands. "
     "An assertion and an artifact are both made of sentences; the difference is "
     "that an artifact has a checkable structure — a countable set of rows, a "
     "recomputable limit, a residue that is either marked or not — and the "
     "protocol refuses to accept claims in any form that cannot be checked "
     "by a process that does not believe them."),
]

# ---------------------------------------------------------------------------
# Stat callout (Chapter 3 close)
# ---------------------------------------------------------------------------

CALLOUT_NUMS = [
    ("8", "gates, one per phase", "every gate demands one artifact"),
    ("3", "kills at one gate end the target", "post-mortem required, logged, kept"),
    ("10", "downstream programs at closure", "the floor of the harvest, not the ceiling"),
]

CALLOUT_CAPTION = ("The protocol's own numbers: the loop rule, the artifact "
                   "discipline, and the harvest floor.")
