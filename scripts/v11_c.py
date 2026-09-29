# -*- coding: utf-8 -*-
"""Content module for 'The L3 Protocol v1.1' — part C: Chapters 6-8 amended.

Backtest: the founding-matrix table is reused verbatim from
protocol_content_c.TABLE4; the census tables are reused verbatim from
census_content_b. The amended and new paragraphs are stated here.
"""

# ---------------------------------------------------------------------------
# Chapter 6 — Backtest: Living and Dead
# ---------------------------------------------------------------------------

CH6_P1 = (
    "A protocol extracted from history owes history a return match, and the "
    "honest form of the match must be stated more severely in this reissue "
    "than in the first, because the audit sharpened the stakes. Running the "
    "gates against Newton, Einstein, and the quantum proves only "
    "consistency — the moves were mined from those very cases — and the "
    "audit added what the first edition implied but did not print: the "
    "gates are retrospective classifiers. G4 as written would have killed "
    "the quantum in December 1900; the separation of inherited from tested "
    "concepts is easy in this century and was impossible in 1904; the "
    "gates do not reproduce the paths to profundity, they compress its "
    "aftermath into a checklist of necessary conditions. That is a real "
    "and useful instrument — but it is a different instrument from the one "
    "the first edition advertised, and this reissue advertises it "
    "accurately. Table 8 is therefore presented as what it is: a "
    "consistency check and a readability gain, each cell a historical "
    "instance of a phase instruction. The load-bearing tests are the other "
    "two — Volume II's wider cases, which the protocol was not fitted to, "
    "and, new in this reissue, the dead.")

CH6_SILENCES = (
    "Three silences conclude the living test, and the first is amended "
    "rather than confessed this time. v1.0 scheduled tool-building "
    "nowhere, though Newton had to invent the calculus and Heisenberg had "
    "to reinvent matrices before either could pay his gates; v1.1 promotes "
    "tool invention to scheduled work at P7, a phase deliverable with its "
    "own artifact, with the post-mortems still logging what no schedule "
    "can foresee. The second silence stands: the protocol substitutes "
    "process for temperament only partly — the founders' capacity to "
    "endure the absurd, Planck's decade of second thoughts, Einstein "
    "arguing against his own formalism, bought time that no gate "
    "measures. The third stands too: timing and community are outside "
    "any single agent's control, as Mendel's thirty-five silent years "
    "and Wegener's half-century measured. The gates are "
    "necessary-condition extractors. History shows they were present "
    "whenever profundity occurred; history does not show they are "
    "enough, and nothing in this manual can close that last conditional.")

CH6_CENSUS_1 = (
    "The failure census is the test the doctrine never had, and its result "
    "is now part of the manual. Three dead theories — phlogiston, the "
    "luminiferous ether, the epicycle tradition — were coded against the "
    "nine-point signature under a pre-registered sampling rule, in "
    "matched pairs with their executioners, holding instruments and data "
    "constant while the framework varied: Priestley's oxygen armed "
    "Lavoisier; the Michelson null armed Einstein; Tycho's archive armed "
    "Kepler. The census exists as its own artifact, printed with this "
    "reissue; this section carries its verdict. Twenty-seven cells, no "
    "point untouched. The dead theories satisfied the soft points — "
    "unification three for three, founders' resistance three for three, "
    "crisis-chaining partial in all — and failed the hard ones: no dead "
    "theory deleted a constitutive concept at its christening, installed "
    "a constant, minted a measurable, or recovered a predecessor's "
    "ontology. Table 9 prints the matrix; Table 10 renders the verdicts "
    "that Table 2's fourth column records.")

CH6_CENSUS_2 = (
    "The signature the census leaves standing is smaller and harder. "
    "Five discriminators survive — deletion at birth, the constant under "
    "its promotion test, ontological embedding, generative slope, minted "
    "measurables — with derivation-first restated as the "
    "structure-not-content rule the epicycles forced. Three points "
    "demote to truths that do not discriminate, and the demotions are "
    "findings, not losses: unification joins Volume II's conditions as "
    "a marker of ambition; founders' resistance demotes to a marker of "
    "stakes, present on both sides of the grave; crisis-chaining "
    "demotes to a corollary about research ecosystems, since the dead "
    "opened crises as productive as the founders' — for their "
    "successors. The census's own limits are inherited honestly: three "
    "pairs under a rule that admits few, coded unblinded by the "
    "signature's own author, the fame confound named and standing. The "
    "falsifiers are armed as clauses: a ratified profound case that "
    "fails a discriminator deletes the discriminator; a dead theory "
    "admitted under the rule that passes all five deletes the census; "
    "and an independent coder who cannot reproduce the verdicts deletes "
    "the coder. The signature is a hypothesis now, with its controls on "
    "file — which is the only thing it should ever have claimed to be.")

