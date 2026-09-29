# -*- coding: utf-8 -*-
"""Content module for 'The Independent Recoding' — part B: Chapters 3-6."""

# ---------------------------------------------------------------------------
# Chapter 3 — the blind matrices (Tables 2 and 3)
# ---------------------------------------------------------------------------

MATRIX_HEADER = ["Point", "Epicycles", "Ether", "Newton", "Phlogiston",
                 "Quantum", "Relativity"]
MATRIX_RATIOS = [0.22, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

TABLE2_ROWS = [
    ("P1 · Deletion at birth", "F", "P", "S", "F", "S", "S"),
    ("P2 · Unification", "P", "S", "S", "S", "S", "S"),
    ("P3 · Universal constant", "F", "F", "S", "F", "S", "S"),
    ("P4 · Derivation-first", "P", "S", "S", "F", "S", "S"),
    ("P5 · Conservative embedding", "F", "S", "S", "F", "S", "S"),
    ("P6 · Formalism / meaning", "S", "S", "S", "F", "S", "S"),
    ("P7 · Founders' resistance", "F", "P", "S", "F", "S", "S"),
    ("P8 · Generative slope", "P", "S then D", "S", "S then D", "S", "S"),
    ("P9 · Crisis-chaining", "P", "S", "S", "P", "S", "S"),
]

TABLE2_CAPTION = ("Table 2 — Coder A's blind coding of the panel: "
                  "fifty-four cells, each returned with a one-sentence "
                  "evidence line citing a named historical fact. The "
                  "living side reads satisfied without exception; no "
                  "cell carries the census's authority.")

TABLE3_ROWS = [
    ("P1 · Deletion at birth", "F", "P", "S", "F", "S", "S"),
    ("P2 · Unification", "P", "S", "S", "P", "S", "S"),
    ("P3 · Universal constant", "F", "P", "S", "F", "S", "S"),
    ("P4 · Derivation-first", "P", "P", "S", "F", "S", "S"),
    ("P5 · Conservative embedding", "P", "S", "S", "F", "S", "S"),
    ("P6 · Formalism / meaning", "S", "S", "S", "F", "S", "S"),
    ("P7 · Founders' resistance", "F", "P", "S", "F", "S", "S"),
    ("P8 · Generative slope", "S then D", "S", "S", "S then D", "S", "S"),
    ("P9 · Crisis-chaining", "P", "S", "S", "P", "S", "S"),
]

TABLE3_CAPTION = ("Table 3 — Coder B's blind coding of the same panel: "
                  "the same reading, made independently — one hundred "
                  "eight cells across the two matrices, zero outright "
                  "contradictions between them.")

# ---------------------------------------------------------------------------
# Chapter 4 — The Unblinding
# ---------------------------------------------------------------------------

CH4_S1 = [
    ("The comparison method is the pre-registered one, restated in one "
     "paragraph so the tables can be read without a key. The census's "
     "matrix holds twenty-seven control cells — three dead theories "
     "by nine points; the blind codings hold those twenty-seven plus "
     "the living twenty-seven for context. The census's one "
     "non-standard entry (the epicycles' <i>confounded</i> on "
     "derivation-first) is read as <i>partial</i>, which is what the "
     "census's own prose means by it. Weighted agreement scores exact "
     "cells at one, category-adjacent cells at one-half, and outright "
     "inversions at zero; the compound slope code is scored with its "
     "degeneration flag as the load-bearing half — a plain "
     "satisfied against a generative-then-degenerating counts as "
     "adjacent, because the coder missed the trend, and the trend is "
     "the point. Under this scheme a coding that reproduced the census "
     "perfectly would score 100 percent; a coding that flipped every "
     "cell would score zero; a coding that merely trembled at category "
     "boundaries would collect its halves and land somewhere in "
     "between, which is where the honest instruments live."),

    ("The headline numbers follow. Living side: perfect — both "
     "coders reproduce Volume I's matrix unprompted, twenty-seven "
     "satisfied cells each; whatever else the recoding finds, the "
     "doctrine's positive content is stable under fresh reading. Dead "
     "side: weighted agreement 70.4 percent per coder — coder A at "
     "fifteen exact cells and four outright inversions, coder B at "
     "fourteen and three — a level that would flatter no clinical "
     "instrument, and whose structure matters more than its level. "
     "Between the blind readers: 94.4 percent weighted across the full "
     "fifty-four-cell panel with zero outright contradictions; "
     "restricted to the census's twenty-seven control cells, 88.9 "
     "percent with the same zero. Three cells — no more — saw "
     "both coders contradict the census outright: the ether on "
     "conservative embedding, and phlogiston and the epicycles each on "
     "founders' resistance. Everything else the census disputes with "
     "one coder at a time; these three it disputes with both, and they "
     "form the adjudication's mandatory docket. Twelve cells — "
     "fewer than half — carry three-way exact agreement, and the "
     "fifteen that do not are where this document earns its keep."),

    ("Read per point, the agreement sorts into three bands, and the "
     "sorting is the finding (Table 4). The high band is the census's "
     "discriminating core holding under fresh reading: the constant at "
     "91.7 percent — the sharpest agreement in the corpus — "
     "with deletion, slope, and crisis-chaining each at 83.3. The "
     "middle band is where strictness differs a category at a time: "
     "unification and derivation-first at 75.0, formalism and meaning at "
     "66.7, embedding at 58.3. The floor is one point: founders' "
     "resistance, at 16.7 percent — not noise but inversion, both "
     "coders reading the point strictly where the census read it "
     "generously, and agreeing with each other while doing so. Where "
     "the disagreement sits is as informative as its level: it "
     "concentrates in the rows the census itself had already demoted, "
     "dual-annotated, or operationalized — the instrument's "
     "declared soft tissue — with one exception that exceeds "
     "every expectation the author held. The founders' point, demoted "
     "as confounded, did not merely wobble under fresh reading; it "
     "inverted, and the inversion means the census's evidence for its "
     "own demotion was the author's generous coding of the dead — "
     "a finding resolved in Chapter 5."),

    ("Figure 1 draws the design that produced these numbers: the "
     "instrument handed verbatim through a blinding envelope to two "
     "fresh contexts, the returned matrices unblinded against the "
     "census, and every contested cell taken to evidence before any "
     "verdict was allowed to move. The design's one asymmetry is "
     "inherited from the census's own confession and is restated here "
     "at full weight: the process that authored the signature also "
     "commissioned the coders, ran the comparison, and will run the "
     "adjudication — the fox is judging the henhouse, and only the "
     "printed evidence, checkable by any reader, stands between the "
     "fox and the hens. That is not a comfortable fact, and Chapter 5 "
     "handles it the only way this series knows: by making the "
     "evidence, not the author, the court, and by moving the census's "
     "own cells wherever both fresh readers agreed against it — "
     "a rule fixed before the unblinding, and kept."),
]

TABLE4_HEADER = ["Signature point", "Agreement", "The disagreement's character"]

TABLE4_ROWS = [
    ("Deletion at birth", "83.3%",
     "The ether's partial: the wave program deleted the corpuscle while "
     "reinstating a medium as its own center."),
    ("Unification", "75.0%",
     "The epicycles demoted a category: one toolkit across planets is "
     "vocabulary, not law."),
    ("Universal constant", "91.7%",
     "The sharpest agreement in the corpus; one coder's partial on the "
     "ether concedes c to the fields in its own evidence."),
    ("Derivation-first", "75.0%",
     "The ether's real derivational firsts weighed against its "
     "dishonored defining note."),
    ("Conservative embedding", "58.3%",
     "The direction-split: two defensible readings of the point, two "
     "verdicts — exposed and split in Chapter 5."),
    ("Formalism / meaning", "66.7%",
     "Satisfied by the dead as written, both coders — the confound "
     "the census's prose had already confessed."),
    ("Founders' resistance", "16.7%",
     "Near-total inversion: defense is not payment; the coders read the "
     "point strictly, the census generously."),
    ("Generative slope", "83.3%",
     "The trend reproduced; the degeneration flag missed once on the "
     "ether."),
    ("Crisis-chaining", "83.3%",
     "The ether's opened crisis read as satisfied as written; the "
     "census had withheld credit on a consideration the instrument "
     "does not contain."),
]

TABLE4_CAPTION = ("Table 4 — Per-point weighted agreement between the "
                  "census and the two blind codings (six comparisons per "
                  "point: three dead theories by two coders). The high "
                  "band is the discriminating core; the floor is one "
                  "point, inverted.")

FIG1_CAPTION = ("Figure 1 — The recoding design: one instrument, verbatim; "
                "two fresh contexts inside the blinding envelope; the "
                "unblinding finds three double inversions; the evidence "
                "court rules on ten cells; the census survives amended.")

# ---------------------------------------------------------------------------
# Chapter 5 — The Adjudication
# ---------------------------------------------------------------------------

CH5_S1 = [
    ("The court convenes under one rule, stated first: evidence over "
     "authorship. Each contested cell is tried against the named "
     "historical record, and the ruling follows the evidence without "
     "regard to which side filed the claim. The structural conflict "
     "stated in Chapter 4 is handled procedurally, and the handling is "
     "the chapter's first exhibit: in every cell where both blind "
     "coders contradicted the census, the census's cell moves — "
     "the author overruled himself where the fresh readers agreed "
     "against him, and the two cells that die in this chapter die by "
     "that rule, not by the author's mercy. Where the evidence sustains "
     "the census against one coder's dissent, that is printed with the "
     "dissent attached, because a dissent that is hidden is a dissent "
     "that was never really tried. Ten cells are contested; Table 5 is "
     "the ledger; the paragraphs below are the rulings, in the order "
     "the docket demands: the refutations first, the direction-split "
     "second, the revisions after, the sustained dissents last."),

    ("The founders' point produces both refutations, and the court's "
     "reading of the two cells is the coders' reading, because the "
     "coders read the instrument correctly and the census did not. The "
     "point, as Volume I wrote it, prices payment: the founders "
     "surrender commitments they actually held to their own theory's "
     "deepest implications — Newton calling action at a distance "
     "through a vacuum <i>so great an absurdity</i> in the 1693 "
     "Bentley letter while his own Principia had made it the law of "
     "the heavens; Planck calling his quantum an <i>act of "
     "desperation</i> in the 1931 letter to Wood, having spent a decade "
     "trying to buy the continuity back. Against that standard the "
     "census's cells cannot stand. Priestley defended phlogiston to "
     "his death in 1804 — but he surrendered nothing to his own "
     "theory's implications; he paid the theory's enemies his loyalty, "
     "which is the opposite coin, and defense of a vocabulary against "
     "a rival is what founders at every level of the ladder do, "
     "profound or not. The epicycles' cell was weaker still: the census "
     "priced the schools and the Church holding the line — "
     "institutional defense, by non-founders, against a successor "
     "— while no founder of the tradition ever disowned the "
     "equant's own tension with the professed uniformity of circular "
     "motion; the demand for physically real spheres came from "
     "outsiders such as Averroes and al-Bitruji, not from Ptolemy's "
     "line. Both cells flip, satisfied to failed. The ether's cell "
     "lands at partial on the coders' evidence and the court's "
     "agreement: Lorentz paid half — the 1895 to 1904 "
     "constructions stripped the ether of every detectable property, "
     "surrendering the program's central coin of detectability — "
     "and refused the other half, keeping the medium itself to the "
     "end. Payment, not defense: that is the point restored to its own "
     "wording, and its consequence reaches the verdict in Chapter 6."),

    ("The ether's embedding cell is the recoding's deepest finding, "
     "and it is not a refutation but a discovery about the instrument "
     "itself. Both coders code the cell satisfied, with impeccable "
     "evidence: Fresnel's wave theory recovered ray optics — "
     "rectilinear propagation, reflection, Snell's law — as the "
     "short-wavelength limit of wave propagation, made rigorous by "
     "Kirchhoff in 1882; the predecessor's laws recovered as limiting "
     "cases, with the failure points marked at the diffraction edge, "
     "exactly as the instrument reads. The census's <i>failed</i> coded "
     "the other direction entirely: relativity recovered the ether as "
     "no limit of anything — the dead theory's fate, not its "
     "charity. The instrument as written contains both directions and "
     "does not distinguish them, and the census had switched between "
     "them silently, reading the living theories' charity (relativity "
     "embeds Newton; the quantum embeds the classical) and the dead "
     "theories' fate (relativity deletes the ether). Once seen, the "
     "split is structural, and it cuts in a direction the census did "
     "not anticipate: predecessor-embedding is cheap — any wave "
     "theory recovers its geometric limit, which is why a dead medium "
     "and a fourteen-century-dead astronomy both satisfy it — "
     "while successor-recovery is the world's verdict on a theory's "
     "ontology, and it is rare. The amended point reads: <i>is the "
     "theory itself recovered as a limit by what replaces it?</i> "
     "There the ether's failed stands. The coders' satisfied stands "
     "beside it, as the correct answer to the cheaper question the "
     "instrument had accidentally asked. One ambiguity, exposed and "
     "split; the discriminator survives in the direction that "
     "discriminates."),

    ("The ether's other contested cells resolve by the same discipline. "
     "Derivation-first: the census's <i>failed</i> overstated, and the "
     "revised cell reads partial — the program's derivational "
     "firsts were real (Young explaining Newton's rings; the Poisson "
     "spot honored inside Arago's own 1819 jury; Hamilton's conical "
     "refraction found by Lloyd within months of the prediction; "
     "Hertz's 1887 waves honoring Maxwell's 1865), and the census's "
     "own prose already contained the reasoning that saves its "
     "verdict: what the ether derived belonged to the wave and field "
     "mathematics that survived it, while the program's defining "
     "promissory note — the detection of the medium — was "
     "dishonored at Michelson–Morley, exactly as coder B's "
     "evidence sentence states it. Formalism and meaning: the coders "
     "code the ether satisfied as written — Lorentz's "
     "transformations complete by 1904 while the medium's meaning "
     "stayed incoherent — and this is not a refutation but a "
     "confirmation; the census's prose had already called the point "
     "satisfied by the dead theory <i>in its sharpest form</i>, and "
     "its table's cautious partial now moves to the as-written "
     "satisfied the prose confessed. Crisis-chaining: the coders "
     "code the ether satisfied as written — the wave theory "
     "closed the corpuscular crisis and opened the ether-drift "
     "problem, a problem only the medium's demand for a detectable "
     "frame made exist — while the census's partial had "
     "withheld full credit on a consideration the instrument does "
     "not contain, productivity for the successor; the cell moves, "
     "and the point's demotion is confirmed from the blind side. "
     "Deletion at birth: the ether's failed moves to partial — "
     "the wave program deleted the light-corpuscle of the "
     "<i>Opticks</i> while its own center was an inherited medium "
     "reinstated — and the point survives in refined form: the "
     "deletion must strike the theory's core posit, and the core "
     "posit must not itself be an inheritance."),

    ("The epicycles' two revisions complete the docket. Unification "
     "moves from satisfied to partial: the coders read the "
     "instrument's exemplars — the apple and the Moon; space "
     "and time; wave and particle — as law-level unifications, "
     "and decline to certify a shared calculating toolkit across "
     "planets as the same achievement, noting that the tradition's "
     "one construction never touched the deepest division, the "
     "superlunar split. The confound verdict survives on narrower "
     "evidence: the ether's satisfied leg carries it alone at full "
     "strength now. Formalism and meaning moves to satisfied as "
     "written — fourteen centuries of computational practice "
     "with the mechanism deferred, from the Almagest's own "
     "mathematical abstention to Osiander's 1543 preface, is the "
     "point satisfied as Volume I wrote it — with the "
     "operationalized form continuing to do the discriminating. The "
     "remaining differences are five cells where one coder dissents "
     "alone, sustained with the dissents printed in Table 5's notes: "
     "coder B's partial on the ether's constant (c belonged to the "
     "fields, the coder's own evidence concedes), coder B's satisfied "
     "on the ether's slope (the degeneration flag missed), coder A's "
     "failed on the epicycles' embedding and partial on their slope, "
     "coder B's partial on phlogiston's unification. The census holds "
     "these cells; the reader holds the evidence; and the distance "
     "between those two facts is the distance Chapter 6 is built to "
     "close."),
]

TABLE5_HEADER = ["Contested cell", "Census", "A / B", "The evidence the court weighed", "Ruling"]

TABLE5_ROWS = [
    ("Ether · founders",
     "S", "P / P",
     "Lorentz's 1895–1904 constructions stripped the ether of every "
     "detectable property — half payment — while he kept the "
     "medium to the end.",
     "Revised to P — payment, not defense"),
    ("Phlogiston · founders",
     "S", "F / F",
     "Priestley defended phlogiston to his death in 1804: defense of a "
     "vocabulary against a rival, with nothing surrendered to his own "
     "theory's implications.",
     "REFUTED — flipped to F"),
    ("Epicycles · founders",
     "S", "F / F",
     "The schools and the Church held the line — institutional "
     "defense, by non-founders; no founder disowned the equant's own "
     "tension; the sphere-demand came from Averroes and al-Bitruji.",
     "REFUTED — flipped to F"),
    ("Ether · embedding",
     "F", "S / S",
     "Fresnel recovered ray optics as the short-wavelength limit "
     "(Kirchhoff, 1882) — yet relativity recovers the ether as no "
     "limit of anything: two directions, one point.",
     "Split: S as written / F on successor-recovery"),
    ("Ether · derivation",
     "F", "S / P",
     "Real firsts (Poisson spot 1819; conical refraction 1832–33; "
     "Hertz 1887); the defining note — detecting the medium — "
     "dishonored in 1887.",
     "Revised to P — restatement reinforced"),
    ("Ether · formalism",
     "P", "S / S",
     "Transformations complete by 1904 while the medium's meaning "
     "stayed incoherent — the census's own prose confession.",
     "Revised to S as written"),
    ("Ether · crisis",
     "P", "S / S",
     "Closed the corpuscular crisis (Fresnel 1819; Foucault 1850); "
     "opened the ether-drift problem (null, 1887) — a problem only "
     "the medium made exist.",
     "Revised to S as written"),
    ("Ether · deletion",
     "F", "P / P",
     "The wave program deleted the light-corpuscle of the Opticks "
     "while its own center was an inherited medium, reinstated.",
     "Revised to P — core-posit refinement"),
    ("Epicycles · unification",
     "S", "P / P",
     "One toolkit across the planets; the superlunar/sublunar divide "
     "untouched; no law-level unification.",
     "Revised to P — vocabulary, not law"),
    ("Epicycles · formalism",
     "P", "S / S",
     "Fourteen centuries of computational practice with the mechanism "
     "deferred — the Almagest to Osiander's 1543 preface.",
     "Revised to S as written"),
]

TABLE5_CAPTION = ("Table 5 — The adjudication ledger: ten contested "
                  "cells, ten rulings, each against named evidence. Notes: "
                  "five further cells saw single-coder dissents and were "
                  "sustained — the ether's constant (B: P, own "
                  "evidence conceding c to the fields), the ether's slope "
                  "(B: S, degeneration flag missed), the epicycles' "
                  "embedding (A: F, the outlier), the epicycles' slope "
                  "(A: P), phlogiston's unification (B: P).")

# ---------------------------------------------------------------------------
# Chapter 6 — The Verdict: The Coder Survives with a Record
# ---------------------------------------------------------------------------

CH6_S1 = [
    ("The registration, clause by clause. The census-killing clauses "
     "do not fire: no dead theory, as blind-coded and "
     "evidence-adjudicated, satisfies the discriminating core — "
     "the ether, the recoding's hardest case, fails the constant "
     "outright under both coders, fails deletion at its core posit, "
     "fails embedding on the successor-recovery direction, and "
     "satisfies formalism and meaning only in the as-written form the "
     "audit already demoted; phlogiston and the epicycles fail by "
     "wider margins. No discriminator is lost. The coder is not "
     "deleted. The payment is real, and it is itemized: of "
     "twenty-seven cells, seventeen stand as coded, eight are "
     "revised, and two are refuted outright — and both deaths "
     "serve a single verdict change, the founders' point, which the "
     "census had demoted as confounded and which the recoding "
     "restates as payment-not-defense, promoted back into the "
     "instrument in restated form. Under the restated reading the "
     "point separates the living from the dead for the first time: "
     "Newton, Planck, and Einstein paying their own coin; Priestley "
     "and the schools only defending theirs. The recoding did not "
     "confirm the census, and it did not demolish it; it amended it, "
     "in the only direction this series has ever endorsed."),

    ("The amended signature, stated whole. Five discriminators stand "
     "— deletion at birth, now with the core-posit refinement; "
     "the universal constant under its promotion test; conservative "
     "embedding on the successor-recovery direction; generative "
     "slope; minted measurables, operationalized. Two points are "
     "restated — derivation-first as the structure-not-content "
     "rule, now double-confirmed; founders' resistance as "
     "payment-not-defense, the recoding's own contribution. Two "
     "stand demoted — unification, its confound narrowed to the "
     "ether's leg; crisis-chaining, its demotion now blind-confirmed. "
     "One discriminates only in its operationalized form. The "
     "instrument leaves its first independent reading smaller and "
     "harder, which is what the census predicted for its contact "
     "with the dead and what this document now demonstrates for the "
     "census's own contact with fresh readers: Table 6 prints the "
     "amended matrix, and the reader who compares it with the "
     "census's Table 2 will find every change in the soft tissue, "
     "none in the load-bearing wall. The sharpest cells were always "
     "the cheapest to reproduce — the constant, the slope, the "
     "deletion — and the cells that moved were the ones where "
     "the instrument's own wording had left the author room to "
     "choose the answer he needed."),

    ("The consequences for the protocol are three, and they are "
     "written where the next run can read them. First, the "
     "census-agreement clause family — Volume III v1.1's Table "
     "12 — has its first registered entry, and the entry cuts "
     "both ways: the core reproduces, one hundred percent on the "
     "living side and high-band agreement on the discriminating "
     "rows, and the soft tissue required amendment, which is what "
     "the clause exists to catch. Second, the instrument carries "
     "five wording amendments forward, each traceable to a flagged "
     "ambiguity and none invented by the author: predecessor "
     "individuation for the deletion and embedding points; the "
     "law-versus-vocabulary threshold for unification; the "
     "direction-split for embedding; the payment-versus-defense "
     "split for the founders; the successor-frontier test for "
     "crisis-chaining, in coder B's own words. An operator running "
     "the census on a future candidate should run it with the "
     "amended instrument — and where the stakes justify the "
     "cost, with a second coder who has not read the operator's "
     "reasoning. Third, the series' kill log records its second "
     "entry: the first was the protocol auditing itself under its "
     "own alarms; this one is the census audited by its first "
     "independent witness — and both entries end the same "
     "way, with the instrument reduced."),

    ("The limits, at the weight the audit taught. Genetic dependence "
     "stands: the coders are the author's lineage, and their "
     "ninety-four percent mutual agreement is one school reading "
     "twice, not pluralism; the day a genuinely alien reader "
     "recodes this panel is the day the census faces a harder test "
     "than this one. The count stands: two coders, one panel, one "
     "instrument, one adjudicator who was also the author — "
     "the mitigations are procedural and printed, not structural, "
     "and the reader who wants the unfoxed verdict can re-run the "
     "adjudication against the public evidence in Table 5, which is "
     "what the table is for. The fame confound is inherited, named, "
     "standing. What this document does not claim is the arc: it "
     "has tested a coding, not the world, and the world's "
     "ratification remains what it was — the only evidence "
     "this series acknowledges it lacks. Its one line for the "
     "ledger, offered without abbreviation, is the census's own "
     "closing sentence, which the recoding now carries a footnote "
     "the census could not have written in advance:"),
]

CH6_QUOTE_CENSUS = (
    "The points that made the doctrine dramatic are the points that "
    "died in the control, and the points that survived are work.",
    "The Failure Census, Chapter 6 — the sentence the recoding "
    "footnotes: one of the dramatic points died only because its "
    "author priced defense as payment.")

CH6_S2 = [
    ("That sentence was true when written, and the recoding adds what "
     "it could not have known: one of the dramatic points — the "
     "founders' coin, the point that reads best aloud — died in "
     "the control only because its author priced defense as payment; "
     "read strictly, it works for a living, and it has been restored "
     "to the instrument, restated. The other two demotions stand on "
     "blind-confirmed evidence now, which is a better foundation than "
     "the author's word. The signature is smaller, harder, and no "
     "longer only the author's — which is what an instrument "
     "becomes when it survives its first independent witness by "
     "getting smaller. The ledger is open. Continue."),
]

TABLE6_HEADER = ["Signature point", "Phlogiston", "The ether", "Epicycles"]

TABLE6_ROWS = [
    ("Deletion at birth",
     "F — renamed Becher's principle; added, deleted nothing",
     "P * — the wave program deleted the corpuscle; its own center "
     "an inherited medium reinstated",
     "F — extended Eudoxus; circularity never touched"),
    ("Unification",
     "S — combustion, calcination, respiration as one principle",
     "S — one medium under optics and electromagnetism",
     "P * — one toolkit across the planets; vocabulary, not law"),
    ("Universal constant",
     "F — no quantitative core; weight forced phlogiston negative",
     "F — c belonged to the fields and outlived the medium; the "
     "medium's own parameters fitted, then abandoned",
     "F — dozens of parameters, zero invariants"),
    ("Derivation-first",
     "F — each new gas retrofitted, after the fact",
     "P * — real derivational firsts; the defining note — "
     "detecting the medium — dishonored in 1887",
     "P — parameters from centuries of records: content, never "
     "structure"),
    ("Conservative embedding",
     "F — deleted without remainder by oxygen chemistry",
     "S as written * / F on successor-recovery — Fresnel embeds "
     "ray optics; relativity recovers the ether as no limit",
     "P — devices survive as Fourier; the ontology deleted by "
     "the ellipse"),
    ("Formalism / meaning",
     "F — no formalism; no measurable ever minted",
     "S as written * — discriminates only operationalized "
     "(A6): minted measurables, one coherent discriminating list",
     "S as written * — the operationalized form discriminates"),
    ("Founders' resistance",
     "F † — Priestley defended, paid nothing: defense is "
     "not payment",
     "P * — Lorentz surrendered detectability, kept the medium",
     "F † — the schools defended; no founder disowned the "
     "equant"),
    ("Generative slope",
     "S then D — the gas family; then negative weight",
     "S then D — Fresnel to the interferometer; then the "
     "incoherence triangle",
     "S then D — fourteen centuries; then the equant wound"),
    ("Crisis-chaining",
     "P — opened the air questions that killed it",
     "S as written * — closed the corpuscular crisis, opened the "
     "drift problem; demoted as confounded regardless",
     "P — the equant objection opened its execution"),
]

TABLE6_CAPTION = ("Table 6 — The census matrix after the recoding: "
                  "seventeen cells stand as coded, eight are revised "
                  "(*), two are refuted (†) and flipped to the "
                  "coders' reading. The discriminating core holds; the "
                  "instrument is amended in its soft tissue.")

CALLOUT_NUMS = [
    ("17", "cells stand as coded", "the load-bearing wall reproduces"),
    ("8", "cells revised on evidence",
     "four toward the census's own prose confessions"),
    ("2", "cells refuted outright",
     "defense was priced as payment; the coders prevail"),
]

CALLOUT_CAPTION = ("The recoding's ledger: the coder survives with a "
                   "record, and the record is printed in full.")
