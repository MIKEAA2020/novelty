# -*- coding: utf-8 -*-
"""Content module for 'The Widened Census' — part B: Chapters 4-6."""

# ---------------------------------------------------------------------------
# Chapter 4 — The Unblinding
# ---------------------------------------------------------------------------

CH4_S1 = [
    ("The comparison method is the pre-registered one, unchanged from "
     "A4b: weighted agreement scoring exact cells at one, "
     "category-adjacent cells at one-half, and outright inversions at "
     "zero, with the slope's compound code scored on its degeneration "
     "flag and the census's one non-standard entry read as partial. "
     "Table 4 assembles the numbers, and the first verdict is visible in "
     "its second row. Against the census as originally written, the "
     "third reading agrees on the dead side at 77.8 percent weighted — "
     "already higher than either A4b coder's 70.4 — with two outright "
     "inversions, both at founders' resistance, the point A4b refuted. "
     "Against the amended census — the same twenty-seven cells after "
     "A4b's ten rulings — agreement rises to 87.0 percent, and the "
     "inversions vanish. That gap is the substitution's question "
     "answered: a fresh reader, handed the original, unamended "
     "instrument, lands on the amended cells rather than on the "
     "originals the author first wrote. Every A4b amendment replicates "
     "blind — the ether's satisfied-as-written cells on formalism and "
     "crisis, its partial on derivation, the epicycles' demoted "
     "unification, the founders' refutations, the constant's failure "
     "under every reading run to date. The amendments were not the "
     "author's taste. They were in the record for any fresh reader to "
     "find, and a third one has."),

    ("The new pair, against the pre-registration: 80.6 percent weighted "
     "over eighteen cells, with the two outright disagreements both at "
     "germ theory and both at the same structural place — the "
     "physics-shaped points. On derivation-first, the pre-registration's "
     "satisfied meets the coding's failed: the theory was established "
     "by its own new experiments — the swan-neck flasks of 1861, Koch's "
     "anthrax lifecycle of 1876, the demonstrated bacillus of 1882 — not "
     "derived from the existing record; Snow's 1855 monograph and "
     "Semmelweis's 1847 results were assimilated by the frame, not "
     "engines of its founding. On formalism and meaning, the "
     "pre-registration's satisfied — coded under the operationalized "
     "form, minted measurables — meets the coding's failed under the "
     "form as written, no symbolic surface existing to reinterpret. The "
     "disagreement is not between two readers; it is between two "
     "versions of the instrument, arriving from opposite directions at "
     "the same cell, and it is the as-written versus operationalized "
     "split demonstrated outside physics for the first time. The "
     "pre-registered fault line — E2, disagreement concentrated at the "
     "constant — fired exactly where predicted; the two distants "
     "surrounding it are the same finding's penumbra."),

    ("The living side's physics trio holds at twenty-five of twenty-seven "
     "exact, and the two breaks deserve their sentences. Newton on "
     "formalism and meaning: the coder's evidence is the post-Principia "
     "contestation — hypotheses non fingo (1713) leaving attraction "
     "without a mechanism, the Leibniz-Clarke exchange, Mach's 1883 "
     "re-reading — a formalism accepted while its meaning was fought "
     "over, which is dissociation as the point writes it; the stricter "
     "reading the coder applied requires profundity to arrive as "
     "interpretation of inherited mathematics, which Newton's was not. "
     "The quantum on derivation-first: the two-births problem in its "
     "pure form — 1900's interpolation to weeks-old measurements "
     "against 1925's rebuild from Balmer (1885) and Ritz (1908) — the "
     "h-counterexample the audit's second alarm already owns, resurfacing "
     "inside a blind reading that had never heard of it. Both breaks "
     "resolve under amendments that already exist, both dissents print "
     "with their evidence, and neither cell moves; what the breaks "
     "measure is the instrument's elasticity, now quantified — two "
     "elastic cells in one hundred thirty-five living-side readings "
     "across three runs."),

    ("The last number before the court convenes is the cluster structure, "
     "and it cuts both ways at once. The three fresh-context runs agree "
     "with each other tightly — A versus B at 94.4 percent, the third "
     "reading against each at 90.7 — far more tightly than any of them "
     "agrees with the author's original census: 70.4, 70.4, and 77.8. "
     "The outlier across all five readings of the dead side was never "
     "the lineage; it was the author's generous cells, and blinding "
     "dominates authorship within this family — a partial mitigation of "
     "the genetic sting. But the cluster is also the confirmation: "
     "three runs of one school reading thrice, converging on the same "
     "amended cells, means the amendments are the school's, and the "
     "school is what the alien clause exists to escape. Twelve of "
     "twenty-seven dead cells now carry five-way agreement — the "
     "load-bearing wall, unmoved through three blind readings and one "
     "author's revision; the fifteen that do not are the court's "
     "docket, and the docket is where the panel's newest members make "
     "their mark."),
]

