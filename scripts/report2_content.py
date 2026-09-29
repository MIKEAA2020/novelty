# -*- coding: utf-8 -*-
"""Content module for 'The Conditions of Depth: Profound Novelty, Volume II'.

Chapter numbering plan (Step 3.5):
| Outline Index | Type    | Chapter # | Title                                                  |
|---------------|---------|-----------|--------------------------------------------------------|
| 1             | cover   | -         | Cover (separate Playwright PDF, merged)               |
| 2             | toc     | -         | Contents                                               |
| 3             | content | 1         | The Question Sharpened: From Signature to Conditions   |
| 4             | content | 2         | The Expanded Case Base: Seven More Diffs              |
| 5             | content | 3         | Six Angles of Analysis                                 |
| 6             | content | 4         | The Necessary Conditions                               |
| 7             | content | 5         | The Common Signature: Invariants Across All Cases      |
| 8             | content | 6         | Intricacies: Prematurity, Multiples, and Prediction   |
| 9             | content | 7         | Conclusion: The Shape of Depth                         |
"""

DOC_TITLE = "The Conditions of Depth: Profound Novelty, Volume II"
DOC_SUBJECT = ("A general theory of profound novelty: the necessary conditions, the "
               "recurring patterns, and the common signature shared by the major "
               "scientific breakthroughs, from Newton and Darwin to Godel, Turing, "
               "Shannon, and plate tectonics.")

# ---------------------------------------------------------------------------
# Chapter titles (numbered as displayed)
# ---------------------------------------------------------------------------

CHAPTERS = [
    ("1", "The Question Sharpened: From Signature to Conditions"),
    ("2", "The Expanded Case Base: Seven More Diffs"),
    ("3", "Six Angles of Analysis"),
    ("4", "The Necessary Conditions"),
    ("5", "The Common Signature: Invariants Across All Cases"),
    ("6", "Intricacies: Prematurity, Multiples, and the Prediction Problem"),
    ("7", "Conclusion: The Shape of Depth"),
]

# ---------------------------------------------------------------------------
# Chapter 1
# ---------------------------------------------------------------------------

CH1 = [
    ("The first volume of this study approached profound novelty the way a naturalist "
     "approaches a rare species: it selected the three cleanest specimens physics offers "
     "— Newtonian mechanics, Einstein's relativity, and the quantum — and took their "
     "diff, comparing the state of the discipline before and after each. The result was "
     "a three-level ladder for measuring depth. Ordinary novelty adds new phenomena "
     "(Level 1, novelty of content) or new laws (Level 2, novelty of structure); profound "
     "novelty rewrites the vocabulary in which the laws themselves are written (Level 3) "
     "— the meanings of space, time, cause, state, and observation. Diffing the three "
     "revolutions against their own pasts also produced a nine-point signature of "
     "profundity: demolition rather than accumulation; unification of the "
     "thought-to-be-separate; installation of new universal constants; derivation ahead "
     "of observation; conservative embedding of the old theory; formalism detached from "
     "meaning; founders overthrown by their own revolution; generative saturation; and "
     "the closing of one crisis by the opening of a deeper one."),

    ("A portrait, however, is not a theory. The signature describes what profundity "
     "looks like in cross-section, after it has happened; it says nothing about where "
     "breakthroughs come from, what must be in place before one is possible, or what — "
     "if anything — is shared by all major scientific breakthroughs rather than by the "
     "three that happened to occur in physics. Those are the questions this second volume "
     "takes up, and they are harder than the first set, because they ask not for a "
     "description of the product but for the conditions of production. What constitutes "
     "a profound, novel breakthrough — what is the change, exactly, when the change is "
     "at the level of vocabulary? What patterns recur beneath the surface differences "
     "between a physics revolution and a biological one, or between a theorem about "
     "arithmetic and a machine that computes? What conditions are necessary — and what "
     "does 'necessary' even mean in a subject that permits no experiments on its own "
     "history? And what, finally, is common to all of them: the invariants that define "
     "the class?"),

    ("The method is the same as Volume I's, extended in two directions. First, widen "
     "the case base. To the physics trio this study adds seven cases chosen for maximum "
     "diversity of domain: Darwin's theory of natural selection, Gödel's incompleteness "
     "theorems, Turing's universal machine, Shannon's theory of information, the "
     "long-delayed vindication of Wegener's continental drift in plate tectonics, "
     "Lavoisier's chemical revolution, and — as a control — Mendel's law of "
     "inheritance, a correct and constitutive idea that history left in its waiting "
     "room for thirty-five years. If a signature derived from mechanics, light, and "
     "atoms survives contact with biology, logic, computation, earth science, and "
     "chemistry, it has earned the title of general pattern. Second, use the failures. "
     "A condition claimed to be necessary can be tested in the only way history "
     "allows: by finding cases where the idea was right but the condition was absent, "
     "and watching what happened. Mendel, Wegener, and Semmelweis are such cases — "
     "natural experiments in which one variable was removed while the others stood. "
     "They are the closest thing this subject has to a control group."),

    ("An honest preamble on evidence. History permits no reruns and no controlled "
     "samples; every claim of necessity below is therefore a pattern-claim, not a "
     "proof: in every observed success the condition was present, and in every "
     "observed failure or delay the record shows the condition missing. This is "
     "abduction over a small and biased sample — biased because the successes were "
     "selected by fame — and it is guarded, though not cured, by the control cases. "
     "Two further cautions. Depth of change is judged after the fact, by an observer "
     "standing inside the very vocabulary the winners installed; there is no view "
     "from nowhere. And the ladder of Volume I is a measuring instrument, not a "
     "historical mechanism — revolutions do not descend rung by rung. With those "
     "limits on the table, the patterns are nonetheless sharp enough to be worth "
     "stating as strongly as the evidence allows, and this study will state them, "
     "and mark their edges, accordingly."),
]

# ---------------------------------------------------------------------------
# Chapter 2
# ---------------------------------------------------------------------------

