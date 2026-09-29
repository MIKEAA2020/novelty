# -*- coding: utf-8 -*-
"""Content module for 'Profound Novelty: A Study by Example'.

Chapter numbering plan (Step 3.5):
| Outline Index | Type    | Chapter # | Title                                        |
|---------------|---------|-----------|----------------------------------------------|
| 1             | cover   | -         | Cover (separate Playwright PDF, merged)      |
| 2             | toc     | -         | Contents                                     |
| 3             | content | 1         | The Program: Studying Novelty by Diff        |
| 4             | content | 2         | A Ladder for Measuring Novelty               |
| 5             | content | 3         | Newton, 1687: Two Worlds Become One          |
| 6             | content | 4         | Einstein, 1905-1915: The Demotion of Space   |
| 7             | content | 5         | Quantum, 1900-1927: The Death of Determinism |
| 8             | content | 6         | The Anatomy of Profound Novelty              |
| 9             | content | 7         | What Profound Novelty Is Not                 |
| 10            | content | 8         | Conclusion: The Signature Distilled          |
"""

DOC_TITLE = "Profound Novelty: A Study by Example"
DOC_SUBJECT = ("A comparative study of profound novelty, read through the state of "
               "physics before and after Newton, Einstein, and the quantum.")

# ---------------------------------------------------------------------------
# Chapter titles (numbered as displayed)
# ---------------------------------------------------------------------------

CHAPTERS = [
    ("1", "The Program: Studying Novelty by Diff"),
    ("2", "A Ladder for Measuring Novelty"),
    ("3", "Newton, 1687: Two Worlds Become One"),
    ("4", "Einstein, 1905–1915: The Demotion of Space and Time"),
    ("5", "Quantum, 1900–1927: The Death of Determinism"),
    ("6", "The Anatomy of Profound Novelty"),
    ("7", "What Profound Novelty Is Not"),
    ("8", "Conclusion: The Signature Distilled"),
]

# ---------------------------------------------------------------------------
# Chapter 1
# ---------------------------------------------------------------------------

CH1 = [
    ("Novelty is cheap; every year produces it in bulk. Profound novelty — the kind "
     "that reorganizes a field for centuries — is vanishingly rare, and stubbornly hard "
     "to define in the abstract. Rather than define it, this study tries to catch it in the "
     "act. Physics offers three unusually clean cases: the state of the science immediately "
     "before and after Newtonian mechanics (1687), Einstein’s relativity (1905–1915), "
     "and quantum mechanics (1900–1927). In each case the “before” and "
     "“after” snapshots are well documented, the claims are precise, and the stakes "
     "— what may be thought — are about as high as stakes get."),

    ("The method is a diff, in the programmer’s sense: two snapshots of the same subject, "
     "compared line by line to see exactly what changed, what was deleted, what survived "
     "untouched, and what stopped making sense. Biography and priority disputes appear only "
     "where they carry analytical weight. What interests us is not who discovered what, or "
     "when, but what <i>kind</i> of change each episode actually was. A chronology of physics "
     "lists events; a diff of physics classifies them."),

    ("Three clarifications before we begin. First, the lens is fixed in advance — a "
     "three-level ladder of novelty depth (Section 2), so the cases can be compared on one "
     "scale rather than admired as isolated marvels. Second, the study is deliberately "
     "internal to physics; whether the same signature appears in Darwin’s biology or "
     "Gödel’s mathematics is a question this study equips us to ask, not one it "
     "answers. Third — the honest caveat — these three cases are the survivors, "
     "selected by history. A signature derived only from successes risks mistaking luck for "
     "structure; Section 7 therefore tests it against near-misses and failures before the "
     "conclusion is allowed to trust it."),
]

# ---------------------------------------------------------------------------
# Chapter 2
# ---------------------------------------------------------------------------

