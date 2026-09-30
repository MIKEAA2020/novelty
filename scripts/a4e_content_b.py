# -*- coding: utf-8 -*-
"""Content module for 'The Second Family: Profound Novelty, Amendment A4e'
— part B (Chapters 4-6)."""

# ---------------------------------------------------------------------------
# Chapter 4 — The Unblinding: The Outgroup Test, Re-Run
# ---------------------------------------------------------------------------

CH4_S1 = [
    ("The scoring rules are the locked ones, restated in one sentence "
     "because the record requires it: exact agreement 1.0, one-step "
     "adjacency 0.5, distance 0; the S-then-D compound scored half "
     "against S and P; dual cells scored on their as-written face; "
     "the census moves only where the outsiders and the blind "
     "readings agree against it. Table 4 prints the unblinding, "
     "every pair on file. The family band remains where A4d measured "
     "it, 88.0 to 94.4 percent, mean 90.2 excluding the A-versus-B "
     "scale pair. The two new readings sit against that band at 86.1 "
     "to 87.2 — the returning family at 86.1 to 87.0, the new family "
     "at 86.1 to 87.2 — a lineage offset of three and a half points, "
     "against the 3.3 the first alien posted. The offset replicates. "
     "And its structure replicates: zero inversions anywhere. In "
     "three hundred and eighty-four cross-family cell-comparisons "
     "across the three alien readings, no external family has ever "
     "placed an S where the family places an F, or an F where the "
     "family places an S. The lineage effect is monotone — a "
     "one-step generosity on the dead side, nothing more."),

    ("The aliens against the census itself: 86.7 percent for both "
     "new readings over the full ninety cells, with the dead side at "
     "82.2 and 83.3 and the living side at 91.1 and 90.0. The offset "
     "lives on the dead side, exactly as at A4d, and the per-point "
     "bands of Table 5 locate it with cell-level precision. The "
     "slope row is unanimous — one hundred percent for both families; "
     "the S-then-D compound is the most reliably read code in the "
     "instrument. The floor is the formalism row at 70 and 75 "
     "percent, then the deletion row at 80, then unification and "
     "embedding at 85. And here the census states the structural "
     "finding of this amendment plainly, because two families have "
     "now confirmed what one suggested: the external dissents land "
     "precisely on the cells where the census's own amendments "
     "changed the original instrument's natural reading. The "
     "birth-window on deletion; the ownership rule on the constant "
     "and the formalism rows; the law-versus-vocabulary ladder on "
     "unification; the graduated founder scale on resistance. The "
     "blind readers receive the original wording — the amendments "
     "are the census's rulings, and the rulings are invisible to "
     "them. Cross-family disagreement is therefore not noise, and "
     "not merely lineage: it is the measured footprint of the "
     "instrument's revision history. The census's error bars are its "
     "amendments, printed."),

    ("The killing clauses stay armed, and stay unfired. Under either "
     "new reading, no dead theory posts a satisfied cell on any of "
     "the five discriminators — deletion, constant, embedding, "
     "measurables, slope: the dead side's deletion row reads partial "
     "at best, the constant row fails outright, the embedding row "
     "carries no S, the minted-measurables row reads partial at "
     "best, and every dead theory's slope is the compound. The "
     "census survives its seventh and eighth readings with every "
     "clause unfired. Thermodynamics, the living side's newest "
     "resident, posts its five discriminators under four readings in "
     "the record's own words: deletion S, S, S, S; constant P, P, P, "
     "F; embedding S, S, P, P; measurables S, S, P, S; slope S, S, "
     "S, S — census, fourth blind, and the two aliens. The two "
     "alien P's are the fork Chapter 5 tries: the "
     "results-standard against the ontology-standard on what "
     "'recovered' means. The middle band holds its middle under "
     "every reading."),
]

TABLE4_HEADER = ["Comparison", "Cells", "Weighted", "Exact / Adj / Dist"]

