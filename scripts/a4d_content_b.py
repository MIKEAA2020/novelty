# -*- coding: utf-8 -*-
"""Content module for 'The Alien Reading, Executed' — part B: Chapters 4-6."""

# ---------------------------------------------------------------------------
# Chapter 4 — The Unblinding: The Outgroup Test
# ---------------------------------------------------------------------------

CH4_S1 = [
    ("The outgroup test is the question this amendment was ordered to "
     "answer, and its headline number comes first. The family now has "
     "four blind runs — the two A4b coders, the third reading, the "
     "fourth — and their mutual weighted agreement spans 88.0 to 94.4 "
     "percent (mean 90.2, the two original coders' 94.4 at the top). "
     "The alien's agreement with those same four runs spans 86.1 to "
     "87.5 percent, mean 86.9. The gap is 3.3 points: the outgroup "
     "sits below the family band, measurably, consistently — and "
     "with zero outright inversions against any family reading, "
     "every single disagreement landing one step away, adjacent, "
     "never opposed. The verdict the census prints is therefore "
     "double-edged and exact. The lineage effect is real: readings "
     "of the same instrument differ by family at a distance the "
     "family's own runs do not match, and the genetic-dependence "
     "confession was load-bearing, not ritual. And the effect is "
     "small and monotone: a calibration offset, not a worldview — "
     "no cell anywhere in the record flips from satisfied to "
     "failed across the lineage fence."),

    ("Where the distance lives is the finding under the headline, "
     "because it is not scattered. Against the two A4b coders, the "
     "alien's per-point agreement bottoms at formalism and meaning "
     "— 66.7 percent, the floor of the entire table — with "
     "conservative embedding at 79.2, deletion at 83.3, and "
     "derivation-first at 87.5; the constant, the slope, and "
     "crisis-chaining sit above 91. Against the third and fourth "
     "readings, the soft band repeats: deletion 78.1, "
     "derivation-first 78.1, unification 81.2. These are, cell for "
     "cell, the instrument's declared elastic joints — the "
     "presence-versus-profundity ambiguity on the formalism point, "
     "the birth-window and direction-split stipulations, the "
     "two-births problem — every one of them printed in the census's "
     "own amendment record before the alien ever ran. The census's "
     "amendment map predicts where an outgroup will part from it. "
     "The disagreements are not noise in the reading; they are the "
     "instrument's own labeled soft spots, seen from the other side "
     "of the lineage fence."),

    ("The alien against the census's own history tells the same "
     "story from a different angle, and its two cleanest facts "
     "belong together. Against the census as originally written, "
     "the alien agrees on the old dead side at 72.2 percent with "
     "two outright inversions — and both of them, inspected, land "
     "on cells the census had already revised before the alien "
     "ran: the ether's derivation-first, where the alien's satisfied "
     "sits one step beyond the amended partial the A4b court "
     "adopted; and phlogiston's founders, where the alien's failed "
     "is the A4b refutation itself, arrived at independently, from "
     "outside the family, without ever having seen the amendment. "
     "Against the amended dead side of four theories the alien "
     "reads 79.2 percent; against the living trio, twenty-six of "
     "twenty-seven, its single break the Newton formalism cell. "
     "The alien, in short, lands on the amendments rather than on "
     "the originals the author first wrote — the substitution's "
     "question from A4c, answered now from outside the school."),

    ("The fourth reading's numbers price the new pair and the "
     "family's stability. Against the census as originally written, "
     "77.8 percent with a single inversion — phlogiston's founders "
     "again, landing on the already-revised cell. Against the "
     "amended dead side of four theories, 86.1. Against the amended "
     "germ profile, 94.4. The living trio, twenty-six of "
     "twenty-seven, the break Newton's formalism cell — the "
     "quantum's derivation cell, broken once by the third reading, "
     "does not break again, and is recorded as the rarer elastic "
     "joint. And against the pre-registration locked before it "
     "ran: 97.2 percent over the new pair's eighteen cells — "
     "caloric exact, cell for cell, all nine; thermodynamics eight "
     "of nine, the disagreement sitting on the derivation cell the "
     "pre-registration itself had named contestable. Table 5 "
     "assembles the numbers; Table 6 the per-point bands; the "
     "court's docket follows from them."),

    ("The docket, before the court convenes. Three cells now carry "
     "post-amendment reading records that no longer support the "
     "census's cells, and in each the alien's vote is among the "
     "movers. Newton's formalism cell: the two A4b coders "
     "satisfied, and then the third reading, the fourth, and the "
     "alien all partial — three consecutive post-amendment readings "
     "plus the outgroup against the census's satisfied. The ether's "
     "embedding cell: the two A4b coders satisfied, the third and "
     "fourth readings partial, the alien partial — the author's "
     "failed, defended since A4b by the successor-recovery "
     "refinement, now the minority reading in the record. And "
     "miasma's crisis cell: three post-amendment readings — third, "
     "fourth, and the alien — all failed against the census's "
     "partial. The motion rule A4c locked before the alien ran "
     "binds the author in advance: where the outsider's reading "
     "and the blind readings agree against the census, the census "
     "moves. Chapter 5 tries the docket under it."),
]

