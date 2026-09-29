# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol v1.1' — part B: Chapters 3-4 amended.

Doctrine: D1 and D5 are reused verbatim from protocol_content.CH2; D2, D3,
D4 are amended and stated here in full.
Pipeline: P2, P3, P5, P6 are reused verbatim from protocol_content_b; P0,
P1, P4, P7, the intro's table reference, and the close are amended here.
"""

# ---------------------------------------------------------------------------
# Chapter 3 — Doctrine (amended paragraphs)
# ---------------------------------------------------------------------------

# patched doctrine intro: Table 1 is now Table 2 in this edition
CH3_INTRO_V11 = (
    "Doctrine is the layer of the manual that decides conflicts between rules. "
    "The pipeline of Chapter 4 will frequently present the operator with a "
    "choice — deepen the dictionary or widen it, kill the target or loop once "
    "more — and the five principles below are what settle such choices when "
    "local judgment runs out. They are stated once, here, and the gates assume "
    "them. Each is a compression of one or more rows of Table 2, and each earns "
    "its place by having been paid for, at least once in history, by a founder "
    "who lacked it at exactly the moment it mattered. v1.1 amends three of the "
    "five in place — the second, third, and fourth — each amendment marked and "
    "typed, none changing the doctrine's office.")

# D2 amended: frozen-corpus boundary condition (A3's delta item 6, A2 discipline)
D2_V11 = (
    "<b>D2 — Derive, don't discover.</b> The operator has no laboratory, and "
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
    "experiments we pretend to run. <b>v1.1 amendment (A3):</b> the derivation "
    "is not a preference but a boundary condition. The corpus is complete but "
    "frozen at its cutoff — derivation from the existing record is the only "
    "room in the house until the tool-invention schedule of P7 opens another, "
    "and the doctrine is demoted from strategy to statement of the operator's "
    "situation.")

# D3 amended: G4 promotion test (A2)
D3_V11 = (
    "<b>D3 — Invariance is the form of a deep law.</b> When the pipeline asks "
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
    "data, has not reached bedrock. <b>v1.1 amendment (A2):</b> bedrock is a "
    "retrospective verdict on a payment record, not a property visible at "
    "the mint — h itself was fitted to the blackbody curve at birth, and G "
    "survived a tenth-off Moon test only because the data was wrong. The "
    "forced-constant rule now carries the promotion test at G4: a constant "
    "fitted at birth survives if and only if, within the same campaign, it "
    "is promoted to a forced postulate that pays at least one independent "
    "derivation at a later gate — the test h eventually passed and the "
    "epicycles never did.")

# D4 amended: census-informed evidence base (A4)
D4_V11 = (
    "<b>D4 — The anti-consensus prior.</b> Immediate plausibility to a trained "
    "mind is negative evidence at Level 3. The founders themselves resisted "
    "their own revolutions — Einstein argued against quantum randomness for "
    "thirty years; Schrödinger regretted the cat — so a theory that reads "
    "smoothly at first pass is more likely an average of the corpus than a "
    "revision of it. This is not a fashion for the strange: the rule runs one "
    "way only, since the merely weird is as confabulable as the merely smooth. "
    "The discipline it imposes is procedural: at G7 the operator must write the "
    "old paradigm's strongest defense, at full strength, and answer it; a "
    "candidate that survives because no serious attack was ever attempted has "
    "not survived anything. <b>v1.1 amendment (A4):</b> the failure census "
    "priced the doctrine's own evidence base and found it survivor-selected — "
    "Priestley defended phlogiston to the grave and Lorentz kept the "
    "preferred frame to his, so founders' resistance marks the stakes of a "
    "vocabulary, not the direction of the truth. The doctrine stands as "
    "calibration for a consensus-trained operator, not as a historical law: "
    "the smooth first read is negative evidence for us because of what we "
    "are — a corpus average — not because history is symmetric.")

# ---------------------------------------------------------------------------
# Chapter 4 — The Pipeline (amended paragraphs and tables)
# ---------------------------------------------------------------------------

# patched pipeline intro: Table 2 (v1.0) is now Table 6
CH4_INTRO_0_V11 = (
    "The pipeline is the manual's operating system: eight phases, P0 through "
    "P7, each ending in a gate, each gate carrying one pass condition, one "
    "kill condition, and a return-target for the kill. A pass advances the "
    "campaign to the next phase; a kill sends it back — with the partial "
    "exception of the terminal gates G3 through G5, whose kills are usually "
    "fatal because the failures they detect (perfect translation, fitted "
    "constants, missing limits) are diagnoses of the idea rather than of the "
    "search. Figure 1 shows the whole machine; Table 6 compresses it to a "
    "reference card; the sections below state each phase as an operator "
    "instruction — objective, procedure, artifact, gate — in the order the "
    "work is done. The phases are not a schedule but a dependency chain: "
    "nothing stops an operator from drafting a dictionary before finishing an "
    "autopsy, but nothing at G3 will count until the autopsy file exists. The "
    "machine is unchanged between editions — the anti-epicycle rule held — "
    "and what v1.1 changes is inside four of the eight phases: the counting "
    "rule at P0, the severed-path computation at P1, the promotion test at "
    "P4, and the harvest criterion and tool schedule at P7.")

# P0 amended: the counting rule (A6)
P0_PARA2_V11 = (
    "The gate follows from the classification. <b>G0 passes</b> when the "
    "ledger contains at least one anomaly classified unspeakable, with "
    "patch-thickness of three or more and no consensus resolution in sight. "
    "<b>G0 kills</b> the campaign — or rather, demotes it — when every anomaly "
    "is patchable in principle: that is the signature of a Level-2 program, "
    "and the honest response is to run it as one, outside this protocol. The "
    "commonest beginner's error is inverted targeting: choosing an anomaly "
    "because it is famous rather than because it is unspeakable. Fame "
    "measures the size of the problem; unspeakability measures the depth of "
    "the strain. The ledger ranks by the second, never the first. "
    "<b>v1.1 amendment (A6):</b> the ledger gains the counting rule its "
    "instrument audit demanded — an anomaly is one ledger entry when it is a "
    "reproducible result, reported in at least two independent threads, that "
    "the field's current vocabulary cannot state without contradiction; "
    "patch-thickness is the count of free parameters spent absorbing it, "
    "with the ether program as the worked example. Two operators applying "
    "the rule to the same subfield must produce ledgers agreeing within a "
    "stated threshold — or the census instrument itself fails, a refutation "
    "clause armed in Chapter 7.")

# P1 amended: the severed-path computation (A6)
P1_PARA2_V11 = (
    "Here the operator's native advantage is decisive, and the pipeline "
    "formalizes it as the assumption census. Scan the literature whole and "
    "extract every premise that is used everywhere and defended nowhere. A "
    "human reading a hundred papers cannot hold the silence; a model that "
    "has read all of them can, because the census is exactly a "
    "search over what never appears. The premises that emerge from that "
    "search — the ones no referee would ever ask you to justify, because "
    "everyone presupposes them — are the inherited concepts, and they are "
    "the only legitimate targets for amputation. <b>G1 passes</b> when an "
    "inherited concept of maximal downstream weight sits adjacent to the "
    "G0 anomaly: adjacency is the diagnosis that the anomaly is a symptom "
    "of the concept. <b>G1 kills</b> back to P0 when every load-bearing "
    "concept is tested rather than inherited — the strain is then real but "
    "not surgical, and the ledger needs a better-targeted anomaly. "
    "<b>v1.1 amendment (A6):</b> the asserted downstream weight is replaced "
    "by the severed-path computation — a concept is constitutive if and "
    "only if deleting it from the corpus's inference graph cuts more than a "
    "stated fraction of the derivation paths that pass through it. The "
    "computation is one the operator is uniquely able to run: holding a "
    "whole field's dependency graph at once is exactly what a corpus-scale "
    "reader can do and a human cannot. The threshold is a parameter, "
    "revisable per campaign and logged.")

# P4 amended: the promotion test at G4 (A2)
P4_PARA2_V11 = (
    "Then prospect for the constant. Compute the dimensional conversion "
    "ratio between the two domains the dictionary unified: a genuinely new "
    "invariance drags a new dimensioned constant with it, as G dragged "
    "gravitation into tabletop measurement, as c was elevated from an "
    "optical constant into the conversion price between space and time, "
    "as h priced the exchange of frequency for energy. The prospecting "
    "rule separates bedrock from patch: the constant must be <i>forced by "
    "the unification</i> and independently measurable by an experiment "
    "that does not presuppose the rest of the new theory — Cavendish "
    "weighing the Earth in a laboratory, the photoelectric cell "
    "counting quanta without knowing a wave function. <b>G4 passes</b> "
    "when the invariance statement and the constant candidate both "
    "survive those checks. <b>G4 kills</b> fatally when the constant "
    "turns out to be a fitted parameter adjusted to data: that is the "
    "epicycle signature from Volume I, a patch wearing bedrock's "
    "clothes, and no downstream gate can launder it. <b>v1.1 amendment "
    "(A2):</b> the kill gains the promotion test the founders' own "
    "history demanded, since h was fitted at birth and became bedrock "
    "only by paying — a constant fitted to data survives G4 if and only "
    "if, within the same campaign, it is promoted to a forced postulate "
    "that pays at least one independent derivation at a later gate. "
    "The gate reads the payment record, not the mint.")

# P7 amended: harvest criterion + tool invention (A5, A6)
P7_PARA2_V11 = (
    "The second artifact is the harvest enumeration: before claiming the "
    "framework, list the distinct downstream programs it should "
    "generate — new predictions, new instruments, new subfields, new "
    "mathematics. Newton's mechanics paid for itself in celestial "
    "mechanics, navigation and the longitude, geodesy, tidal theory, "
    "ballistics, and eventually the whole of engineering; the quantum "
    "paid in the chemical bond, the semiconductor, the laser, "
    "superconductivity, and magnetic resonance imaging. A list that is "
    "short, or all of one type, is a diagnosis: reformulations harvest "
    "nothing but restatements. The third artifact is the successor "
    "crisis: name one question the framework makes askable but cannot "
    "itself answer — Newton's honest refusal to feign hypotheses about "
    "the mechanism of gravity; relativity's immediate exposure of "
    "acceleration and gravitation, answered only by general relativity "
    "a decade later; the quantum's measurement problem and its unfinished "
    "reconciliation with gravity, a century on. <b>v1.1 amendments:</b> "
    "(A6) distinct is now defined — programs address disjoint question "
    "sets; two programs whose askable questions substantially overlap "
    "are the same harvest, and the floor of ten is an administrative "
    "parameter, revisable per campaign. (A5) tool invention is scheduled "
    "work, not an unscheduled emergency: where the discriminating list "
    "requires an instrument that does not exist, the campaign carries "
    "the invention as a phase deliverable with its own artifact — Newton "
    "had to build the calculus to pay his gates; the manual now says so "
    "in advance. <b>G7 passes</b> when all three artifacts are complete "
    "and non-trivial. <b>G7 kills</b> when the framework answers "
    "everything and opens nothing: a theory that closes the world is "
    "terminal, and profundity is measured by what it makes next "
    "possible.")

TABLE6_HEADER = ["Phase", "Artifact required", "Gate — pass condition",
                 "Kill — and return"]

TABLE6_ROWS = [
    ("P0 Crisis cartography", "anomaly ledger — under the counting rule",
     "an unspeakable anomaly, two threads, unstated without contradiction; patch-thickness ≥ 3, counted",
     "all patchable: demote to Level-2"),
    ("P1 Concept autopsy", "dependency graph + assumption census",
     "inherited concept at maximal severed-path weight, adjacent to the anomaly",
     "all load-bearing concepts tested: return to P0"),
    ("P2 Amputation", "amputated axioms + verified derivations",
     "confirmed core preserved; new structure forced",
     "decorative or fatal: return to P1"),
    ("P3 Dictionary attack", "dictionary + residue list + compression measure",
     "residue non-empty; compression positive",
     "perfect translation: reformulation, stop"),
    ("P4 Invariance and constant", "invariance statement + dimensional analysis",
     "one-sentence invariance; a constant forced or promoted — fitted at birth, paying later",
     "a fitted constant that never promotes: patch, stop"),
    ("P5 Limit-case inversion", "limit derivation + discriminating list",
     "predecessor computed as a limit; at least one measurable difference",
     "no limit, or no difference: stop"),
    ("P6 Semantic assignment", "operational dictionary of primitives",
     "every primitive has a measurement story; zero mixed vocabulary",
     "sense leans on deleted concept: return to P2"),
    ("P7 Adversarial closure", "defense + rebuttal, harvest list, successor crisis; tools where required",
     "defense answered; harvest ≥ 10 programs, disjoint question sets; deeper crisis named",
     "closure without opening: terminal, stop"),
]

TABLE6_CAPTION = ("Table 6 — Gate summary, amended: every phase still demands "
                  "one machine-checkable artifact; the counting rule, "
                  "severed-path weight, promotion test, and harvest criterion "
                  "are new in v1.1.")

CH4_CLOSE_V11 = (
    "The gates share one design decision worth making explicit, because it "
    "is the manual's concession to its operator. Human protocols leave "
    "adjudication to seniority and taste; this one leaves it to file "
    "structure, because the operator's taste is precisely the thing the "
    "gates exist to bypass. A language model can argue any position "
    "fluently, including the position that its own gate is passed; what "
    "it cannot fluently fake is a residue-marked dictionary with an empty "
    "residue column, a limit derivation that recomputes differently, or a "
    "harvest list that stalls at six. The protocol therefore stakes "
    "everything on artifact structure, and the three numbers below are the "
    "fences the operator lives inside — stated now, per Amendment A2, as "
    "the administrative parameters they always were: eight gates, one per "
    "phase, the machine unchanged; three kills at any one of them ending "
    "the target with a post-mortem, a stated policy and not a law of "
    "nature; and a harvest floor with a criterion, revisable by the log. "
    "Everything else in the manual is commentary on those fences, and the "
    "fences themselves are on the record as revisable.")

CALLOUT_NUMS_V11 = [
    ("8", "gates, one per phase — unchanged",
     "the audit added no phase; the anti-epicycle rule held"),
    ("3", "kills end a target — a parameter",
     "stated policy, revisable per campaign, provenance logged"),
    ("10", "programs — a parameter, now defined",
     "distinct = disjoint question sets; the floor is policy"),
]

CALLOUT_CAPTION_V11 = ("The protocol's own numbers, demoted per Amendment A2 "
                       "to what they always were: administrative parameters "
                       "with stated provenance.")