TABLE4_HEADER = ["Comparison", "Cells", "Weighted", "Exact / Adj / Dist"]

TABLE4_ROWS = [
    ("Third reading vs census v1 (dead side)", "27", "77.8%",
     "17 / 8 / 2"),
    ("Third reading vs amended census (dead side)", "27", "87.0%",
     "20 / 7 / 0"),
    ("Third reading vs A4b coder A", "54", "90.7%", "44 / 10 / 0"),
    ("Third reading vs A4b coder B", "54", "90.7%", "44 / 10 / 0"),
    ("Third reading vs pre-registration (new pair)", "18", "80.6%",
     "13 / 3 / 2"),
    ("Third reading vs Vol I's living profile", "27", "92.6%", "25 / 2 / 0"),
    ("A4b: coder A vs coder B (for scale)", "54", "94.4%", "48 / 6 / 0"),
]

TABLE4_CAPTION = ("Table 4 — The unblinding, all readings: the third blind "
                  "run agrees with the amended census at 87.0 percent and "
                  "with the original at 77.8 — the amendments replicate "
                  "blind. The new pair's two distants both sit at germ "
                  "theory's physics-shaped points.")

TABLE5_HEADER = ["Signature point", "vs census v1", "vs A4b A+B",
                 "The disagreement's character"]

TABLE5_ROWS = [
    ("Deletion at birth", "100.0%", "91.7%",
     "The ether's F/P: as-written severity against the core-posit "
     "refinement."),
    ("Unification", "66.7%", "95.8%",
     "The dead's leg demotes: a posited substance is vocabulary, not "
     "law."),
    ("Universal constant", "100.0%", "95.8%",
     "The sharpest row in every run — and the one that does not travel "
     "out of physics."),
    ("Derivation-first", "83.3%", "87.5%",
     "The two-births problem, now named and stipulated."),
    ("Conservative embedding", "66.7%", "87.5%",
     "The direction-split, applied unprompted to miasma and germ."),
    ("Formalism / meaning", "83.3%", "83.3%",
     "Presence versus profundity — the coder's flag, adopted."),
    ("Founders' resistance", "16.7%", "83.3%",
     "The floor again, and stricter: neither defense nor compromise "
     "priced as full payment."),
    ("Generative slope", "100.0%", "91.7%",
     "All four dead traditions generative-then-degenerating; no living "
     "theory."),
    ("Crisis-chaining", "83.3%", "100.0%",
     "The ether's opened drift problem, satisfied a third time."),
]

TABLE5_CAPTION = ("Table 5 — Per-point weighted agreement: dead side "
                  "against the census (three cells) and the full panel "
                  "against the two A4b coders (twelve comparisons). The "
                  "high band is the discriminating core, reproducing "
                  "across runs; the floor is one point, inverted three "
                  "ways now.")

FIG1_CAPTION = ("Figure 1 — The widened census design: the instrument "
                "handed verbatim through the envelope to a third fresh "
                "context (the alien slot, unfilled — the family is the "
                "author's own, the refusal printed); the panel widened "
                "by the census's own extension rule; the unblinding "
                "finding the amendments replicated blind; the court "
                "convening under pre-registered rules; the verdict "
                "marking the constant's domain and shipping the "
                "replication kit.")