CH2_P1 = ("Begin with biology, because it is the furthest from physics and therefore "
          "the best test of transfer. In 1859 the concept of species was the most "
          "settled object in natural history: a species was a fixed essence, "
          "reproducing after its kind since the Creation, and the exquisite fit of "
          "organisms to their lives was the readiest argument for a designer — natural "
          "theology was not a decoration on biology but its licensing authority. "
          "Darwin's Level 1 contribution was modest: pigeon fancying, barnacle "
          "taxonomy, the heavily documented variability of ordinary life. What he "
          "rewrote was the concept underneath. Species are populations in flux, and "
          "adaptation is the output of an algorithm — variation, heredity, "
          "differential survival — that runs for millions of years without a designer, "
          "or rather with all the designer's work done by the arithmetic of death and "
          "multiplication. The change reached the concept of explanation itself: to "
          "explain a trait is no longer to exhibit its purpose but to reconstruct its "
          "selection history. Two constitutive deletions followed — fixed species, "
          "designed adaptation — and one unification with teeth: the human being "
          "entered the tree of descent as data, and the theorist became a specimen of "
          "his own theory.")

CH2_P2 = ("Turn to mathematics, where the objects are the most abstract and therefore "
          "the test is the purest. By 1930, David Hilbert's program had reduced the "
          "ancient dream of perfect certainty to a technical project: formalize "
          "mathematics completely, prove the formalism consistent, and decide every "
          "well-posed question mechanically. That September, in Königsberg, Hilbert "
          "closed a radio broadcast of his retirement address with the program's "
          "motto. Days earlier, at the same conference, in a roundtable discussion on "
          "the foundations of mathematics, a twenty-four-year-old Austrian logician "
          "named Kurt Gödel had quietly announced the result that would break the "
          "program: any consistent formal system rich enough for arithmetic contains "
          "true statements it cannot prove. The proof's instrument was the reflexive "
          "move in miniature — Gödel numbered the symbols, so that arithmetic could "
          "speak about sentences of arithmetic, and constructed a sentence that said, "
          "in effect, 'this sentence is not provable in this system.' Truth and proof, "
          "assumed coextensive since Aristotle, separated permanently. The deletions "
          "were total: completeness, and soon decidability with it. Yet the embedding "
          "was equally total — every classical theorem survived, and incompleteness "
          "bites only above a threshold of formal strength, below which weak "
          "arithmetics remain complete and decidable. Mathematics did not lose a "
          "fact; it learned the shape of its own boundary.")

CH2_QUOTE_HILBERT = ("“Wir müssen wissen. Wir werden wissen.”",
                     "— David Hilbert, radio address, Königsberg, September 1930 — "
                     "“We must know. We will know,” later carved on his tombstone. "
                     "At the same conference, days earlier, Gödel had announced the "
                     "first incompleteness theorem.")

CH2_P3 = ("The machine case begins, oddly, inside the same Hilbert program. "
          "'Computer,' in 1936, named a profession: a person calculating with pencil, "
          "rules, and patience. To settle Hilbert's decision problem, Alan Turing "
          "needed a precise definition of what such a person could in principle do — "
          "and found, by stripping the human clerk down to bare procedure, the Turing "
          "machine: a head reading symbols on a tape, governed by a finite table of "
          "instructions. The definition demolished the assumption that computation is "
          "tied to any particular device or any particular thinker, and then delivered "
          "the deepest result of the century's logic: a universal machine, one that "
          "simulates any other by reading the other's instruction table from its own "
          "tape. Hardware and software separated in 1936, a decade before the first "
          "electronics. The decision problem fell — independently of Alonzo Church's "
          "lambda-calculus, whose equivalence with machine computability Turing proved "
          "in an appendix, welding the two formulations into one concept. And the "
          "case carries a unique property: the computer is the only major artifact of "
          "civilization that was deduced before it was desired. A mathematical "
          "refutation of Hilbert's dream, published in 1936, booted as a stored-"
          "program machine in 1948, and the world's industrial base reorganized "
          "around it.")

CH2_P4 = ("Information was, until 1948, a property of minds: a message meant "
          "something, and communication was the transport of meaning. Claude Shannon "
          "expelled meaning from the engineering definition — deliberately, not as an "
          "oversight. Information is what remains measurable when you do not know "
          "what a message means: a unit (the bit, one binary choice), a source with a "
          "statistical character and an entropy, a channel with a capacity, and a "
          "theorem that near-errorless transmission is possible at any rate below "
          "that capacity, in the presence of any noise. Every craft that had grown "
          "up around a medium — telegraphy, telephony, broadcast — collapsed into one "
          "science of the channel; and the same quantity later proved to be the "
          "currency of the genetic code, so that the merger eventually reached living "
          "chemistry. The deletion was the assumption that fidelity requires "
          "understanding; a code can beat a linguist, and does, every hour of every "
          "day. The embedding is worth pausing on: every existing code became a "
          "suboptimal special case, improvable in principle toward the new bounds — "
          "engineers did not have to abandon their practice to enter the theory, only "
          "to see its ceiling. The bit joined G, c, and h: a new fixed point around "
          "which a science reorganized.")

CH2_P5 = ("In 1912 the meteorologist Alfred Wegener proposed that the continents "
          "move. He had what a naturalist could have: the fit of the Atlantic "
          "coasts, the same fossil ferns (Glossopteris) on continents now separated "
          "by oceans, the same strata on both sides of the Atlantic, ancient climates "
          "frozen into rocks where those climates no longer make sense. What he did "
          "not have was what the physics cases had — a mechanism the era's "
          "instruments could even describe. The ocean floor was less mapped than the "
          "visible face of the Moon; nothing was known of its youth at the ridges; "
          "paleomagnetism, which would write the wandering of the poles into cooling "
          "rock, was thirty years in the future. Wegener knew exactly what was "
          "missing. The theory was essentially correct; the instruments were absent; "
          "the community, offered a constitutive deletion — the fixity of the crust — "
          "with no mechanism to purchase it with, closed ranks for fifty years. When "
          "the instruments finally arrived — sonar maps of a great rift valley "
          "running the length of the mid-Atlantic, and the magnetic stripes that "
          "dated the ocean floor — the same idea, essentially unchanged, took the "
          "entire field within five years and became plate tectonics: the unification "
          "of earthquakes, volcanoes, mountain belts, and coastlines under one "
          "engine.")

CH2_QUOTE_WEGENER = ("“The Newton of drift theory has not yet appeared.”",
                     "— Alfred Wegener, The Origin of Continents and Oceans (1915), "
                     "reporting the missing condition of his own theory")