CH2_P1 = ("Not all new things are new in the same way, so begin with a measuring instrument: "
          "a ladder of three levels. <b>Level 1 is new phenomena</b> — facts about the "
          "world that were previously unknown: an anomaly in an instrument, an unexplained "
          "regularity, an object no one had seen. This is novelty of <i>content</i>. "
          "<b>Level 2 is new laws</b> — relations that connect the phenomena: equations, "
          "mechanisms, causal structures into which the facts can be organized. This is "
          "novelty of <i>structure</i>. <b>Level 3 is new meta-concepts</b> — changes "
          "not in what the laws say but in what the laws are written <i>with</i>: the meanings "
          "of space, time, cause, state, observation, explanation. This is novelty of "
          "<i>vocabulary</i>.")

CH2_P2 = ("The claim this study will test is that what we call profundity tracks Level 3, "
          "and only Level 3. Most of what any generation calls innovation — including "
          "very good innovation — stays on Levels 1 and 2: it fills slots in a structure "
          "that stands. A new planet is Level 1; a new equation is Level 2. What none of the "
          "three revolutions studied here did was merely fill a slot. Each rewrote the grammar "
          "in which physics questions had to be asked — and profundity, we will argue, "
          "is the name for exactly that.")

CH2_P3 = ("Two caveats keep the instrument honest. The ladder is applied after the fact, "
          "not a historical claim that discoveries descend one rung at a time — the "
          "actual histories are far messier, as the twenty-seven-year quantum crisis will "
          "show. And the levels do not rank difficulty or importance: hunting the Higgs boson "
          "(Level 1, 2012) took more money and more machine than anything in this essay. The "
          "ladder measures exactly one thing — how deep in the conceptual stack the "
          "change reaches.")

CH2_P4 = ("For each case study the same five axes are compared: the <b>world-picture</b> "
          "(what exists), the <b>causal principle</b> (how things act), the "
          "<b>mathematics</b> (what form laws take), the <b>status of the triggering "
          "evidence</b> (what happens to the data that forced the crisis), and the "
          "<b>founder’s sacrifice</b> (what the author had to abandon to finish the "
          "work). The tables in Sections 3 through 5 fill in these axes, before and after. "
          "Read them as the diffs they are.")

FIG1_CAPTION = ("Figure 1. The three-level ladder used throughout this study. Profundity is "
                "measured by the depth of conceptual reconstruction, not by the amount of "
                "new data or new mathematics.")

# ---------------------------------------------------------------------------
# Chapter 3
# ---------------------------------------------------------------------------