TABLE4_ROWS = [
    ("FAMILY BAND — X3 vs coder A", "54", "90.7%", "44 / 10 / 0"),
    ("FAMILY BAND — X3 vs coder B", "54", "90.7%", "44 / 10 / 0"),
    ("FAMILY BAND — B4 vs coder A", "54", "88.0%", "41 / 13 / 0"),
    ("FAMILY BAND — B4 vs coder B", "54", "89.8%", "43 / 11 / 0"),
    ("FAMILY BAND — B4 vs X3", "72", "91.7%", "60 / 12 / 0"),
    ("FAMILY BAND — coder A vs B (for scale)", "54", "94.4%", "48 / 6 / 0"),
    ("ALIEN MUTUAL — gpt-10 vs grok-10", "90", "97.8%", "86 / 4 / 0"),
    ("ALIEN MUTUAL — gpt-10 vs gpt-8 (re-administration)", "72", "100.0%",
     "72 / 0 / 0"),
    ("ALIEN MUTUAL — grok-10 vs gpt-8", "72", "100.0%", "72 / 0 / 0"),
    ("gpt-10 vs B4", "90", "86.1%", "65 / 25 / 0"),
    ("gpt-10 vs X3", "72", "86.1%", "52 / 20 / 0"),
    ("gpt-10 vs coders A / B", "54", "87.0%", "40 / 14 / 0"),
    ("grok-10 vs B4", "90", "87.2%", "67 / 23 / 0"),
    ("grok-10 vs X3", "72", "86.1%", "52 / 20 / 0"),
    ("grok-10 vs coders A / B", "54", "87.0%", "40 / 14 / 0"),
    ("gpt-10 vs census (post-A4d)", "90", "86.7%", "66 / 24 / 0"),
    ("grok-10 vs census (post-A4d)", "90", "86.7%", "66 / 24 / 0"),
    ("gpt-10 vs census — dead side", "45", "82.2%", "29 / 16 / 0"),
    ("grok-10 vs census — dead side", "45", "83.3%", "30 / 15 / 0"),
    ("gpt-10 vs census — living side", "45", "91.1%", "37 / 8 / 0"),
    ("grok-10 vs census — living side", "45", "90.0%", "36 / 9 / 0"),
    ("gpt-10 vs A4d pre-registration (new pair)", "18", "83.3%",
     "12 / 6 / 0"),
    ("grok-10 vs A4d pre-registration (new pair)", "18", "83.3%",
     "12 / 6 / 0"),
]

TABLE4_CAPTION = ("Table 4 — The unblinding, every pair on file. The two "
                  "external families agree with each other above the "
                  "family's own band; each sits three and a half points "
                  "below it; nothing anywhere inverts.")

TABLE5_HEADER = ["Signature point", "gpt-10 vs census",
                 "grok-10 vs census"]

TABLE5_ROWS = [
    ("P1 · Deletion at birth", "8.0 / 10 (80.0%)", "8.0 / 10 (80.0%)"),
    ("P2 · Unification", "8.5 / 10 (85.0%)", "8.5 / 10 (85.0%)"),
    ("P3 · Universal constant", "9.5 / 10 (95.0%)", "9.0 / 10 (90.0%)"),
    ("P4 · Derivation-first", "9.0 / 10 (90.0%)", "8.5 / 10 (85.0%)"),
    ("P5 · Conservative embedding", "8.5 / 10 (85.0%)",
     "8.5 / 10 (85.0%)"),
    ("P6 · Formalism / meaning", "7.0 / 10 (70.0%)", "7.5 / 10 (75.0%)"),
    ("P7 · Founders' resistance", "8.5 / 10 (85.0%)", "9.0 / 10 (90.0%)"),
    ("P8 · Generative slope", "10 / 10 (100.0%)", "10 / 10 (100.0%)"),
    ("P9 · Crisis-chaining", "9.0 / 10 (90.0%)", "9.0 / 10 (90.0%)"),
]