CH2_P6 = ("Chemistry's case is the oldest and the neatest. Antoine Lavoisier, working "
          "through the 1770s and 1780s with the precision balance as his new "
          "instrument, rewrote combustion: burning is not the escape of phlogiston, "
          "the fire-principle, from a material — it is the combination of the "
          "material with oxygen. Metals calcine heavier, not lighter, because they "
          "have absorbed gas; the balance, not the theory of qualities, decides. "
          "Phlogiston was deleted; conservation of mass became the bookkeeping of "
          "chemistry; the element was redefined from an Aristotelian principle to a "
          "substance not yet decomposed; and, in the same program, respiration was "
          "revealed as slow combustion — fire and life unified as one chemistry. The "
          "control case completes the row. Gregor Mendel, in 1865, published a law of "
          "inheritance as quantitative and constitutive as anything in this study: "
          "segregation in clean ratios, characters carried by discrete factors. The "
          "paper appeared in a real journal, was read, and was ignored for "
          "thirty-five years. Nothing was wrong with the idea. The community that "
          "could have heard it did not yet exist — the statistical habits that make "
          "a three-to-one ratio informative had not entered biology. Mendel's case "
          "is the study's single most valuable negative result, and it will be used "
          "as such throughout.")

CH2_P7 = ("Set the seven new cases beside the three from Volume I and the pattern "
          "not only survives; it sharpens. Every case rewrites a constitutive "
          "concept — gravity, space and time, state and observation, species, proof, "
          "machine, information, element, continent. Every case deletes something "
          "that had been constitutive, not merely wrong. Every case unifies a duality "
          "that had been taken for deep: heaven and earth, space and time, wave and "
          "particle, human and animal, calculation and machine, fire and life. Every "
          "case embeds its predecessor as a limit. Three of Volume I's nine "
          "signature points, however, transform rather than repeat. The new "
          "universal constant becomes a structural invariant: not a number like G, "
          "c, or h, but a form — the algorithm (selection), the boundary (the "
          "provable), the universal machine, the bit, conservation itself. "
          "Derivation-ahead-of-observation weakens: Darwin retrodicted, and his "
          "theory's sharpest predictions — Mendelian ratios among them — took a "
          "second discipline to state. And the dissociation of formalism from "
          "meaning recurs only where formalism exists: Gödel's theorem means "
          "differently to a Platonist and a formalist, but it compels both. Table 1 "
          "summarizes the diffs.")

TABLE1_CAPTION = ("Table 1. The expanded case base: six constitutive rewrites beyond the "
                  "physics trio of Volume I. Mendel is deliberately absent — he is the "
                  "control, not the pattern.")
TABLE1_HEADER = ["Case", "Concept Rewritten (Level 3)", "What Was Deleted", "What Was Unified"]
TABLE1_ROWS = [
    ("Darwin, 1859",
     "species: from fixed essence to population in flux; explanation becomes selection history",
     "Fixed species; designed adaptation",
     "Human and animal; artificial with natural selection"),
    ("Gödel, 1931",
     "proof and truth: from assumed coextensive to provably distinct",
     "Completeness and decidability — Hilbert's dream",
     "Mathematics with metamathematics, via numbering"),
    ("Turing, 1936",
     "machine and computation: from device (or clerk) to mathematical object",
     "The binding of calculation to a device or a person",
     "Human calculation with machine process; hardware with software"),
    ("Shannon, 1948",
     "information: from meaning to measurable quantity",
     "The requirement that communication carry semantics",
     "Wire, wave, image, and gene — one measure, one theory of the channel"),
    ("Wegener, 1912 → 1968",
     "continent: from permanent bedrock to mobile plate",
     "The fixity of oceans and lands",
     "Earthquakes, volcanoes, mountain belts, coasts — one engine"),
    ("Lavoisier, 1789",
     "element and combustion: from qualities to conserved substances",
     "Phlogiston",
     "Fire and life — respiration as slow combustion"),
]

# ---------------------------------------------------------------------------
# Chapter 3
# ---------------------------------------------------------------------------

CH3_P0 = ("One case is an anecdote; ten cases are a matrix, and a matrix can be viewed "
          "from more than one side. This chapter walks around the aggregate six times "
          "— epistemologically, logically, ontologically, cognitively, sociologically, "
          "and instrumentally — collecting on each pass a different set of conditions "
          "and properties. No single angle sees the whole object; the point of "
          "circling is to find which features stay visible from everywhere, because "
          "those are the candidates for the invariants of Chapter 5.")

CH3_P1 = ("<b>1 · The epistemological angle.</b> This angle asks where, in the stack "
          "of knowledge, the change lands. The stack has three levels — data, laws, "
          "and the vocabulary in which laws are written — and profundity tracks the "
          "bottom level. The immediate consequence is what Kuhn called "
          "incommensurability and what is better described as translation failure: "
          "after a vocabulary change, the old claims can be paraphrased but not "
          "translated word for word, because the words no longer point at the same "
          "invariants. 'Mass' before and after Einstein is the same word over a "
          "different quantity; 'species' before and after Darwin is the same word "
          "over a different kind of object. Popper's falsifiability, so useful for "
          "separating science from non-science, does no work at this level — every "
          "case in this study was falsifiable, so falsifiability cannot be what "
          "separates the profound from the ordinary. Lakatos gets closer: a research "
          "program degenerates when its patches multiply and its novel predictions "
          "dry up, and profound novelty is recognizable in retrospect as the moment "
          "a degenerating program was replaced by a progressive one. Phlogiston "
          "chemistry patching itself with negative-weight fire, while Lavoisier's "
          "balance piled up unanticipated hits, is the clean example.")

CH3_P2 = ("<b>2 · The logical angle.</b> This angle exposes the strangest recurring "
          "device in the case base: the reflexive turn — the framework being turned "
          "on itself. Newton's sky became an object of mechanics; Einstein's "
          "observer entered the physics as a measuring instrument among instruments; "
          "Gödel's arithmetic was made to speak about arithmetic; Turing's human "
          "calculator became the definition of the machine; Darwin's theorist "
          "descended into his own tree as a specimen; Shannon's channel — the very "
          "medium through which theory travels — became an object of the theory of "
          "engineering. The deepest results in the record all use the system's own "
          "strength against it, and they say the same thing in different grammars: "
          "<i>this framework cannot express, decide, or guarantee X</i>. Cantor's "
          "diagonal, Tarski's undefinability of truth, Gödel's sentence, and Turing's "
          "halting problem are one family of argument — the family of "
          "self-application. Profound novelty, generalized, is never a claim within "
          "a framework; it is a claim about what frameworks can say.")