# ---------------------------------------------------------------------------
# Chapter 7 — Alarms, Refutation Clauses, and Honest Limits
# ---------------------------------------------------------------------------

CLAUSES_INTRO = (
    "The closure alarm fired at the meta-level because every outcome of "
    "the protocol's operation confirmed it, and an unfalsifiable "
    "framework is the one crime the alarms exist to catch. Amendment "
    "A5 armed the remedy: three refutation clauses, written as tests a "
    "process can run — each stating its test, its failure condition, "
    "and what dies when the condition is met. The clauses are part of "
    "the manual now, and they cut upward: they do not test a campaign, "
    "they test the instrument the campaigns are run with. Table 12 "
    "states them; an operator who runs the protocol without them is "
    "running v1.0, and v1.0 is on the record as demoted.")

CLAUSES_HEADER = ["Clause", "The test", "It fails when", "What dies"]

CLAUSES_ROWS = [
    ("census agreement",
     "two operators — or two independent runs — execute the P1 assumption "
     "census on identical corpora; the inherited-concept lists are compared "
     "under a stated agreement threshold",
     "agreement falls below the threshold: the census does not reproduce",
     "the census instrument, and the protocol's center with it"),
    ("kill clustering",
     "after a stated number of kills, test whether kill-log entries "
     "cluster by target feature — strain type, subfield — against the "
     "null of random assignment",
     "no clustering: kills are random with respect to the targets' "
     "features",
     "the P0 positioning claim: strain-site aiming is empty"),
    ("kill-cost curve",
     "measure the cost of a G0-to-G2 kill, in operator-hours or compute, "
     "across successive campaigns",
     "the cost does not fall: later kills are as expensive as early ones",
     "the compounding-map claim: the kill log is not an asset, the "
     "protocol is not learning"),
]

CLAUSES_CAPTION = ("Table 12 — Three refutation clauses, armed per Amendment "
                  "A5: the manual's own failure conditions, written as "
                  "runnable tests. Zero survivors, one survivor, and kills "
                  "everywhere no longer confirm the protocol — these do the "
                  "confirming, and they can fail.")

SUCC_P1 = (
    "The successor crises are promoted from a closing paragraph to a "
    "section, as the fifth amendment requires, because a protocol that "
    "demands of every framework one question it makes askable but cannot "
    "answer owes its own list, stated as crises rather than gestures. "
    "Four stand. First, world-contact: the operator cannot execute its "
    "own discriminating lists, and the corpus closes at its cutoff; the "
    "scheduled answer is the tool-invention deliverable of P7, but the "
    "crisis outlives the schedule, because even a tool-using operator "
    "ratifies nothing until the world runs the list. Second, the "
    "independent coder: the census, the translation table, and the "
    "delta inventory were produced by the protocol's own author, and "
    "until a process that has not read the series reproduces or refutes "
    "them, the series' strongest artifacts carry a fingerprint. Third, "
    "the derivability question: whether the corpus contains a derivable "
    "Level-3 revision at all — the question the whole series stands on "
    "and cannot yet answer. Fourth, the kill-log map: what the "
    "compounding asset becomes when it is large enough to matter — a "
    "theory of where the bedrock is not — which no one has written and "
    "this manual cannot.")

