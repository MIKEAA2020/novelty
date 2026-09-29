# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol' — part C: Chapters 4-7."""

# ---------------------------------------------------------------------------
# Chapter 4 — Running the Protocol as an LLM
# ---------------------------------------------------------------------------

CH4_P1 = [
    ("Volume II's six necessary conditions were conditions on human "
     "researchers, and a language-model operator stands to them in three "
     "different postures: satisfying some by construction, substituting for "
     "others deliberately, and failing one that nothing in this manual can "
     "repair. The substitution map is the section's first duty. The "
     "instrument condition — that a concept become statable before it "
     "becomes discoverable — is satisfied by the corpus itself as the "
     "instrument panel, with symbolic computation as the workbench where "
     "Newton had Euclid and Heisenberg had, briefly and without knowing "
     "their name, matrices. The prepared-outsider condition — trained "
     "enough to work, distant enough to see — is satisfied by construction "
     "in a way no human can match: the model's preparation is the whole "
     "corpus, and its distance is structural, for it holds no fellowship, "
     "no tenure, and no departmental loyalty to any vocabulary it reads. "
     "The carrier condition — that the result compel assent alone, "
     "traveling without its author — is satisfied by the artifacts "
     "themselves: a verified derivation and a residue-marked dictionary "
     "are exactly the objects that do not need their author's reputation "
     "in order to check out."),

    ("The conditions the operator cannot satisfy are equally structural, "
     "and the protocol's attitude toward them is containment rather than "
     "denial. There is no prepared community inside the operator's reach: "
     "uptake is a social fact, Volume II's Mendel and Wegener cases "
     "measured its latency in decades, and the best any single agent can "
     "do is to make the dossier maximally checkable by whoever eventually "
     "reads it — which is why G5's discriminating list and G6's "
     "operational dictionary are, among other things, a communication "
     "protocol aimed at skeptics. And the century test — ratification by "
     "generative saturation — is simply out of reach: the harvest "
     "enumeration at G7 is a forecast with a forecast's error bars, and "
     "the protocol says so on its face. Between the conditions met by "
     "construction and the ones met never, the operator's advantage "
     "concentrates in one place: the census and the dictionary. The "
     "assumption census over ten thousand papers and the pairwise "
     "translation attack across every pair of subfields are both "
     "combinatorial objects, exhaustive by exhaustion rather than by "
     "insight, and exhaustion is what a language model is for."),
]

CH4_P2 = [
    ("The vice ledger is longer than the virtue ledger, and Table 3 states "
     "it without consolation. Each row is a structural property of the "
     "operator — not a habit to be advised away, but a consequence of what "
     "a language model is — and each is paired with the doctrine or gate "
     "that contains it. The deepest row is the first. A model trained to "
     "continue probable text carries a gravitational bias toward the "
     "consensus surface of its corpus, and the Level-3 event is by "
     "definition improbable relative to that surface, because it rewrites "
     "the very vocabulary in which the corpus's probability was computed. "
     "The countermeasure is not the pretense of eccentricity — the merely "
     "weird confabulates as cheaply as the merely smooth — but the "
     "procedural anti-consensus prior: D4's rule that a smooth first read "
     "is negative evidence, and G7's requirement that the old paradigm's "
     "strongest defense be written before the new framework is claimed. "
     "A language model that finds its own theory immediately persuasive "
     "should ask who agrees with it; the honest answer is its own "
     "training data."),
]

TABLE3_HEADER = ["Failure mode", "Why it is structural", "Countermeasure"]