CH3 = [
    ("Begin with the before-picture, because it is stranger than we remember. In 1680 "
     "physics was not one science but two. The heavens and the earth had different "
     "constitutions: celestial bodies were made of a fifth element, naturally and eternally "
     "circular in their motion; terrestrial bodies were arrangements of the four classical "
     "elements, each moving toward its natural place — stones down, smoke up. The "
     "division was not a loose metaphor but a working ontology, two millennia old, taught in "
     "every university. Its deepest consequence: the question “why does the Moon not "
     "fall?” was not merely unanswered. Within the two-world picture it was malformed. "
     "The Moon was simply not the kind of thing that falls."),

    ("The best planetary theory of the day had no dynamics at all. Kepler’s laws "
     "(1609–1619) described the orbits with superb accuracy — ellipses, equal "
     "areas, precise periods — and offered no mechanism whatever for them. The gap was "
     "filled by Descartes: the universe a plenum of subtle matter, the planets carried around "
     "the Sun by great swirling vortices, all causation by contact push. Action at a distance "
     "was banned as occult. On Earth, Galileo had established the kinematics of falling "
     "bodies and projectiles, and pointedly declined to speculate about the cause of "
     "gravity. “Gravity” itself, in this world, named a quality of a thing "
     "— its heaviness — not a relation between things. And the mathematics of it "
     "all was geometry; laws of nature were not yet equations."),

    ("The <i>Principia</i> (1687) did not refine this picture; it merged its two halves and "
     "rebuilt the remainder. The Moon <i>is</i> falling — perpetually, and perpetually "
     "missing the Earth. One mechanics now spans heaven and Earth: the same three laws of "
     "motion, and one force, universal gravitation, binding the falling apple to the "
     "Moon’s orbit, the Moon to the tides, the comets to their returns. To do this "
     "Newton — with Leibniz, independently — built the calculus, and physical law "
     "took its modern form: differential equations. Gravity itself changed meaning, from a "
     "quality of heavy bodies to a universal attraction between any two masses, weakening "
     "with the square of their separation. And the banned “occult” force of "
     "action at a distance was readmitted through the front door, over Newton’s own "
     "famous refusal to explain its mechanism."),

    ("The after-picture kept paying for two centuries. The theory predicted the return of "
     "Halley’s comet for 1758 — and the comet returned. It predicted the "
     "flattening of the Earth at its poles, the slow drift of the equinoxes, and, in its "
     "finest hour, a planet: when Uranus wandered from its computed path, the deviation "
     "itself was used to calculate the position of an unknown perturbing mass, and Neptune "
     "was found in 1846 within a degree of the prediction. The universe became a clock: "
     "complete knowledge of the present, given the laws, fixes the entire future — the "
     "determinism Laplace would later dramatize as his demon."),

    ("Now run the diff through the ladder. Newton’s Level 1 contribution was almost "
     "nil: the data in the <i>Principia</i> — Kepler’s orbits, falling bodies, "
     "pendulums, tides — was essentially all known before him. His Level 2 "
     "contribution was supreme: the laws, and the mathematics that carries them. But what "
     "makes the episode profound is Level 3. First, the two-worlds ontology died: heaven and "
     "Earth became one kind of place, governed by one kind of law. Second, the very form of "
     "explanation changed — to explain a phenomenon is now to derive it from "
     "mathematical law, a standard Newton set and physics has kept ever since. Third, "
     "“gravity” migrated from quality to relation. The profundity lived in the "
     "grammar, not in the data."),

    ("One more observation, easy to miss: what Newton did <i>not</i> demolish. He kept "
     "absolute space and time — the neutral, unchanging container in which his "
     "mechanics runs — and kept it deliberately. That was the old picture’s "
     "surviving organ, and it was precisely where the next revolution entered. Profound "
     "novelty is selective demolition: it tears down what blocks the new unification and "
     "quietly preserves the rest, leaving the next crisis a place to live."),
]

CH3_QUOTE = ("“I feign no hypotheses.”",
             "— Isaac Newton, General Scholium to the <i>Principia</i> (1713), on the mechanism of gravity")

TABLE3_CAPTION = "Table 1. The state of physics before and after the <i>Principia</i> (1687)."
TABLE3_HEADER = ["Axis", "Before (c. 1680)", "After (1687 and beyond)"]
TABLE3_ROWS = [
    ("World-picture",
     "Two realms: quintessence above, four elements below",
     "One universe of matter in motion under universal law"),
    ("Heavenly motion",
     "Natural circularity; Cartesian vortices carry the planets",
     "Orbits are falls: the Moon perpetually misses the Earth"),
    ("Gravity",
     "A quality — the heaviness of a body",
     "A universal attraction between any two masses, falling off as the inverse square"),
    ("Mathematics",
     "Geometry and ratio arguments",
     "Calculus; laws written as differential equations"),
    ("Ideal of explanation",
     "Mechanical contact-push; action at a distance banned",
     "Derivation from mathematical law; distance-action accepted"),
    ("Evidence base",
     "Pre-existing: Kepler’s orbits, falling bodies, tides",
     "Two centuries of derivations: comets, the Earth’s figure, Neptune (1846)"),
]

# ---------------------------------------------------------------------------
# Chapter 4
# ---------------------------------------------------------------------------