# ---------------------------------------------------------------------------
# Chapter 5 — The Adjudication
# ---------------------------------------------------------------------------

CH5_S1 = [
    ("The court reconvenes under the same rule A4b fixed before its own "
     "unblinding, and this run inherited both clauses unamended: evidence "
     "over authorship, with every contested cell tried against named "
     "historical fact; and the motion rule — where independent readings "
     "agree against the author's cell, the cell moves. The pre-"
     "registration added a third constraint this time, written before "
     "any coder ran: the expected fault lines and their permitted "
     "resolutions were locked to file, so that no ruling below can have "
     "been invented after seeing the numbers it rules on. The docket has "
     "three parts — the new pair's cells, the living side's two breaks, "
     "and the dead-side movements — and Table 6 is its ledger. The new "
     "pair is tried first, because the extension is this document's "
     "reason to exist."),

    ("Miasma, tried first. Deletion at birth: failed, and the ruling "
     "adopts the stipulation the coder's seventh note exposes as "
     "missing — for multi-century doctrines the census codes the "
     "consolidated form that held the field, which is the nineteenth-"
     "century sanitary miasma, and that form deleted nothing; the "
     "Hippocratic birth's deletion of divine etiology belongs to a "
     "different christening two millennia upstream. The coder's partial "
     "is recorded as the correct answer to the question the instrument "
     "left open — the same service A4b's coders performed on the "
     "embedding point. Conservative embedding: failed, and the "
     "pre-registration's partial moves against itself — the court's own "
     "rule executed on the author's cell. The evidence is the coder's "
     "and it is decisive: Koch's comma bacillus (1884) and the "
     "unfiltered-Hamburg against filtered-Altona contrast of 1892 "
     "refuted miasma outright, and the surviving sanitation is craft "
     "re-founded on new reasons, not structure recovered as a limit — "
     "parity with phlogiston's deletion without remainder, not with the "
     "epicycles' Fourier. Crisis-chaining: partial stands — the "
     "environmental question the sanitary program opened, and the "
     "archive it built, remained productive for the successor, which is "
     "the demoted point's pattern among the dead. The profile after the "
     "court: zero clean satisfied cells, all five discriminators "
     "failed. The census-killing clause does not fire, and the oldest "
     "corpse in the history of science is now also the weakest resident "
     "of the control."),

    ("Germ theory, the extension's real test, and the court's rulings "
     "cell by cell. Deletion and unification: satisfied, both readings, "
     "no contest — the double deletion of spontaneous generation and "
     "foul-air etiology; the brewer's vat and the surgical ward made "
     "one (Lister's first antiseptic operation, August 1865, citing "
     "Pasteur). The universal constant: failed, both readings, the same "
     "way — no dimensionful constant exists to install, and the coder's "
     "first note names the ownership rule the court adopts: a constant "
     "is credited to the frame that makes it invariant, not the frame "
     "that measures it, and germ theory's nearest candidates — Koch's "
     "postulates, the one-germ-one-disease specificity — are criteria "
     "and taxonomic principles, not constants of nature. Derivation-"
     "first: revised to partial, split exactly as the ether's was — "
     "real promissory notes honored across a century (the specific "
     "agent for influenza in 1933, poliomyelitis in 1949), a founding "
     "carried by its own new experiments rather than derived from the "
     "existing record. Formalism and meaning: the dual cell, now "
     "doctrine — failed as written, for the theory's decisive surface "
     "was demonstration, not symbolism; satisfied operationalized, for "
     "the causal organism itself was minted: stainable (Gram, 1884), "
     "countable, cultivable (Koch's solid media, 1881; the Petri dish, "
     "1887), with instruments built because the theory demanded them — "
     "the swan-neck flask, the autoclave, the Chamberland filter — and "
     "one coherent discriminating list, the postulates, which could and "
     "did return negative results. Founders' resistance: partial — "
     "Pasteur's surrender of the chemical-catalysis theory of "
     "fermentation he absorbed from his own formation, paid publicly "
     "against Liebig to the elder's death in 1873, is payment; "
     "Koch's tuberculin catastrophe of 1890 is a cost imposed on the "
     "theory, not a coin its maker surrendered. Slope and crisis: "
     "satisfied, no dissent — the century's unordered harvest, and the "
     "etiological wound the theory closed by opening immunology, "
     "virology, and the asymptomatic-carriage problem (Typhoid Mary, "
     "1907) that broke the naive reading of its own postulates."),

    ("The living side's two breaks, tried and sustained as dissents "
     "with the cells unmoved. Newton's formalism cell: the evidence — "
     "attraction left mechanism-less from 1713 to Mach — is dissociation "
     "as the instrument writes it, and the stricter reading the coder "
     "applied (profundity as interpretation of inherited mathematics) "
     "is recorded as the point's genuine second sense; the flag — "
     "presence versus profundity — is adopted into the instrument's "
     "printed ambiguities. The quantum's derivation cell: the 1925 "
     "founding is derivation-first on the record — Heisenberg's "
     "rebuild from Balmer and Ritz — and the 1900 interpolation is the "
     "constant's birth story, already adjudicated by the promotion test "
     "the second amendment installed for exactly this case; the "
     "birth-window stipulation is adopted so the point never has to "
     "choose a birthday again. Neither cell moves; the elasticity "
     "itself is the finding — the instrument bends at named joints, "
     "and the joints are now documented for any future coder."),

    ("The dead-side movements, two cells, both against the author. The "
     "epicycles' founders' cell moves to partial, and the movement is "
     "the third position this point has held across three readings — "
     "the census's satisfied, A4b's refutation to failed, now a partial "
     "on evidence neither prior ruling weighed: Ptolemy's own equant "
     "compromise, uniform circular motion professed at Almagest IX.2 "
     "and violated at IX.5-6, a founder's real cost that Ibn al-Haytham "
     "collected in 1028 and the tradition was still paying when "
     "Copernicus built his epicyclets to restore the principle. "
     "Payment admits degrees — surrender (Newton's action at a "
     "distance, Planck's continuity), compromise (Ptolemy's equant, "
     "Lorentz's detectability), defense (none of it payment) — and "
     "the graduated scale enters the instrument with the coder's "
     "refused-coin test beside it: refusal counts only when the refused "
     "coin is the successor revolution's central concept. Phlogiston's "
     "unification cell moves to partial on the same discipline: a "
     "posited substance is not a dissolved joint, and the law-level "
     "unification of the same phenomena was Lavoisier's, achieved by "
     "deleting phlogiston rather than by positing it — the coder's "
     "evidence, matching A4b's coder B dissent that the sustained "
     "ruling had overruled one-to-one. The confound verdict now rests "
     "on the ether's leg alone, which is where A4b's narrowing already "
     "left it. Two cells move; the author is overruled in both; the "
     "ledger prints the rest."),
]