TABLE5_CAPTION = ("Table 5 — Per-point weighted agreement against the "
                  "post-A4d census, ten cells per point. The floor is "
                  "the formalism row, then the deletion row — the two "
                  "most amendment-dependent rows in the instrument; "
                  "the slope row is unanimous.")

TABLE6_HEADER = ["Contested cell", "A", "B", "X3", "G8", "B4", "G10",
                 "K10", "Census"]

TABLE6_ROWS = [
    ("Phlogiston · unification", "S", "S", "P", "S", "P", "S", "S",
     "P *"),
    ("Miasma · deletion", "-", "-", "P", "P", "F", "P", "P", "F"),
    ("Germ · founders", "-", "-", "P", "F", "F", "F", "F", "P"),
    ("Newton · formalism", "S", "S", "P", "P", "P", "P", "P",
     "dual S/P"),
    ("Epicycles · formalism", "S", "S", "P", "P", "P", "P", "P", "S"),
    ("Ether · formalism", "S", "S", "S", "P", "P", "P", "P", "S"),
    ("Phlogiston · formalism", "F", "F", "F", "P", "F", "P", "P", "F"),
    ("Ether · constant", "F", "F", "F", "P", "F", "P", "P", "F"),
    ("Ether · crisis", "S", "S", "S", "P", "S", "P", "P", "S *"),
    ("Germ · unification", "-", "-", "S", "P", "S", "P", "P", "S"),
    ("Germ · formalism", "-", "-", "F", "P", "F", "P", "P", "dual F/S"),
    ("Caloric · deletion", "-", "-", "-", "-", "F", "P", "P", "F"),
    ("Caloric · embedding", "-", "-", "-", "-", "P", "F", "F", "P"),
    ("Caloric · founders", "-", "-", "-", "-", "F", "P", "F", "F"),
    ("Thermo · constant", "-", "-", "-", "-", "P", "P", "F", "P"),
    ("Thermo · derivation", "-", "-", "-", "-", "S", "S", "P", "S"),
    ("Thermo · formalism", "-", "-", "-", "-", "S", "P", "S", "S"),
    ("Thermo · founders", "-", "-", "-", "-", "P", "S", "S", "P"),
]

TABLE6_CAPTION = ("Table 6 — The reading records: every cell the two new "
                  "aliens contest against the census, with all seven "
                  "prior readings beside them. The columns are the "
                  "census's whole replication history in one table: "
                  "two A4b coders, the third blind, the first alien, "
                  "the fourth blind, and the two new aliens.")

CH3_QUOTE_GROK = (
    "Boltzmann's k is a real universal constant inside T10's stated "
    "statistical-mechanical scope, but it does not found the 1850-51 "
    "laws the way h founds quantum theory; I therefore coded T10 as "
    "F and T4 as P. The point's restriction to G, c, and h as 'the "
    "three load-bearing constants' is doing a lot of silent work.",
    "The second family's point note on the constant — an alien "
    "reader, blind, locating the exact seam the census's own "
    "amendment history had already caulked: the domain-marked "
    "discriminator, and the J/k dual that fills its middle band.")

# ---------------------------------------------------------------------------
# Chapter 5 — The Adjudication: Three Duals
# ---------------------------------------------------------------------------