CH3_P3 = ("<b>3 · The ontological angle.</b> This angle inventories what exists, and "
          "finds change of three kinds. Deletions: the two-world cosmos, absolute "
          "simultaneity, the ether, determinism at the microscale, fixed species and "
          "designed adaptation, phlogiston, the fixity of the crust, Hilbert's "
          "complete system. Mergers: space with time, mass with energy, wave with "
          "particle, human with animal, calculation with machine, fire with life — "
          "and, once molecular biology read the code, chemistry with heredity. And "
          "admissions, which are better than additions: fields, tectonic plates, "
          "genes-as-information, algorithms, the bit, and that strange citizen of "
          "the modern world, the universal machine itself. The asymmetry worth "
          "noticing is that additions are news, but deletions are relief. Nobody "
          "mourns the ether; each generation after a revolution finds the world "
          "lighter, not heavier — the post-revolutionary ontology feels cleaner "
          "because the concepts it deleted had been quietly carrying explanatory "
          "debt. This is why the winners' textbooks read as simplifications even "
          "when the underlying formalism got harder.")

CH3_P4 = ("<b>4 · The cognitive angle.</b> This angle asks what changes in the minds "
          "that receive the idea. The recurring description is the gestalt switch: "
          "the same data, differently organized — and Kuhn's observation that "
          "'what a man sees depends both upon what he looks at and also upon what "
          "his previous visual-conceptual experience has taught him to see' is the "
          "entire mechanism in one sentence. Conceptually, the move installs a new "
          "metaphor as literal: time is a dimension, species are populations, proof "
          "is mechanical, information is quantity, the mind is a computer. Each of "
          "these began as heresy, passed through usefulness, and ended as the "
          "default lens — Lakoff and Johnson's diagnosis that thought runs on "
          "metaphor explains why installing a literal metaphor is a rewrite of the "
          "engine rather than a new trip. The sociographic fact is the "
          "insider-outsider paradox: the breakthrough mind must be trained enough to "
          "command the instruments and distant enough not to have over-learned the "
          "ontology they carry. That is why the roster is so full of the young and "
          "the peripheral — Einstein examining patents in Bern, Wegener the "
          "meteorologist lecturing geologists, Darwin the gentleman naturalist "
          "outside the professoriate, Gödel twenty-four and at the edge of the "
          "Vienna Circle, Turing fresh out of Cambridge. Veblen named the complement "
          "of the asset: trained incapacity — expertise so complete that certain "
          "questions no longer parse. The corollary deserves to be uncomfortable: "
          "the best-trained are, on precisely that account, the least likely to "
          "perform the deepest revisions.")

CH3_P5 = ("<b>5 · The sociological angle.</b> This angle corrects a moral habit. "
          "Resistance to profound novelty is usually narrated as folly — old men "
          "failing to see. But the record shows the community's skepticism was, in "
          "its own terms, defensible: the early evidence for every true revolution "
          "was thin. Galileo's strongest argument for the Earth's motion — his "
          "theory of the tides — was wrong. Darwin could not supply a mechanism of "
          "heredity, and the blending theory of his era would have sunk natural "
          "selection had it been true. Wegener could not supply a mechanism at all. "
          "General relativity's earliest confirmations carried generous error bars. "
          "A community that demands strong evidence before rewriting its "
          "constitutive concepts is not broken; it is doing its job — and the price "
          "is that the genuine article must survive the same gauntlet as the false. "
          "What actually spreads a revolution is demographic: the old guard does "
          "not convert; it retires. Alongside the demographic clock runs an "
          "absorption trajectory regular enough to be memorized as a law of the "
          "epistemic economy: first the idea is impossible; then it is interesting "
          "but surely wrong; then it is right but surely not important; then it is "
          "in the textbooks; and finally it is invisible — no longer an idea but "
          "the light one sees by, spoken with the accent of common sense. "
          "Profundity's ultimate trophy is anonymity.")

CH3_QUOTE_PLANCK = ("“A new scientific truth does not triumph by convincing its "
                    "opponents and making them see the light, but rather because its "
                    "opponents eventually die, and a new generation grows up that is "
                    "familiar with it.”",
                    "— Max Planck, Scientific Autobiography (1949)")

CH3_P6 = ("<b>6 · The instrumental angle.</b> This angle identifies what the "
          "breakthrough had to have in hand before it could exist. Instruments come "
          "in three kinds. Physical instruments extend the senses: the telescope "
          "before heliocentrism settled, the balance before the chemical revolution, "
          "the spectroscope before the quantum atom, the sonar map and the "
          "magnetometer before plate tectonics. Formal instruments extend the "
          "mathematics: the calculus before Newton's dynamics, tensor calculus and "
          "Riemannian geometry before general relativity, Gödel numbering before "
          "incompleteness. And conceptual instruments extend the thinkable: "
          "Malthus's arithmetic of population before Darwin's selection, Hilbert's "
          "formalism before Gödel could break it, the very idea of a defined "
          "mechanical procedure before Turing's machine. Level 1 discoveries "
          "usually wait on physical instruments; Level 3 revisions wait on formal or "
          "conceptual ones — a new kind of seeing before a new thing to be seen. "
          "This is Kauffman's adjacent possible: at any moment only some ideas are "
          "reachable, because the instruments that make them thinkable do not yet "
          "exist. Newton's letter to Hooke — if he saw further it was by standing "
          "on the shoulders of giants — is the instrument ladder described with "
          "renaissance brevity. Put the six angles together and the picture "
          "assembles into a model: conditions converge on a moment, and consequences "
          "diverge from it. Figure 1.")

FIG1_CAPTION = ("Figure 1. The convergence model of profound novelty. Five upstream "
                "conditions meet in a moment — the instruments that make the concept "
                "statable, the mind at the right distance, the carrier that travels, "
                "the embedding that bridges, the community that can verify. The "
                "aftermath is as characteristic as the origin: unanticipated harvest "
                "for decades, a deeper problem standing where the old one fell, and "
                "finally absorption — the idea becoming invisible as an idea.")

# ---------------------------------------------------------------------------
# Chapter 4
# ---------------------------------------------------------------------------

CH4_P1 = ("The words 'necessary condition' require disarming before arming. In "
          "history there are no reruns, no controls, and no forward experiments; "
          "what remains is a pattern-test. A condition enters the necessary list "
          "if it is present in every success in the record, and if its documented "
          "absence coincides, case after case, with the delay or failure of ideas "
          "that were themselves correct. The second clause is what saves the claim "
          "from tautology — the prematurity cases of Chapter 6 are the removal "
          "experiments, and they behave with striking regularity. The list that "
          "follows has six conditions, organized by the three phases of a "
          "breakthrough's life: what must hold for the idea to be possible at all "
          "(origination), for it to survive its author (fixation), and for it to "
          "become what we later call profound (recognition).")