TABLE6_HEADER = ["Contested cell", "Readings", "The evidence the court weighed",
                 "Ruling"]

TABLE6_ROWS = [
    ("Miasma · deletion", "F / P",
     "The Hippocratic birth deleted divine etiology (On the Sacred "
     "Disease); the nineteenth-century form deleted nothing — Snow's "
     "evidence met with restatements.",
     "F stands; birth-window stipulation adopted"),
    ("Miasma · embedding", "P / F",
     "Hamburg unfiltered against Altona filtered, 1892 — miasma refuted "
     "outright; sanitation survives as practice, not structure.",
     "Revised to F — the prereg moves against itself"),
    ("Miasma · crisis", "P / F",
     "The environmental question the sanitary program opened, and the "
     "GRO archive it built, armed Snow and Koch — productive for the "
     "successor.",
     "P stands; dissent recorded"),
    ("Germ · derivation", "S / F",
     "Founded by its own new experiments (flasks 1861; anthrax 1876; "
     "the bacillus 1882); promissory notes honored across a century.",
     "Revised to P — the ether's split, applied"),
    ("Germ · formalism", "S / F",
     "No symbolic surface to reinterpret — but the organism minted: "
     "stainable, countable, cultivable; the flask, the filter, the "
     "Petri dish built on demand.",
     "Dual: F as written / S operationalized"),
    ("Germ · constant", "F / F",
     "No dimensionful constant to install; the nearest candidates are "
     "criteria and taxonomy, not constants of nature.",
     "F — the point demotes to domain-marked"),
    ("Newton · formalism", "S / P",
     "Hypotheses non fingo (1713) left attraction contested to Mach "
     "(1883) — meaning fought over a working formalism.",
     "S as written; presence/profundity flag adopted"),
    ("Quantum · derivation", "S / P",
     "1925 rebuilt mechanics from Balmer (1885) and Ritz (1908); 1900's "
     "interpolation is the promotion test's own case.",
     "S stands; birth-window stipulation adopted"),
    ("Epicycles · founders", "F / P",
     "Ptolemy's equant: uniformity professed (IX.2), violated (IX.5-6); "
     "the debt collected from Ibn al-Haytham (1028) to Copernicus.",
     "Revised to P — payment graduated"),
    ("Phlogiston · unification", "S / P",
     "A posited substance is not a dissolved joint; the law-level "
     "unification was Lavoisier's, by deletion.",
     "Revised to P — the confound narrows to the ether"),
]