TABLE5_HEADER = ["Comparison", "Cells", "Weighted", "Exact / Adj / Dist"]

TABLE5_ROWS = [
    ("Alien (gpt) vs A4b coder A", "54", "87.0%", "40 / 14 / 0"),
    ("Alien (gpt) vs A4b coder B", "54", "87.0%", "40 / 14 / 0"),
    ("Alien (gpt) vs third reading X3", "72", "86.1%", "52 / 20 / 0"),
    ("Alien (gpt) vs fourth reading B4", "72", "87.5%", "54 / 18 / 0"),
    ("B4 vs A4b coder A", "54", "88.0%", "41 / 13 / 0"),
    ("B4 vs A4b coder B", "54", "89.8%", "43 / 11 / 0"),
    ("B4 vs third reading X3", "72", "91.7%", "60 / 12 / 0"),
    ("X3 vs A4b coders A and B (A4c, for scale)", "54", "90.7%",
     "44 / 10 / 0"),
    ("A4b coder A vs A4b coder B (A4b, for scale)", "54", "94.4%",
     "48 / 6 / 0"),
    ("Alien (gpt) vs census v1 (old dead side)", "27", "72.2%",
     "14 / 11 / 2"),
    ("Alien (gpt) vs amended census (dead side)", "36", "79.2%",
     "21 / 15 / 0"),
    ("B4 vs amended census (dead side)", "36", "86.1%", "26 / 10 / 0"),
    ("B4 vs the A4d pre-registration (new pair)", "18", "97.2%",
     "17 / 1 / 0"),
]

TABLE5_CAPTION = ("Table 5 — The unblinding, all readings: the family's "
                  "four runs span 88.0-94.4 percent mutual agreement; the "
                  "alien spans 86.1-87.5 against them — 3.3 points below "
                  "the band, zero inversions. The new pair's pre-registered "
                  "coding holds at 97.2 under the fourth blind reading.")

TABLE6_HEADER = ["Signature point", "Alien vs A4b A+B",
                 "Alien vs X3+B4", "The disagreement's character"]

TABLE6_ROWS = [
    ("Deletion at birth", "83.3%", "78.1%",
     "The birth-window: deletions spread over decades, and the "
     "christening question the census had to stipulate."),
    ("Unification", "95.8%", "81.2%",
     "Postulated-substance unity versus dissolved joints — the "
     "alien's own flag, matching the demotion."),
    ("Universal constant", "95.8%", "93.8%",
     "The sharpest row holds cross-family — with the ether's "
     "ownership dissent the one recorded break."),
    ("Derivation-first", "87.5%", "78.1%",
     "The two-births problem and the founding's instruments."),
    ("Conservative embedding", "79.2%", "87.5%",
     "The direction-split and the attribution rule — the softest "
     "joint, from both sides of the fence."),
    ("Formalism / meaning", "66.7%", "84.4%",
     "The floor of the table: presence versus profundity, flagged "
     "by every reading that ever broke the cell."),
    ("Founders' resistance", "91.7%", "93.8%",
     "The coin threshold: whose surrender counts, paid when."),
    ("Generative slope", "91.7%", "100.0%",
     "Every dead tradition generative-then-degenerating, no "
     "living theory — unanimous with the fourth reading."),
    ("Crisis-chaining", "91.7%", "84.4%",
     "Deeper floor versus deferred question versus fatal anomaly."),
]