CH4_P2 = ("<b>C1 — Instrument availability: the adjacent possible must have a "
          "door.</b> No profound revision in the record was performed without a "
          "pre-existing instrument — physical, formal, or conceptual — that made "
          "the new concept statable. Curved spacetime waited half a century after "
          "Riemann's 1854 lecture on the foundations of geometry, and more than a "
          "decade after Ricci and Levi-Civita's tensor calculus, for the man who "
          "could put them to work; without the mathematics, the idea is not "
          "difficult, it is unsayable. Gödel is the purest exhibit: incompleteness "
          "could not exist in 1831 or 1879, because the concept of a fully "
          "formalized system did not exist to be proven incomplete — Hilbert had "
          "to build the object before Gödel could break it, and Principia "
          "Mathematica had to be written before anyone could show it could not "
          "finish its job. Turing needed the Entscheidungsproblem to be posed — "
          "Hilbert and Ackermann posed it in 1928 — and the logical tradition that "
          "made 'mechanical procedure' a mathematical question rather than a "
          "phrase. Darwin's door was conceptual, and he described opening it "
          "himself, in the most quoted sentence of his autobiography. The "
          "generalization is strict: a science cannot jump past its own "
          "instruments, and the depth of its next constitutive revision is bounded "
          "by the vocabulary its tools can express.")

CH4_QUOTE_DARWIN = ("“I happened to read for amusement Malthus on Population … it "
                    "at once struck me that under these circumstances favourable "
                    "variations would tend to be preserved, and unfavourable ones "
                    "to be destroyed. Here then I had at last got a theory by which "
                    "to work.”",
                    "— Charles Darwin, Autobiography (1876), describing October 1838")

CH4_P3 = ("<b>C2 — Cognitive distance: the prepared outsider.</b> The mind that "
          "performs the revision must satisfy two conditions at once, and they pull "
          "against each other: enough training to command the instruments, and "
          "enough distance to doubt the ontology the old instruments carry. Full "
          "insiders have the first and lack the second; pure outsiders have the "
          "second and lack the first. The record's solution is a particular "
          "demographic edge — the young, the peripheral, the dual-trained. Einstein "
          "at the Bern patent office was arguably in the perfect position: trained "
          "in physics to the frontier, employed outside the professoriate, and "
          "surrounded by the era's flood of electro-technical time-synchronization "
          "patents — clock coordination as daily bread, which is to say, the "
          "relativity of simultaneity as a day job. Distance, in short, is not the "
          "absence of preparation. It is preparation with the inoculation removed.")

CALLOUT_AGES = [
    ("22", "1831", "Darwin boards the Beagle"),
    ("26", "1905", "Einstein's miracle year"),
    ("24", "1936", "Turing's universal machine"),
]
CALLOUT_CAPTION = ("Age at first entry into the problem. The pattern repeats across the "
                   "case base — Newton was in his early twenties in the miracle years, "
                   "Heisenberg was 23 at Helgoland, Gödel was 24 at Königsberg — "
                   "because youth is not energy but the absence of sunk conceptual "
                   "costs.")

CH4_P4 = ("<b>C3 — The carrier: the idea must travel without its maker.</b> A "
          "profound idea must survive contact with its author's mortality, and the "
          "carriers in the record are proofs, formalisms, books, and artifacts, "
          "with different grips. Gödel's proof is the most perfect carrier in the "
          "study: it compels step by step, requires no charisma, and converts each "
          "verifier into a vector — von Neumann grasped the Königsberg announcement "
          "immediately, sought Gödel out, and within months had derived the second "
          "incompleteness theorem from it. The Origin of Species carried a "
          "different way: one long argument, engineered for the educated reader, "
          "with the evidence massed so the book could argue alone. Turing's case is "
          "unique twice over — first the proof carried the concept, and then the "
          "artifact itself became the carrier, the universal machine demonstrating "
          "universality by existing. The counterexample calibrates the condition: "
          "Leonardo's notebooks, written in mirror script and unpublished, carried "
          "his constitutive insights into the grave, and centuries passed before "
          "others re-derived them. Publication is not carriage. A paper in a "
          "journal the field cannot yet read is a message in a bottle addressed to "
          "a reader who does not yet exist.")

CH4_P5 = ("<b>C4 — Conservative embedding: the bridge to the old order.</b> A "
          "revision that leaves the establishment no bridge is received as a "
          "declaration of war, and loses the peace even when it wins battles. "
          "Every case in this study handed the old theory a limit case and a role: "
          "Newton's mechanics inside Einstein's at low speeds — and Einstein's "
          "first public triumph, the perihelion of Mercury, was precisely the "
          "recovery of Newton's own number plus his known error; classical logic "
          "intact below the threshold of Gödel's strength, where weak systems "
          "remain complete and decidable; artificial selection as the "
          "demonstration case inside natural selection; the phlogiston chemists' "
          "genuine successes — the weight relations, the transfer of fire — "
          "re-explained without the fire-principle. Embedding is the technical form "
          "of an old psychological truth: it lets the old guard be right, "
          "degenerately, while joining the new order. Where embedding was "
          "impossible, the record turns tragic. Semmelweis could offer only a "
          "naked empirical regularity — wash your hands, and the deaths fall "
          "tenfold — with no mechanism to embed it in, and a correct practice "
          "died with its reception.")

CH4_P6 = ("<b>C5 — The prepared community.</b> Uptake requires a receiver trained "
          "to verify. Mendel's ratios were published in 1866 and comprehensible to "
          "perhaps a hundred people alive, most of whom never opened the journal; "
          "the identical law in 1900 met a generation carrying statistical habits "
          "into breeding experiments, and became genetics within a decade. "
          "Wegener's continental fit was an argument in 1912 and an exhibit in "
          "1963, when oceanographers held the sonar maps and the magnetic data "
          "that made mobility checkable; the idea needed no new statement, only "
          "new verifiers. The condition is not the community's virtue but its "
          "capacity: a field can only uptake what its instruments and habits let "
          "it test — which reframes 'premature' from a compliment into a "
          "measurement, the distance between an idea and its receivers. "
          "<b>C6 — Generative saturation: the century test.</b> Profoundness is "
          "ratified retrospectively, by the harvest: Newton's mechanics paying out "
          "for two centuries; Darwin's algorithm still compounding through the "
          "modern synthesis into evolutionary medicine; the Gödel–Turing boundary "
          "results seeding computability, complexity theory, and the machine age; "
          "Shannon's bounds governing every channel built since. This is a "
          "condition on the verdict rather than the event — profundity, it turns "
          "out, is not a property a breakthrough has but a property history "
          "confers, on evidence that takes decades to accrue.")