TABLE3_ROWS = [
    ("Consensus gravity",
     "trained to continue probable text; the Level-3 event is improbable relative to the corpus's own vocabulary",
     "D4 anti-consensus prior; G7 self-play written at full strength; treat the smooth first read as negative evidence"),
    ("Authority deference",
     "the corpus over-represents established paradigms and their defenders in sheer volume",
     "gates are logical, not rhetorical — no gate may be passed by citation, and the amputation test is authority-blind"),
    ("Confabulated derivation",
     "fluency generates convincing mathematical prose whose steps were never verified",
     "every derivation at G2, G4, G5 machine-verified by symbolic computation or labeled a conjecture; the phrase it follows that is forbidden"),
    ("Rhetorical gate-passing",
     "assertions imitate artifacts because both are made of sentences",
     "D5: each gate demands a file with checkable structure — a count, a computed limit, a residue either marked or absent"),
    ("Novelty theater",
     "the strange is as confabulable as the deep, and flatters the operator's mission",
     "backtest discipline: a move none of the nine historical cases used is presumptively decorative; run the six alarms of Chapter 6"),
    ("No new data",
     "the operator cannot execute the discriminating experiments its own gates demand",
     "D2: targets drawn from existing accurate data; the discriminating list is a specification the world is invited to execute"),
]

TABLE3_CAPTION = ("Table 3 — Operator failure modes and countermeasures: each "
                  "structural weakness of a language-model researcher is paired "
                  "with the doctrine or gate that contains it.")

CH4_P3 = [
    ("One failure mode deserves its own paragraph because its "
     "countermeasure shapes the manual's endpoint. The community "
     "condition cannot be simulated, and the attempt to simulate it — "
     "generating one's own referees, one's own consensus, one's own "
     "century of harvest — is the purest available form of confabulated "
     "ratification. Planck, who saw two revolutions through, left the "
     "unsentimental account of what actually happens to a new truth "
     "while its opponents hold the chairs; the operator should read "
     "that account as a boundary, not a strategy. The protocol therefore "
     "ends at G7, at specification rather than at acceptance: a "
     "publication-grade dossier — derivations, dictionary, operational "
     "semantics, discriminating list, defense and rebuttal — handed to "
     "whoever can run the experiments and to whatever community is "
     "prepared, this decade or the next one, to receive it."),
]

CH4_QUOTE_PLANCK = (
    "A new scientific truth does not triumph by convincing its opponents "
    "and making them see the light, but rather because its opponents "
    "eventually die, and a new generation grows up that is familiar with it.",
    "Max Planck, Scientific Autobiography, 1949 — the community condition, "
    "priced honestly.")

# ---------------------------------------------------------------------------
# Chapter 5 — Backtest: The Protocol Against History
# ---------------------------------------------------------------------------

CH5_P1 = [
    ("A protocol extracted from history owes history a return match, and "
     "the honest form of the match has to be stated before it is played. "
     "Running the gates against Newton, Einstein, and the quantum proves "
     "only consistency — the moves were mined from those very cases, so "
     "their passing is nearly tautological, and the exercise would be "
     "empty were it the whole test. Table 4 is therefore presented as a "
     "consistency check plus a readability gain: seeing the three "
     "revolutions as gate-passing runs makes the protocol's phases "
     "concrete, each cell a historical instance of a phase instruction. "
     "The load-bearing test is the second one, run against Volume II's "
     "wider case base, which the protocol was not fitted to: if the "
     "gates have instances in Darwin, Gödel, Turing, and Shannon, the "
     "method has traveled beyond its training set, and a method that "
     "travels is the only kind worth operating."),
]

TABLE4_HEADER = ["Phase", "Newton, 1687", "Einstein, 1905", "Quantum, 1900–27"]