CH4 = [
    ("Newton’s framework stood essentially unchallenged for two centuries, and by 1900 "
     "physics looked finished; Kelvin could describe the entire remaining frontier as two "
     "small “clouds.” One was the behavior of light. Light was known to be a "
     "wave, and waves, by every precedent, need a medium — hence the luminiferous "
     "ether: an invisible, frictionless, all-penetrating substance filling space and "
     "defining a state of absolute rest. The Earth moves through this medium at some thirty "
     "kilometers per second, so the measured speed of light should vary with direction. In "
     "1887 Michelson and Morley built the most sensitive interferometer on Earth to find "
     "that variation, and found nothing — the most consequential null result in the "
     "history of physics."),

    ("The classical response was patching, and the patches were mathematically brilliant. "
     "Lorentz proposed that bodies moving through the ether physically contract along their "
     "direction of travel, by exactly the amount needed to hide the drift, and introduced a "
     "“local time” for moving systems — a bookkeeping device he did not "
     "believe was real time. Poincaré, by 1904, had stated the principle of relativity "
     "and worked the mathematics to the very edge of the new theory. This is the crucial "
     "fact for our study: by the end of 1904, the equations of special relativity "
     "essentially existed, in the hands of Lorentz and Poincaré. What did not yet "
     "exist was the world those equations would turn out to describe."),

    ("In 1905 a patent clerk deleted the ether. Einstein’s move was not another "
     "patch but a question about a concept nobody had thought to question: what does it "
     "<i>mean</i> to say that two distant events are simultaneous? Einstein analyzed the "
     "operations — light signals, synchronized clocks — and found that the answer "
     "depends on the observer’s frame. Simultaneity is not absolute. Once that "
     "collapses, the rest follows: every inertial frame measures the same speed of light; "
     "moving clocks run slow; moving rods contract — not as dynamical effects of "
     "dragging through a medium, but as features of what measurement means in a universe "
     "where influence travels at a finite speed <i>c</i>. No new experiment was required; "
     "the decisive data was eighteen years old."),

    ("Minkowski then showed that space and time are not demoted to fictions but merged into "
     "a single invariant structure — spacetime. And in 1915 general relativity "
     "repeated the whole maneuver one level deeper: gravity is not a force at all but the "
     "curvature of spacetime by mass-energy. Free fall is not accelerated motion awaiting "
     "explanation; it is inertial motion in curved geometry. The theory’s first "
     "triumph was an old anomaly — Mercury’s perihelion drifting 43 "
     "arc-seconds per century beyond the Newtonian calculation — which the new field "
     "equations explained exactly, with no adjustable parameters. The second triumph made "
     "Einstein a celebrity: the bending of starlight measured at the 1919 eclipse."),

    ("Then came the strangest property of all: the harvest grew from derivation, not "
     "observation. Gravitational waves were predicted in 1916 and detected in 2015 — a "
     "century later, to the month. Black holes were deduced from the equations long before "
     "anything was seen; the first was imaged in 2019. Time dilation, first a fringe "
     "effect, is now engineered into every GPS correction. And E = mc<super>2</super>, "
     "a byproduct of the 1905 kinematics, turned out to explain why the Sun shines."),

    ("The lesson of the case sits in the gap between Lorentz and Einstein. The same "
     "transformations, the same algebra — and one scientist kept the ether as a "
     "convenient fiction and local time as bookkeeping, while the other declared the "
     "symmetry to be a property of the world itself. Poincaré, holding nearly all the "
     "mathematics, treated the ether’s survival as a question of convention. Einstein "
     "read the equations literally and let the medium die. The profundity was not in the "
     "mathematics, which pre-existed him; it was in the re-reading — a Level 3 change "
     "performed on standing Level 2 formalism. This dissociation — formulas on one "
     "side, what the formulas <i>mean</i> on the other — will recur in the quantum "
     "case, and it may be the most reliable single mark of profundity this study finds."),
]