CH5_S1 = [
    ("The rules were locked before any of these readings ran, and "
     "nothing in this amendment bends them: evidence over "
     "authorship; the motion rule — where the outsiders' reading and "
     "the blind readings agree against the census, the census moves; "
     "the killing clauses armed. The court's docket this round holds "
     "seventeen cells, and the first structural fact about them is "
     "that they sort cleanly into two kinds. There are "
     "history-forks: cells where the readings divide over a question "
     "of fact about the world — when a deletion happened, whose coin "
     "was tendered, whether a grouping survived. And there are "
     "rule-forks: cells where the readings divide over a question "
     "about the instrument itself — who owns a re-reading, which "
     "face of a composite cell counts. The history-forks are the "
     "court's to settle, and the census's dual device — both faces "
     "printed, neither erased — is how it settles them. The "
     "rule-forks are the census's to own: the amendments are its "
     "rulings, the blind readers never saw them, and a dissent that "
     "measures the distance between the original wording and the "
     "amended one is recorded as exactly that — a cross-family "
     "constant of the instrument, printed in the amendment map, not "
     "a ballot against the ruling."),

    ("Three cells move, and all three move to duals. Phlogiston's "
     "unification: the readings stand five to two for S — both A4b "
     "coders and all three aliens against the census's partial — "
     "and the fork is a real question of fact: the "
     "combustion-calcination grouping WAS real and survived into "
     "oxygen chemistry (the S face, the original wording's own "
     "reading, and the census's own v1 verdict), while the "
     "law-versus-vocabulary amendment's point stands (the P face: a "
     "posited substance is not a dissolved joint). The cell becomes "
     "the fourth dual. Miasma's deletion: the readings stand four "
     "to one for P — the third blind is the family's defector — "
     "and the fork is where the birth-window sits: the Hippocratic "
     "tradition deleted divine etiology two millennia before "
     "Chadwick's consolidated doctrine inherited foul air whole. "
     "The cell becomes a dual: P for the tradition at large, F "
     "within the consolidated doctrine's window. Germ theory's "
     "founders: the readings stand four to one for F — only the "
     "third blind holds with the census — and the fork is the coin "
     "question: Pasteur tendered Liebig his chemistry, publicly, "
     "1857 to 1873 (the P face, the graduation's compromise coin), "
     "against the original wording's demand that the founders' own "
     "central commitments cost them something (the F face: they "
     "defended and won). The cell becomes the fifth dual."),

    ("One cell is confirmed rather than moved, and it deserves the "
     "record's plainest sentence: Newton's formalism dual, the "
     "census's first, is now its best-attested cell. The "
     "interpretation-arrival face carries five readings — the third "
     "blind, the first alien, the fourth blind, and both new aliens "
     "— against two for the as-written face, the two A4b coders. "
     "No motion is needed; the dual was already the census's "
     "answer, and five readings have now paid it the compliment of "
     "arriving at it independently from outside."),

    ("The defenses are printed with their forks, and the forks are "
     "now measured cross-family constants. The ether's constant "
     "stays failed: the ownership rule is the census's own "
     "convention — credit the frame that installs the invariant "
     "role, not the program that produced the measurement — and "
     "three external administrations read the other convention; "
     "the fork is the finding, and it is stable. The formalism row "
     "stays as written for the epicycles and the ether, on the "
     "exemplar defense: the instrument's own canonical example — "
     "Lorentz held the equations before Einstein's reading — is "
     "source-held formalism, and the aliens' reader-ownership rule "
     "would fail the exemplar itself; the census keeps the "
     "source-credit reading and prints the fork, now the widest "
     "on the map. Phlogiston's formalism stays failed on the "
     "operationalized face: the aliens' partial is the rival-owned "
     "meaning-split of Priestley's gas, which the minted-measurables "
     "amendment already prices. The ether's crisis cell stays "
     "satisfied-as-written and demoted: the wave program closed the "
     "corpuscular crisis and opened the drift problem inside its "
     "own run; the aliens read the successor-owned chain, and the "
     "elasticity is recorded. Germ theory's unification stays "
     "satisfied, and the defense is the aliens' own criterion: "
     "both families credit phlogiston's grouping because the "
     "grouping survived, and both deny germ theory's — whose "
     "cause-class also survived, by the same test they themselves "
     "state. Germ theory's formalism dual is confirmed as a span: "
     "both aliens land at partial, inside the declared "
     "F-to-operationalized-S interval, filling its middle from "
     "outside. Caloric's deletion stays failed on the pre-fixed "
     "birth-window answer — the Traite's deletions were the oxygen "
     "pair's christening, and the panel prices them there; the "
     "expected dissent is printed at full weight, twice. Caloric's "
     "embedding stays partial: the aliens read the strict downward "
     "face — did caloric recover its own predecessors — and code "
     "failed, correctly, under that reading; the census's partial "
     "is the machinery-survival composite, Fourier verbatim and "
     "Carnot standing today, and both faces now print. Caloric's "
     "founders stays failed, the external verdict split: a "
     "posthumously discovered conversion is neither tendered nor "
     "costly. Thermodynamics' constant stays partial, bracketed — "
     "one family reads the J/k dual, the other the strict failure, "
     "and the census cell sits exactly between them, which is what "
     "a middle band means. Thermodynamics' derivation stays "
     "satisfied — the aliens split, and the two-roads stipulation "
     "carries: Mayer from the old gas data, Helmholtz from "
     "physiology and electromagnetism, Joule from the paddle "
     "wheel; the simultaneous-discovery record is the "
     "over-determination itself. Thermodynamics' formalism stays "
     "satisfied — the split lands on the depth question, and the "
     "S face (Clausius re-reading Clapeyron's cycle, Boltzmann "
     "re-reading Clausius's entropy) carries. And thermodynamics' "
     "founders stays partial, the E2 answer pre-fixed before the "
     "fourth reading ran: Kelvin's coin was tendered and paid — "
     "formed in Regnault's caloric laboratory, publicly resistant "
     "to Joule, publicly surrendering in 1851, his own scale's "
     "foundation rebuilt at the cost — and the depth remains the "
     "contestable half, four years of published formation against "
     "Newton's lifelong mechanical philosophy; both aliens read "
     "the S face, the pre-registration printed that dissent in "
     "advance, and the P stands with the fork recorded."),
]