TABLE6_CAPTION = ("Table 6 — The adjudication ledger, third reading: ten "
                  "cells tried, three revised (two against the author's "
                  "own pre-registration), one dual, six sustained — every "
                  "ruling against named evidence, every stipulation "
                  "traceable to a coder's flag.")

# ---------------------------------------------------------------------------
# Chapter 6 — The Verdict: Four Plus One, and the Standing Offer
# ---------------------------------------------------------------------------

CH6_S1 = [
    ("The registration, clause by clause. The census survives the "
     "widened panel: no dead theory — three physics corpses and now "
     "the oldest framework in the history of science — passes any of "
     "the five discriminators under any reading run to date, and the "
     "ether's lone as-written satisfied is the confound the audit "
     "already adjudicated. The living side admits its first non-physics "
     "resident, and the admission prices the extension's one "
     "amendment. Germ theory — ratified by the world, generative "
     "without degeneration, the unifier of the brewery vat and the "
     "surgical ward — fails the universal constant under every "
     "reading, including the pre-registered one that expected the "
     "failure and the blind one that refused to inflate the point to "
     "save it. The pre-registered resolution executes as written: the "
     "constant demotes to a domain-marked discriminator. Within "
     "quantitative physics it discriminates six for six across the "
     "census's pairs — the sharpest row in every run, one hundred "
     "percent agreement across five readings — and outside physics it "
     "abstains: it does not call germ theory shallow, it declines to "
     "speak. The alternative — restating the point as any invariant "
     "anchor of any kind — was named and rejected in advance as the "
     "first alarm's scam, an inflation fitted to the case; the "
     "anti-epicycle rule held, and the demotion is the demotion the "
     "rule permits."),

    ("The amended signature, stated whole. Four domain-general "
     "discriminators: deletion at birth, now with the core-posit and "
     "birth-window refinements; successor-recovery embedding, the "
     "direction that discriminates; generative slope, the trend; minted "
     "measurables, operationalized — the form that travels, and the "
     "one germ theory passes at full strength. One domain-marked "
     "discriminator: the universal constant, physics-relative, "
     "sharpest inside its domain and silent outside it. Two restated "
     "points, now double-restated: derivation-first as structure-not-"
     "content with the birth-window stipulation; founders' resistance "
     "as payment-not-defense, now graduated — surrender, compromise, "
     "defense — with the refused-coin test beside it. Two demoted: "
     "unification, its dead-side leg narrowed to the ether alone; "
     "crisis-chaining, blind-confirmed twice. The instrument that "
     "began as nine equal claims is now a marked map — which parts "
     "are physics, which are general, which are conditions rather "
     "than tests — and Table 7 prints it against the widened panel. "
     "Smaller, harder, and now scoped: what contact with a wider "
     "world does to an instrument fitted in one discipline."),

    ("The alien clause, settled honestly. The order was for a "
     "different model family; the environment supplies one; the "
     "probes are printed; the slot was filled by a third same-family "
     "blind reading, and this document does not claim otherwise. "
     "Genetic dependence is no longer a named confound — it is a "
     "demonstrated availability fact, and the census's honest "
     "sentence about it is that the day of the harder test has not "
     "arrived. What has arrived instead: the third reading's "
     "replication of every amendment blind, at eighty-seven percent "
     "against the amended matrix with zero inversions; the "
     "extension's amendments, pre-registered and adjudicated on "
     "evidence; and the replication kit — the instrument verbatim, "
     "the panel of eight with its scope lines, the scale, the "
     "evidence rule, the weighted scoring scheme, and the "
     "pre-registered adjudication rules, printed here and archived "
     "with this run's complete prompt and output files. Any "
     "genuinely external reader — a human historian, or a model from "
     "another family, run by anyone, anywhere — can execute the "
     "alien reading without the author in the loop, and the series' "
     "pre-registered motion rule binds the author's response in "
     "advance: where the outsider's reading and the blind readings "
     "agree against the census, the census moves. The kit converts "
     "the clause from a purchase the environment cannot make into a "
     "standing offer the world can accept — and under the series' "
     "own logic, the world's participation has always been the only "
     "evidence this corpus acknowledges it lacks. The missing "
     "reader now joins that list, in kit form, ready."),

    ("The limits, at the weight the audit taught. Genetic "
     "dependence: standing, demonstrated, and now carried by three "
     "same-family runs whose mutual tightness — 90.7 to 94.4 "
     "percent — measures the school, not the world; the A4b "
     "coders' runtime model was never logged and is presumed to be "
     "the same lineage, a presumption printed rather than hidden. "
     "The count: four pairs, eight theories, five readings per "
     "dead-side cell — still thin, still fame-confounded, and the "
     "fame residual now doubled, miasma and germ theory being the "
     "most famous pair medicine owns. The adjudicator was again "
     "the author, again mitigated by the pre-registration and the "
     "printed evidence, and again overruled where the readings "
     "agreed — two cells this time, one of them the author's own "
     "pre-registered coding, which is the point of pre-registering. "
     "What this document does not claim is the larger arc, "
     "unchanged from the first census: a coding is not the world; "
     "the signature's domain marks are confessions, not triumphs; "
     "and the world's ratification remains the only evidence this "
     "series acknowledges it lacks. The ledger is open. Continue."),
]