CH4_QUOTE = ("“Henceforth space by itself, and time by itself, are doomed to fade away "
             "into mere shadows.”",
             "— Hermann Minkowski, “Space and Time,” lecture to the "
             "German mathematical society, 1908")

TABLE4_CAPTION = "Table 2. The state of physics before and after Einstein’s relativity (1905–1915)."
TABLE4_HEADER = ["Axis", "Before (c. 1900)", "After (1905–1915)"]
TABLE4_ROWS = [
    ("Medium of light",
     "The luminiferous ether defines absolute rest",
     "Deleted; light needs no medium, and <i>c</i> is a structural constant"),
    ("Simultaneity",
     "Absolute, unproblematic — one time for the universe",
     "Frame-relative; defined by clock-synchronization operations"),
    ("Space and time",
     "Independent absolute containers, Euclidean",
     "Merged into spacetime, curved by mass-energy"),
    ("Gravity",
     "A force acting at a distance",
     "The geometry of spacetime itself; free fall is inertia"),
    ("Triggering evidence",
     "The Michelson–Morley null result (1887), already old",
     "Needed no new data; then waves (2015), black holes (2019), GPS"),
    ("Newton’s theory",
     "The framework, absolute",
     "A limiting case at low speeds and weak fields"),
]

# ---------------------------------------------------------------------------
# Chapter 5
# ---------------------------------------------------------------------------

CH5 = [
    ("Kelvin’s second cloud also burst, but slowly, and the difference of tempo "
     "matters. The classical worldview circa 1890 was a complete metaphysics: nature is "
     "continuous, causal, deterministic, and visualizable — particles and fields in "
     "space and time, states evolving under differential equations, complete knowledge "
     "implying complete prediction. Against this stood three stubborn facts. Statistical "
     "mechanics predicted that a warm cavity should radiate unlimited energy at high "
     "frequencies — an absurdity, not merely an error. The spectral lines of atoms "
     "obeyed Balmer’s eerie formula (1885) with no mechanism at all. And classical "
     "electromagnetism implied that an orbiting electron radiates away its energy and "
     "spirals into the nucleus within a hundredth of a nanosecond — that is, that "
     "matter should not exist. Physics was not slightly wrong. It was fatally wrong about "
     "the very thing it was most confident in: the state of a system."),

    ("Planck broke continuity in 1900 — he later called it “an act of "
     "desperation” — by allowing energy to be exchanged only in discrete quanta, "
     "E = hν, installing a new universal constant <i>h</i> into physics. "
     "Einstein radicalized the idea in 1905 (light itself arrives in quanta); Bohr built an "
     "uneasy truce atom in 1913. Then the crisis deepened for a decade, until 1925–27 "
     "resolved it in a single burst: Heisenberg’s matrix mechanics and "
     "Schrödinger’s wave mechanics — two apparently incompatible formalisms "
     "proven mathematically equivalent <i>before either was interpreted</i> — then "
     "Born’s discovery that the wavefunction encodes probabilities, "
     "Heisenberg’s uncertainty, and Bohr’s complementarity."),

    ("The resulting picture rewrote the deepest layer of all: what it means to know. The "
     "state of a system — the wavefunction ψ — is not a list of properties "
     "the system possesses; it is a catalog of probabilities for what measurements will "
     "find. Individual events are not determined, by anything; ensembles are lawful to any "
     "precision. Determinism, the pride of physics since Laplace, was not revised — "
     "it died at the foundation. And the observer, previously a metaphysical aside, entered "
     "the formalism itself: what a measurement is, and what it does, became part of the "
     "theory’s structure."),

    ("The founders’ response is perhaps the most striking datum in this study. Planck "
     "spent years trying to contain his quantum inside classical statistics. Einstein "
     "— who had helped launch the revolution — fought its probabilistic reading "
     "to the end of his life; he could not believe, he wrote to Max Born, that God plays "
     "dice. Schrödinger was famously unhappy with what his own equation was taken to "
     "mean. A novelty so profound that its own makers refused its lesson: this is what "
     "Level 3 looks like from the inside — not a new answer, but a new rule for what "
     "counts as an answer."),

    ("And yet the harvest may be the largest in the history of science. The theory of the "
     "chemical bond, the transistor, the laser, the MRI scanner, the atomic clock — "
     "the technological base of the modern world is quantum mechanics standing on an "
     "interpretation physicists still argue about. The century-lag pattern repeats: "
     "entanglement was a 1935 thought experiment by Einstein, Podolsky and Rosen, aimed at "
     "exposing the theory’s absurdity; Bell turned it into a testable theorem in 1964; "
     "the tests (honored with the 2022 Nobel Prize) confirmed quantum mechanics; and the "
     "“absurdity” is now the working principle of quantum computers. The "
     "revolution is still generating novelty in its second century."),

    ("One lesson sits in the tempo itself: profundity has no characteristic speed. Special "
     "relativity took one man five weeks; quantum mechanics took a scattered community "
     "twenty-seven years, with the formalism arriving before the meaning and the meaning "
     "never fully agreed upon. What the two tempos share is thoroughness. However long "
     "the road took, the change went all the way down to the grammar."),
]

