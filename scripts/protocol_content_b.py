# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol' — part B: Chapter 3, the pipeline."""

# ---------------------------------------------------------------------------
# Chapter 3 — The Pipeline: Eight Phases, Eight Gates
# ---------------------------------------------------------------------------

CH3_INTRO = [
    ("The pipeline is the manual's operating system: eight phases, P0 through "
     "P7, each ending in a gate, each gate carrying one pass condition, one "
     "kill condition, and a return-target for the kill. A pass advances the "
     "campaign to the next phase; a kill sends it back — with the partial "
     "exception of the terminal gates G3 through G5, whose kills are usually "
     "fatal because the failures they detect (perfect translation, fitted "
     "constants, missing limits) are diagnoses of the idea rather than of the "
     "search. Figure 1 shows the whole machine; Table 2 compresses it to a "
     "reference card; the sections below state each phase as an operator "
     "instruction — objective, procedure, artifact, gate — in the order the "
     "work is done. The phases are not a schedule but a dependency chain: "
     "nothing stops an operator from drafting a dictionary before finishing an "
     "autopsy, but nothing at G3 will count until the autopsy file exists."),

    ("Two reading rules keep the pipeline honest. First, the gates are checks, "
     "not judgments: each is phrased so that a process which does not believe "
     "the operator's claims can evaluate them — a count, a computation, a "
     "residue either marked or absent. Second, every phase's artifact is "
     "cumulative with the earlier ones; the closure dossier at P7 quotes the "
     "ledger from P0, the census from P1, the amputated axioms from P2, and the "
     "derivations from P4 and P5, so that the final document is an audit trail "
     "rather than a performance. The whole design serves the asymmetry stated "
     "in Chapter 1: the protocol cannot force a breakthrough, but it can force "
     "the operator to be exactly as wrong as they are, no more, and to find it "
     "out at the cheapest possible moment."),
]

FIG1_CAPTION = ("Figure 1 — The L3 Protocol pipeline. Phases run downward in two "
                "columns; every gate carries a pass condition and a kill with its "
                "return-target. Passes are expensive; kills are cheap.")

CH3_P0 = [
    ("<b>P0 · Crisis cartography — find the strain.</b> The objective is to "
     "locate live strain between data and vocabulary, which is not where open "
     "problems live. Open problems — the ones the field poses at its annual "
     "meetings — are by construction stated in the current language, and the "
     "signature of profundity's preconditions is instead the anomaly that is "
     "measured accurately but cannot be said without embarrassment. Build the "
     "anomaly ledger: enumerate reproducible results that the field treats as "
     "ignored footnotes, special cases awaiting cleanup, or measurement "
     "problems that will resolve themselves. Classify each entry three ways: "
     "a missing constant (a Level-2 candidate, as Neptune was for the "
     "irregularities of Uranus), a missing entity (Level-1, as the Higgs was "
     "for the standard model's bookkeeping), or <i>unspeakable</i> — the result "
     "can be measured but not stated in the framework's vocabulary without "
     "contradiction, as the blackbody spectrum was measured to high precision "
     "years before anyone could say it, and as the stability of the atom was "
     "flatly impossible rather than merely unexplained. Then estimate "
     "patch-thickness: count the free parameters the field has already spent "
     "absorbing the anomaly. The ether program had accumulated the "
     "Lorentz-FitzGerald contraction, its ad hoc deformation hypothesis, and "
     "several auxiliary assumptions by 1905; a rising patch-thickness is the "
     "cheapest indicator that a program is degenerating toward its vocabulary "
     "rather than merely missing a piece."),

    ("The gate follows from the classification. <b>G0 passes</b> when the "
     "ledger contains at least one anomaly classified unspeakable, with "
     "patch-thickness of three or more and no consensus resolution in sight. "
     "<b>G0 kills</b> the campaign — or rather, demotes it — when every anomaly "
     "is patchable in principle: that is the signature of a Level-2 program, "
     "and the honest response is to run it as one, outside this protocol. The "
     "commonest beginner's error is inverted targeting: choosing an anomaly "
     "because it is famous rather than because it is unspeakable. Fame "
     "measures the size of the problem; unspeakability measures the depth of "
     "the strain. The ledger ranks by the second, never the first."),
]