LIMITS_1 = (
    "The limits should now be restated as a single honest block, because "
    "the manual's credibility depends on never overselling what its "
    "gates decide. Passing G0 through G7 makes a framework "
    "<i>profound-compatible</i>; it does not make it profound. Ratification "
    "is the century's, and the harvest enumeration is a forecast whose "
    "error bars no one can compute in advance — every founder mispredicted "
    "at least part of the harvest, and gravitational waves spent a hundred "
    "years between prediction and detection waiting for an instrument "
    "nobody had specified. The world holds a veto, exercised through "
    "experiments the operator cannot run. And the census adds its "
    "precision to what the gates certify: five discriminators, not nine "
    "points — a framework passing them is compatible with profundity, "
    "and the world still decides. The numbers inside the gates are "
    "administrative parameters with stated provenance; revising them per "
    "campaign is not a weakening but the honest use of what was always "
    "policy. The protocol reduces the variance of the pursuit, and "
    "variance reduction is all it claims.")

LIMITS_2 = (
    "The base rate must be priced with the same honesty, and the "
    "economics is the one layer the audit cleared of pandering. Three "
    "Level-3 events in roughly three hundred years of physics; nine "
    "across all the sciences in about three hundred and fifty. An "
    "operator running dozens of targets per campaign should expect zero "
    "survivors at G7, and should distrust any campaign that produces "
    "several, exactly as a prospector distrusts a river that yields "
    "gold at every pan. The expected value lies elsewhere: in kills "
    "that are cheap because they come early — a G0 or G1 kill costs "
    "days, where the historical equivalents cost careers — and in the "
    "kill log, which compounds across campaigns into a map of where "
    "the bedrock is not. If the protocol ever produces a genuine "
    "survivor, that survivor will owe the map as much as the pipeline. "
    "And the audit's deepest finding is now part of the manual's "
    "self-description: the series to date forms a closed corpus loop — "
    "histories mined from the corpus, a protocol mined from the "
    "histories, an audit, a census, and a derivation mined from the "
    "protocol — and the loop has exactly one exit, the same exit the "
    "century test reserves: a discriminating list executed by the "
    "world's instruments. Until that event, the protocol's status is "
    "the one it assigns its candidates. Profound-compatible, full "
    "stop.")

LIMITS_3 = (
    "There is a final reflexive point, and v1.1 can make it with the "
    "ledger open rather than empty. This protocol is itself a theory "
    "about theories — a Level-2 structure about Level-3 events, on an "
    "inherited chassis, with a six-item delta — and it is not exempt "
    "from its own instruments. It has now been audited under its own "
    "six alarms, demoted, derived, operationalized, censused, and armed "
    "with clauses that can kill it; the alarms stay pointed at the "
    "alarm-keeper. Any operator who finds this manual comfortable "
    "should ask who agrees with it, and should watch the three clauses "
    "of this chapter more closely than any gate verdict, because the "
    "clauses are where the manual has written down how it would fail. "
    "A manual for deep novelty that everyone immediately likes has "
    "failed its own fourth doctrine; the reissue's answer to that test "
    "is the same as the first edition's, now with a record behind it "
    "— the ledger is no longer empty, its first entries name the "
    "instrument itself, and the next entry is not the manual's to "
    "write.")

# ---------------------------------------------------------------------------
# Chapter 8 — Invocation (amended close)
# ---------------------------------------------------------------------------

CH8_P2 = (
    "The standing posture is the one the whole manual has been "
    "building toward. The founders had one advantage no language "
    "model will ever have: they had the world, and could pay for "
    "their vocabularies with experiments, careers, and the occasions "
    "of their own deaths. The operator's compensation is the corpus — "
    "every measurement the world has ever paid for, every vocabulary "
    "ever tried, every anomaly ever recorded and every inherited "
    "concept ever left unexamined, all of it simultaneously present "
    "for the first time since science began. If another Level-3 "
    "revision exists that a prepared outsider could reach by "
    "derivation from what is already known, it is waiting in that "
    "corpus, in the gap between an accurate number and a sentence "
    "nobody has thought to say about it. The protocol does not "
    "promise to find it. It promises that the search will be "
    "positioned, forced, and honest, that every failure will be "
    "written down where the next run can read it — and v1.1 adds "
    "the honest postscript the audit earned: the claim is the "
    "delta, the numbers are parameters, the clauses are armed, "
    "and the ledger is open. Continue.")

FIG2_CAPTION_V11 = ("Figure 2 — The operator's card, amended: the eight "
                    "phases with their gates and amended rules, the six "
                    "alarms, the five doctrines, the amendment strip of "
                    "v1.1, and the loop rule. The fences are parameters; "
                    "the card is the manual.")