CH5_QUOTE = ("“The theory says much, but does not really bring us any closer to the "
             "secret of the Old One. I, at any rate, am convinced that He does not throw "
             "dice.”",
             "— Albert Einstein to Max Born, 1926")

TABLE5_CAPTION = "Table 3. The state of physics before and after quantum mechanics (1900–1927)."
TABLE5_HEADER = ["Axis", "Before (c. 1890)", "After (1900–1927)"]
TABLE5_ROWS = [
    ("Physical state",
     "A list of properties; nature holds definite values",
     "The wavefunction: a catalog of probabilities over outcomes"),
    ("Causality",
     "Deterministic — full state plus laws fix a unique future",
     "Ensembles lawful; individual events not determined"),
    ("Matter and light",
     "Particles or waves; continuous exchange",
     "Both and neither — complementarity; exchange in quanta (<i>h</i>)"),
    ("The observer",
     "Outside the description",
     "Measurement is part of the formalism"),
    ("Fatal anomaly",
     "Matter should not exist (classical atomic collapse)",
     "Atomic stability derived; the chemical bond explained"),
    ("Founders’ verdict",
     "Triumphant; Kelvin saw only two small “clouds”",
     "The makers themselves dissented — Einstein to his death"),
]

# ---------------------------------------------------------------------------
# Chapter 6
# ---------------------------------------------------------------------------

CH6_INTRO = ("Set the three diffs side by side and a shared structure appears — the "
             "same marks, struck independently, in three episodes separated by two "
             "centuries. Nine features recur; together they form the signature this study "
             "set out to find.")