CH4_P7 = ("One expected condition is missing from the list, deliberately: the "
          "crisis. Kuhn's classic model — anomaly accumulates, crisis deepens, "
          "revolution follows — is the folk theory of breakthrough conditions, "
          "and the case base bends it in two places. Anomalies are not "
          "sufficient: as Volume I recorded, the patching repertoire of a living "
          "framework is indefinitely elastic — epicycles absorbed every planetary "
          "irregularity for fourteen centuries, and the Lorentz contraction "
          "absorbed the Michelson–Morley null result with mathematics so good the "
          "equations survived the theory's death. And anomalies are not strictly "
          "necessary, in the operational sense above: Darwin faced no crisis in "
          "natural theology, since no observation had falsified special creation; "
          "Gödel faced no crisis in mathematics, since the theorems were arriving "
          "on schedule. What both faced was a prepared community with a rising, "
          "unnamed appetite for a different kind of explanation. The honest "
          "revision: anomaly surplus is a sociological accelerant, not a logical "
          "trigger. It raises the tolerance for reconceptualization and lowers "
          "the reputational price of the deletion; it does not cause the grammar "
          "change, and no quantity of anomaly ever did. Table 2 assembles the six "
          "conditions against four decisive cases.")

TABLE2_CAPTION = ("Table 2. The six conditions against four decisive cases. Wegener's "
                  "row is the pattern's power test: one absent condition (C1), fifty "
                  "years of delay.")
TABLE2_HEADER = ["Condition", "Darwin, 1859", "Gödel, 1931", "Turing, 1936", "Wegener, 1912"]
TABLE2_ROWS = [
    ("C1 · instrument",
     "Malthus's arithmetic; Lyell's geology",
     "Hilbert's formalism; Principia",
     "Formal logic; the posed Entscheidungsproblem",
     "Absent — seafloor and paleomagnetic instruments lay decades ahead"),
    ("C2 · distance",
     "Gentleman naturalist outside the schools",
     "24, at the edge of the Vienna Circle",
     "24, new from Cambridge",
     "Meteorologist among geologists"),
    ("C3 · carrier",
     "The Origin — one long argument",
     "The proof — compels step by step",
     "The proof, then the machine itself",
     "The book — vivid, with a hole where the mechanism belonged"),
    ("C4 · embedding",
     "Artificial selection as demonstration case",
     "All classical theorems survive",
     "All effective procedures simulated",
     "None possible without a mechanism"),
    ("C5 · community",
     "Partial — the field split for sixty years",
     "Ready — trained to check proofs",
     "Small but ready (Church, von Neumann)",
     "Absent — hostile until the instruments"),
    ("C6 · harvest",
     "Modern synthesis to evo-devo",
     "Computability to complexity theory",
     "The digital age",
     "Arrived with plate tectonics, 1960s"),
]

# ---------------------------------------------------------------------------
# Chapter 5
# ---------------------------------------------------------------------------

CH5_P1 = ("Now take the intersection. Nine cases — the physics trio of Volume I and "
          "the six revisions of Chapter 2 — with Mendel excluded as the control that "
          "tests the rules rather than the pattern they describe. Eight properties "
          "occur in all nine. None of the eight is novel as an observation; what is "
          "new is their joint invariance, and the fact that no other property in "
          "the record is shared so universally — which is why this study calls "
          "them, together, the common signature. Table 3 states each with its "
          "cross-case evidence.")

TABLE3_CAPTION = ("Table 3. The common signature: eight invariants present in every "
                  "case in the study, on every continent of the map of knowledge "
                  "sampled.")
TABLE3_HEADER = ["Invariant", "What It Means", "Across the Cases"]
TABLE3_ROWS = [
    ("Vocabulary change",
     "The revision lands in the constitutive terms, not in the sentences",
     "gravity; space and time; species; proof; machine; information; element; continent"),
    ("Selective demolition",
     "Something constitutive is deleted, not patched",
     "two-world cosmos; ether; determinism; phlogiston; fixed species; Hilbert's "
     "complete system; the fixed crust"),
    ("A duality unified",
     "Deep opposites are shown to be one thing",
     "heaven/earth; space/time; wave/particle; human/animal; calculation/machine; "
     "fire/life"),
    ("Conservative embedding",
     "The predecessor survives as a limit case",
     "Kepler in Newton; Newton in Einstein; classical theorems below Gödel's "
     "threshold; artificial in natural selection"),
    ("The reflexive turn",
     "The framework is aimed at its own foundations, user, or medium",
     "the observer inside the physics; arithmetic about arithmetic; the clerk as "
     "machine; man inside Darwin's tree; the channel as object"),
    ("A deeper problem opened",
     "The triumph installs a harder question than it answered",
     "action at a distance; heredity; quantum gravity; the measurement problem; "
     "what truth outruns proof; the halting problem; what drives the plates"),
    ("Generative saturation",
     "The harvest runs for decades, unanticipated",
     "two centuries of celestial mechanics; the modern synthesis; the machine age; "
     "every channel since Shannon"),
    ("Retrospective inevitability",
     "A generation later it cannot be seen as an idea at all",
     "the continent fit as a children's puzzle; selection felt as arithmetic; "
     "'the machine computes' as trivia"),
]

CH5_P2 = ("Two of the eight deserve expansion because they are the least expected. "
          "The first is the reflexive turn. Every framework in the record was, at "
          "its moment of profundity, pointed at its own foundations, user, or "
          "medium: the sky entered mechanics, the observer entered the physics, "
          "arithmetic became an object of arithmetic, the human calculator became "
          "the definition of the machine, the theorist became a specimen of the "
          "theory, the channel became an object of the engineering. This is not an "
          "accident of style but a structural necessity. Constitutive concepts are, "
          "by definition, the ones the framework stands on; to revise them, the "
          "apparatus must be aimed downward at its own supports, and "
          "self-application is the only aim that reaches. The reflexive turn is "
          "also why the boundary results cluster so tightly — Cantor, Gödel, "
          "Tarski, Turing, and, in its biological accent, Darwin's removal of the "
          "exemption for the theorist's own species: each is the system "
          "describing the limits of its own descriptive power, which is the only "
          "place such limits could be written down.")