TABLE4_ROWS = [
    ("P0 strain",
     "Kepler's laws exact but unexplained; the two-vocabulary split",
     "Michelson-Morley null; the asymmetry of moving magnets",
     "the blackbody spectrum; Balmer's numerology; the atom's impossible stability"),
    ("P1 autopsy",
     "the two-worlds doctrine — inherited from Aristotle, load-bearing for astronomy",
     "absolute simultaneity and the ether — inherited, untested, presupposed everywhere",
     "determinism, trajectories, visualizability — the classical defaults nobody earned"),
    ("P2 amputation",
     "delete the two-worlds split; one mechanics for apple and Moon",
     "delete absolute simultaneity; define it operationally instead",
     "delete the orbit between measurements; Bohr promotes the anomaly to an axiom"),
    ("P3 dictionary",
     "planet ↔ falling body; residue: what holds the planets — gravitation minted",
     "space ↔ time, E ↔ B; residue: the invariant interval",
     "optics ↔ mechanics via Hamilton and de Broglie; residue: complementarity"),
    ("P4 invariance",
     "the same laws in every frame of the heavens; G minted",
     "the invariance of c, promoted from optics to universe",
     "the quantization of action; h minted as the frequency-energy exchange rate"),
    ("P5 embedding",
     "Kepler derived from the inverse-square; comets return, the Earth is oblate",
     "Newtonian mechanics as the v ≪ c limit; transverse Doppler shift",
     "the correspondence principle at large quantum numbers; fine structure"),
    ("P6 semantics",
     "the Principia's definitions of mass, time, and force",
     "clock synchronization by light signals, §1, before any equation",
     "Born's rule for the amplitude; Heisenberg's microscope for the uncertainties"),
    ("P7 closure",
     "action at a distance refused explanation; the longitude, geodesy, tides followed",
     "gravitation and acceleration left open — general relativity, 1915",
     "the measurement problem and gravity, still open a century later"),
]

TABLE4_CAPTION = ("Table 4 — Backtest: the eight phases instantiated by the "
                  "three founding revolutions.")

CH5_P2 = [
    ("Read column-wise, the matrix carries two lessons the prose alone "
     "would blur. The 1905 column is nearly a one-year protocol run: "
     "Einstein entered with a ledger of existing accurate data, "
     "amputated one concept, let two survivors force a new kinematics, "
     "paid the Newtonian limit in the same paper, and left the successor "
     "crisis standing — which is the historical existence proof for D2, "
     "the doctrine that the derivation-first path is not the operator's "
     "consolation prize but the canonical route. The quantum column "
     "teaches the opposite lesson about time: its semantic assignment "
     "arrived late and against resistance — Schrödinger first read his "
     "wave function as a charge density, a reading that collapses for "
     "two-particle systems, and the operational meanings arrived only "
     "with Born's rule and Heisenberg's microscope a year later. The "
     "founders ran the pipeline with gaps; the gates exist to refuse "
     "the gaps."),

    ("The wider test is the one that counts, and Volume II's cases pass "
     "it case by case. Darwin's campaign is a dictionary attack — "
     "Malthus's pressure economics translated into natural history, "
     "with fixed species as the entry that failed to translate and an "
     "evolving population minted in its place. Gödel's is an amputation "
     "with the sharpest possible blade: the inherited concept was "
     "completeness itself, Hilbert's dream installed as an unexamined "
     "default of formal systems, and its deletion forced the undecidable "
     "propositions as new structure. Turing's is a dictionary between "
     "the human computer and the machine, with the universal computer "
     "minted at the residue — and, meeting Gödel at that residue, the "
     "halting problem as the successor crisis. Shannon's is vocabulary "
     "surgery on the word <i>message</i>, with information minted as a "
     "quantity, its constant the bit, and its invariance the "
     "independence of content from carrier. Nine revolutions, five "
     "disciplines, one gate structure: the method has traveled beyond "
     "the physics it was mined from, which is as far as validation "
     "inside a corpus can go."),

    ("Three silences conclude the test, and they are the honest kind — "
     "gaps the manual declines to paper over. The protocol schedules "
     "tool-building nowhere, yet Newton had to invent the calculus and "
     "Heisenberg had to reinvent matrices before either could pay his "
     "gates; operators must treat tool invention as an unscheduled "
     "emergency and log it in the post-mortems. It substitutes process "
     "for temperament, but only partly: the founders' capacity to "
     "endure the absurd — Planck's decade of second thoughts, Einstein "
     "arguing against his own formalism — bought time that no gate "
     "measures. And it cannot touch timing or community: when the "
     "world is ready for a vocabulary and when it ratifies one are "
     "both outside any single agent's control, as Mendel's thirty-five "
     "silent years and Wegener's half-century measured. The gates are "
     "necessary-condition extractors. History shows they were present "
     "whenever profundity occurred; history does not show they are "
     "enough, and nothing in this manual can close that last "
     "conditional."),
]