CH6_QUOTE_A4B = (
    "The day a genuinely alien reader recodes this panel is the day "
    "the census faces a harder test than this one.",
    "The Independent Recoding, Chapter 6 — the clause, re-armed: that "
    "day has not arrived; the environment stocks one lineage. The "
    "offer therefore ships as a kit, for the first reader who is not "
    "of this school.",
)

TABLE7_HEADER = ["Signature point", "Phlogiston", "The ether", "Epicycles",
                 "Miasma", "Germ theory (living)"]

TABLE7_RATIOS = [0.21, 0.15, 0.17, 0.15, 0.15, 0.17]

TABLE7_ROWS = [
    ("Deletion at birth",
     "F — renamed Becher's principle; added, deleted nothing",
     "P * — the wave program deleted the corpuscle; its own center "
     "an inherited medium reinstated",
     "F — extended Eudoxus; circularity never touched",
     "F — the consolidated form deleted nothing; the Hippocratic "
     "birth was another theory's christening",
     "S — the double deletion: spontaneous generation and foul-air "
     "etiology"),
    ("Unification",
     "P * — a posited substance is not a dissolved joint",
     "S — one medium under optics and electromagnetism",
     "P * — one toolkit across the planets; vocabulary, not law",
     "P — the zymotic class: administrative, not natural",
     "S — the brewer's vat and the surgical ward, one cause-class"),
    ("Universal constant",
     "F — no quantitative core; weight forced phlogiston negative",
     "F — c belonged to the fields and outlived the medium",
     "F — dozens of parameters, zero invariants",
     "F — nothing constant; fitted coefficients that shifted each "
     "epidemic",
     "F — domain-marked: no constant to install; the point abstains "
     "outside physics"),
    ("Derivation-first",
     "F — each new gas retrofitted, after the fact",
     "P * — real derivational firsts; the defining note dishonored "
     "in 1887",
     "P — parameters from centuries of records: content, never "
     "structure",
     "F — the incumbent; data broke it rather than being derived",
     "P * — promissory notes honored; the founding carried by its "
     "own new experiments"),
    ("Conservative embedding",
     "F — deleted without remainder by oxygen chemistry",
     "S as written * / F on successor-recovery — Fresnel embeds ray "
     "optics; relativity recovers the ether as no limit",
     "P — devices survive as Fourier; the ontology deleted by the "
     "ellipse",
     "F — refuted outright (Hamburg-Altona, 1892); the surviving "
     "sewerage is craft, not structure",
     "P — the practice recovered, the ontology deleted; no limit in "
     "which foul air causes anything"),
    ("Formalism / meaning",
     "F — no formalism; no measurable ever minted",
     "S as written * — discriminates only operationalized (A6)",
     "S as written * — the operationalized form discriminates",
     "F — no symbolic surface; no unit of miasma ever named",
     "F as written / S operationalized — the organism minted: "
     "stainable, countable, cultivable"),
    ("Founders' resistance",
     "F † — Priestley defended, paid nothing: defense is not payment",
     "P * — Lorentz surrendered detectability, kept the medium",
     "P * — Ptolemy's equant: a founder's compromise, collected "
     "for fourteen centuries",
     "F — Chadwick, Nightingale, Pettenkofer's 1892 self-experiment: "
     "refusal at the price of the body itself",
     "P — Pasteur paid Liebig his chemistry; Koch's tuberculin was "
     "a cost imposed, not a coin surrendered"),
    ("Generative slope",
     "S then D — the gas family; then negative weight",
     "S then D — Fresnel to the interferometer; then the "
     "incoherence triangle",
     "S then D — fourteen centuries; then the equant wound",
     "S then D — the sanitary acts and the register; then the "
     "restatements",
     "S — virology, immunology, antibiotics, molecular genetics: "
     "still generating"),
    ("Crisis-chaining",
     "P — opened the air questions that killed it",
     "S as written * — closed the corpuscular crisis, opened the "
     "drift problem; demoted regardless",
     "P — the equant objection opened its execution",
     "P — the environmental question armed its executioner",
     "S — closed the etiological deadlock; opened the host, the "
     "filterable agents, the carrier state"),
]

TABLE7_CAPTION = ("Table 7 — The census matrix after the extension and the "
                  "third reading: four dead theories, the first living "
                  "non-physics resident, and a signature that now says "
                  "where it speaks. Cells marked * revised this run or "
                  "A4b's; † refuted outright. The five-discriminator core "
                  "holds on every column; the constant's column carries "
                  "the domain mark.")

CALLOUT_NUMS = [
    ("4", "matched pairs under the census's rule",
     "miasma admitted; germ theory enters the case base"),
    ("87", "percent: the third reading's agreement with the amended "
     "census",
     "against 77.8 with the original — every amendment replicated blind"),
    ("0", "alien readers the environment supplies",
     "genetic dependence: named, probed, standing"),
]

CALLOUT_CAPTION = ("The widened census's own numbers: the panel doubled "
                   "in span, the amendments replicated blind, and the "
                   "one reader this series still cannot buy.")