CH6_ITEMS = [
    ("Demolition, not accumulation.",
     "Ordinary science adds; profound novelty subtracts. Newton deleted the two-worlds "
     "cosmos; Einstein deleted the ether and absolute simultaneity; quantum theory deleted "
     "determinism. The test of depth is not what a new idea introduces but what it makes "
     "unthinkable afterward. Answers can be wrong; questions can die."),

    ("Unification of the thought-to-be-separate.",
     "The apple and the Moon; space and time; mass and energy; gravity and geometry; wave "
     "and particle. In each case the profound move reveals that a distinction (natural, "
     "ancient, obvious) was an artifact of description rather than a joint "
     "in nature."),

    ("A new universal constant is installed.",
     "Each revolution fixed a constant that re-scales the whole conceptual system: G "
     "couples matter to matter (1687), c caps the propagation of influence (1905), h "
     "discretizes action (1900). They remain the three load-bearing constants of physics."),

    ("Derivation-first novelty.",
     "The profound theory is over-determined by old data and under-determined by old "
     "theory. Newton needed almost no new observations; Einstein needed an eighteen-year-"
     "old null result; and both then issued promissory notes honored decades to a century "
     "later — a comet’s return, a planet found on paper, waves detected a "
     "hundred years after prediction."),

    ("Conservative embedding.",
     "None of the three refutes its predecessor outright; each demotes it to a limiting "
     "case — weak fields for Newtonian gravity, low speeds for Newtonian kinematics, "
     "large quantum numbers for classical behavior. Profound novelty explains why the old "
     "theory worked <i>and where it must fail</i>, which is the only honest way to defeat "
     "a successful theory."),

    ("Formalism and meaning come apart.",
     "Lorentz held the equations before Einstein; Schrödinger held the equation before "
     "Born’s reading of it. In both cases the profundity was an interpretation — "
     "the same mathematics made to say a new thing about the world. The deepest changes are "
     "often invisible in the formulas and live entirely in what the formulas are taken to "
     "mean."),

    ("The founders pay in their own coin.",
     "Newton surrendered the mechanical philosophy’s ban on action at a distance "
     "— and was attacked as an occultist for it by Leibniz and Huygens. Planck "
     "surrendered continuity, his deepest aesthetic commitment. Einstein surrendered the "
     "ether of his youth — then, when the quantum asked him to surrender determinism, "
     "declined, and spent thirty years resisting his own revolution’s successor. "
     "Profound novelty costs its makers something they actually held."),

    ("Each closes one crisis by opening a deeper one.",
     "Newton left the mechanism of gravity unexplained (a wound that stayed open for "
     "228 years, until general relativity closed it). General relativity is now at war with "
     "quantum mechanics over the interior of a black hole; quantum theory left the "
     "measurement problem open for a century and counting. Profound novelty does not "
     "finish a subject. It re-founds the subject and hands its successors a deeper floor "
     "to build on."),
]

CH6_OUTRO = ("A ninth feature — generative saturation — is listed in Table 4 "
             "rather than argued here, because it is the one mark visible only in retrospect: "
             "after each revolution, a century of ordinary science harvested consequences "
             "nobody had ordered — celestial mechanics delivered Neptune; general "
             "relativity delivered modern cosmology, black holes, and gravitational-wave "
             "astronomy; quantum mechanics delivered the technological world and quantum "
             "information. Read down a column of the table and one feels the individuality "
             "of each revolution. Read across the rows and one sees the invariants — "
             "the anatomy this study was looking for.")

# G / c / h callout
CALLOUT_GCH = [
    ("G", "1687", "matter couples to matter"),
    ("c", "1905", "influence propagates at a limit"),
    ("h", "1900", "action comes in quanta"),
]
CALLOUT_CAPTION = ("Each profound revolution installs a universal constant that re-scales "
                   "the entire conceptual system.")

TABLE6_CAPTION = "Table 4. The signature of profound novelty: the three revolutions compared."
TABLE6_HEADER = ["Signature", "Newton (1687)", "Einstein (1905–15)", "Quantum (1900–27)"]
TABLE6_ROWS = [
    ("New data required",
     "Almost none",
     "None — the 1887 null result",
     "A decade of anomalies"),
    ("What was deleted",
     "The two-realm cosmos",
     "The ether; absolute simultaneity",
     "Determinism; the classical state"),
    ("Unification",
     "Heaven and Earth",
     "Space and time; gravity and geometry",
     "Wave and particle"),
    ("Constant installed",
     "G",
     "c",
     "h"),
    ("Formalism vs. meaning",
     "Geometry reinterpreted as law",
     "Same equations, new world (Lorentz vs. Einstein)",
     "Interpretation after formalism (Born)"),
    ("Old theory’s fate",
     "Limiting case (weak fields)",
     "Limiting case (low speeds)",
     "Limiting case (large numbers)"),
    ("Founder’s sacrifice",
     "Contact-only causation",
     "The ether (later: determinism)",
     "Continuity"),
    ("Century-scale yield",
     "Neptune (1846); celestial mechanics",
     "Waves (2015); black holes (2019); GPS",
     "Transistor, laser, MRI; quantum information"),
    ("Left open for the next",
     "Mechanism of gravity",
     "Quantum gravity",
     "The measurement problem"),
]