TABLE7_HEADER = ["Contested cell", "Readings (census vs 7)",
                 "The evidence the court weighed", "Ruling"]

TABLE7_ROWS = [
    ("Phlogiston · unification", "P / S,S,P,S,P,S,S",
     "The combustion-calcination grouping survived into oxygen "
     "chemistry; the amendment's law-versus-vocabulary ladder "
     "prices it partial — both faces real, both read.",
     "Revised to dual: S as originally worded / P under the "
     "law-vs-vocabulary amendment — the motion rule fired"),
    ("Miasma · deletion", "F / P,P,F,P,P",
     "The Hippocratic tradition deleted divine etiology; the "
     "consolidated 1842 doctrine inherited foul air whole — the "
     "birth-window's placement is the whole dispute.",
     "Revised to dual: P for the tradition at large / F within "
     "the birth-window — the motion rule fired"),
    ("Germ · founders", "P / P,F,F,F,F",
     "Pasteur tendered Liebig his chemistry, publicly, 1857-73; "
     "the founders' central commitments cost them nothing — both "
     "faces documented, both priced.",
     "Revised to dual: F as originally worded / P under the "
     "graduation — the motion rule fired"),
    ("Newton · formalism", "dual / S,S,P,P,P,P,P",
     "The inverse-square formalism common currency before 1684; "
     "the interpretation fought over from 1713 to Mach.",
     "Confirmed: the arrival face now carries five readings — "
     "the census's best-attested cell"),
    ("Ether · constant", "F / F,F,F,P,F,P,P",
     "Maxwell's c-ratio measured inside the program; the "
     "invariant speed installed by 1905 — the ownership rule, "
     "dissenting three times from outside.",
     "F stands; the ownership fork recorded as a cross-family "
     "constant"),
    ("Epicycles + ether · formalism", "S / S,S,P(S),P,P,P,P",
     "The instrument's own exemplar — Lorentz held the equations "
     "before Einstein — is source-held formalism; the aliens' "
     "reader-ownership rule would fail the exemplar itself.",
     "S as written stands; the reader-ownership fork recorded "
     "— the map's widest"),
    ("Phlogiston · formalism", "F / F,F,F,P,F,P,P",
     "The aliens' partial is the rival-owned meaning-split of "
     "Priestley's gas; the minted-measurables amendment prices "
     "the operationalized face.",
     "F stands on the operationalized face; the fork recorded"),
    ("Ether · crisis", "S / S,S,S,P,S,P,P",
     "The wave program closed the corpuscular crisis and opened "
     "the drift problem inside its own run; the aliens read the "
     "successor-owned chain.",
     "S as written stands, demoted as before; elasticity "
     "recorded"),
    ("Germ · unification", "S / S,P,S,P,P",
     "Both families credit phlogiston's grouping because it "
     "survived — and deny germ theory's, whose cause-class also "
     "survived, by the same stated test.",
     "S stands on the aliens' own criterion; the asymmetry "
     "printed"),
    ("Germ · formalism", "dual / F,P,F,P,P",
     "Both aliens land at partial — inside the declared "
     "F-to-operationalized-S span, not outside it.",
     "Dual confirmed as a span; the external P its midpoint"),
    ("Caloric · deletion", "F / F,P,P",
     "The Traite's deletions were the oxygen pair's christening; "
     "the panel prices them there — E1's pre-fixed answer, the "
     "dissent expected and printed.",
     "F stands; the expected dissent printed at full weight"),
    ("Caloric · embedding", "P / P,F,F",
     "Carnot's theorem and Fourier's equation survive verbatim; "
     "caloric recovered no predecessor of its own — the two "
     "faces of one composite cell.",
     "P stands; both faces printed; the two-faces fork recorded"),
    ("Caloric · founders", "F / F,P,F",
     "Carnot's private notes surrendered conservation by 1832; "
     "published 1878, after his death — never tendered, never "
     "costly.",
     "F stands; the split external verdict printed"),
    ("Thermo · constant", "P / P,P,P,F",
     "J the unit bridge, demoted to a definition; k minted by the "
     "consolidation — one family reads the dual, the other the "
     "strict failure.",
     "P stands — bracketed from both sides: the middle band "
     "confirmed as a middle"),
    ("Thermo · derivation", "S / S,S,P",
     "Mayer 1842 from gas data in print; Helmholtz 1847; Joule "
     "1843-49 — the simultaneous-discovery record is the "
     "over-determination.",
     "S stands; the two-roads stipulation carries; the split "
     "printed"),
    ("Thermo · formalism", "S / S,P,S",
     "Clapeyron's cycle re-read by Clausius without conservation; "
     "Boltzmann's probabilistic meaning on Clausius's entropy.",
     "S stands; the depth fork recorded"),
    ("Thermo · founders", "P / P,S,S",
     "Kelvin formed in caloric physics, publicly surrendered "
     "1849-51, rebuilt his own scale's foundation — the coin "
     "tendered and paid; the depth the contestable half.",
     "P stands under E2's pre-fixed graduation; the S-reading "
     "printed at full weight"),
]