TABLE6_CAPTION = ("Table 6 — Per-point weighted agreement for the alien "
                  "reading: against the two A4b coders (twelve comparisons "
                  "per point) and against the third and fourth readings "
                  "(sixteen cells per point). The floor is the formalism "
                  "point; the soft band is the census's own amendment "
                  "record.")

FIG1_CAPTION = ("Figure 1 — The A4d design: the replication kit leaves "
                "the series through its owner, is administered to a "
                "reader of another family (gpt), and returns as the "
                "alien reading; the fourth blind coding widens the panel "
                "to ten; the outgroup test measures the lineage gap "
                "(3.3 points, zero inversions); the court moves three "
                "cells under the pre-registered motion rules; the kit "
                "re-issues at ten theories.")

# ---------------------------------------------------------------------------
# Chapter 5 — The Adjudication
# ---------------------------------------------------------------------------

CH5_S1 = [
    ("The court reconvenes under the rules A4c locked before the alien "
     "ever ran, and they are restated before any ruling: evidence over "
     "authorship, every contested cell tried against named historical "
     "fact; the motion rule — where the outsider's reading and the "
     "blind readings agree against the census, the census moves; and "
     "the census-killing clauses stay armed. The docket has three "
     "parts — the motion cells, the contested cells of the new pair, "
     "and the defended dissents — and Table 7 is its ledger. What "
     "makes this session different from every court before it is "
     "written into each movement: the alien's vote is among the "
     "movers, and the movements are therefore the reading's material "
     "effect on the census, not its decoration."),

    ("Newton's formalism cell, tried first because the record is now "
     "unambiguous. The readings: the two A4b coders satisfied; the "
     "third reading, the fourth, and the alien all partial — three "
     "post-amendment family readings plus the outgroup, against the "
     "census's satisfied. The evidence both ways: on one side, the "
     "inverse-square law was common currency before the Principia — "
     "Halley, Wren, and Hooke all held it from Kepler's third law "
     "plus Huygens's centrifugal measure, and Halley's 1684 visit "
     "posed the orbit question Newton's dynamics answered — so the "
     "profound move was new mathematics plus new system, not an "
     "interpretation of inherited mathematics; on the other, the "
     "formalism was accepted for a century and a half while its "
     "meaning was fought over, hypotheses non fingo in 1713 to "
     "Mach's re-reading in 1883, which is dissociation exactly as "
     "the point writes it. The ruling: the cell moves to the dual "
     "form — satisfied as written, partial on the "
     "interpretation-arrival reading — the living side's first dual "
     "cell, and the presence-versus-profundity flag that A4c adopted "
     "is now a cross-family fact of the instrument rather than one "
     "school's scruple."),

    ("The ether's embedding cell, tried second, because the "
     "pre-registration's own convention is at stake. The readings: "
     "the two A4b coders satisfied, the third and fourth readings "
     "partial, the alien partial — the author's failed, defended "
     "since A4b by the successor-recovery direction, now the "
     "minority position in the record. The evidence: Maxwell's "
     "equations survived the medium's deletion without a changed "
     "symbol, and Fresnel's dragging coefficient — conjectured from "
     "Arago's 1810 null, confirmed by Fizeau in 1851 — is recovered "
     "exactly as the first-order term of the relativistic velocity "
     "addition, a theorem surviving as a limit; the medium itself, "
     "meanwhile, received no domain of validity anywhere. The ruling: "
     "the composite cell moves to partial, and the discriminating "
     "face is restated as the direction the census always meant — "
     "successor-recovery of the ontology, on which every dead "
     "theory in the panel fails without exception. With the "
     "structure-versus-craft distinction now doctrine — theorems "
     "survived the ether, the epicycles, and caloric; craft "
     "survived miasma; nothing survived phlogiston — the composite "
     "records what survived, and the direction keeps the "
     "discrimination. The demotion is a restatement, not an "
     "inflation: the fifth pair forced it by being the first "
     "quantitative corpse."),

    ("Miasma's crisis cell, tried third. The readings: the census's "
     "partial — pre-registered in A4c and sustained there against "
     "the third reading's dissent — now against the third reading, "
     "the fourth, and the alien, all failed. The evidence, both "
     "ways: the sanitary program's archive and its environmental "
     "question armed Snow and Koch, which was the A4c ruling's "
     "ground; but the doctrine itself closed no crisis — it was the "
     "inherited frame, not a founding — and it opened no deeper "
     "floor: it faded, its last theoretical gesture (Pettenkofer's "
     "groundwater variant, 1869-73) generating no successor program. "
     "The archive's productivity is real, and it belongs to the "
     "apparatus — the registers, the infrastructure — which CR-2 "
     "already credits separately as death-of-ontology-not-of-"
     "apparatus. The ruling: the cell moves to failed, the census "
     "against its own pre-registered coding, the motion rule "
     "executed a third time; the oldest corpse in the history of "
     "science is now also the emptiest profile the census has ever "
     "recorded — one partial in nine cells."),

    ("The contested cells of the new pair, tried under the same "
     "rules, with the fourth reading as the blind evidence and the "
     "alien silent (its panel ends at eight). Caloric's profile "
     "stands as pre-registered — deletion failed, the substance "
     "inherited and renamed by the Traité while the famous "
     "deletions in the same book belong to the oxygen pair's "
     "christening; unification partial, vocabulary-level; the "
     "constant failed; derivation partial, the structure-not-"
     "content rule's strongest case, Carnot's theorem surviving the "
     "frame that derived it while the friction anomalies were "
     "retrofitted; embedding partial, the theorems surviving "
     "verbatim with no parameter limit in sight; measurables "
     "partial — minted at a strength no dead theory had shown, "
     "the killing coin the successor's; founders failed, Carnot's "
     "private recantation never tendered; the slope "
     "generative-then-degenerating; crisis partial, the "
     "motive-power question opened inside the program becoming the "
     "successor's foundation. Thermodynamics, with its two "
     "contested cells: derivation-first stands satisfied — the "
     "first law is the textbook case of multiple independent "
     "discovery, Mayer's 1842 derivation from the old gas data "
     "and Helmholtz's 1847 synthesis needing no new instruments, "
     "with Joule's measurements the third road — and the two-roads "
     "stipulation (the derivation road and the experimental road, "
     "both founding the same law) enters the instrument beside "
     "the birth-window; the dissent is printed with its evidence. "
     "The constant stands partial — the J/k dual structure, "
     "printed in full in the pre-registration — and with it the "
     "domain-marked discriminator gains its first within-physics "
     "middle band: caloric failed, thermodynamics partial, the "
     "trio satisfied."),

    ("The defended dissents, printed with their evidence and left "
     "standing. Germ theory's founders cell holds at partial with "
     "the record split — the third reading partial, the fourth and "
     "the alien failed — because the evidence is specific: "
     "Pasteur's surrender of the chemical-catalysis theory of "
     "fermentation he absorbed from his own formation, paid "
     "publicly against Liebig to the elder's death in 1873, is "
     "payment; the dissenting readings' evidence — costs paid by "
     "forerunners against incumbents, Semmelweis's ruin above all "
     "— is real and prices other people's coins, not the founders' "
     "own; the cell is recorded as elastic, the graduated scale "
     "holding at compromise-to-surrender. The ether's constant "
     "cell holds failed under the ownership rule — a constant is "
     "credited to the frame that makes it invariant, not the frame "
     "that measures it — with the alien's partial recorded as the "
     "ownership question's cross-family elasticity, its own point "
     "note naming the same fork. Miasma's embedding cell holds "
     "failed — the craft that survived was engineering, not "
     "theory, and the structure-versus-craft distinction is now "
     "the doctrine's answer to the fourth reading's dissent. And "
     "the two as-written formalism cells — the ether's and the "
     "epicycles' — hold their duals, their cross-family splits "
     "recorded in the ledger as the presence-versus-profundity "
     "joint's measured width."),
]