CH3_P1 = [
    ("<b>P1 · Concept autopsy — find what to delete.</b> The objective is to "
     "identify the surgery site: the constitutive concept whose revision the "
     "anomaly is a symptom of. Extract the field's concept inventory — its "
     "undefined primitives and load-bearing definitions, the terms every "
     "paper uses and no paper earns. Build the dependency graph on them: "
     "which claims presuppose which concepts, and how much downstream weight "
     "each concept carries. Then run the separation that everything else "
     "depends on: tested versus inherited. A tested concept has survived "
     "independent verification; an inherited one was never verified at all — "
     "it was imported from everyday intuition or from a previous framework "
     "and left in place because nobody's attention ever fell on it. Absolute "
     "time was inherited from experience; the ether was inherited from "
     "medium-borne wave propagation; the two-worlds split between celestial "
     "and terrestrial matter was inherited from Aristotle, twenty centuries "
     "deep and load-bearing for all of astronomy; determinism was inherited "
     "as classical mechanics' unexamined default long after it had stopped "
     "being a finding. Inherited and maximally load-bearing is the profile "
     "of a Level-3 target."),

    ("Here the operator's native advantage is decisive, and the pipeline "
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
     "not surgical, and the ledger needs a better-targeted anomaly."),
]

CH3_P2 = [
    ("<b>P2 · Amputation — delete, and see what survives.</b> The objective is "
     "to determine whether the strain requires vocabulary surgery rather than "
     "one more patch, and the move is exactly the signature's first point "
     "converted into a procedure. Take the top-leverage inherited concept and "
     "delete it from the axioms. Do not assert that it is false; assert that "
     "it is <i>meaningless without an operational definition</i> — this is "
     "the Level-3 signature, distinguishing surgery from contradiction. "
     "Einstein did not prove absolute simultaneity false; he showed it was "
     "undefined until one specified a measurement procedure, then defined it "
     "with light signals and let the Lorentz transformations fall out of what "
     "survived. Write the survivors down: what remains of the theory when the "
     "concept is gone. The survivors must force new structure — if "
     "simultaneity is conventional, then the relativity principle plus "
     "Maxwell's invariance jointly force the new kinematics — and the forcing "
     "is the derivation you must produce, verified by symbolic computation, "
     "with no step permitted to rest on the phrase <i>it follows that</i>."),

    ("Two auxiliary moves complete the phase. The first is anomaly promotion, "
     "the Bohr move: when the ledger's anomaly is classified unspeakable, stop "
     "trying to derive it and promote it to an axiom instead. Bohr took the "
     "classically impossible stability of the atom and postulated stationary "
     "states; Planck took the classically impossible spectrum and installed "
     "the quantum of action as a premise. Promotion is not surrender — it "
     "converts the anomaly from a problem into a tool, and it is the correct "
     "response whenever derivation has genuinely exhausted itself. The second "
     "is the amputation audit, which checks the deletion for both failure "
     "modes. <b>G2 passes</b> when the deletion is conservative enough to "
     "preserve the confirmed core and radical enough to force new structure: "
     "new transformations, new composition laws, new quantization conditions. "
     "<b>G2 kills</b> in two directions — a deletion that changes no "
     "prediction was aimed at metaphysical decoration, and a deletion that "
     "destroys everything without forcing anything new was aimed at the wrong "
     "concept, and the campaign returns to P1 for a better-targeted autopsy."),
]

CH3_QUOTE_HEISENBERG = (
    "It seems sensible to discard all hope of observing hitherto unobservable "
    "quantities such as the position and period of the electron.",
    "Werner Heisenberg, on the move that became matrix mechanics, 1925 — the "
    "amputation, performed on schedule.")

CH3_P3 = [
    ("<b>P3 · Dictionary attack — mine the untranslatable.</b> The objective "
     "is the unification the signature's second point demands, made "
     "systematic instead of lucky. Choose the two domains the strain lives "
     "between: celestial and terrestrial mechanics before Newton; optics and "
     "mechanics before de Broglie — whose dictionary, it is worth recording, "
     "was sitting in Hamilton's papers for ninety years before anyone "
     "weaponized it; economics and natural history before Darwin read "
     "Malthus. Build the translation dictionary term by term: for each "
     "concept in domain A, its counterpart in domain B. Then mine the "
     "residue, because the residue is the whole point: entries with no "
     "counterpart are exactly where new concepts must be minted. <i>Planet</i> "
     "translated into <i>falling body</i> cleanly; <i>what holds the planets "
     "in place</i> had no translation until universal gravitation was minted "
     "to fill the gap. Frequency and energy resisted translation until h was "
     "installed as the exchange rate between them. The human <i>computer</i> "
     "— the clerk with pencil and rules — translated into machine only after "
     "Turing minted the universal machine at the residue between what the "
     "clerk does and what any existing device could do."),

    ("The dictionary must then pass the compression test: the unified "
     "framework has to be strictly smaller than the two domains side by "
     "side — one mechanics where there were two, one spacetime where there "
     "were space and time and an ether, one dynamics for rays and particles "
     "where there were two theories of light and matter. Compression is "
     "measurable, in axioms and in laws, and it is the honest form of the "
     "elegance the founders kept reporting. <b>G3 passes</b> when the residue "
     "is non-empty and the compression is positive — something minted, "
     "something saved. <b>G3 kills</b> fatally when the translation is "
     "perfect: a dictionary with no residue is the proof that the two "
     "domains already spoke one language, and whatever was built on that "
     "discovery is a reformulation — possibly beautiful, permanently "
     "Level-2 — and the campaign stops rather than loops."),
]