TABLE7_CAPTION = ("Table 7 — The adjudication ledger: seventeen cells "
                  "tried, three revised to duals, one confirmed, "
                  "thirteen defended with their forks recorded — every "
                  "revision by the pre-registered motion rule, no "
                  "revision against it.")

# ---------------------------------------------------------------------------
# Chapter 6 — The Verdict: The Census After Eight Readings
# ---------------------------------------------------------------------------

CH6_S1 = [
    ("Table 8 prints the census as it stands after eight readings. "
     "The dead side carries five theories and five duals' worth of "
     "printed faces: phlogiston's unification and miasma's deletion "
     "join the record this round; the ether's embedding keeps its "
     "direction-split composite; the slope row remains the compound "
     "every reading has ratified. The instrument's amendment map — "
     "the census's own error bars — now lists four domain-general "
     "discriminators and one domain-marked, five duals, and six "
     "named forks: ownership on the constant, reader-ownership on "
     "formalism, the birth-window on deletion, law-versus-"
     "vocabulary on unification, the graduation on resistance, and "
     "the two-faces split on embedding. Every fork is measured — "
     "each carries its reading record, and each record now "
     "includes at least two external administrations. The census "
     "has stopped pretending its instrument is seamless; it prints "
     "the seams and their widths."),

    ("The living side, Table 9, changes by one annotation: germ "
     "theory's founders' cell becomes the record's fifth dual, "
     "and thermodynamics' middle band gains its bracket. Nothing "
     "else moves, and the stillness is the finding: after three "
     "external readings — two families, three administrations, "
     "ninety cells each — the living side's satisfied cells stand "
     "where Volume I wrote them, with Newton's formalism dual the "
     "single, best-attested exception, and the two "
     "second-residents' partials (germ theory's constant, "
     "thermodynamics' constant and founders) exactly where the "
     "domain-marked and graduated amendments put them before any "
     "alien read a word."),

    ("What eight readings did to the genetic-dependence limit is "
     "now on the record in full. Amendment A4b confessed it; A4c "
     "ordered the alien reading and the infrastructure refused; "
     "A4d accepted the first delivery and measured the offset at "
     "3.3 points; this amendment receives two more deliveries — "
     "one from the returning family, one from a family never met — "
     "and finds them identical to the first on every shared cell. "
     "The limit dies as a threat not because the census won an "
     "argument but because the argument stopped being available: "
     "the verdicts are over-determined by readers this environment "
     "cannot select, cannot see, and cannot instruct. What remains "
     "of lineage is a calibration offset of three and a half "
     "points, monotone, zero inversions in three hundred and "
     "eighty-four cross-family comparisons, mapped cell for cell "
     "onto the instrument's own declared elastic cells. The "
     "census's error bars are its amendments, printed; its "
     "replication record is its defense, filed."),

    ("The standing offer remains standing, and it travels with "
     "this record. The kit is unchanged at ten theories — the "
     "verbatim prompt, the panel, the scale, the evidence rule, "
     "the forbidden list — and any third family, any human "
     "historian, any reader of any lineage can execute it; the "
     "convergence record printed here is the prior they will be "
     "measured against, and the brackets on the fifth pair are "
     "the cells their reading will fill. The census does not "
     "ask to be believed. It asks to be run — again, by anyone, "
     "under rules locked in advance — and prints what returns. "
     "The ledger is open."),
]