TABLE7_HEADER = ["Contested cell", "Readings", "The evidence the court weighed",
                 "Ruling"]

TABLE7_ROWS = [
    ("Newton · formalism", "S / P,P,P",
     "The inverse-square law common currency before 1684; the "
     "formalism fought over from 1713 to Mach — both readings of "
     "the point in one cell.",
     "Dual: S as written / P on the arrival reading — the motion "
     "rule fired"),
    ("Ether · embedding", "F / S,S,P,P,P",
     "Maxwell's equations and Fresnel's coefficient survive (the "
     "latter as the first-order limit); the medium recovered as "
     "no limit anywhere.",
     "Revised to P; successor-recovery of ontology restated as "
     "the discriminating face"),
    ("Miasma · crisis", "P / F,F,F",
     "The archive's productivity belongs to the apparatus (CR-2); "
     "the doctrine closed no crisis and faded, Pettenkofer's "
     "variant generating no successor.",
     "Revised to F — the census moves against its own "
     "pre-registration"),
    ("Germ · founders", "P / P,F,F",
     "Pasteur's Liebig surrender, paid publicly 1857-73 — against "
     "costs paid by forerunners, which price other people's coins.",
     "P stands; elasticity recorded"),
    ("Ether · constant", "F / F,F,F,P",
     "Maxwell's c-ratio measured inside the program; the "
     "invariant speed installed by 1905 — the ownership rule.",
     "F stands; the ownership fork now cross-family"),
    ("Miasma · embedding", "F / F,F,P",
     "The surviving sanitation was craft, not theory-structure; "
     "no theorems existed to survive.",
     "F stands; structure-versus-craft adopted"),
    ("Caloric · profile", "prereg / B4",
     "Nine cells pre-registered before the fourth reading ran; the "
     "blind reading returns the identical nine — the strongest "
     "corpse: partials on structure, machinery, measurables.",
     "Stands as pre-registered, cell for cell"),
    ("Thermo · derivation", "S / P",
     "Mayer 1842 from the old gas data; Helmholtz 1847; Joule's "
     "measurements the third road — the simultaneous-discovery "
     "record is the over-determination itself.",
     "S stands; the two-roads stipulation adopted; dissent "
     "printed"),
    ("Thermo · constant", "P / P",
     "J minted at the founding, a unit bridge demoted to a "
     "definition; k minted by the consolidation — the J/k dual.",
     "P stands — the constant's middle band, in physics"),
]