CH5_P3 = ("The second is retrospective inevitability, and it is stranger than it "
          "sounds. At the moment of proposal, each of these ideas was "
          "unbelievable — not slightly doubtful but, by the standards of its day, "
          "structurally absurd: the Moon falling, species dissolving, proof "
          "failing, the clerk being a machine. A generation later, each is "
          "unnoticeable — the continental fit is now a children's puzzle, "
          "selection feels like arithmetic, and speaking of machines computing is "
          "too obvious to remark on. The whiplash from absurd to self-evident, "
          "within a single demographic turnover, is the most distinctive "
          "phenomenological signature of the level, and it has a consequence that "
          "Turing, characteristically, stated in advance as a prediction about his "
          "own idea.")

CH5_QUOTE_TURING = ("“I believe that at the end of the century the use of words and "
                    "general educated opinion will have altered so much that one will "
                    "be able to speak of machines thinking without expecting to be "
                    "contradicted.”",
                    "— Alan Turing, “Computing Machinery and Intelligence,” Mind (1950)")

CH5_P4 = ("That sentence is the absorption trajectory of Chapter 3 written from "
          "inside, by the man whose sentence was about to ride it: profundity's "
          "last disguise, as he saw, is fluency. What is common to all major "
          "scientific breakthroughs can now be said in one figure of grammar, "
          "one metric, and one law. The figure: ordinary science writes new "
          "sentences in a standing grammar; profound novelty changes the "
          "grammar, after which the old sentences can be paraphrased but not "
          "translated word for word, and the new sentences were unsayable before "
          "— incommensurability is translation failure, nothing more mystical. "
          "The metric: profundity is proportional to the depth at which the "
          "revision lands in the knowledge-generating stack — data, laws, "
          "vocabulary — and the breadth of consequence and the duration of the "
          "aftermath scale with that depth, which is why Level 3 changes "
          "reorganize fields for centuries while Level 1 changes reorganize "
          "curricula for a season. And the law, the strongest generalization this "
          "study supports: every profound breakthrough is a boundary statement — "
          "a claim about what frameworks can express, decide, or guarantee — and "
          "never merely a content statement within one. No clock can define its "
          "own simultaneity (Einstein); no proof can certify its own consistency "
          "(Gödel); no machine can decide its own halting (Turing); no channel "
          "can carry more than its capacity (Shannon); no mind is required for "
          "the work of minds (Darwin); nothing is created or destroyed "
          "(Lavoisier); and no crust is permanent (the closing irony of the "
          "drift). Boundary statements are also, structurally, unanswerable "
          "within the framework they bound — which is why each had to wait for "
          "an instrument from outside.")

# ---------------------------------------------------------------------------
# Chapter 6
# ---------------------------------------------------------------------------

CH6_P0 = ("The conditions of Chapter 4 make testable predictions, and history, "
          "uncooperative about controlled experiments, has nonetheless run the "
          "removal trials: right ideas with one missing condition. Three are "
          "famous enough to carry the argument, and Table 4 sets them side by "
          "side. What the table shows on close reading is the striking fact of "
          "the pattern: when the missing condition arrived, the idea required no "
          "new statement. Mendel's 1866 paper was the 1900 law, in the same "
          "words, waiting; Wegener's fit was plate tectonics' exhibit A, "
          "waiting; the antisepsis that Pasteur's germs finally justified was, "
          "in its practice, Semmelweis's practice, waiting. Ideas wait; "
          "conditions do not. It is the cleanest confirmation available to a "
          "study that cannot experiment — the conditions, not the ideas, carry "
          "the clock.")

TABLE4_CAPTION = ("Table 4. Prematurity as natural experiment: correct ideas, "
                  "missing conditions, and what happened when each condition "
                  "arrived.")
TABLE4_HEADER = ["Case", "What Was Right", "The Missing Condition", "What Happened When It Arrived"]
TABLE4_ROWS = [
    ("Mendel, 1865",
     "Quantitative inheritance: segregation in clean ratios, discrete factors",
     "C5 — a community with statistical habits; biology had none yet",
     "1900: de Vries, Correns, Tschermak; the same paper became genetics"),
    ("Wegener, 1912",
     "Mobile continents: the fit of coasts, fossils, and strata",
     "C1 — instruments for the mechanism; C5 followed from it",
     "1963: Vine–Matthews and the magnetic stripes; the field converted "
     "within five years"),
    ("Semmelweis, 1847",
     "Antisepsis: childbed mortality fell from around ten percent to under two",
     "C1 conceptual — germ theory; and no embedding for brute fact",
     "1860s–80s: Pasteur and Lister; the practice returned without the "
     "argument"),
]

CH6_P1 = ("The convergence model predicts a second, subtler signature: "
          "multiplicity. If breakthroughs are products of converging conditions, "
          "they should arrive more than once, to whoever stands in the stream — "
          "and the record obliges, embarrassingly. The calculus: Newton and "
          "Leibniz. Evolution by selection: Darwin and Wallace, whose Ternate "
          "letter of 1858 forced the joint reading at the Linnean Society, "
          "history's gentlest collision. Conservation of energy: Mayer, Joule, "
          "and Helmholtz within five years — and Mayer's first paper was "
          "rejected by the leading physics journal of the day. Oxygen: "
          "Priestley, Scheele, and Lavoisier, where the first two held the gas "
          "and the third held the meaning — Volume I's dissociation between "
          "formalism and meaning, replayed inside a single element. Neptune: "
          "Adams and Le Verrier, the same perturbation arithmetic done "
          "independently. Non-Euclidean geometry: Gauss, who suppressed it "
          "fearing the 'clamor of the Boeotians,' Lobachevsky, and Bolyai. And "
          "the boundary of computation itself: Church's lambda-definability "
          "and Turing's machines, months apart, proved equivalent by Turing's "
          "appendix — even the founding document of the computer age is a "
          "multiple. Merton's reading of multiples is the right one: they are "
          "not coincidence but a census result, the epistemic system "
          "reporting that the credit belongs to the conditions. Genius "
          "determines who arrives first, in what form, and how well it is "
          "argued; the conditions determine whether the arrival happens at "
          "all. The corollary is a warning label on priority disputes: the "
          "Newton–Leibniz war, prosecuted with a stacked Royal Society "
          "report and a British loyalty to fluxions that arguably cost "
          "English mathematics a century of isolation, was the spectacle of "
          "two men fighting over the deed to a river.")