CH3_P4 = [
    ("<b>P4 · Invariance and constant prospecting — write the law at "
     "bedrock.</b> The objective is to state the surviving structure in the "
     "grammar deep laws are written in. Recast the candidate theory as an "
     "invariance claim: what remains unchanged under the transformation "
     "group the amputation and unification have installed. Mechanics is "
     "the same in the freely falling laboratory and on the Moon's orbit; "
     "the laws keep their form in every inertial frame; probability is "
     "conserved under every step the formalism allows. If the theory's "
     "content cannot be stated as what stays fixed while something else "
     "varies, then what one has is a description, and descriptions do not "
     "survive paradigm shifts. The discipline is one sentence: the "
     "invariance statement must be writable in a single line that a "
     "skeptical reader can check against cases — it is exactly this "
     "compressibility that made the founding principles teachable to "
     "schoolchildren within a generation of their publication."),

    ("Then prospect for the constant. Compute the dimensional conversion "
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
     "clothes, and no downstream gate can launder it."),
]

CH3_P5 = [
    ("<b>P5 · Limit-case inversion — pay the old theory.</b> The objective "
     "is the conservative embedding the signature demands, performed as a "
     "computation rather than a courtesy. Expand the candidate framework "
     "in the regime where the old theory was confirmed and derive the old "
     "law, with its constants and its successes, from the new one: the "
     "Lorentz transformations collapse to Galilean kinematics as v/c "
     "approaches zero, and the classical trajectory returns as h goes to "
     "zero — the small parameter the founders left in the formalism as a "
     "door for their ancestors. Bohr's correspondence principle is this "
     "phase used as a construction rule rather than a check: he built "
     "the quantum postulates under the constraint that large quantum "
     "numbers must reproduce classical radiation, and the constraint was "
     "load-bearing. The derivation must be symbolic and complete, and the "
     "re-entry of the deleted concept must be visible in it: simultaneity "
     "returns as an approximation valid exactly when the light-signal "
     "corrections are negligible, which is to say, in every laboratory "
     "Newton ever used."),

    ("The inversion then demands its payment: the discriminating list, "
     "which is where the new theory spends its difference from the old "
     "one. List the regimes where the two disagree and the disagreement "
     "is measurable in principle — the transverse Doppler shift for "
     "relativity, the precession of Mercury's perihelion at forty-three "
     "seconds of arc per century for gravitation, the fine structure of "
     "the spectral lines for the quantum, the return of Halley's comet "
     "and the shape of the Earth for Newton. A theory with no "
     "discriminating regime is empirically empty, however deep its "
     "vocabulary surgery, and an assertion that the old theory is "
     "“recovered in the limit” is exactly that — an assertion — until "
     "the expansion exists as a file. <b>G5 passes</b> when the limit "
     "derivation is computed and at least one discriminating regime is "
     "specified. <b>G5 kills</b> fatally in either absence: no derivable "
     "limit means the structure is wrong or incomplete, and no "
     "measurable difference means it is not a theory at all."),
]

CH3_P6 = [
    ("<b>P6 · Semantic assignment — make it mean a world.</b> The objective "
     "is to complete the step at which the Lorentz program failed: formalism "
     "can precede meaning, but unless meaning arrives the equations remain "
     "a coordinate change and the revolution does not happen. Einstein's "
     "1905 paper opens with the operational question — what procedure "
     "synchronizes two clocks — and answers it before a single dynamical "
     "equation appears; that ordering is the phase. For every primitive of "
     "the new formalism, write the measurement story: what a competent "
     "observer does, with what instrument, to assign the primitive a "
     "number. Born's rule gave the squared amplitude its story; "
     "Heisenberg's microscope gave the uncertainty relations theirs; "
     "without those stories the formalism of 1925–26 was, as its own "
     "authors admitted, a bookkeeping device whose referent was unknown. "
     "A primitive without a story is not yet a concept, and a theory "
     "whose primitives all lack stories is a notation, not physics."),

    ("The phase carries one strict discipline: the mixed-vocabulary ban. "
     "No sentence of the finished theory may combine the new primitives "
     "with the deleted ones — once simultaneity is operational, "
     "“really simultaneous” is unsayable; once outcomes are "
     "probabilistic, “the electron really had a position” is unsayable "
     "inside the theory. The ban is what makes the revision a vocabulary "
     "surgery rather than an appended interpretation: a theory that "
     "needs the deleted concept in half its sentences has not amputated "
     "it, only insulted it. <b>G6 passes</b> when every primitive carries "
     "a measurement story and a full audit of the theory's statements "
     "finds zero mixed-vocabulary sentences. <b>G6 kills</b> back to P2 "
     "when primitives only make sense relative to the deleted concept: "
     "the surgery was incomplete, and the cut must go deeper."),
]