TABLE7_CAPTION = ("Table 7 — The adjudication ledger: nine cells tried, "
                  "three revised — every revision by the pre-registered "
                  "motion rule, the alien's vote among the movers each "
                  "time — one dual created, five sustained, the new pair's "
                  "profile standing as pre-registered. The author is "
                  "overruled on his own cells three times, which is what "
                  "pre-registering is for.")

# ---------------------------------------------------------------------------
# Chapter 6 — The Verdict: The Limit Broken and Measured
# ---------------------------------------------------------------------------

CH6_S1 = [
    ("The registration, clause by clause. The census survives its "
     "sixth reading, its first from another family: no dead theory "
     "— three physics corpses, the oldest framework in the history "
     "of science, and now the strongest quantitative corpse — "
     "passes any of the five discriminators under any reading ever "
     "run, and the ether's lone as-written satisfied remains the "
     "adjudicated confound it has been since A4b. Three cells "
     "moved, every one by the motion rule locked before the alien "
     "ran, the alien's vote among the movers each time: Newton's "
     "formalism cell to the dual form, the ether's embedding cell "
     "to partial with the discriminating direction restated, "
     "miasma's crisis cell to failed. The living side admits its "
     "strongest second resident — thermodynamics, six satisfied, "
     "two partial, zero failed — and pays for it with the "
     "constant's middle band: caloric failed, thermodynamics "
     "partial, the trio satisfied, the domain-marked point now "
     "printing a gradient inside its own domain instead of "
     "pretending to a clean line."),

    ("The genetic-dependence limit's new status, stated at the "
     "weight the series owes its loudest confession. Broken, as an "
     "availability fact: a cross-family reading exists, archived "
     "whole, and it did not merely validate — it moved the census, "
     "three cells, its vote the decisive one where the family's "
     "post-amendment readings were already leaning. Measured, for "
     "the first time: 3.3 points below the family band, zero "
     "inversions, the disagreements concentrated cell for cell on "
     "the instrument's declared elastic joints. And therefore "
     "reduced to what it always really was: a calibration "
     "question, not a validity question. The amendments replicate "
     "across the lineage precisely where they are amendments of "
     "the instrument — the alien lands on the ether's and "
     "phlogiston's revised cells without ever having seen them; "
     "the school's readings are not the world's; and the "
     "difference between them is now a number with a location, "
     "printed above, where any future alien reading can be "
     "measured against it. The day A4b promised has arrived, and "
     "the census is smaller, harder, and — for the first time — "
     "partly not the author's school's."),

    ("The amended signature, stated whole, and printed in Tables 8 "
     "and 9 against the five dead theories and the two living "
     "residents. Four domain-general discriminators: deletion at "
     "birth, with the core-posit and birth-window refinements; "
     "successor-recovery of the ontology — the embedding point's "
     "restated face, on which every dead theory fails; generative "
     "slope, the trend; minted measurables, operationalized. One "
     "domain-marked discriminator with a middle band: the "
     "universal constant, physics-relative and gradient-printing. "
     "Two restated points, now doubly restated: derivation-first "
     "as structure-not-content with the birth-window and "
     "two-roads stipulations; founders' resistance as "
     "payment-not-defense, graduated, with the refused-coin test. "
     "Two demoted: unification, its dead-side leg substance-"
     "narrowed; crisis-chaining, its weakest dead-side cell now "
     "weaker still. And the record now carries a gradient where "
     "it once carried a wall: the dead side runs from miasma — "
     "one partial in nine, the emptiest profile ever recorded — "
     "through phlogiston, deleted without remainder, to the "
     "structure-survivors, the epicycles, the ether, and caloric, "
     "the strongest corpse, three clean partials deep — while the "
     "living side runs from germ theory to thermodynamics to the "
     "trio, and the first dual cell sits on Newton. The census "
     "no longer sorts its panel into two heaps; it grades a "
     "slope."),

    ("The limits, at the weight the audit taught, and the kit "
     "renewed. One alien reading is a first measurement, not a "
     "law: the outgroup number is n=1, its family attested by "
     "delivery and interface markers rather than verifiable from "
     "inside, and a second family's reading could sit elsewhere "
     "in the band the first one defined. The adjudicator was "
     "again the author — mitigated, as before, by "
     "pre-registrations locked before runs and evidence printed "
     "for every ruling — and overruled three times, which is the "
     "design working, not the design failing. The count remains "
     "small and fame-confounded, and the fifth pair is the most "
     "famous pair heat owns. What this document does not claim "
     "is the larger arc, unchanged from the first census: a "
     "coding is not the world; the domain marks and the middle "
     "bands are confessions, not triumphs; and the world's "
     "ratification remains the only evidence this series "
     "acknowledges it lacks. The kit re-issues with this "
     "amendment at ten theories — the instrument, the panel, "
     "the scale, the evidence rule, the scoring scheme, and the "
     "adjudication rules verbatim, the widened prompt printed "
     "and archived — so that the next alien reading, from any "
     "family, run by anyone, anywhere, can test the ten and not "
     "only the eight. The ledger is open. Continue."),
]