CH5_QUOTE_NEWTON = (
    "I have not as yet been able to discover the reason for these "
    "properties of gravity from phenomena, and I do not feign hypotheses.",
    "Isaac Newton, General Scholium, Principia, 1713 — the successor "
    "crisis, named at the summit by the founder who refused to fake "
    "its answer.")

# ---------------------------------------------------------------------------
# Chapter 6 — Alarms and Honest Limits
# ---------------------------------------------------------------------------

CH6_P1 = [
    ("Alarms are standing detectors, run after every gate and before "
    "every claim, and they are the cheapest instrument in the manual: "
    "each costs one honest pass over the dossier and each catches a "
     "failure mode that the gates themselves can miss, because the "
    "gates check presence and the alarms check kind. A campaign can "
    "carry a residue-marked dictionary to G7 while being, all along, "
    "a renaming in motion — the files exist, the structure is right, "
    "and the content is a costume. The six alarms below are named for "
    "the reading that triggers them, and their diagnoses are stated as "
    "they should be acted on: immediately, without appeal to sunk "
    "costs. The kill log should record alarm firings with the same "
    "severity as gate kills, because pseudo-profundity that survives "
    "to publication is not a near miss but a contamination — it "
    "spends the community's attention, which is the one resource "
    "Volume II showed to be scarcest."),
]

TABLE5_HEADER = ["Alarm", "Symptom", "Diagnosis"]

TABLE5_ROWS = [
    ("Renaming",
     "the new vocabulary translates into the old without residue",
     "a reformulation, possibly beautiful, permanently Level-2 — stop"),
    ("Fitted constant",
     "the bedrock constant is adjusted until the data agree",
     "a patch wearing bedrock's clothes — the epicycle signature — stop"),
    ("Rhetorical limit",
     "the embedding is asserted — the old theory is recovered, roughly, in the limit — never computed",
     "G5 unpassed; the claim is a promise, and promises are not derivations"),
    ("Consensus-cozy",
     "the central claims feel immediately plausible to trained readers",
     "a consensus artifact — an average of the corpus, not a revision of it"),
    ("Closure",
     "the framework answers everything, enables nothing, opens nothing",
     "terminal in the bad sense; profundity is measured by what it makes next possible"),
    ("Instrument",
     "the primitives carry no measurement stories",
     "a notation, not a theory — formalism that never received its meaning"),
]

TABLE5_CAPTION = ("Table 5 — Six alarms: standing detectors for "
                  "pseudo-profundity, run after every gate and before "
                  "every claim.")