TABLE8_HEADER = ["Signature point", "Phlogiston", "The ether", "Epicycles",
                 "Miasma", "Caloric"]

TABLE8_RATIOS = [0.20, 0.16, 0.16, 0.16, 0.16, 0.16]

TABLE8_ROWS = [
    ("Deletion at birth",
     "F — Becher's principle renamed; nothing deleted",
     "P * — the wave program deleted the corpuscle; its own center "
     "an inherited medium reinstated",
     "F — extended Eudoxus; circularity never touched",
     "F within the birth-window / P for the tradition at large — "
     "the Hippocratic deletion, dual (revised this run)",
     "F — the fire-principle renamed and quantified; the Traite's "
     "deletions were the oxygen pair's christening"),
    ("Unification",
     "S as originally worded — the grouping survived into oxygen "
     "chemistry / P under the law-vs-vocabulary amendment — a "
     "posited substance is not a dissolved joint, dual (revised "
     "this run)",
     "S — one medium under optics and electromagnetism",
     "P * — one toolkit across the planets; vocabulary, not law",
     "P — the zymotic class: administrative, not natural",
     "P — one substance's bookkeeping; the substance-versus-motion "
     "division begged"),
    ("Universal constant",
     "F — no quantitative core; weight forced phlogiston negative",
     "F — c belonged to the fields and outlived the medium (the "
     "ownership fork: three external dissents, recorded)",
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
     "P — the machinery survives verbatim (Fourier, Carnot); no "
     "predecessor recovered (the two-faces fork, recorded)"),
    ("Formalism / meaning",
     "F — no formalism; no measurable ever minted (the operationalized "
     "face; the aliens' as-written partial recorded)",
     "S as written * — discriminates only operationalized (A6); "
     "the reader-ownership fork recorded",
     "S as written * — the operationalized form discriminates; the "
     "reader-ownership fork recorded",
     "F — no symbolic surface; no unit of miasma ever named",
     "P — minted (Black's latent heat, the calorie, the "
     "calorimeter); the killing coin was the successor's"),
    ("Founders' resistance",
     "F — Priestley defended, paid nothing: defense is not payment",
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
     "F — it faded; the archive was apparatus, not doctrine",
     "P — the motive-power question, opened inside the program, "
     "became the successor's foundation"),
]