CH6_QUOTE_KIT = (
    "The kit converts the clause from a purchase the environment "
    "cannot make into a standing offer the world can accept.",
    "The Widened Census, Chapter 6 — the offer was accepted; the "
    "receipt is Chapters 3 through 5 of this document; the offer "
    "re-issues at ten theories.",
)

TABLE8_HEADER = ["Signature point", "Phlogiston", "The ether", "Epicycles",
                 "Miasma", "Caloric"]

TABLE8_RATIOS = [0.21, 0.14, 0.16, 0.15, 0.15, 0.19]

TABLE8_ROWS = [
    ("Deletion at birth",
     "F — Becher's principle renamed; nothing deleted",
     "P * — the wave program deleted the corpuscle; its own "
     "center an inherited medium reinstated",
     "F — extended Eudoxus; circularity never touched",
     "F — the consolidated form deleted nothing",
     "F — the fire-principle renamed and quantified; the "
     "Traité's deletions were the oxygen pair's christening"),
    ("Unification",
     "P * — a posited substance is not a dissolved joint",
     "S — one medium under optics and electromagnetism",
     "P * — one toolkit across the planets; vocabulary, not law",
     "P — the zymotic class: administrative, not natural",
     "P — one substance's bookkeeping; the substance-versus-motion "
     "division begged"),
    ("Universal constant",
     "F — no quantitative core; weight forced phlogiston negative",
     "F — c belonged to the fields and outlived the medium",
     "F — dozens of parameters, zero invariants",
     "F — nothing constant; fitted coefficients per epidemic",
     "F — material properties; Dulong-Petit the exception-ridden "
     "regularity the successor explained"),
    ("Derivation-first",
     "F — each new gas retrofitted, after the fact",
     "P * — real derivational firsts; the defining note dishonored "
     "in 1887",
     "P — parameters from centuries of records: content, never "
     "structure",
     "F — the incumbent; data broke it rather than being derived",
     "P — Carnot's theorem survived the frame; the friction "
     "anomalies retrofitted"),
    ("Conservative embedding",
     "F — deleted without remainder by oxygen chemistry",
     "P * — the equations survived (Fresnel's coefficient as the "
     "first-order limit); the medium recovered as no limit — "
     "direction: F",
     "P — devices survive as Fourier; the ontology deleted",
     "F — the surviving sanitation was craft; no theorems existed "
     "to survive",
     "P — the theorems survive verbatim (Fourier, Carnot); no "
     "parameter limit"),
    ("Formalism / meaning",
     "F — no formalism; no measurable ever minted",
     "S as written * — discriminates only operationalized (A6)",
     "S as written * — the operationalized form discriminates",
     "F — no symbolic surface; no unit of miasma ever named",
     "P — minted (Black's latent heat, the calorie, the "
     "calorimeter); the killing coin was the successor's"),
    ("Founders' resistance",
     "F † — Priestley defended, paid nothing: defense is not "
     "payment",
     "P * — Lorentz surrendered detectability, kept the medium",
     "P * — Ptolemy's equant: a founder's compromise, collected "
     "for fourteen centuries",
     "F — refusal at the price of the body itself",
     "F — Carnot's private recantation, published 1878, was never "
     "tendered"),
    ("Generative slope",
     "S then D — the gas family; then negative weight",
     "S then D — Fresnel to the interferometer; then the "
     "incoherence triangle",
     "S then D — fourteen centuries; then the equant wound",
     "S then D — the sanitary acts and the register; then the "
     "restatements",
     "S then D — calorimetry to Carnot; then the capacity "
     "epicycles against Joule"),
    ("Crisis-chaining",
     "P — opened the air questions that killed it",
     "S as written * — closed the corpuscular crisis, opened the "
     "drift problem; demoted regardless",
     "P — the equant objection opened its execution",
     "F ‡ — it faded; the archive was apparatus, not doctrine "
     "(revised this run)",
     "P — the motive-power question, opened inside the program, "
     "became the successor's foundation"),
]