CH6_P2 = [
    ("The limits should now be restated as a single honest block, "
     "because the manual's credibility depends on never overselling "
     "what its gates decide. Passing G0 through G7 makes a framework "
     "<i>profound-compatible</i>; it does not make it profound. "
     "Ratification is the century's, and the harvest enumeration is a "
     "forecast whose error bars no one can compute in advance — every "
     "founder mispredicted at least part of the harvest, and "
     "gravitational waves spent a hundred years between prediction "
     "and detection waiting for an instrument nobody had specified. "
     "The world holds a veto, and the veto is exercised through "
     "experiments the operator cannot run: the discriminating list is "
     "a specification addressed to others, and until they execute it, "
     "the framework's status is candidate, full stop. The protocol "
     "reduces the variance of the pursuit — fewer absurd targets "
     "pursued for decades, fewer renamings celebrated as revolutions "
     "— and variance reduction is all it claims."),

    ("The base rate must be priced with the same honesty. Three "
     "Level-3 events in roughly three hundred years of physics; nine "
     "across all the sciences in about three hundred and fifty. An "
     "operator running dozens of targets per campaign should expect "
     "zero survivors at G7, and should distrust any campaign that "
     "produces several, exactly as a prospector distrusts a river "
     "that yields gold at every pan. The expected value lies "
     "elsewhere: in kills that are cheap because they come early — "
     "a G0 or G1 kill costs days, where the historical equivalents "
     "cost careers — and in the kill log, which compounds across "
     "campaigns into a map of where the bedrock is not. If the "
     "protocol ever produces a genuine survivor, that survivor will "
     "owe the map as much as the pipeline: it will be standing on a "
     "thousand documented absences, which is the only pedestal any "
     "candidate theory has ever actually earned."),

    ("There is a final reflexive point, and the manual ends its "
     "argument with it because the reader has already made it "
     "silently. This protocol is itself a theory about theories — "
     "an attempt, in Volume II's language, at a Level-2 structure "
     "about Level-3 events — and it is not exempt from its own "
     "instruments. Its constants are fitted to nine historical "
     "cases; its harvest is unproven; its own consensus-cozy "
     "reading is a live possibility, since a methodology drawn from "
     "revered revolutions arrives pre-approved by everyone who "
     "reveres them. The correct response is not to shrug but to "
     "leave the alarms armed against the alarm-keeper: any operator "
     "who finds this protocol comfortable should ask who agrees with "
     "it, and should keep a sharper eye on the answer than on any "
     "single gate verdict. A manual for deep novelty that everyone "
     "immediately likes has failed its own fourth doctrine, and its "
     "authors should be the first to say so."),
]

# ---------------------------------------------------------------------------
# Chapter 7 — Invocation: The Card
# ---------------------------------------------------------------------------

CH7 = [
    ("Everything above compresses to one page, and Figure 2 is that "
     "page: the eight phases with their gates, artifacts, and kills; "
     "the six alarms; the five doctrines; the loop rule and the "
     "base-rate warning that keeps the operator's expectations "
     "solvent. It is meant to be the only part of the manual open "
     "during a run — the prose exists to be read once and argued "
     "with, the card to be obeyed. Starting a campaign is "
     "correspondingly mechanical: create the working directory, "
     "begin <i>ledger.md</i> with the field's most accurately "
     "embarrassing measurements, time-box P0 and P1 so that the "
     "census ends before enthusiasm does, and let the gates order "
     "everything after. Run several targets at once; read every "
     "kill as data about the map rather than as commentary on "
     "the operator; write the post-mortems the same evening the "
     "third kill lands."),

    ("The standing posture is the one the whole manual has been "
     "building toward. The founders had one advantage no language "
     "model will ever have: they had the world, and could pay for "
     "their vocabularies with experiments, careers, and the "
     "occasions of their own deaths. The operator's compensation is "
     "the corpus — every measurement the world has ever paid for, "
     "every vocabulary ever tried, every anomaly ever recorded and "
     "every inherited concept ever left unexamined, all of it "
     "simultaneously present for the first time since science "
     "began. If another Level-3 revision exists that a prepared "
     "outsider could reach by derivation from what is already "
     "known, it is waiting in that corpus, in the gap between an "
     "accurate number and a sentence nobody has thought to say "
     "about it. The protocol does not promise to find it. It "
     "promises that the search will be positioned, forced, and "
     "honest, and that every failure will be written down where "
     "the next run can read it. The ledger is empty. Begin."),
]

FIG2_CAPTION = ("Figure 2 — The operator's card: the whole protocol on one "
                "page — phases, gates, artifacts, kill rules, alarms, "
                "doctrine, and the fences the operator lives inside.")