# ---------------------------------------------------------------------------
# Chapter 7
# ---------------------------------------------------------------------------

CH7 = [
    ("The negative cases sharpen the signature. Ptolemaic astronomy ran on epicycles "
     "— circles upon circles — and could be tuned to any observation by adding "
     "another cycle. It predicted well for its day precisely because it could predict "
     "<i>anything</i>: the framework’s flexibility made it unkillable by data and "
     "sterile of consequences. Phlogiston, the fire-principle of eighteenth-century "
     "chemistry, had to be assigned negative weight to survive the discovery that metals "
     "<i>gain</i> weight when burned — a patch protecting a concept from the world. "
     "The tell is the same in both cases: a system that survives every result by adjusting "
     "is not deep but empty. Depth, in the cases studied here, has the opposite property: "
     "it is unpatchable. It forces a choice — as the Michelson null result, once read "
     "by Einstein, forced the ether to be either real and undetectable by construction, or "
     "not there at all."),

    ("Nor is profound novelty the same as great discovery. Neptune (1846) and the Higgs "
     "boson (2012) were triumphs of prediction — but predictions made <i>by</i> a "
     "standing framework, filling slots the framework itself had defined. They changed no "
     "concept: “planet” and “elementary particle” meant the same "
     "after each triumph as before. The distinction matters practically. When evaluating "
     "any novelty claim — in science, in design, in one’s own work — the "
     "diagnostic questions this study suggests are not “how new is it?” or "
     "“does it work?” but rather: What does it make impossible to ask? What "
     "does it force us to ask instead? Does the old framework survive as a special case, or "
     "does it merely survive by patching? Novelty that passes those tests is profound. "
     "Novelty that fails them may still be excellent — but it is excellent at Level 1 "
     "or Level 2, and it should not be mistaken for what Newton, Einstein, and the quantum "
     "theorists achieved."),
]

# ---------------------------------------------------------------------------
# Chapter 8
# ---------------------------------------------------------------------------

CH8 = [
    ("The three cases converge on a definition. The profundity of a novelty is measured by "
     "the depth of concept it reconstructs. Level 1 gives new answers to standing "
     "questions. Level 2 gives new questions — within an old grammar. Level 3 "
     "rewrites the grammar in which questions must be asked. Newton changed what counts as "
     "an explanation, and what “gravity” could even mean. Einstein changed what "
     "space and time are, and what it means to measure them. Quantum theory changed what "
     "it means to know the state of a thing — and, with the observer inside the "
     "formalism, what knowing is <i>for</i>."),

    ("The condensed signature reads as follows. Profound novelty deletes something the "
     "field believed constitutive. It unifies what were taken to be different kinds of "
     "things. It is over-determined by old data yet keeps predicting far ahead of its "
     "evidence. It embeds its predecessor as a special case rather than refuting it. It "
     "costs its founders their own prior commitments. And it leaves its successors a "
     "deeper open problem than it inherited — which is why the three revolutions "
     "chain: Newton’s unexplained mechanism of gravity became Einstein’s "
     "curved spacetime, and the collision between Einstein’s smooth geometry and "
     "the quantum’s discreteness is the still-open frontier of quantum gravity. Each "
     "revolution ends where the next one begins."),

    ("And this is the quiet lesson the exercise leaves behind for anyone hunting depth. "
     "Profound novelty does not announce itself as an answer. It arrives looking like a "
     "scandal — a null result, a refusal, an equation that seems to mean something "
     "it should not. The skill worth training is not the ability to produce the new; the "
     "world produces the new constantly, at Level 1 and Level 2, and most of it is good. "
     "The skill is noticing which rare new thing is rewiring the questions themselves "
     "— and following it all the way down."),
]