TABLE8_CAPTION = ("Table 8 — The census matrix after the fifth pair and "
                  "the alien reading: five dead theories, the dead side "
                  "now a graded slope from the emptiest profile ever "
                  "recorded to the strongest corpse. Cells marked * "
                  "revised this run or an earlier amendment's; † refuted "
                  "outright; ‡ revised by the motion rule this run. The "
                  "five-discriminator core holds on every column, on the "
                  "restated faces.")

TABLE9_HEADER = ["Signature point", "Germ theory (living)",
                 "Thermodynamics (living, new)"]

TABLE9_RATIOS = [0.22, 0.39, 0.39]

TABLE9_ROWS = [
    ("Deletion at birth",
     "S — the double deletion: spontaneous generation and "
     "foul-air etiology",
     "S — the double deletion: the substance of heat and "
     "unlimited convertibility"),
    ("Unification",
     "S — the brewer's vat and the surgical ward, one cause-class",
     "S — heat and work one currency; the firebox and the falling "
     "weight the same phenomenon"),
    ("Universal constant",
     "F — domain-marked: no constant to install; the point "
     "abstains outside physics",
     "P — the J/k dual: a conversion constant demoted to a "
     "definition; the true invariant minted by the consolidation — "
     "the middle band, in physics"),
    ("Derivation-first",
     "P * — promissory notes honored; the founding carried by its "
     "own new experiments",
     "S — over-determined by three roads (Mayer's derivation, "
     "Helmholtz's synthesis, Joule's measurements); the "
     "simultaneous-discovery record is the over-determination "
     "itself"),
    ("Conservative embedding",
     "P — the practice recovered, the ontology deleted; no limit "
     "in which foul air causes anything",
     "S — the strongest embedding in the census: Carnot verbatim, "
     "Fourier untouched, the no-work sector recovered with the "
     "reason why"),
    ("Formalism / meaning",
     "F as written / S operationalized — the organism minted: "
     "stainable, countable, cultivable",
     "S — absolute temperature, the joule, entropy minted; the "
     "efficiency bound a discriminating list that returns "
     "negatives"),
    ("Founders' resistance",
     "P — Pasteur paid Liebig his chemistry; Koch's tuberculin a "
     "cost imposed — elastic: two readings dissent",
     "P — Kelvin's tendered coin: formed in the caloric physics, "
     "publicly surrendered 1849-51, his own scale's foundation "
     "rebuilt — compromise-to-surrender"),
    ("Generative slope",
     "S — virology, immunology, antibiotics, molecular genetics: "
     "still generating",
     "S — Gibbs, the third law, the quantum, Shannon's entropy, "
     "black holes: the deepest cross-domain harvest on record"),
    ("Crisis-chaining",
     "S — closed the etiological deadlock; opened the host, the "
     "filterables, the carrier state",
     "S — closed the motive-power question; opened time's arrow, "
     "175 years and counting"),
]

TABLE9_CAPTION = ("Table 9 — The living residents after the fifth pair: "
                  "germ theory's profile unchanged from A4c; "
                  "thermodynamics the strongest second resident the case "
                  "base has admitted — and the first to give the "
                  "domain-marked constant a middle band.")

CALLOUT_NUMS = [
    ("1", "alien reading delivered across families",
     "the genetic-dependence limit broken as an availability fact — "
     "and its vote moved three cells"),
    ("3.3", "points the outgroup sits below the family band",
     "the lineage effect, measured: real, monotone, zero inversions"),
    ("10", "theories in the panel after the fifth pair",
     "no dead theory passes any discriminator under any of six "
     "readings"),
]

CALLOUT_CAPTION = ("The alien reading's own numbers: the offer accepted, "
                   "the lineage gap measured, and the panel the next "
                   "alien will be handed.")