TABLE8_CAPTION = ("Table 8 — The census matrix after eight readings: "
                  "five dead theories, five duals, six named forks. "
                  "Revisions this run in full text; fork annotations "
                  "carry their reading records in Table 6.")

TABLE9_HEADER = ["Signature point", "Germ theory (living)",
                 "Thermodynamics (living)"]

TABLE9_RATIOS = [0.22, 0.39, 0.39]

TABLE9_ROWS = [
    ("Deletion at birth",
     "S — the double deletion: spontaneous generation and foul-air "
     "etiology",
     "S — the double deletion: the substance of heat and unlimited "
     "convertibility"),
    ("Unification",
     "S — the brewer's vat and the surgical ward, one cause-class",
     "S — heat and work one currency; the firebox and the falling "
     "weight the same phenomenon"),
    ("Universal constant",
     "F — domain-marked: no constant to install; the point "
     "abstains outside physics",
     "P — the J/k dual, now bracketed by two external families: "
     "one reads the dual, the other the strict failure — the "
     "middle band confirmed as a middle"),
    ("Derivation-first",
     "P * — promissory notes honored; the founding carried by its "
     "own new experiments",
     "S — over-determined by three roads (Mayer's derivation, "
     "Helmholtz's synthesis, Joule's measurements)"),
    ("Conservative embedding",
     "P — the practice recovered, the ontology deleted",
     "S — Carnot verbatim, Fourier untouched, the no-work sector "
     "recovered with the reason why (the aliens' ontology-standard "
     "dissent recorded as the fork)"),
    ("Formalism / meaning",
     "F as written / S operationalized — the organism minted: "
     "stainable, countable, cultivable; the external readings fill "
     "the span's middle at P",
     "S — absolute temperature, the joule, entropy minted; the "
     "efficiency bound a discriminating list that returns "
     "negatives"),
    ("Founders' resistance",
     "F as originally worded — the founders defended and won / P "
     "under the graduation — Pasteur's tendered Liebig coin, "
     "1857-73, dual (revised this run)",
     "P — Kelvin's tendered coin: formed in the caloric physics, "
     "publicly surrendered 1849-51, his own scale's foundation "
     "rebuilt (the depth fork recorded)"),
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

TABLE9_CAPTION = ("Table 9 — The living residents after eight readings: "
                  "one new dual on germ theory's founders' row; "
                  "thermodynamics' middle band bracketed; every other "
                  "cell where it stood before any alien read a word.")

CH5_QUOTE_GPT = (
    "Reinterpretation often occurs when a successor takes over a "
    "theory's results; crediting the superseded theory equally "
    "would obscure which program made the change.",
    "The returning family's point note on the formalism row — the "
    "reader-ownership argument, stated by its holder, and the exact "
    "seam the court prices in Table 7.")

CALLOUT_NUMS = [
    ("72", "shared-panel cells on which both external families "
     "return the first alien's verdict exactly",
     "seventy-two cells, zero exceptions, twice — the instrument's "
     "verdicts over-determined by readers this environment cannot "
     "select"),
    ("4", "cells where the two families part company",
     "all inside the fifth pair, all one step, all pre-registered "
     "as contestable before either family ran"),
    ("0", "distant disagreements in eight readings",
     "no external family has ever placed an S where the family "
     "places an F, or an F where the family places an S — the "
     "lineage effect is monotone"),
]