CH6_P2 = ("One boundary case disciplines the pattern: technology. The great "
          "engineering marvels of the record — the jet, the rocket, the "
          "transistor as artifact — are Level 1 and Level 2 events: superb "
          "new sentences in a standing grammar, better answers to standing "
          "questions. The computer is the exception that proves the demotion "
          "it illustrates. It existed as a Level 3 concept — the universal "
          "machine, 1936 — a decade before it existed as a working artifact, "
          "and it was deduced from a vocabulary change rather than built to "
          "a need. This is why the computer keeps escaping every category "
          "assigned to it: a machine whose purpose is general is a category "
          "error made industrially real, and the source of its "
          "uncategorizability is precisely that it descends from a grammar "
          "change and not from a requirements document. The lesson "
          "generalizes: artifacts whose concept is Level 3 reorganize the "
          "world around them; artifacts whose concept is Level 1 or 2, "
          "however magnificent, reorganize their industry.")

CH6_P3 = ("Can the pattern predict? The honest answer is a structural no, "
          "with practical asterisks. No: the conditions are visible only in "
          "retrospect — the adjacent possible is named after the door opens; "
          "the community's judgment at time zero is systematically wrong "
          "(Hilbert expected completeness within the decade, at the same "
          "conference where Gödel had already announced its negation; "
          "Kelvin's two clouds were offered as small print on a finished "
          "building); and a constitutive claim cannot be evaluated in the "
          "old vocabulary it proposes to retire — the referee is always "
          "inside one of the frameworks being bounded. The asterisks: "
          "leading indicators exist, are honest, and are ignored at cost. "
          "When a formal instrument matures at a discipline's frontier, a "
          "Level 3 revision is loading — spectroscopy before the quantum "
          "atom, X-ray diffraction before the structure of DNA (a case this "
          "study bracketed, and which fits every rule here), and the reader "
          "can supply the current candidates. When anomaly patches begin "
          "to accumulate visibly, tolerance is rising. When the young and "
          "the dual-trained begin crossing into a field carrying foreign "
          "instruments, the demographics of C2 are assembling. Indicators "
          "indicate; they do not schedule. The pattern's honest product is "
          "not prediction but recognition — the ability to tell, at the "
          "moment an unfashionable idea is being declined, which queue it "
          "belongs in.")

CH6_P4 = ("Finally, the pattern's own boundary conditions. The case base "
          "spans the exact and natural sciences: mechanics, light, atoms, "
          "chemistry, logic, computation, heredity, and the solid Earth. "
          "Extrapolation to the sciences of the complex — economics, "
          "psychology, their hybrids — is plausible, and their candidate "
          "Level 3 revisions (the market as an information processor, the "
          "mind as a computation) are, on this framework, mid-absorption: "
          "too young for the century test, which is why they still read as "
          "ideology to some and as grammar to others. Art and politics "
          "share the grammar metaphor but fail the embedding criterion — "
          "cubism did not have to contain classicism as a limit case to "
          "win — and so a theory of scientific profundity stops, honestly, "
          "at the edge of its evidence. The boundary is itself a boundary "
          "statement, and this study declines to be the exception to its "
          "own law.")

# ---------------------------------------------------------------------------
# Chapter 7
# ---------------------------------------------------------------------------

CH7 = [
    ("The theory assembled across the two volumes can now be stated in a "
     "single connected sentence, and it is long because the thing it "
     "describes is. A profound, novel breakthrough is a revision at the "
     "level of the vocabulary of a science — the meanings of its "
     "constitutive terms, the grammar in which its laws are written — made "
     "possible when the adjacent possible supplies an instrument that "
     "renders the new concept statable; performed by a mind trained enough "
     "to command the instruments and distant enough to doubt the ontology "
     "they carry; carried in a medium that compels without its author; "
     "admitted by embedding the old order as a limit case rather than an "
     "error; taken up by a community trained to verify it; ratified over "
     "decades by a harvest nobody anticipated; and remembered — its final "
     "paradox — by becoming invisible, the light its successors see by."),

    ("Beneath the sentence sit two patterns deep enough to be called the "
     "shape of depth. The first is the reflexive turn: every framework at "
     "its moment of profundity was aimed at its own foundations, user, or "
     "medium — because constitutive concepts can only be revised from "
     "inside the apparatus that stands on them, and because the strongest "
     "available statement any system can make is a statement of its own "
     "boundary. The second is convergence: the multiples census shows that "
     "the breakthrough is an attractor of the epistemic system's state — a "
     "place history goes when its conditions point there — not the private "
     "property of the minds that arrive first. The individuals of this "
     "study were extraordinary; the pattern of their replaceability is the "
     "finding. Wallace, Church, Scheele, Adams: at every profundity in the "
     "record, there was a second reader standing in the same river."),

    ("The demotion of the individual is the study's most counterintuitive "
     "result, and it should be read as leverage, not insult. If profundity "
     "were personal magic, nothing could be done about its scarcity; "
     "because it is the convergence of conditions, the conditions can be "
     "protected. Tolerate anomaly without demanding immediate repair — the "
     "patching reflex feels like hygiene and is the enemy of revision. "
     "Fund instruments with no application in sight — Riemann's lecture was "
     "pure mathematics for sixty years, the sonar survey was military "
     "geography, and general relativity runs on both. Respect the "
     "peripheral and the young — the patent clerk, the meteorologist, the "
     "twenty-four-year-old at the edge of the circle; they are not "
     "ornaments of the story but its delivery mechanism, the demographic "
     "in which distance and preparation coexist. Protect the carriers — "
     "open, checkable publication, because a proof is a mind that travels "
     "without a passport. And teach the old theories as limit cases, not "
     "as errors: the bridge is how crossings are made, and every Newton of "
     "the future will need an Einstein to walk across. One warning belongs "
     "in the margin of every syllabus and grant proposal, and it is this "
     "study's last word: on this evidence, the next profound novelty is "
     "most likely already in print — correct, patient as arithmetic, cited "
     "by almost no one — waiting, as Mendel waited, for the conditions to "
     "arrive. The discoverers are replaceable. The reading is not."),
]