CH3_P7 = [
    ("<b>P7 · Adversarial closure — resist it, then enumerate it.</b> The "
     "objective is to pay the signature's three closing points while there "
     "is still time to be changed by them. The first artifact is the "
     "self-play defense: write the strongest defense of the old paradigm "
     "against the new theory — the one its best contemporary would have "
     "written, not a strawman assembled for the pleasure of burning it. "
     "Newton's defenders called action at a distance an occult quality "
     "and meant it; Lorentz accepted the transformations to his death and "
     "refused the relativity of simultaneity; Einstein spent thirty years "
     "arguing that the quantum's randomness could not be nature's last "
     "word. These were not fools — they were the strongest objections the "
     "old vocabulary could field, and the historical founders could not "
     "always answer their own. The defense must be written at that "
     "strength, and then answered; a candidate that survives only because "
     "no serious attack was attempted has survived nothing, and the "
     "calibration is discomfort — if the defense reads comfortably "
     "refutable, it was not written at full strength."),

    ("The second artifact is the harvest enumeration: before claiming the "
     "framework, list at least ten distinct downstream programs it should "
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
     "reconciliation with gravity, a century on. <b>G7 passes</b> when "
     "all three artifacts are complete and non-trivial. <b>G7 kills</b> "
     "when the framework answers everything and opens nothing: a theory "
     "that closes the world is terminal, and profundity is measured by "
     "what it makes next possible."),
]

TABLE2_HEADER = ["Phase", "Artifact required", "Gate — pass condition",
                 "Kill — and return"]

TABLE2_ROWS = [
    ("P0 Crisis cartography", "anomaly ledger",
     "an unspeakable anomaly; patch-thickness ≥ 3",
     "all patchable: demote to Level-2"),
    ("P1 Concept autopsy", "dependency graph + assumption census",
     "inherited concept of maximal weight, adjacent to the anomaly",
     "all load-bearing concepts tested: return to P0"),
    ("P2 Amputation", "amputated axioms + verified derivations",
     "confirmed core preserved; new structure forced",
     "decorative or fatal: return to P1"),
    ("P3 Dictionary attack", "dictionary + residue list + compression measure",
     "residue non-empty; compression positive",
     "perfect translation: reformulation, stop"),
    ("P4 Invariance and constant", "invariance statement + dimensional analysis",
     "one-sentence invariance; a forced, independently measurable constant",
     "a fitted parameter: patch, stop"),
    ("P5 Limit-case inversion", "limit derivation + discriminating list",
     "predecessor computed as a limit; at least one measurable difference",
     "no limit, or no difference: stop"),
    ("P6 Semantic assignment", "operational dictionary of primitives",
     "every primitive has a measurement story; zero mixed vocabulary",
     "sense leans on deleted concept: return to P2"),
    ("P7 Adversarial closure", "defense + rebuttal, harvest list, successor crisis",
     "defense answered; harvest ≥ 10; deeper crisis named",
     "closure without opening: terminal, stop"),
]

TABLE2_CAPTION = ("Table 2 — Gate summary: every phase demands one "
                  "machine-checkable artifact; pass and kill are stated as "
                  "checks, not judgments.")

CH3_CLOSE = [
    ("The gates share one design decision worth making explicit, because it "
     "is the manual's concession to its operator. Human protocols leave "
     "adjudication to seniority and taste; this one leaves it to file "
     "structure, because the operator's taste is precisely the thing the "
     "gates exist to bypass. A language model can argue any position "
     "fluently, including the position that its own gate is passed; what "
     "it cannot fluently fake is a residue-marked dictionary with an empty "
     "residue column, a limit derivation that recomputes differently, or a "
     "harvest list that stalls at six. The protocol therefore stakes "
     "everything on artifact structure, and the three numbers below are the "
     "fences the operator lives inside: eight gates, one per phase; three "
     "kills at any one of them ends the target and demands a post-mortem; "
     "ten downstream programs are the floor beneath which no framework may "
     "be claimed as profound-compatible. Everything else in the manual is "
     "commentary on those fences."),
]
