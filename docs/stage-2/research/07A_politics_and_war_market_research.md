# Politics & War market research — Stage 2 Prompt 07A

**Version:** 1.0 · **Created:** 2026-10-28 · **Stage 2, Prompt 07A** · **Research and documentation only**
**Status:** Research complete. **No Nation Supremacy market rule, fee, limit, price band, order type or settlement rule is approved by this document.** The findings are evidence for Prompt 07B, not decisions.
**Research access date:** 2026-10-28 (all URLs re-read on that date unless a publication date is stated).
**External-reference restriction:** Politics & War is the **only** external game used for game-design research in this report. No other game was searched, compared, cited or used to fill a gap. General technical vocabulary (offer, matching, settlement, atomicity, reservation) is used descriptively, not imported from another game.
**Identifier spaces:** sources `PWS-001…PWS-022`; findings `PWR-001…PWR-030`. Neither space collides with the project's `D-`, `DD-`, `UD-`, `REQ-`, `DMP-`, `F-` or `T` identifiers.
**Next intended task at publication (2026-10-28):** Stage 2 **Prompt 07B — market foundations**, only after this report is reviewed and accepted. Prompt 07B and 07C had **not** started. *Since superseded: 07B completed on 2026-10-28 — see [B-07](../13_trade_and_markets.md); 07C completed on 2026-10-29 — see [the workflows and acceptance companion](../14_market_workflows_and_acceptance.md).*

---

## Section 1 — Executive summary

Politics & War's trade system is best described as **a set of player-posted trade offers, not a conventional exchange**. The evidence supports a global market, an alliance market and private trades as distinct surfaces, with the global market being the one that is publicly visible and the one that produces the published price information.

The strongest verified or well-corroborated findings are:

1. **Multiple trade surfaces.** The global market, a shared alliance market and private trades are referred to as separate channels in a 2022 official staff announcement (indexed excerpt) and in a 2018 player answer about blockades. The same 2022 text says deleting a trade offer affects the global market only, not private trades or shared alliance markets. *Moderate evidence; current status likely but not directly observed.* `PWR-001`
2. **The global market is a posted-offer board with manual acceptance.** A 2014 official-forum tutorial describes two ways to trade: accept another nation's deal from the market, or post your own offer. A 2019 player suggestion states that the game "has no automatic matching module", which is consistent with the offer table and with a 2022 staff discussion of per-resource offer caps. No official page was found that documents an automatic matching algorithm. *Moderate evidence; the 2019 statement is historical and player-authored.* `PWR-002`
3. **An offer is a quantity of a resource for a money return, displayed with a per-unit price.** A public nation trade-activity page observed on 2026-10-28 lists, for each trade, the selling nation, the buying nation, the date offered, the offer quantity, the money return and the per-unit figure in parentheses (for example, 1,000 units for 74,000, "(74 ea)"), plus a status and an acceptance date. *Verified interface observation.* `PWR-003`, `PWR-004`
4. **Offers persist until accepted.** The same observed page contains completed offers that were posted hours or days before acceptance (one was posted on 10/19 and accepted on 10/23). It does not establish an expiry rule; it establishes that offers are not instantaneous-only. *Moderate interface evidence.* `PWR-004`
5. **Posting an offer does not appear to reserve the goods or the money.** A 2015 player report describes repeatedly clicking a global-market offer and receiving "this nation has insufficient resources" or "insufficient cash"; a 2022 staff discussion of offer caps and a 2019 suggestion both treat offers as postings that can outlive the poster's stock. No official rule was found that states reservation at posting. *Moderate, historical, player-reported; the absence of an official rule is itself a gap.* `PWR-005`
6. **Price information is published, but it is an average, not a live quote.** The trade page observed on 2026-10-28 displays a "Current Market Index" and per-resource "Average Prices" for Food, Steel, Aluminum, Munitions, Gasoline, Coal, Oil, Uranium, Iron, Bauxite, Lead and Credits, plus a link to average-price history. The community wiki says averages are measured at the end of each day and that a 60-day history page exists; player discussion says the average tracks the global market only, not alliance or private trades. *Verified interface observation for the display; moderate community evidence for the computation.* `PWR-011`, `PWR-012`
7. **Trade activity is public per nation.** The observed nation page exposes 86 offers with counterparties, dates, quantities, returns and statuses to a logged-out visitor. This is a transparency feature and a privacy/competition consideration at the same time. *Verified interface observation.* `PWR-013`
8. **Trade is restricted by account and network policy, not only by price.** The official Game Rules prohibit more than one nation per person, restrict same-network nations from interacting (including "sweetheart trades" and third-nation routing in the community FAQ), prohibit automated trading and banking, and prohibit new nations from sending all or most of their money and resources. The community FAQ adds a **±30% price band** around the average market price for nations under 30 days old (buying) and for same-network-flagged nations (buying and selling). *Official rules: strong. ±30% band: moderate community evidence, current status unverified.* `PWR-016`…`PWR-019`
9. **Fees are not documented in the sources reached.** No official page or announcement establishing a trade fee, listing fee or percentage was found. This is **not** proof that no fee exists; it is a research gap. *Unknown.* `PWR-010`
10. **Matching priority, partial fills and expiry are undocumented in the sources reached.** The interface shows whole offers and a status; it does not establish whether a buyer may take part of an offer, whether crossed offers are matched by price or time, or whether offers expire. These are research gaps, not negative findings. *Unknown.* `PWR-006`

**Documented strengths.** The system is conceptually simple (browse and accept, or post an offer); it communicates quantity, total return and unit price together; it works asynchronously because offers wait for a taker; it publishes enough history for price comparison; and the existence of global, alliance and private channels lets players choose a trust/visibility level. These are supported by the interface and by the tutorial, not by a player survey. `PWR-002`…`PWR-004`, `PWR-011`…`PWR-013`, `PWR-001`

**Documented frustrations.** The best-supported complaint is **stale or unfunded offers that fail when clicked** (2015, single source, consistent with no reservation at posting). A 2019 player suggestion describes the **absence of automatic matching** as allowing buy offers above sell offers. A 2022 staff post acknowledges **trade spam** and proposes per-resource active-offer caps. A 2022 suggestion describes **confirmation fatigue** (an identical confirmation for every trade leads to automatic acceptance), and a 2014 suggestion describes confusion over the **trade-activity display**. None of these establishes prevalence; each is reported as a documented experience with its own confidence. `PWR-022`…`PWR-026`

**Critical uncertainties.** (a) No authenticated interface inspection was possible, so the order form, reservation behaviour, partial-fill behaviour, cancellation, expiry and fee display were not directly observed. (b) Several official-forum bodies did not render; for those, only the indexed excerpt or meta description was available, and this is disclosed per source. (c) The 2022 per-resource cap is an announced policy, not a verified current implementation. (d) The community wiki may lag the live game. (e) No player survey, percentage or frequency data exists in this research, so no claim of "widespread" sentiment is made.

**Implications for Prompt 07B (questions only).** The evidence gives Prompt 07B a realistic reference for a **posted-offer market with manual acceptance, public price averages, asynchronous offers and account-level anti-abuse restrictions**. It does **not** decide whether Nation Supremacy should use posted offers, an order book, automatic matching, reservations, boundary settlement, fees, price bands or offer caps. Those choices must be made against Nation Supremacy's existing decisions — in particular D-016 (directed offers do not reserve), D-017 (trade terms are parties-only; no public offer book at first playable), REQ-010 (a listing market only after gate G-1…G-6), ECN-211 (atomic settlement at P4, shared `transfer_id`, warehouse check) and B-03's fresh-nation transfer rule, whose fair-value band and window Prompt 07 owns. `PWR-001`…`PWR-006`, `PWR-010`, `PWR-016`…`PWR-019`

---

## Section 2 — Research scope and methodology

### 2.1 What was investigated

The research covered the questions in the Prompt 07A brief: market structure; tradeable resources; order creation; matching and settlement; fees and financial rules; order lifecycle; market activity and information; trade restrictions; trading's relationship to production, war, alliances and progression; manipulation and abuse; and usability/player experience. No Nation Supremacy mechanic was designed, changed or approved.

### 2.2 Source categories used

| Category | What it contributed | Sources |
|---|---|---|
| Official rulebook | Account, network, trading-fairness and automation rules | `PWS-001` |
| Official game pages (logged out) | Trade-page framing, market index and average prices; public nation trade history | `PWS-002`, `PWS-003` |
| Official forum tutorial/announcements | The two ways to trade; embargoes; the 2022 content announcement; the 2022 offer-cap discussion | `PWS-007`, `PWS-011`, `PWS-016`, `PWS-008` |
| Community wiki | FAQ on one account, same-network restrictions and the ±30% band; average-price definition; historical resource geography | `PWS-004`, `PWS-005`, `PWS-006`, `PWS-020` |
| Player forum threads | Reported failures, matching observations, confirmation fatigue, display confusion, price comparison | `PWS-009`, `PWS-010`, `PWS-012`…`PWS-015`, `PWS-017`, `PWS-018`, `PWS-022` |
| Player community (Reddit) | Attempted; blocked by a login wall | `PWS-019` |
| Official API | A trade-price endpoint exists but requires a key | `PWS-021` |

### 2.3 Method

1. Searched for the official rules, trade pages, help material, changelog/announcements and forum discussions, restricted to Politics & War.
2. Fetched the official rulebook and the public trade pages directly. The trade page and the nation trade-activity page were readable **without signing in**; the order form itself was not.
3. For Fandom pages that returned **403** as rendered HTML, retrieved the same page's **wikitext** through the wiki's `?action=raw` endpoint. This is the community wiki's own content endpoint, not a search-engine cache.
4. For official-forum topics whose bodies are loaded dynamically, recorded only what the page's title, meta description or indexed excerpt actually establishes, and marked the limitation on each affected source.
5. Classified every material finding with one evidence label (§2.4) and one confidence level (§2.5).
6. Cross-checked claims against a second source where one existed; where it did not, the finding is labelled single-source.
7. Deliberately did **not** place, cancel or modify any order, did not sign in, and did not use any credential.

### 2.4 Evidence classifications

The report uses exactly these labels:

| Label | Meaning in this report |
|---|---|
| **Verified official rule** | A current rule stated by Politics & War's own rulebook, official page or staff announcement. |
| **Verified interface observation** | Something directly observed on a public Politics & War page on 2026-10-28, read-only. |
| **Corroborated player experience** | A player-reported experience supported by at least two independent, relevant sources. |
| **Single-source player report** | A reported experience found in one source only. |
| **Historical behaviour** | Behaviour documented in an older source that may no longer describe the current game. |
| **Researcher interpretation** | An analytical reading of what the evidence may mean. It is not a game rule. |
| **Unverified hypothesis** | A question or possibility for which no sufficient evidence was found. |

A single sentence does not mix labels: where a paragraph moves from an observed interface to an interpretation, it says so.

### 2.5 Confidence levels

| Level | Test applied |
|---|---|
| **Strong** | Current official documentation, or a direct interface observation on the access date, establishes the claim. |
| **Moderate** | Credible evidence supports the claim, but it is a single official statement without a current confirmation, or a community source that may lag, or a player report consistent with the interface. |
| **Weak** | Isolated anecdote, ambiguous description, an old source, a title-only source, or untested interpretation. |

Confidence is assigned per finding in Section 11, with the reason where it is not obvious.

### 2.6 Authenticated browser research — actual outcome

**No suitable access to the owner's Chrome session was available, and no authenticated inspection was performed.**

The working environment has a Chromium preview tool, but it does **not** share the owner's local Chrome profile, cookies or Politics & War session. No sign-in was attempted, no password or code was requested, and no cookie, token or session secret was read, exported or stored. The pages actually observed were the **public, logged-out** trade page (`PWS-002`) and a **public nation trade-activity page** (`PWS-003`). They are recorded as verified interface observations of what a logged-out visitor sees, not as an inspection of the account-holder's market screen.

Consequently the following were **not** observed: the create-offer form and its fields; any reservation indicator; partial-fill controls; cancel/replace controls; expiry display; fee display; error messages after a failed acceptance; and the alliance or private trade screens.

### 2.7 Limitations

1. **Forum bodies.** Several Invision Community topics returned only the title and a meta-description snippet; the reply bodies are loaded dynamically. For `PWS-007`, `PWS-009`…`PWS-019` and `PWS-022`, only the indexed excerpt is cited, and the limitation is stated in the source register.
2. **No authenticated session.** See §2.6.
3. **No official documentation of matching, priority, partial fills, expiry or fees.** Their absence from this report is a documentation gap, not evidence that the features do not exist.
4. **Community wiki may lag.** `PWS-004`/`PWS-005` are community-maintained. The ±30% band and the averaging rule are recorded as community statements, not official rules.
5. **Historical sources.** The 2014 tutorial, the 2014 embargo announcement and the 2019/2022 player threads are dated. They are used for structure and player experience, not as proof of current rules, unless a later source corroborates them.
6. **No player statistics.** No survey, percentage, trade volume or complaint frequency was found or is claimed. Each player report is one report.
7. **No live order placement.** The study did not test settlement, cancellation or a failed trade by acting on an account; doing so was prohibited.
8. **One nation's history is not the market.** The observed 86 trades are one nation's activity, not a representative sample of global volume, price or liquidity.
9. **No competitor cross-check.** By instruction, no other game was consulted, so a claim that a design is "common in the genre" cannot be made from this report.

---

## Section 3 — Verified Politics & War market overview

### 3.1 The trade page as observed

The public trade page (`PWS-002`, observed 2026-10-28, logged out) describes itself as the place to **"Buy and sell resources in the live, laissez-faire global market."** It displays a **Current Market Index** and a row of **Average Prices** for Food, Steel, Aluminum, Munitions, Gasoline, Coal, Oil, Uranium, Iron, Bauxite, Lead and Credits, with a link to **"See Average Price History"**. The order form itself sits behind the sign-in boundary and was not observed.

This establishes three things and no more: (a) Politics & War presents one global market as its main trading surface; (b) it publishes a current index and per-resource averages on that page; (c) it offers a history view. It does not establish how those averages are computed, which trades they include, or whether the index is a price, a volume or a composite. The community wiki and player discussion supply the computation claims in §5.3, at lower confidence.

### 3.2 Three trade surfaces

The evidence points to **three distinct surfaces**, not one:

| Surface | Description | Evidence | Confidence |
|---|---|---|---|
| **Global market** | Public posted offers between nations; the surface that produces the displayed average prices. | `PWS-002`, `PWS-003`, `PWS-007`, `PWS-008` | **Strong** that it exists; **moderate** for its exact rules |
| **Alliance market** | A shared market for an alliance's members, referred to as separate from the global market. | `PWS-011` (2022 official announcement, indexed excerpt), `PWS-012` (2018 player answer) | **Moderate** |
| **Private trades** | Direct trades between two nations, outside the global and alliance markets. | `PWS-011`, `PWS-012`, `PWS-015` (average prices exclude them) | **Moderate** |

**Why this matters.** A 2022 staff announcement's indexed excerpt says that deleting a trade offer **"does not impact private trades or shared alliance markets, only global market trades"** (`PWS-011`). That sentence is the clearest official evidence found for the three-surface model. It also shows that the **global market has its own offer lifecycle** — an offer can be deleted — which is not necessarily the same lifecycle as a private trade.

**What is not established.** Whether the alliance market is a separate order board, a shared pool, or a permissioned view of the global market; whether private trades require an offer/accept flow; whether private trades settle differently; and whether the three surfaces share one price or three. The 2018 player answer says a blockade stops "global market, alliance market, personal trade offers" (`PWS-012`), which implies all three are trade surfaces, but it is a player answer, not a rulebook.

### 3.3 The global market is an offer board

The evidence supports a **posted-offer board**: a nation publishes an offer, and another nation accepts it. It does **not** support a conventional continuous order book or an automatic matching engine.

- The 2014 official-forum tutorial's indexed excerpt describes **two options**: "Accepting another nations trade deal" from the market, or posting your own offer (`PWS-007`). That is the classic offer-board workflow.
- A 2019 player suggestion states: **"Presently, the game has no automatic matching module, which means it is possible for there to be buy offers above the value of the current sell offers"** (`PWS-009`). The claim is player-authored and historical, but it is specific, technically coherent and consistent with the rest of the evidence.
- A 2022 staff post about **restricting market trades** discusses "active buy offers and active sell offers" per resource (`PWS-008`), which presumes offers that rest until accepted or deleted.
- The observed trade-activity table has an **Offer** column and a **Return** column and a **Status** of `Accepted` (`PWS-003`). That is the record shape of a bilateral offer accepted by a counterparty, not a fill report from a matching engine.

**Therefore:** the verified core is *offer → accept*, with the taker choosing the offer. Price-time priority, pro-rata allocation and automatic crossing are **not documented** and must not be assumed. `PWR-002`, `PWR-006`

### 3.4 What is traded

The public trade page's average-price row names the resources a player can compare: **Food, Steel, Aluminum, Munitions, Gasoline, Coal, Oil, Uranium, Iron, Bauxite, Lead** and **Credits** (`PWS-002`). The observed trade history is consistent with resource-for-money offers (`PWS-003`).

Three cautions:

1. **Credits are a premium currency, not a resource.** The page lists them alongside resources, and the 2022 staff post explicitly says the proposed per-resource offer cap does **not** affect Credits (`PWS-008`). Credits should not be treated as an ordinary material in any comparison.
2. **The exact tradeable set is not confirmed as a rule.** The page shows prices for the named resources; it does not prove that every one is tradeable in every direction or that no other asset is tradeable. The historical wiki guide describes six continents each producing three of six resources (`PWS-020`), which is a **historical** geography and does not match the current eleven-resource price row. `PWR-021`
3. **Money is one side of the observed trades.** Every observed trade is a resource quantity against a money return. No barter, auction or multi-resource bundle was observed. That is an interface observation, not a prohibition. `PWR-003`, `PWR-004`

### 3.5 Public trade activity

The nation trade-activity page (`PWS-003`) exposes, to a logged-out visitor, a table with these columns:

| Column | Example | What it establishes |
|---|---|---|
| Selling Nation | Nation A / Leader A / Alliance A | The seller's nation, leader and alliance are shown. |
| Buying Nation | Nation B / Leader B / Alliance B | The buyer's nation, leader and alliance are shown. |
| Date Offered | `10/26/2026 11:49 pm` | Offers carry a publication timestamp. |
| Offer | `1,000` | The resource quantity. |
| Return | `74,000 (74 ea)` | The money total and the per-unit figure. |
| Status | `Accepted 10/27/2026 08:37 pm` | The terminal state and its timestamp. |

This is a **public transaction history**, not just a private order list. It is a significant transparency choice with obvious competitive and privacy consequences (§8). It also gives a researcher a way to check arithmetic: every observed row is consistent with `return = offer × per-unit price` (for example 1,000 × 74 = 74,000; 200 × 73 = 14,600; 20 × 3,199 = 63,980; 15 × 3,118 = 46,770). That is an **arithmetic observation from the display**, not a published formula. `PWR-003`, `PWR-013`

### 3.6 Lifetime and scale of the observed sample

The observed page reports **86 offers** for one nation and shows the first 15. The visible completions span 10/16/2026 to 10/27/2026, and one offer posted on 10/19 was accepted on 10/23. That establishes that offers can remain open for days and that the page is a historical record, not a live book. It does **not** establish a maximum lifetime, a default expiry, a minimum or maximum order size, or global volume. `PWR-004`

### 3.7 What the overview does not establish

The following are **unknown** after this research and are carried to Section 12: the create-offer form's exact fields; whether an offer can be edited rather than deleted and reposted; whether a partial acceptance is possible; whether a taker can accept multiple offers in one action; whether offers expire; whether a fee is charged; whether funds or goods are reserved at posting; whether a buy offer and a sell offer can cross automatically; and how the alliance market and private trades are implemented.

---

## Section 4 — Trading rules and order lifecycle

### 4.1 Lifecycle at a glance

| Stage | What the evidence establishes | Evidence class | Source | Confidence |
|---|---|---|---|---|
| **Creation** | A nation can post a buy offer or a sell offer for a resource. The offer has a quantity and a money return. The exact form fields were not observed. | Verified official rule (existence of buy/sell offers); historical tutorial for the two paths | `PWS-008`, `PWS-007` | Moderate |
| **Publication** | The offer appears in the global market and, once accepted, in the nation's public trade activity. | Verified interface observation (history); moderate for market listing | `PWS-003`, `PWS-002` | Moderate |
| **Reservation** | No official rule found. Player reports are consistent with **no reservation at posting**: a clicked offer can fail because the counterparty lacks resources or cash. | Single-source player report, historical | `PWS-010` | Weak to moderate |
| **Matching** | Manual acceptance by a counterparty. No automatic matching module is documented; a player states there is none. | Historical player report + tutorial | `PWS-009`, `PWS-007` | Moderate |
| **Priority** | No price-priority or time-priority rule documented. The taker selects the offer. | Unverified hypothesis (no documentation) | — | Unknown |
| **Partial fill** | No evidence of partial acceptance; observed rows are whole offers. | Unverified hypothesis | `PWS-003` | Unknown |
| **Settlement** | On acceptance, the offer's status becomes `Accepted` with a timestamp. Resources and money appear to move at acceptance. | Verified interface observation + inference | `PWS-003` | Moderate |
| **Failure** | A click can fail with "this nation has insufficient resources" or "insufficient cash". | Single-source player report, historical | `PWS-010` | Weak to moderate |
| **Cancellation** | A player can delete a trade offer; the 2022 announcement distinguishes global-market deletion from private/alliance trades. | Official announcement (indexed excerpt) | `PWS-011` | Moderate |
| **Expiry** | No expiry rule found; offers persist for days in the observed sample. | Interface observation + absence of documentation | `PWS-003` | Unknown |
| **Limits** | A 2022 staff post says at most **3 active buy offers and 3 active sell offers per resource**, Credits unaffected. Implementation/current status not verified. | Official staff post (announced policy) | `PWS-008` | Moderate for the announcement; weak for current |
| **Fees** | No fee documented in the sources reached. | Unverified hypothesis (absence of evidence) | `PWS-001`, `PWS-002` | Unknown |

### 4.2 Creation and pricing

**Observed pricing shape.** An offer carries a **quantity** and a **money return**; the interface derives and displays a **per-unit price**. Every observed row is arithmetically consistent with `return = quantity × unit price`. The interface displays whole units and whole money (`PWS-003`). Whether the form asks for a total or a unit price first is **not observed**; the 2014 tutorial's indexed excerpt does not say.

**What this means for comparison.** Politics & War's offer is a **total-value bargain**, with the unit price shown for comparability. A player comparing two offers must divide or use the displayed unit figure. This is a different mental model from an order book that quotes a unit price and derives the total. It is a **research interpretation**, not a rule.

**No documented minimum, maximum, price floor or price ceiling** was found for the global market as a whole. The only price constraint found is the ±30% band applied to **new nations under 30 days** and to **same-network-flagged nations**, in the community FAQ (`PWS-004`). It is applied to buying for new nations and to both buying and selling for flagged networks. `PWR-016`

**No documented rounding rule** was found. The observed values are integers, and the totals are exact multiples, so the display is consistent with integer arithmetic; that is not proof that the game forbids fractional prices internally.

### 4.3 Posting, reservation and offer honesty

The strongest player-experience evidence in the whole research is the 2015 report that clicking an offer can produce **"this nation has insufficient resources"** or **"insufficient cash"** (`PWS-010`). If that report is accurate, then a posted offer is **not** backed by reserved goods or money at posting: the offer is a pledge, and acceptance re-validates the counterparty.

This reading is corroborated in structure, though not in direct observation, by:

- the 2022 staff discussion of **active offer caps**, which is a spam control rather than a stock control (`PWS-008`);
- the 2019 statement that there is **no automatic matching module**, which is consistent with offers being inert until a human accepts (`PWS-009`);
- the 2014 tutorial's two-path model, in which accepting someone else's deal is a distinct action (`PWS-007`).

**However:** no official rule was found that says "offers do not reserve". The finding is therefore **single-source player report** for the failure symptom, and **researcher interpretation** for the no-reservation mechanism. `PWR-005`, `PWR-022`

### 4.4 Matching and priority

No Politics & War documentation was found that defines:

- whether a new offer that crosses an existing offer executes immediately;
- whether the oldest offer, the cheapest offer or the largest offer is presented first;
- whether a taker can choose any offer or only the best one;
- whether two offers from the same nation can match;
- whether a partially filled offer remains open for the remainder;
- whether a taker can accept only part of an offer.

The 2019 player statement that buy offers can sit **above** sell offers is direct evidence that the system does **not** automatically cross the book (`PWS-009`). If it did, a buy at 80 and a sell at 74 would have executed. That is an inference from a player report, but it is a strong structural inference because the claimed state is observable and the claim is specific.

**Therefore:** the evidence supports **manual taker selection**, not price-time priority. The absence of a documented priority rule is a finding in itself: a future designer cannot cite Politics & War as having a published matching policy. `PWR-002`, `PWR-006`, `PWR-023`

### 4.5 Settlement and failure

The observed `Accepted` status with an acceptance timestamp is consistent with **settlement at acceptance** (`PWS-003`). The page does not show a pending state, a settlement delay, or a boundary. The 2015 failure report implies that acceptance is the moment of re-validation and that a failed acceptance moves nothing (`PWS-010`, if accurate).

What is **not** established: whether settlement is a single atomic transaction in the engine; whether a failure can leave one leg moved; whether a retry can double-settle; and whether an accepted trade can later be reversed. Those are engineering properties, not observable from the public record. They must not be inferred from the status label.

### 4.6 Cancellation and expiry

The 2022 content announcement's indexed excerpt refers to **deleting a trade offer** and says it does **not** impact private trades or shared alliance markets, only global market trades (`PWS-011`). That supports a delete/cancel action on the global market. It does **not** establish whether deletion is immediate, whether it is blocked once a taker has accepted, whether a fee is forfeited, or whether a deleted offer disappears from history.

**Expiry:** no rule found. The observed sample includes offers open for four days, so either expiry is long, absent, or conditional. The safest research statement is: **offers can persist for days; an expiry rule is undocumented and unverified.** `PWR-004`, `PWR-009`

### 4.7 Limits and eligibility

| Restriction | What is documented | Status | Source |
|---|---|---|---|
| One nation per person | "No individual player is allowed to have more than one nation for any reason"; nation-sitting prohibited. | **Verified official rule** | `PWS-001` |
| Same-network nations | No limit on nations per network if each is controlled by a separate person; automatic restrictions apply; using alliance banks to evade trade restrictions is bannable. | **Verified official rule** | `PWS-001` |
| Same-network interaction | Community FAQ: different people may play from one network but "cannot interact in-game in any way", including "sweetheart trades", third-nation routing and shared wars; many restrictions are mechanically imposed and can be removed by verification. | **Community statement; moderate** | `PWS-004` |
| New-nation price band | Nations under 30 days may not buy outside **±30%** of the average market price; same-network-flagged nations face the band on buying and selling. | **Community statement; moderate; current unverified** | `PWS-004` |
| New-nation transfers | New nations may not send all or most of their money and resources; nations created to send value are a serious violation. | **Verified official rule** | `PWS-001` |
| Automated trading/banking | Scripts, bots, macros and automated trading/banking are prohibited; read-only price-notification scripts are allowed if the player still trades manually. | **Verified official rule** | `PWS-001` |
| Active offer cap | 3 active buy + 3 active sell offers per resource; Credits unaffected. | **Staff-announced 2022; implementation unverified** | `PWS-008` |
| Embargo | An embargo list prevents the two nations from trading with each other on the global market. | **Official 2014 announcement; historical but plausibly current** | `PWS-016`, `PWS-006` |
| Blockade | A blockaded nation's trade "does not work in any way" — no global, alliance or personal trade. | **Single-source player answer; weak** | `PWS-012` |
| Verification | Shared-network restrictions can be removed by verification. | **Official verification page referenced by the wiki; not fetched in this pass** | `PWS-004` |

**Interpretation.** The restrictions are **account- and network-level**, not merely price-level. Politics & War relies on a combination of identity policy, interaction bans, a price band and manual review. The community FAQ explicitly says the ±30% band exists "to prevent new nations from being created to immediately trade away all of their money" (`PWS-004`). This is a **documented design rationale**, though from a community source. `PWR-016`, `PWR-017`, `PWR-019`

### 4.8 Fees and precision — what is genuinely unknown

No fee schedule, listing fee, transaction percentage or trade tax was found on the official rulebook, the public trade page, the FAQ or the forum material reached. That is a **negative research result**, not a verified absence. The report does not claim Politics & War is fee-free. A future researcher with an authenticated session should check the create-offer screen for a fee line and the trade history for a fee column. `PWR-010`

Likewise, the research did not establish a rounding rule, a minimum price increment, or a maximum total. The observed totals are exact, but that is consistent with integer inputs rather than proof of an integer-only engine.

---

## Section 5 — Market information and player workflows

### 5.1 Discovery

A player reaches the market through the trade page (`PWS-002`). The page presents the current index, the per-resource average prices and a history link **before** any offer list, so price context is available before a trade is chosen. The 2014 tutorial's excerpt refers to selecting the resource a player wants and then finding offers, which implies a resource filter (`PWS-007`). The modern page's resource row is consistent with that model, but the filter control itself was not observed because the order interface is behind sign-in.

**Unknown:** default sorting, search, pagination, whether offers from embargoed or same-network nations are hidden or merely rejected, and whether a player can save a resource as a favourite. `PWR-011`

### 5.2 Offer and transaction visibility

| Information | Visibility | Evidence |
|---|---|---|
| Global-market offers | Public to signed-in players; the offer board was not observed logged out | `PWS-002`, `PWS-008` |
| Completed trades | **Public per nation**, including counterparty, alliance, date, quantity, return and unit price | `PWS-003` |
| Average prices | Public on the trade page; per-resource | `PWS-002`, `PWS-005` |
| Price history | Public link; the wiki says 60 days by default | `PWS-002`, `PWS-005` |
| Alliance-market terms | Separate from the global market; visibility to alliance members is implied, not documented in this pass | `PWS-011` |
| Private-trade terms | Separate; excluded from the average price | `PWS-011`, `PWS-015` |
| Fees | Not observed | — |

**Interpretation.** Politics & War is unusually transparent for a browser strategy game: a third party can read a nation's completed trades and infer its supply relationships and economic posture. That is useful for price discovery and accountability, and it is also a strategic-intelligence surface. The report records the trade-off; it does not recommend either posture for Nation Supremacy. `PWR-013`

### 5.3 Price information — what the averages mean

The community wiki states that average prices are shown on the trade menu, are **measured at the end of each day**, and can be viewed historically (past 60 days by default) on a dedicated history page; the dates are calendar dates, not the in-game Orbis date (`PWS-005`). A player discussion says the average **only tracks the global market** and does not include alliance-specific or personal trades (`PWS-015`). Another player discussion says the price "moves per 1,000 units sold" and only on the global market (`PWS-018`).

**Confidence.** The existence of a daily average and a history page is **moderate** (community wiki, consistent with the public page's link). The end-of-day timing is **moderate**. The "global market only" scope is **weak to moderate** (two player discussions, same claim, but neither official). The "per 1,000 units" movement rule is **weak** (player belief, not documented) and is not used in this report as a rule.

The average is therefore best understood as an **information product about the global market**, not a settlement price. The observed trades occurred at 71–85 per unit for the same resource across ten days, which shows that individual offers can deviate substantially from a single average. That is an arithmetic observation from the sample, not a claim about the market's distribution. `PWR-011`, `PWR-012`

### 5.4 A typical evidenced workflow

1. Open the trade page and read the current index and average prices (`PWS-002`).
2. Choose a resource and browse offers, or post an offer with a quantity and a return (`PWS-007`, `PWS-008`).
3. Wait for a counterparty; offers persist and can be accepted later (`PWS-003`).
4. A taker accepts an offer; the trade appears as `Accepted` with a timestamp (`PWS-003`).
5. If the counterparty lacks the goods or money, the acceptance can fail with an insufficient-resources or insufficient-cash message (`PWS-010`).
6. The poster can delete a global-market offer (`PWS-011`).
7. Completed trades appear in the nation's public trade activity and feed the global average (`PWS-003`, `PWS-015`).

Steps 1, 3, 4 and 7 are supported by interface observations; steps 2 and 6 by official-forum excerpts; step 5 by one player report. The workflow is therefore a **composite of evidence classes**, not a single verified sequence.

### 5.5 What the interface does well, on the evidence

- **Quantity and value are shown together.** An offer is not a bare price; the player sees the amount, the total and the unit figure in one row (`PWS-003`).
- **The unit figure makes offers comparable.** A player does not have to normalise every offer mentally (`PWS-003`, interpretation).
- **Price context precedes the trade.** Index and averages are on the trade page (`PWS-002`).
- **History exists.** A 60-day price history and a per-nation trade history make the market legible after the fact (`PWS-005`, `PWS-003`).
- **Asynchronous by construction.** An offer waits; a player does not need to be online with a counterparty (`PWS-003`).

### 5.6 What the interface evidence cannot support

It cannot support a claim that the market is **liquid**, **fair**, **cheap**, **fast** or **popular**. The research observed one nation's history and one page's header. No volume, depth, spread, fill rate, time-to-fill or player count was collected. Those would require a different study.

---

## Section 6 — Player-reported strengths

This section lists only positives that a source actually supports. It does not infer approval from the absence of complaints, and it does not turn a design feature into a player preference.

### 6.1 A two-path mental model is easy to explain

**Finding:** `PWR-002`. **Sources:** `PWS-007`, `PWS-003`. **Evidence:** historical tutorial excerpt plus interface structure. **Confidence:** moderate.

The 2014 official-forum tutorial's indexed excerpt says there are two options when trading resources: accept another nation's trade deal from the market, or post your own. That is a complete mental model in one sentence. The observed trade history is consistent with it: every row is one nation's offer accepted by another.

**What it establishes:** the system can be taught as "take an offer or make one". **What it does not establish:** that new players find it easy in practice; no onboarding feedback was found.

### 6.2 Offers are asynchronous

**Finding:** `PWR-004`. **Source:** `PWS-003`. **Evidence:** verified interface observation. **Confidence:** moderate.

The observed history contains offers accepted hours or days after posting. A posted offer therefore does not require both players to be online at the same moment. For a browser game with a global player base, that is a real convenience: a player can leave an offer and return to a completed trade.

**Caveat:** the interface shows the outcome, not the notification or the wait. Whether a player is told promptly, and whether an unaccepted offer feels like wasted effort, is not established.

### 6.3 Quantity, total and unit price are legible together

**Finding:** `PWR-003`. **Source:** `PWS-003`. **Evidence:** verified interface observation. **Confidence:** strong (for the display).

The history row shows `1,000`, `74,000` and `(74 ea)` together. A player can see the size, the total commitment and the comparable unit rate without arithmetic. The per-unit figure is especially useful when offers differ in size.

**Interpretation:** this reduces the cognitive cost of comparing a 200-unit offer with a 2,000-unit offer. It is a display strength, not evidence that players use it well.

### 6.4 Price context and history are public

**Finding:** `PWR-011`, `PWR-012`. **Sources:** `PWS-002`, `PWS-005`, `PWS-015`, `PWS-018`. **Evidence:** verified interface observation (index/averages/history link); community wiki (end-of-day, 60 days); player discussion (global-only). **Confidence:** strong for the existence of the display; moderate for the computation.

The trade page puts a current index and per-resource averages in front of the player before an offer is chosen. The wiki describes a 60-day history page and end-of-day measurement. A player can therefore form a view of "normal" before accepting a price.

**Caveat:** an average is not a quote. It does not tell a player whether a buyer is available at that price now, and it excludes alliance and private trades (per player discussion). A new player could over-trust it.

### 6.5 Public trade history supports accountability

**Finding:** `PWR-013`. **Source:** `PWS-003`. **Evidence:** verified interface observation. **Confidence:** strong.

A third party can see who traded with whom, when, in what quantity and at what unit price. That makes repeated self-dealing or a suspicious transfer pattern visible to other players and to moderators. It is a transparency feature that supports the anti-abuse rules in `PWS-001`.

**Trade-off:** the same visibility reveals supply relationships and economic strategy. The report records both sides; it does not decide which matters more.

### 6.6 Multiple channels let players choose a trust level

**Finding:** `PWR-001`. **Sources:** `PWS-011`, `PWS-012`, `PWS-015`. **Evidence:** official announcement excerpt plus player answer. **Confidence:** moderate.

A global market, an alliance market and private trades imply three different audiences: the whole world, a trusted group, and a single counterparty. That is a recognisable social structure for a nation game: alliance members can trade internally, and allies can deal privately, without exposing every transaction to the global book.

**Caveat:** the research did not observe the alliance or private interfaces. The claim is about the existence of the surfaces, not their usability.

### 6.7 Trading supports specialization and shortage response

**Finding:** `PWR-020`, `PWR-021`. **Sources:** `PWS-020` (historical community guide), `PWS-003`, `PWS-002`. **Evidence:** historical guide plus interface. **Confidence:** weak to moderate.

The historical guide recommends that new nations extract resources and sell them on the market, and describes continents with different resource endowments. The current trade page lists eleven resources with market prices. The structural implication is that a nation can specialise in what it produces well and buy what it lacks.

**What it does not establish:** that the current game uses geography or distance, that specialisation is optimal, or that a new player can reliably find a buyer. The guide is marked **Obsolete** by the wiki, and the current resource set differs from the six-resource geography it describes. `PWR-021` is **historical only**.

### 6.8 The market is not an automated treadmill

**Finding:** `PWR-018`. **Source:** `PWS-001`. **Evidence:** verified official rule. **Confidence:** strong.

Politics & War prohibits automated trading and automated banking, while allowing scripts that only notify a player of prices if the trade is completed manually. The rule is a deliberate protection of human agency and a level playing field. A player who wants to trade must make a judgement; the market cannot be farmed by a bot.

**Trade-off:** the same rule limits accessibility for players who cannot watch the market frequently, and it creates demand for external notification tools. The report records the rule and the tension; it does not recommend either.

### 6.9 What is *not* established as a strength

No source establishes that the market is **liquid**, **fast**, **cheap**, **fair**, **profitable**, or **popular**. No player quoted in this research says the market is enjoyable in general. The positives above are structural or display-level, not a satisfaction survey.

---

## Section 7 — Player frustrations and weaknesses

Each item records the finding, the source and date, the evidence class, the affected group where the source identifies one, and the uncertainty. No frequency or prevalence claim is made.

### 7.1 Stale or unfunded offers fail when clicked

**Finding:** `PWR-022`. **Source:** `PWS-010` (2015-08-20). **Class:** single-source player report, historical. **Confidence:** weak to moderate. **Affected:** any taker; new players are the most likely to be confused.

The report says that clicking a global-market offer can return **"this nation has insufficient resources"** or **"insufficient cash"**, and that this happened "not once but numerous times". The author attributes it to the system rather than to a single careless seller.

**Why it matters:** if offers are not backed at posting, the market can display an offer that cannot settle. The taker spends attention and gets a failure. A novice may not understand that the offer was a pledge, not a reservation.

**Uncertainty:** one report, eleven years old. The mechanism is inferred, not confirmed; the game may since have changed. The report does not give a failure rate.

### 7.2 Crossed offers and the absence of automatic matching

**Finding:** `PWR-023`. **Source:** `PWS-009` (2019-01-30). **Class:** single-source player report/interpretation, historical. **Confidence:** weak. **Affected:** buyers and sellers who expect the best available price.

A player suggestion states that the game has **no automatic matching module**, so a buy offer can be above a sell offer. If accurate, a seller could accept a lower-priced buy offer while a higher one sits on the book, and a buyer could pay more than the lowest ask. The market would depend on players browsing rather than on an execution rule.

**Why it matters:** it is the clearest documented efficiency cost of a manual offer board. It also shows that the absence of matching is a **deliberate or accepted** state, not an oversight the documentation hides.

**Uncertainty:** one player, seven years ago. The claim is specific and structurally plausible, but no official statement confirms it and no current observation tested it.

### 7.3 Trade spam and per-resource offer caps

**Finding:** `PWR-024`. **Source:** `PWS-008` (2022-04-28). **Class:** official staff post (announced policy). **Confidence:** moderate for the announcement; weak for current implementation. **Affected:** active traders, especially those posting many prices.

The staff post opens by saying the team is "looking at reducing trade spam, reducing the number of active trades a player can have for a certain resource", and states that players can have at most **3 active buy offers and 3 active sell offers per resource** (Credits unaffected). It then polls whether a fourth posting should auto-delete the oldest or be refused.

**Why it matters:** it confirms that unconstrained offer posting created a spam/visibility problem large enough for staff to intervene. It also confirms that a per-resource cap was the chosen direction.

**Uncertainty:** the post is a discussion/poll, not a changelog entry. The research did not verify that the cap shipped, what the final rule is, or whether the auto-delete option was chosen. No current interface test was possible.

### 7.4 Confirmation fatigue

**Finding:** `PWR-025`. **Source:** `PWS-013` (2022-08-21). **Class:** single-source player suggestion. **Confidence:** weak. **Affected:** frequent traders.

The indexed excerpt says a trade confirmation "doesn't really help, because it is identical and appears for every trade, so after a while you just automatically accept", and suggests showing it only when the price is wrong and the trade is not private.

**Why it matters:** a safety confirmation that fires on every action stops being a safety check. The complaint is about **attention**, not about the market's rules.

**Uncertainty:** one player, no corroboration, and the excerpt may omit context. It is not evidence that confirmations are absent or that players routinely mis-trade.

### 7.5 Trade-activity display confusion

**Finding:** `PWR-026`. **Source:** `PWS-014` (2014). **Class:** single-source player suggestion, historical. **Confidence:** weak. **Affected:** players reading another nation's history.

The indexed excerpt describes a specific confusion: a player saw a food trade for 2,000 food and could not tell from the display how the money and food sides related. The thread is titled "Rework how Trade Activity is displayed".

**Why it matters:** a public history is only useful if a reader can tell which side gave what. The observed 2026 table has explicit Selling/Buying Nation and Offer/Return columns, which may already address the 2014 complaint. The finding is therefore **historical**, not a current defect.

**Uncertainty:** the 2014 interface is not the 2026 interface. The current table was observed and is clearer; the old complaint should not be presented as current.

### 7.6 Restrictions can be difficult to understand and can burden legitimate players

**Finding:** `PWR-016`, `PWR-017`. **Sources:** `PWS-004`, `PWS-001`. **Class:** community statement + official rule; the burden is a **researcher interpretation**. **Confidence:** moderate for the rules; weak for the burden. **Affected:** new players, households, shared networks, students, co-workers.

The community FAQ says nations on the same network "cannot interact in-game in any way" and that many restrictions are mechanically imposed; it offers verification as the removal path. It also says new nations under 30 days cannot buy outside ±30% of the average price. The official rulebook confirms the one-nation rule and the same-network restrictions.

**Why it matters:** a legitimate household or shared student network is treated as restricted until reviewed. The rules are published, but the practical effect is that ordinary trades can be blocked or price-limited for reasons unrelated to the player's intent.

**Uncertainty:** the FAQ is a community page and may lag. The research found no player complaint thread about the burden, so the burden is an interpretation of the rule, not a documented experience.

### 7.7 Price information may be over-trusted or misunderstood

**Finding:** `PWR-012`. **Sources:** `PWS-005`, `PWS-015`, `PWS-018`. **Class:** community wiki + two player discussions. **Confidence:** weak to moderate. **Affected:** new players, casual players.

The average is computed at the end of the day and (per players) only from global-market trades. It therefore excludes alliance and private deals and lags the current book. A player who treats it as a live quote may misprice an offer.

**Why it matters:** the interface presents an average next to a live-looking index; the difference between "average yesterday" and "best offer now" is not visible in the data collected.

**Uncertainty:** no source shows a player actually mispricing because of this. The finding is an information-design risk, not a documented complaint.

### 7.8 The market may require frequent checking

**Finding:** `PWR-018`, `PWR-004`. **Sources:** `PWS-001`, `PWS-003`. **Class:** researcher interpretation. **Confidence:** weak. **Affected:** casual players, players in different time zones.

Because offers are manual and automated trading is prohibited, a player who wants the best price must browse repeatedly. The rulebook explicitly permits read-only notification scripts, which suggests a demand for alerts without automating the trade.

**Why it matters:** a manual board plus an anti-automation rule can reward players who can check often, even though the offers themselves are asynchronous.

**Uncertainty:** no player in the sources says "I must check too often". The finding is an inference from the rule and the offer model. It should not be presented as a confirmed frustration.

### 7.9 Thin market and volatility — not established

**Finding:** `PWR-030` is not used for this claim. No source in this research establishes that the Politics & War market is thin, illiquid or unusually volatile. The observed ten-day price range for one resource (71–85 per unit) is **one nation's trades**, not a market index, and cannot support a volatility claim. Any such claim is an **unverified hypothesis** and is left to a future study with volume data.

### 7.10 Fees — no complaint found, no rule found

**Finding:** `PWR-010`. No source reached documents a trade fee, and no player complaint about a fee was found. This is **not** evidence that no fee exists. The report does not list "excessive fees" as a weakness because the research cannot establish that fees exist at all.

---

## Section 8 — Systemic causes and trade-offs

This section separates the **confirmed mechanics** from the **interpretation** of why they produce the reported experiences.

### 8.1 Offer honesty versus failed acceptance

**Mechanic:** offers appear to be pledges, not reservations (§4.3). **Benefit:** a player can post an offer without locking stock, so the offer does not dead-lock inventory that might be needed for production or another sale. **Cost:** a taker can click an offer that cannot settle, producing the 2015 failure report.

**Interpretation:** this is the central trade-off of the observed model. Reserving at posting makes every displayed offer good but freezes inventory; not reserving keeps inventory fluid but makes the book partly aspirational. Politics & War appears to have chosen fluidity plus re-validation. The research does not establish whether that choice was deliberate.

**For Nation Supremacy:** this is exactly the question D-016 already answers for **directed offers** — an offer does not reserve, and acceptance re-validates both sides. Prompt 07B must decide whether a *listing* is the same object or a different one. The research supplies the cost of the no-reservation choice, not the answer. `PWR-005`, `PWR-022`

### 8.2 Manual acceptance versus matching efficiency

**Mechanic:** a taker chooses an offer; no automatic matching is documented. **Benefit:** the taker keeps control, the system is simple, and no algorithm has to price a trade. **Cost:** crossed offers can persist, and a player may not get the best price without browsing.

**Interpretation:** a manual board is a **relationship market** as much as a price market. It rewards attention and negotiation, and it makes every trade a visible bilateral act. An automated book would improve price discovery but would also remove the taker's choice and create a new class of matching rules (priority, self-match, restricted pairs).

**For Nation Supremacy:** the existing design distinguishes directed, private trade from a gated listing market (D-017, REQ-010). The research suggests that if a listing market is built, the choice between manual acceptance and automatic matching is a **design-defining** one, not an implementation detail. `PWR-002`, `PWR-023`

### 8.3 Transparency versus strategic exposure

**Mechanic:** completed trades are public per nation; averages are public. **Benefit:** price discovery, accountability, visible manipulation. **Cost:** competitors can infer supply relationships, stockpiles and military preparation.

**Interpretation:** the transparency is consistent with a game whose social layer is public alliances and wars; hiding every trade would protect privacy but weaken the social record. The trade-off is a posture choice, not a bug.

**For Nation Supremacy:** D-017 already chooses **parties-only** terms with no public offer book at first playable, and D-027 requires k = 5 for aggregates. The Politics & War posture is the opposite on both counts. Prompt 07B must not import it without acknowledging that it would require superseding D-017. `PWR-013`

### 8.4 Daily averages versus live prices

**Mechanic:** averages are end-of-day and (per players) global-market-only. **Benefit:** a stable, hard-to-manipulate reference. **Cost:** lag, exclusion of private/alliance trades, and possible over-trust.

**Interpretation:** a daily average is a **reference**, not a settlement price; it is closer to a published statistic than to a quote. That is a defensible choice for a game that wants price context without a live ticker.

**For Nation Supremacy:** B-04's reference prices are **book values**, not market prices (ECN-027), and D-017 keeps terms private. If Prompt 07B wants a public reference, it must decide whether it is a book value, a daily average, or something else, and how it relates to ECN-027/ECN-109's fair-value gap. `PWR-011`, `PWR-012`

### 8.5 Caps versus legitimate multi-price trading

**Mechanic:** a 2022 staff direction caps active offers at 3 buy + 3 sell per resource. **Benefit:** less spam, a more readable board, less scattershot price posting. **Cost:** a trader cannot post a ladder of prices for one resource; the cap may bind on legitimate market-making.

**Interpretation:** the cap is a **visibility** control, not an economic one. It treats the board as a shared attention resource. The optimal number is not established; the 2022 post is a proposal, not a measured result.

**For Nation Supremacy:** D-024 requires every subsystem to declare a visible limit. If a listing market is built, an offer cap is one candidate; the research gives no evidence for a specific number. `PWR-024`

### 8.6 Price bands versus legitimate new players

**Mechanic:** ±30% band for new nations and flagged networks. **Benefit:** makes starter-bundle farming and sweetheart pricing less profitable. **Cost:** a legitimate new player cannot accept a genuinely unusual price, and a household cannot trade at market if flagged.

**Interpretation:** the band is a **targeted** control: it applies to the populations most likely to be used for transfer, not to everyone. It is paired with interaction bans and verification, not used alone. The community FAQ presents it as anti-farming, which is a credible rationale.

**For Nation Supremacy:** B-03's ONB-031/ONB-032 already require a fresh-nation **one-sided transfer** restriction with a fair-value band, and B-04's ECN-208 assigns the band and window to Prompt 07. The Politics & War band is evidence of a structure (a percentage around a published average) and a rationale, not a value to copy. `PWR-016`, `PWR-019`

### 8.7 Multiple channels versus fragmentation

**Mechanic:** global, alliance and private surfaces. **Benefit:** trust-level choice, alliance coordination, private deals. **Cost:** the public average excludes two of the three surfaces, so the visible price is a partial price; liquidity is split; and a player must know which channel to use.

**Interpretation:** multiple channels are a **social** feature that makes the market less legible as a single price. That is acceptable if the game values relationships over price discovery, and costly if it values a single reference price.

**For Nation Supremacy:** the existing design has directed private trade and a possible gated listing market; it does **not** have an alliance market. Whether to add one is Prompt 09's/Gate work, not 07A's. `PWR-001`, `PWR-012`

### 8.8 Immediate settlement versus a shared turn

**Mechanic:** Politics & War appears to settle on acceptance, not at a fixed turn boundary. **Benefit:** a trade completes when both parties act, with no wait. **Cost:** for a game with a two-hour global turn, immediate settlement would introduce a second clock and a latency advantage.

**Interpretation:** this is the **largest structural difference** between the reference and Nation Supremacy. Politics & War's market assumes a live, always-on economy; Nation Supremacy's economy resolves on a shared boundary (B-02 P4). A direct copy of acceptance-time settlement would conflict with B-02's action classes and reservation rules.

**For Nation Supremacy:** Prompt 07B must decide whether a market action is class Q (queued to the boundary), immediate-with-record, or a hybrid. The research shows what immediate settlement feels like, not whether it fits Nation Supremacy. `PWR-007`

### 8.9 Who is affected

| Player group | Likely exposure (interpretation) | Evidence |
|---|---|---|
| New players | Price band; advice to sell raw resources; possible confusion at a failed acceptance; less price history to judge | `PWS-004`, `PWS-010`, `PWS-020` |
| Established/wealthy nations | Can post large offers and absorb failed attempts; may dominate visible supply | `PWS-003` (one nation's volume), interpretation |
| Casual players | Asynchronous offers help; manual browsing and no automation may disadvantage | `PWS-003`, `PWS-001` |
| Highly active players | Can browse and re-post more often; caps limit laddering | `PWS-008`, interpretation |
| Economic specialists | Specialisation and arbitrage are possible; public history reveals positions | `PWS-020`, `PWS-003`, interpretation |
| Militarily focused players | Depend on munitions/steel/fuel; blockades can cut trade | `PWS-012` (weak), interpretation |
| Shared-network households | Interaction ban and ±30% band until verification | `PWS-001`, `PWS-004` |
| Alliance members | Alliance market and bank; internal trust lowers search cost | `PWS-011`, `PWS-012` |

**Caution:** the table is a **researcher interpretation**. The sources do not measure how each group experiences the market. It is included to stop a later reader from treating "the market" as a single player experience. `PWR-016`…`PWR-019`

---

## Section 9 — Cross-system relationships in Politics & War

This section describes relationships the sources support. It does not claim Nation Supremacy has or should have the same relationships.

### 9.1 Production and specialisation

The historical community guide describes six continents, each producing three of six resources, and advises a new nation to extract resources and sell them on the market (`PWS-020`). The current trade page prices eleven resources (`PWS-002`). The guide is marked **Obsolete**, and its six-resource geography is **historical**, so it cannot be used as a description of the current resource system (`PWR-021`).

What survives as a structural observation is simpler: the game exposes a set of resources with market prices, and a nation that produces more of one than it consumes can sell the surplus. Whether the current game enforces geography, distance or a resource-endowment map was **not established**. The observed 86 trades are consistent with nations selling a single resource in large lots for money (`PWS-003`), which is the behaviour a specialisation model predicts.

**Interpretation:** trade is the mechanism that turns a production advantage into money and turns money into missing inputs. That is a design relationship, not a measured outcome.

### 9.2 Treasury and money

Every observed trade has a money return (`PWS-003`). The market is therefore a **money sink and source at the level of an individual trade**: the buyer's money becomes the seller's money, while the resource moves the other way. The market page also lists **Credits**, a premium currency, alongside resources (`PWS-002`), and the 2022 staff post explicitly excludes Credits from the per-resource offer cap (`PWS-008`). Credits are not an ordinary material and should not be compared with one.

No source establishes a trade fee, a money-creation effect or a tax on trades. The research cannot say whether the market is money-neutral beyond the two-sided transfer.

### 9.3 War, blockades and embargoes

The 2014 official announcement introduces **embargoes**: a nation adds another to its embargo list and the two cannot trade with each other on the global market (`PWS-016`). The current site still lists **Embargoes** in the world menu (`PWS-002` observation of the navigation), which is consistent with the feature surviving, but the announcement itself is historical. `PWR-014`

A 2018 player answer says a blockaded nation's trade "does not work in any way. No global market, no alliance market, no personal trade offers" (`PWS-012`). This is a **single-source player answer**, not an official rule, and it is included only as a reported relationship. If accurate, a blockade is a total trade cut, not a price penalty. `PWR-015`

The observed trade page and rulebook do not document how war demand affects prices. The historical guide mentions military preparation and resource demand in general terms, but no price series was collected. Any claim that war raises munitions or steel prices in Politics & War is an **unverified hypothesis** for this report.

### 9.4 Alliances and alliance banks

The official rulebook says same-network nations may be in the same alliance but may not declare wars on the same nations, and that using **Alliance Banks** to evade trade restrictions is a bannable offence (`PWS-001`). The 2022 announcement distinguishes **shared alliance markets** from the global market (`PWS-011`). The community FAQ says flagged same-network nations cannot use alliance banks to transfer funds to each other (`PWS-004`).

Taken together, the evidence supports an alliance layer with its own market and bank, and a rule that treats the bank as a value-transfer surface that must not become a laundering route around trade restrictions. That is a **structural** relationship; the implementation is not observed. `PWR-001`, `PWR-017`

### 9.5 New-player progression

The historical guide advises new nations to extract resources and sell them to larger nations (`PWS-020`). The community FAQ says new nations under 30 days face the ±30% band, explicitly to prevent a new nation from being created to trade away its money (`PWS-004`). The official rulebook separately prohibits new nations from sending all or most of their money and resources (`PWS-001`).

**Interpretation:** the market is part of the new-player economy — it is how a small nation converts raw output into cash — and it is also the most obvious route for starter-value farming. The band and the transfer rule are two different controls on the same route: one prices the trade, the other restricts the gift. `PWR-016`, `PWR-019`, `PWR-020`

### 9.6 Information ecosystem

The trade page publishes a current index, per-resource averages and a history link (`PWS-002`, `PWS-005`). The official API exposes a trade-price endpoint, though the request without a key returned `{"success": false, "general_message": "Invalid API key."}` (`PWS-021`). The rulebook permits scripts that **notify** a player of prices if the trade is completed manually, while prohibiting automated trading (`PWS-001`).

**Interpretation:** Politics & War has an information layer around the market — averages, history, API, notification tools — that is separate from execution. That layer lowers the cost of price discovery without automating the trade. It is a plausible model for a browser game that wants an informed market without bots. `PWR-011`, `PWR-018`, `PWR-029`

### 9.7 Integrity and enforcement

The official rules join several controls: one nation per person, same-network interaction restrictions, a fairness rule against new-nation value dumping, an anti-automation rule, and a ban on account selling and real-world trades (`PWS-001`). The community FAQ adds the ±30% band and the verification path (`PWS-004`). The 2022 staff post adds offer caps for spam (`PWS-008`).

**Interpretation:** integrity is treated as a **portfolio** of identity, interaction, price and attention controls, not as a single detector. No source claims the portfolio is complete; the rulebook's own moderation section reserves discretion. `PWR-017`, `PWR-018`, `PWR-019`, `PWR-024`

### 9.8 What is not established

No source establishes: trade volumes; the share of the economy that is traded; the effect of trade on growth; the effect of war on prices; the frequency of failed acceptances; the number of active offers; the distribution of offer sizes; the share of trades that are private or alliance-internal; or the revenue (if any) the market generates. These are not small omissions; they are the difference between a structural description and an economic measurement.

---

## Section 10 — Relevance to Nation Supremacy

**This section does not design Nation Supremacy's market.** Each item separates what Politics & War establishes, why it may matter, how the two games differ, and what Prompt 07B must decide. No item is a recommendation, and no item overrides an existing decision.

### 10.1 Market shape: posted offers, order book or hybrid

- **Findings / sources:** `PWR-001`, `PWR-002`, `PWR-003`; `PWS-002`, `PWS-003`, `PWS-007`, `PWS-008`, `PWS-009`.
- **What the research establishes:** Politics & War's global market is a posted-offer board with manual acceptance; a separate alliance market and private trades also exist. No automatic matching engine is documented, and a 2019 player states there is none.
- **Player need / design concern:** a small, browser-based world needs a market that is legible to a new player, works when few people are online, and does not require a matching engine to be useful.
- **Potential relevance:** the posted-offer shape is the closest evidenced reference to Nation Supremacy's already-approved directed trade (Report 07 §10.2; ECON-013). A listing market could be an extension of that object rather than a new exchange.
- **Key difference:** Nation Supremacy has no public offer book at first playable (D-017) and a listing market is gated behind G-1…G-6 (REQ-010). Politics & War's global book is public and central. Nation Supremacy's economy also resolves on a two-hour boundary, not continuously.
- **Prompt 07B questions:** Is the first market a private directed offer, a public listing, or both? If both, is the listing the same object as a directed offer or a distinct one? Does the gate permit designing the listing now while keeping it inactive?
- **Confidence:** moderate for the reference; the Nation Supremacy question is open by design.

### 10.2 Execution: manual acceptance versus automatic matching

- **Findings / sources:** `PWR-002`, `PWR-006`, `PWR-023`; `PWS-007`, `PWS-009`, `PWS-003`.
- **What the research establishes:** the taker selects an offer; crossed buy/sell offers can coexist; no price-time priority, partial-fill rule or self-match rule is documented.
- **Player need / design concern:** a taker wants the best available price without reading every offer; a maker wants a fair chance of being filled; the operator wants a deterministic, cheap-to-run execution path.
- **Potential relevance:** manual acceptance preserves player choice and avoids a matching engine, but it reproduces the crossed-book inefficiency. Automatic matching improves price discovery but creates priority, self-match, restricted-pair and determinism problems that a 2-hour boundary would have to settle.
- **Key difference:** Nation Supremacy's existing pair matrix blocks a market match with a restricted account at the match point (D-034 row 4). An automatic matcher must evaluate that before reserving; a manual taker check is simpler but must still block the pair.
- **Prompt 07B questions:** Does a taker choose a specific offer, or does the system execute against the best offer? If the latter, what is the priority rule, how are ties broken, and how are restricted pairs excluded without leaking their existence?
- **Confidence:** moderate for the reference; the Nation Supremacy choice is open.

### 10.3 Reservation at posting

- **Findings / sources:** `PWR-005`, `PWR-022`; `PWS-010`, `PWS-008`, `PWS-009`.
- **What the research establishes:** the evidence is consistent with **no reservation at posting**: a clicked offer can fail because the counterparty lacks resources or cash. No official rule states this, and the report labels the mechanism as an interpretation.
- **Player need / design concern:** a displayed offer should be credible; a seller should not have inventory frozen by an offer nobody accepts; a buyer should not reserve money for a trade that may never happen.
- **Potential relevance:** Nation Supremacy already has a reservation model for accepted actions (B-02 TR-067…070), and D-016 says a **directed offer** does not reserve. A listing is a different object and could have a different rule, but that would be a new decision, not an inherited one.
- **Key difference:** B-04's ledger and B-02's reservation rules are stricter than the apparent Politics & War behaviour; ECN-211 requires both legs or neither and a shared `transfer_id`. Nation Supremacy cannot copy "no reservation and hope the acceptance works" without deciding what happens to a failed acceptance in its ledger.
- **Prompt 07B questions:** Does a listing reserve the committed side at posting? If not, what does the UI promise? If yes, how is the reservation released on cancel/expiry, and how does it interact with warehouse and treasury reservations? Does D-016 need a scoped amendment for listings, or does its wording already cover them?
- **Confidence:** weak for the reference mechanism; the Nation Supremacy question is a genuine open design choice.

### 10.4 Settlement timing

- **Findings / sources:** `PWR-007`, `PWR-004`; `PWS-003`, `PWS-002`.
- **What the research establishes:** Politics & War appears to settle at acceptance, not at a fixed turn boundary; offers wait for a taker.
- **Player need / design concern:** a trade should complete predictably; a player should not have to be online at a boundary; a global turn game should not let connection speed decide who gets a bargain.
- **Potential relevance:** Nation Supremacy's whole economy is boundary-resolved (B-02 P3/P4). A market that settles immediately would be a second clock and would complicate reservation, idempotency and the "no presence" guarantee.
- **Key difference:** Politics & War's apparent immediate settlement is not compatible with B-02's action classes without a decision. B-02 classifies directed-trade acceptance as **Q** (queued until boundary) and the trade relationship as settling at P4.
- **Prompt 07B questions:** Is a market acceptance immediate-with-record, queued to P4, or a hybrid (reserve now, settle at P4)? What does the player see between acceptance and settlement? How does a boundary failure release both legs?
- **Confidence:** moderate for the reference; the Nation Supremacy question is constrained by B-02.

### 10.5 Price information and a public reference

- **Findings / sources:** `PWR-011`, `PWR-012`; `PWS-002`, `PWS-005`, `PWS-015`, `PWS-018`.
- **What the research establishes:** Politics & War publishes a current index, end-of-day per-resource averages and a 60-day history; players say the average covers the global market only.
- **Player need / design concern:** a new player needs a sense of "normal" before accepting a price; a trader needs to compare offers of different sizes; the operator needs a reference that is hard to manipulate.
- **Potential relevance:** Nation Supremacy already has **reference prices** as book values for accounting (ECN-027), not market prices. A market reference would be a different number and must not be confused with book value.
- **Key difference:** D-017 keeps trade terms parties-only and there is no public offer book at first playable; D-027 requires k = 5 for any aggregate. A public average is therefore a **gate-stage** feature, not a first-playable one.
- **Prompt 07B questions:** Is any price information public at first playable? If a reference is published later, is it a daily average, a book value, or a band? How is it labelled so a player does not treat it as a quote? Does it feed the fair-value band, and if so, how is manipulation handled?
- **Confidence:** strong for the reference display; the Nation Supremacy choice is open and constrained by D-017.

### 10.6 Multiple channels

- **Findings / sources:** `PWR-001`; `PWS-011`, `PWS-012`, `PWS-015`.
- **What the research establishes:** global, alliance and private trade surfaces coexist; the public average excludes the latter two (per players).
- **Player need / design concern:** alliances want internal supply; allies want private deals; the world market wants a public price.
- **Potential relevance:** Nation Supremacy has directed private trade and a possible gated listing market, but **no alliance market**. An alliance market would be a new subsystem with its own permissions, bank interaction and audit rules.
- **Key difference:** Nation Supremacy's D-034 pair matrix already restricts alliance-bank use for flagged pairs; an alliance market would need the same pair checks. Prompt 09 owns alliances, not Prompt 07.
- **Prompt 07B questions:** Does Prompt 07 design only the global/directed layer and leave an alliance market to Prompt 09? If an alliance market is mentioned, is it explicitly out of scope? How are private and public trades distinguished in the ledger?
- **Confidence:** moderate for the reference; scope is a project decision for 07B/09.

### 10.7 Offer limits and spam

- **Findings / sources:** `PWR-024`; `PWS-008`.
- **What the research establishes:** staff proposed/announced a cap of 3 active buy and 3 active sell offers per resource to reduce trade spam; implementation and current value are unverified.
- **Player need / design concern:** a readable board; a fair chance for a new offer to be seen; freedom to post a price ladder.
- **Potential relevance:** D-024 requires every subsystem to declare a visible limit; a listing market without an offer cap can be spammed. The reference gives a candidate structure (per-resource active offer cap) but no validated number.
- **Key difference:** Nation Supremacy's free-first infrastructure and smaller population make a fixed cap more consequential; a cap tuned for a large live market may be too tight or too loose.
- **Prompt 07B questions:** Is there a per-nation offer cap? Per resource or total? What happens at the cap — refuse, or replace the oldest? Is the cap visible before posting? What evidence would set the number in Prompt 14?
- **Confidence:** moderate for the announced policy; weak for the number.

### 10.8 Fresh-nation band and transfer window

- **Findings / sources:** `PWR-016`, `PWR-019`; `PWS-004`, `PWS-001`.
- **What the research establishes:** Politics & War applies a **±30%** band around the average market price to new nations under 30 days (buying) and same-network-flagged nations (buying and selling), and separately prohibits new nations from sending all or most of their money and resources.
- **Player need / design concern:** a new player must be able to trade legitimately; the starter bundle must not become a transfer to another account; a household must not be punished forever for sharing a network.
- **Potential relevance:** B-03 ONB-031/ONB-032 already requires a fresh-nation **one-sided transfer** restriction with a fair-value band and a window; B-04 ECN-208 assigns the band and window to Prompt 07. The reference supplies a structure (percentage around a published average) and a rationale, not a value.
- **Key difference:** Nation Supremacy's band must work without a public market price at first playable; its `reference price` is a book value (ECN-027). The band could therefore be defined against the book value, but that is a Prompt 07B decision. Nation Supremacy's window is already provisionally 30 days/360 turns.
- **Prompt 07B questions:** What is the band's base — book value, last trade, or a published average? What is the band width? Is it symmetric? Does it apply to both sides of a trade? How is a legitimate new-player trade at a genuinely unusual price handled? What is the review threshold?
- **Confidence:** moderate for the reference; the Nation Supremacy values are explicitly open.

### 10.9 Account and network pair restrictions

- **Findings / sources:** `PWR-017`; `PWS-001`, `PWS-004`.
- **What the research establishes:** one nation per person; same-network nations may not interact, including sweetheart trades and third-nation routing; using alliance banks to evade trade restrictions is bannable.
- **Player need / design concern:** prevent collusive value transfer without banning households; keep ordinary trade open for unrelated players.
- **Potential relevance:** Nation Supremacy already has a five-state pair model and a verb matrix (D-034) that blocks directed trade and market matching between restricted pairs, and allows public market participation with third parties. The research corroborates the **shape** of that policy.
- **Key difference:** Nation Supremacy blocks the pair **before reservation** and records the attempt (NET-029); Politics & War's rules are published but their mechanical coverage is not documented. Nation Supremacy's one-account rule is already fixed; this research does not reopen it.
- **Prompt 07B questions:** Does the market check the pair at posting, at acceptance, at settlement, or all three? What does a blocked taker see? How does the market avoid revealing that a specific counterparty is restricted? Are alliance-market and private-trade paths covered by the same check?
- **Confidence:** strong for the reference rules; Nation Supremacy's matrix already decides the policy.

### 10.10 Public trade history and privacy

- **Findings / sources:** `PWR-013`; `PWS-003`.
- **What the research establishes:** completed trades are public per nation, with counterparties and unit prices.
- **Player need / design concern:** accountability and price discovery versus strategic privacy.
- **Potential relevance:** Nation Supremacy's D-017 chooses the opposite posture for terms (parties-only) and D-027 requires k = 5 for aggregates. A public per-trade history would contradict D-017 unless it is superseded.
- **Key difference:** Politics & War's public history is tied to its public global market; Nation Supremacy's first-playable trade is directed and private. A public history is a **gate-stage** question, not a first-playable default.
- **Prompt 07B questions:** What does each party see after a trade? Is the existence of a trade public even if the terms are not? Does an aggregate need k = 5? Is a counterparty's identity ever disclosed without consent?
- **Confidence:** strong for the reference; Nation Supremacy's visibility rule is already decided by D-017.

### 10.11 Anti-automation and notification tools

- **Findings / sources:** `PWR-018`, `PWR-029`; `PWS-001`, `PWS-021`.
- **What the research establishes:** automated trading and banking are prohibited; read-only price-notification scripts are allowed; a trade-price API exists but requires a key.
- **Player need / design concern:** a level playing field versus accessibility for players who cannot watch the market.
- **Potential relevance:** Nation Supremacy's fairness rules will need an automation posture, and its free-first API surface may or may not expose prices.
- **Key difference:** Nation Supremacy has no public market price at first playable (D-017), so a price-notification tool has nothing public to read until the gate. Its enforcement design belongs to Prompt 12, not 07B.
- **Prompt 07B questions:** Does the market expose any read-only feed? Is a notification tool allowed? Does the answer depend on the gate? What rule prevents a script from completing a trade while still allowing an alert?
- **Confidence:** strong for the reference rule; Nation Supremacy's posture is open.

### 10.12 Fees

- **Findings / sources:** `PWR-010`; `PWS-001`, `PWS-002`, `PWS-004`.
- **What the research establishes:** no fee is documented in the sources reached; the absence is not proven.
- **Player need / design concern:** a fee can fund operations, damp repetitive transfer, or deter wash trading; it also taxes ordinary trade and is regressive on small deals.
- **Potential relevance:** Nation Supremacy's Stage 1 fee policy is explicitly deferred to the gate (ECON-016, G-5), and ECN-211 requires that a trade never create or destroy value **except an explicit fee**. Prompt 07B must either keep the fee at zero or decide a structure; it must not import a Politics & War rate, because none was established.
- **Key difference:** Nation Supremacy's directed trade is approved as **fee-free** at first playable; a listing fee would be a gate-stage decision.
- **Prompt 07B questions:** Is the first-playable fee zero? Is a listing fee a gate-stage question? If a fee exists later, is it fixed, proportional or none, and what ledger entry records it? Does the fee apply to the buyer, the seller, or both?
- **Confidence:** unknown for the reference; the Nation Supremacy question is explicitly deferred.

### 10.13 Free-first data volume

- **Findings / sources:** `PWR-003`, `PWR-013`; `PWS-003`.
- **What the research establishes:** a public trade history stores counterparties, dates, quantities, returns and statuses per trade; a nation's page can show 86 offers.
- **Player need / design concern:** history is useful, but every offer and trade is a row that must be written, read and retained.
- **Potential relevance:** Nation Supremacy has a free-first write budget and a retention policy (D-026), plus a per-nation-turn digest cost. A market that writes several rows per offer, acceptance and settlement could dominate the write budget at scale.
- **Key difference:** Politics & War's infrastructure is not Nation Supremacy's, and its scale is not measured here. No inference about Nation Supremacy's capacity follows from Politics & War's history page.
- **Prompt 07B questions:** What is the minimum row set for an offer, an acceptance and a settled trade? Which rows are permanent audit records and which are compactable? What is the read pattern for a market list, and can it be bounded? What must Stage 3 measure before a listing market is enabled?
- **Confidence:** strong for the reference shape; capacity is an open measurement task.

### 10.14 New-player price literacy

- **Findings / sources:** `PWR-012`, `PWR-022`, `PWR-020`; `PWS-005`, `PWS-010`, `PWS-020`.
- **What the research establishes:** the game publishes averages and a history, but a failed acceptance and an end-of-day average can both mislead a new player; the historical guide advises selling raw resources.
- **Player need / design concern:** a new player needs to know what a fair price looks like and why a trade failed, without a finance education.
- **Potential relevance:** Nation Supremacy's onboarding and explanation contract (B-02's digest, B-04's reports) already require visible causes and no silent loss. A market must explain a rejected or failed trade in the same voice.
- **Key difference:** Nation Supremacy can show a **book value** as a stable anchor from day one, whereas Politics & War's anchor is a daily market average. The two are not the same number and must not be labelled the same way.
- **Prompt 07B questions:** What does a new player see as a price anchor? How is a failed trade explained? Is the anchor labelled "book value" or "market average"? Does the UI show the difference between a reference and a live offer?
- **Confidence:** moderate for the reference; the Nation Supremacy requirement is already implied by B-02/B-04.

---

## Section 11 — Research findings register

Every row is one claim. `Class` uses the labels in §2.4. `Strength` uses §2.5. A row with `Unknown` strength is a research gap, not a negative finding.

| ID | Feature or issue | Class | Strength | Sources | Verified claim or labelled interpretation | Status | Relevance to Nation Supremacy | Open question |
|---|---|---|---|---|---|---|---|---|
| PWR-001 | Three trade surfaces | Corroborated player experience + official announcement excerpt | Moderate | PWS-011, PWS-012, PWS-015 | A global market, a shared alliance market and private trades are referred to as separate surfaces; deleting a global-market offer does not affect the other two. | Likely current; not directly observed | A future scope choice: global only, or also alliance/private | Are all three still live, and do they share one ledger or three? |
| PWR-002 | Global market is a posted-offer board | Historical behaviour + corroborated structure | Moderate | PWS-007, PWS-009, PWS-003, PWS-008 | Players either accept another nation's offer or post their own; a 2019 player states there is no automatic matching module; the record is an offer/return/status table. | Current structure likely; 2019 claim historical | The closest evidenced reference to a manual offer market | Is there any automatic crossing at all, and is it documented anywhere? |
| PWR-003 | Offer shape and display | Verified interface observation | Strong | PWS-003 | An offer shows a resource quantity, a money return and a per-unit figure; every observed row satisfies return = quantity × unit price. | Current on 2026-10-28 | Suggests quantity + total + unit price as a legible presentation | Does the form take a total or a unit price first? |
| PWR-004 | Offers persist until accepted | Verified interface observation | Moderate | PWS-003 | Accepted rows carry a later timestamp; one offer was posted 10/19 and accepted 10/23; the page shows 86 offers. | Current sample | Asynchronous offers reduce the need for simultaneous presence | Is there a maximum lifetime, default expiry or auto-cancel? |
| PWR-005 | No reservation at posting | Single-source player report + interpretation | Weak to moderate | PWS-010, PWS-008, PWS-009 | A clicked offer can fail for insufficient resources or cash; this is consistent with offers being pledges, not reservations. No official rule states it. | Historical report; mechanism inferred | Directly relevant to D-016 and to whether a listing is a different object | Does a posted offer reserve anything, and what happens on a failed acceptance? |
| PWR-006 | Matching priority, partial fills, expiry | Unverified hypothesis | Unknown | PWS-003, PWS-009 | No documented price-time priority, partial-fill rule, self-match rule or expiry rule was found; observed rows are whole offers. | Undocumented | 07B must not cite Politics & War as having a published matching policy | Can a taker accept part of an offer? Are crossed offers matched? Do offers expire? |
| PWR-007 | Settlement timing | Researcher interpretation from interface | Moderate | PWS-003, PWS-002 | The public record shows `Accepted` with an acceptance timestamp and no pending state; this is consistent with settlement at acceptance, not at a fixed boundary. | Current inference | A key difference from Nation Supremacy's P4 boundary | Is settlement atomic and immediate, and can an accepted trade be reversed? |
| PWR-008 | Per-resource active-offer cap | Official staff post (announced policy) | Moderate for announcement; weak for current | PWS-008 | Staff proposed/announced at most 3 active buy and 3 active sell offers per resource, Credits unaffected, and polled whether a fourth posting should auto-delete the oldest. | 2022 policy; implementation unverified | A candidate shape for a visible offer limit under D-024 | Did the cap ship, at what value, and with which overflow behaviour? |
| PWR-009 | Delete a global-market offer | Official announcement (indexed excerpt) | Moderate | PWS-011 | A player can delete a trade offer; the change affects global-market trades only, not private trades or shared alliance markets. | 2022; current likely | A cancel path is part of any offer lifecycle | Is deletion immediate, blocked after acceptance, or fee-bearing? |
| PWR-010 | Trade fees | Unverified hypothesis | Unknown | PWS-001, PWS-002, PWS-004 | No trade fee, listing fee or percentage was found in the rulebook, trade page, FAQ or forum material reached. Absence is not proof. | Unknown | 07B must decide a fee structure rather than copy one | Is a fee displayed on the create-offer screen or deducted from the return? |
| PWR-011 | Public price information | Verified interface observation | Strong | PWS-002, PWS-005 | The trade page shows a Current Market Index, per-resource Average Prices and a link to average-price history. | Current on 2026-10-28 | Price context before a trade; a possible gate-stage reference | What exactly does the index measure, and how is it computed? |
| PWR-012 | Average computation | Community wiki + player discussions | Moderate for end-of-day; weak to moderate for global-only | PWS-005, PWS-015, PWS-018 | Averages are measured at the end of each day and a 60-day history exists; players say the average covers global-market trades only. | Community claim; may lag | A published reference would need a declared base and scope | Is the average a simple mean, a volume-weighted mean, or a trimmed value? |
| PWR-013 | Public per-nation trade history | Verified interface observation | Strong | PWS-003 | A logged-out visitor can see a nation's 86 offers with counterparty, alliance, date, quantity, return, unit price and status. | Current on 2026-10-28 | Transparency and strategic exposure are both real | Is every trade public, or only global-market trades? |
| PWR-014 | Embargoes | Verified official rule (historical announcement) | Moderate | PWS-016, PWS-006 | An embargo list prevents two nations from trading with each other on the global market. | 2014; feature still in the site menu | A diplomacy trade control belongs to Prompt 08 | Does an embargo also block the alliance and private channels? |
| PWR-015 | Blockades and trade | Single-source player report | Weak | PWS-012 | A player answer says a blockaded nation's trade does not work in any way: no global, alliance or personal offers. | 2018; unverified | A war-time trade cut is Prompt 10's question | Is a blockade a total trade ban, and does it block incoming offers too? |
| PWR-016 | ±30% trade band | Community statement | Moderate | PWS-004 | New nations under 30 days cannot buy outside ±30% of the average market price; same-network-flagged nations face the band on buying and selling. | May lag the live game | B-03/ECN-208 require a band and window; this is a structural reference | Is the band computed from the daily average or the current best offer? |
| PWR-017 | One account and same-network restrictions | Verified official rule | Strong | PWS-001, PWS-004 | One nation per person; same-network nations may not interact, including sweetheart trades and third-nation routing; verification can restore interaction. | Current official rule | Corroborates D-018/D-034's shape; no reopening | How are same-network pairs detected, and what is the appeal path? |
| PWR-018 | Anti-automation | Verified official rule | Strong | PWS-001 | Automated trading and banking are prohibited; scripts that only notify a player of prices are allowed if the trade is manual. | Current official rule | 07B must not assume bots; Prompt 12 owns enforcement | Where is the line between an alert and an automated acceptance? |
| PWR-019 | New-nation value transfer | Verified official rule | Strong | PWS-001 | New nations may not send all or most of their money and resources; nations created to send value are a serious violation. | Current official rule | B-03 ONB-031 already restricts one-sided transfers; this corroborates the harm | How is "all or most" measured, and is it a rule or a review signal? |
| PWR-020 | Trade and early growth | Historical community guide + interface | Weak to moderate | PWS-020, PWS-003 | The guide advises new nations to extract resources and sell them; the observed trades are large single-resource lots for money. | Historical guide; current behaviour consistent | Supports specialisation as a design goal, not a rule | Is selling raw output still the recommended early path? |
| PWR-021 | Geographic resource distribution | Historical behaviour | Weak | PWS-020 | A historical guide describes six continents each producing three of six resources. The wiki marks the guide Obsolete and the current price row has eleven resources. | Historical only | A mapless game cannot copy this; it is a contrast, not a model | Did the current game retain any geography or distance in trade? |
| PWR-022 | Stale offers fail at acceptance | Single-source player report | Weak to moderate | PWS-010 | Clicking a global-market offer can return insufficient resources or insufficient cash, repeatedly. | 2015; may have changed | The main documented cost of a no-reservation offer board | Does the failure message say which side failed, and is the offer removed? |
| PWR-023 | Crossed offers | Single-source player report | Weak | PWS-009 | Because there is no automatic matching module, buy offers can sit above sell offers. | 2019; historical | The main documented efficiency cost of manual acceptance | Can a taker always see the best opposite offer, or only a page of offers? |
| PWR-024 | Trade spam | Official staff post | Moderate | PWS-008 | Staff opened a discussion to reduce trade spam and cap active offers per resource. | 2022; implementation unverified | A visible limit is required by D-024; the number is not | What cap protects readability without blocking legitimate price ladders? |
| PWR-025 | Confirmation fatigue | Single-source player suggestion | Weak | PWS-013 | An identical confirmation on every trade leads players to accept automatically; the author suggests showing it only for a wrong price and non-private trades. | 2022; one player | A safety confirmation must be informative, not routine | Which trades need a confirmation, and what should it show? |
| PWR-026 | Trade-activity display confusion | Single-source player suggestion | Weak | PWS-014 | A 2014 player could not tell from the trade-activity display how the food and money sides of a trade related. | 2014; the 2026 table is clearer | Public history must state which side gave what | Does the current display resolve the 2014 complaint? |
| PWR-027 | Price comparison against the market | Single-source player post | Weak | PWS-017 | A player declines a private price because it is "cheaper than that on the global market". | Undated; one post | Players use the global market as a reference even in private deals | How often do private deals track the global price? |
| PWR-028 | Official market framing | Verified interface observation | Strong | PWS-002 | The trade page describes the market as "live, laissez-faire". | Current on 2026-10-28 | A stated design posture: minimal intervention | Is "laissez-faire" a rule or marketing language? |
| PWR-029 | Trade-price API | Verified interface observation | Strong | PWS-021 | A trade-price API endpoint exists and returns `Invalid API key` without a key. | Current on 2026-10-28 | An information layer can exist without an execution API | What does the endpoint return with a key, and is it official or partner-only? |
| PWR-030 | Players seek trading guidance | Single-source title/snippet | Weak | PWS-019 | A Reddit thread asks for "the top ingame trading strategies"; the page was login-blocked, so only the title is evidence. | 2023; title only | Suggests trading is non-obvious to some players; not proof of a defect | What do experienced players actually recommend? |

### 11.1 Findings deliberately not claimed

- **No liquidity claim.** No volume, depth, spread, fill rate or time-to-fill data was collected.
- **No fee claim.** No fee is documented, but no source proves the absence of one.
- **No prevalence claim.** No player report is treated as a majority view; no percentage is invented.
- **No balance claim.** The observed price range is one nation's trade history, not a market index.
- **No current-geography claim.** The six-continent guide is obsolete and is labelled historical.
- **No implementation claim.** No interface action was taken, so no settlement, cancellation or failure was reproduced.

---

## Section 12 — Research gaps and uncertainties

### 12.1 Features and rules that could not be established

| Unknown | Why it matters | What would resolve it | Current status |
|---|---|---|---|
| Create-offer form fields and order of input (quantity, total, unit price) | Determines whether an offer is a unit-price order or a total-value bargain | Authenticated read-only inspection of the create-offer screen; official help page | **Unverified** — form behind sign-in |
| Reservation at posting | Determines whether a displayed offer is credible and whether stock/money is frozen | Official rule; authenticated observation of the offer screen and a failed acceptance | **Unverified** — only a 2015 player report, interpreted |
| Partial fills | Determines whether a taker can buy part of an offer and how the remainder is handled | Authenticated acceptance flow; official rule | **Unknown** |
| Price-time priority or any matching rule | Determines who gets filled when offers compete | Official rule or a controlled test | **Unknown** — a 2019 player says there is no matching module |
| Self-match and same-nation match | Determines whether a player can trade with an alt or a second nation | Official rule; controlled test | **Unknown** |
| Expiry | Determines whether an old offer is still good | Official rule; authenticated observation | **Unknown** — offers persist for days in the sample |
| Fees | Determines the real cost and whether a trade creates or destroys value | Official rule; create-offer screen; trade history | **Unknown** — no fee found |
| Rounding and precision | Determines the exact total and whether fractions exist | Official rule; form observation | **Unknown** — display is integer-consistent |
| Minimum and maximum order size | Determines whether small or large trades are possible | Official rule; form observation | **Unknown** |
| The exact current active-offer cap | Determines whether the 2022 policy shipped and at what value | Official changelog; authenticated observation | **Unverified** — 2022 staff post only |
| Which trades feed the average | Determines whether the published price is a global-market price or a whole-market price | Official documentation; player corroboration | **Weak to moderate** — players say global only |
| Whether the average is volume-weighted or simple | Determines how representative it is | Official documentation | **Unknown** |
| Alliance-market mechanics | Determines whether there is a third price and a third settlement path | Official rule; authenticated observation | **Unknown** |
| Private-trade mechanics | Determines whether a private trade is an offer/accept flow, a gift, or a settlement | Official rule; authenticated observation | **Unknown** |
| Blockade effect on each channel | Determines whether war can cut all trade | Official rule | **Weak** — one player answer |
| Whether the ±30% band is current and how it is computed | Determines whether the reference band is a live constraint | Official rule; current FAQ | **Moderate** — community wiki may lag |
| Whether Credits are tradeable like a resource | Determines whether a premium currency is a market asset | Official rule | **Unknown** — the price row lists Credits, the cap excludes them |

### 12.2 Conflicting or incomplete accounts

1. **"No automatic matching" (2019) versus a modern offer board (2026).** The two are consistent, but the 2019 statement is player-authored and seven years old. The report treats manual acceptance as the best-supported structure, not as a proven current rule. `PWR-002`, `PWR-023`
2. **2014 tutorial versus the 2026 interface.** The tutorial describes two paths; the 2026 page shows a much larger resource row and a public history. The interface has clearly changed, so the tutorial is used only for the two-path model. `PWR-002`, `PWR-021`
3. **Obsolete geography versus the current resource row.** The wiki guide's six-continent, three-of-six model cannot describe an eleven-resource price row. The guide is marked Obsolete; the report labels the geography **historical only**. `PWR-021`
4. **Public history versus private/alliance trades.** If the public history includes every trade, then private and alliance terms are not actually private. The 2022 announcement says deletion affects global-market trades only, which suggests the history may be global-only or may mix surfaces. The research could not resolve this. `PWR-001`, `PWR-013`
5. **The 2022 cap: discussion or rule?** The thread is a staff discussion with a poll, not a changelog. The report records the policy direction and refuses to present the number as current. `PWR-008`

### 12.3 Inaccessible sources

| Source | Access result | Effect on the report |
|---|---|---|
| Fandom wiki rendered HTML (`PWS-004`, `PWS-005`, `PWS-020`) | HTTP **403** on the rendered page | Retrieved the same pages' **wikitext** via `?action=raw`; content is the wiki's own, not a search cache. |
| Official forum topic bodies (`PWS-007`…`PWS-018`, `PWS-022`) | Page shell returned; reply bodies are loaded dynamically; only the title and meta-description/indexed excerpt were available | Claims from these sources are limited to the visible excerpt and labelled accordingly. Full-thread context (including corrections later in the thread) was not read. |
| Reddit thread (`PWS-019`) | Login wall | Only the title/snippet is used; no claim about its content beyond the title. |
| Official trade API (`PWS-021`) | `Invalid API key` | Confirms the endpoint exists; no price data retrieved. |
| Authenticated trade interface | No access to the owner's Chrome session | The create-offer form, cancel flow, fees, partial fills and failure messages were not observed. |

### 12.4 Consequence of the missing authenticated session

The single largest limitation is the inability to inspect the signed-in market. As a result:

- the report cannot say whether a **reservation** is shown at posting;
- it cannot say whether a **partial acceptance** is offered;
- it cannot say whether a **fee** is displayed or deducted;
- it cannot distinguish a **buy offer** screen from a **sell offer** screen;
- it cannot reproduce a **failed acceptance** or a **cancellation**;
- it cannot verify the **current** offer cap or the current ±30% band.

These are **evidence gaps**, not findings that the features are absent. A later research pass with read-only authenticated access could close most of them in an hour.

### 12.5 What would most improve the next study

1. A read-only, authenticated walkthrough of the create-offer, accept-offer, cancel-offer and trade-history screens, with screenshots or field lists, and **no state-changing action**.
2. The current official help page or changelog for trade, if one exists.
3. A controlled test of a failed acceptance (for example, an offer whose seller has since spent the goods), if it can be done without harming another player.
4. A volume sample across several nations and resources, to replace the one-nation history with a market-level description.
5. A current statement on the active-offer cap and the ±30% band from an official source.

---

## Section 13 — Source register

All URLs were requested on **2026-10-28**. `Type` distinguishes official, community and player-generated material. `Limitation` records what the source cannot establish.

| ID | Title | URL | Date | Type | Supports | Limitation |
|---|---|---|---|---|---|---|
| PWS-001 | Game Rules — Politics & War | https://politicsandwar.com/rules/ | Undated; current page read 2026-10-28 | Official rulebook | Rules 1 (one nation), 2 (same-network restrictions, bank evasion), 3 (fairness in trading/banking), 8–9 (automated trading/banking), 11 (account selling), 12 (real-world transactions) | Rules describe policy, not mechanics; enforcement is moderator-discretionary |
| PWS-002 | Trade — Politics & War | https://politicsandwar.com/nation/trade/ | Read 2026-10-28 | Official game page, logged out | "Buy and sell resources in the live, laissez-faire global market"; Current Market Index; per-resource Average Prices; history link; resource row including Credits | Order form behind sign-in; index definition not shown |
| PWS-003 | Nation trade activity (public page; nation anonymised here) | https://politicsandwar.com/nation/id=798501&display=trade | Observed 2026-10-28; trades dated 10/16–10/27/2026 | Official public interface | Columns: Selling Nation, Buying Nation, Date Offered, Offer, Return, Status; 86 offers; `Accepted` timestamps; per-unit figures | One nation's history, not a market sample; logged-out view; no fee column observed |
| PWS-004 | Frequently Asked Questions — Politics and War Wiki | https://politicsandwar.fandom.com/wiki/Frequently_Asked_Questions?action=raw | Undated; read 2026-10-28 | Community wiki | One account/nation; same-network "cannot interact in-game in any way"; sweetheart trades and third-nation routing prohibited; ±30% band for under-30-day and flagged nations; verification path | Community-maintained; may lag; not official |
| PWS-005 | Average Prices — Politics and War Wiki | https://politicsandwar.fandom.com/wiki/Average_Prices?action=raw | Undated; read 2026-10-28 | Community wiki | Averages shown on the trade menu; measured at the end of each day; 60-day history page; dates are calendar dates | Community-maintained; no formula; old price examples are historical |
| PWS-006 | Category:Mechanics of Trade — Politics and War Wiki | https://politicsandwar.fandom.com/wiki/Category:Mechanics_of_Trade | Read 2026-10-28 | Community wiki category | At access, the category contained only **Average Prices** and **Embargoes** | The wiki's trade coverage is thin; absence of a page is not absence of a mechanic |
| PWS-007 | How to Trade Resources — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/2973-how-to-trade-resources/ | Published 2014-10-07 | Official-forum tutorial (historical) | Indexed excerpt: two options — accept another nation's trade deal from the market, or post your own offer | Body not rendered; 2014 tutorial; may describe an older interface |
| PWS-008 | Restricting Market Trades — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/33081-restricting-market-trades/ | 2022-04-28 | Official staff post | At most 3 active buy and 3 active sell offers per resource; Credits unaffected; poll on auto-deleting the oldest offer | Staff discussion/poll, not a changelog; implementation unverified; body only partially visible |
| PWS-009 | Market Improvements — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/24708-market-improvements/ | 2019-01-30 | Player suggestion | Indexed excerpt: "Presently, the game has no automatic matching module, which means it is possible for there to be buy offers above the value of the current sell offers" | Single player; 2019; body not rendered |
| PWS-010 | Trade — InSufficient Resources or Cash — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/8078-trade-insufficient-resources-or-cash/ | 2015-08-20 | Player report | Clicking a global-market offer can yield "this nation has insufficient resources" or "insufficient cash"; reported as recurring | Single player; 2015; body not rendered; no failure rate |
| PWS-011 | Content Announcement: Smaller updated, larger update — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/33099-content-announcement-smaller-updated-larger-update/ | 2022-05-02 | Official staff announcement | Indexed excerpt: a trade offer can be deleted; this does not affect private trades or shared alliance markets, only global-market trades | Body not rendered; exact rule text not visible; date from topic |
| PWS-012 | Question about Blockades, Taxes and allocating Alliance treasury — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/22908-question-about-blockades-taxes-and-allocating-alliance-treasury-to-others/ | 2018-04-06 | Player Q&A | Indexed excerpt: a blockaded nation's trade "does not work in any way. No global market, no alliance market, no personal trade offers" | Single player answer, not official; body not rendered |
| PWS-013 | Trade improvements — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/33543-trade-improvements/ | 2022-08-21 | Player suggestion | Indexed excerpt: trade confirmation is identical for every trade and players automatically accept; suggest showing it only for a wrong price and non-private trades | Single player; body not rendered; not evidence of a defect |
| PWS-014 | Rework how Trade Activity is displayed — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/4431-rework-how-trade-activity-is-displayed/ | 2014 (exact day not visible) | Player suggestion | Indexed excerpt: confusion over how a 2,000-food trade and its money side were displayed | Single player; 2014 interface; body not rendered |
| PWS-015 | Creating More Accurate Average Trade Prices — Politics & War Forum | https://forum.politicsandwar.com/?app=core&module=system&controller=content&do=find&content_class=forums_Topic&content_id=10696&content_commentid=194504 | Undated | Player discussion | Indexed excerpt: the average tracks only the global market and does not factor in alliance-specific or personal trades | Player claim; undated; content-find URL rather than canonical topic page |
| PWS-016 | 9/17/2014 — Embargoes and Improvement Destruction — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/2839-9172014-embargoes-and-improvement-destruction/ | 2014-09-17 | Official announcement (historical) | An embargo list prevents two nations from trading with each other on the global market | 2014; may have changed; body not rendered |
| PWS-017 | Buying 1M food — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/29829-buying-1m-food/ | Undated | Player free-trade post | Indexed excerpt: a price is rejected because it is cheaper on the global market | Single post; undated; not a rule |
| PWS-018 | Question/suggestion about average trade price — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/2625-questionsuggestion-about-average-trade-price/ | 2014 | Player discussion | Indexed excerpt: the price moves per 1,000 units sold and only on the global market | Player belief, not official; 2014; body not rendered |
| PWS-019 | What are the top ingame trading strategies? — r/PoliticsandWar | https://www.reddit.com/r/PoliticsandWar/comments/18ufxnn/what_are_the_top_ingame_trading_strategies/ | 2023 ("2 years ago" relative to 2026) | Player community | Title shows players ask for trading strategies | **Login wall**; only the title/snippet was available; no content claims |
| PWS-020 | Fundamentals of Gameplay — Politics and War Wiki | https://politicsandwar.fandom.com/wiki/Fundamentals_of_Gameplay?action=raw | Undated; read 2026-10-28 | Community guide, marked **Obsolete** | Trade is a major international activity; six continents with three of six resources; new nations can sell raw output | Obsolete; historical geography; not a current rule |
| PWS-021 | Trade price API — Politics & War | https://politicsandwar.com/api/tradeprice/resource=coal | Read 2026-10-28 | Official API | Endpoint exists; without a key returns `{"success": false, "general_message": "Invalid API key."}` | No data without a key; response shape with a key unknown |
| PWS-022 | Giving Colors Some Power Over the Market — Politics & War Forum | https://forum.politicsandwar.com/index.php?/topic/2753-giving-colors-some-power-over-the-market/ | 2014 | Player suggestion | Indexed excerpt discusses cartels and player-set minimum or maximum trade prices | 2014; single player; body not rendered; not evidence that cartels exist |

---

## Section 14 — Handoff to Prompt 07B

### 14.1 What Prompt 07B inherits

Prompt 07B is the **market-foundations design** stage. It must decide Nation Supremacy's market structure and rules, using this report as evidence and the existing Stage 2 documents as binding constraints. **Prompt 07A has approved no Nation Supremacy market rule.** It has not chosen a market model, a reservation rule, an execution rule, a fee, a price band, an offer cap, a settlement timing or a tradable-resource list. Nothing in this report may be cited as an approved mechanic.

### 14.2 Strongest verified or well-corroborated findings

1. Politics & War's global market is a **posted-offer board with manual acceptance**, not a documented automatic matching engine (`PWR-002`, `PWR-006`; strong-to-moderate).
2. An offer is a **quantity for a money return**, with the **unit price** displayed; the public record is consistent with `return = quantity × unit price` (`PWR-003`; strong interface).
3. **Offers persist** and can be accepted hours or days later; the sample has no observed expiry (`PWR-004`; moderate).
4. A clicked offer can **fail for insufficient resources or cash**, which is consistent with **no reservation at posting** (`PWR-005`, `PWR-022`; weak-to-moderate, historical).
5. The game publishes a **current index, per-resource averages and a 60-day history**; the averages are end-of-day and, per players, global-market-only (`PWR-011`, `PWR-012`; strong display, moderate computation).
6. **Completed trades are public per nation**, with counterparties and unit prices (`PWR-013`; strong interface).
7. Trade is governed by **account- and network-level rules**, not only price: one nation per person, same-network interaction bans, a ±30% band for new/flagged nations, a new-nation transfer rule, and an anti-automation rule (`PWR-016`…`PWR-019`; strong for the official rules, moderate for the band).
8. **Three surfaces** are referred to — global, alliance and private (`PWR-001`; moderate).
9. **No fee is documented** in the sources reached (`PWR-010`; unknown, not a proven absence).
10. **Matching priority, partial fills, self-match and expiry are undocumented** (`PWR-006`; unknown).

### 14.3 Positive design lessons to consider (as questions, not rules)

- **One-sentence teachability.** Can a new player be told "take an offer or make one" and understand the market? (`PWR-002`)
- **Show quantity, total and unit price together.** Does the offer row let a player compare different sizes without arithmetic? (`PWR-003`)
- **Let offers wait.** Does a trade require both players online, or can it complete asynchronously? (`PWR-004`)
- **Give price context before the trade.** Is there a stable, clearly labelled reference, and is it distinguishable from a live quote? (`PWR-011`, `PWR-012`)
- **Make the record legible.** Can a player see what happened, which side moved, and why a trade failed? (`PWR-013`, `PWR-026`)
- **Separate trust levels.** Is there a place for a private deal, an alliance deal and a world offer, without confusing the three? (`PWR-001`)
- **Keep integrity in layers.** Is the market protected by identity, pair, price and attention controls together, rather than one detector? (`PWR-017`…`PWR-019`, `PWR-024`)

### 14.4 Best-supported frustrations to design against

1. **A displayed offer that cannot settle.** The strongest documented failure. A taker clicks and is told the other side has nothing. (`PWR-022`)
2. **Crossed offers and no matching.** A buyer and seller can both be on the book at compatible prices and not trade. (`PWR-023`)
3. **Trade spam and offer caps.** Staff treated unconstrained posting as a readability problem. (`PWR-024`)
4. **Confirmation fatigue.** A safety prompt that fires on every trade becomes noise. (`PWR-025`)
5. **Display ambiguity.** A public history is only useful if the two sides of a trade are unambiguous. (`PWR-026`)
6. **Restriction friction.** A legitimate household or new player can be blocked or price-limited by a rule aimed at abusers. (`PWR-016`, `PWR-017`)

**Do not overstate these.** Items 1, 2, 4 and 5 are single-source; item 3 is an official staff direction without a verified current rule. None is a measured prevalence.

### 14.5 Trade-offs Prompt 07B must hold together

| Choice | What it buys | What it costs | Evidence |
|---|---|---|---|
| Reserve at posting vs re-validate at acceptance | Credible offers vs fluid inventory and money | Failed acceptances vs frozen stock | `PWR-005`, `PWR-022` |
| Manual acceptance vs automatic matching | Player control and simplicity vs price discovery and fill efficiency | Crossed book and browsing vs priority/self-match complexity | `PWR-002`, `PWR-023` |
| Public price/history vs parties-only | Discovery and accountability vs strategic privacy | Manipulation visibility vs information leakage | `PWR-012`, `PWR-013` |
| Daily average vs live quote | Stable reference vs timeliness | Lag and exclusion vs manipulability | `PWR-011`, `PWR-012` |
| Offer cap vs open posting | Readable board vs freedom to ladder prices | Spam control vs legitimate market-making | `PWR-024` |
| Price band vs free pricing | Anti-farming vs legitimate unusual trades | Protection vs friction | `PWR-016`, `PWR-019` |
| Immediate settlement vs boundary settlement | Instant completion vs one shared clock and fairness | A second clock vs a wait | `PWR-007` |
| Multiple channels vs one book | Trust and relationships vs a single price | Fragmentation and a partial average | `PWR-001` |

### 14.6 Existing Nation Supremacy documents Prompt 07B must read first

Read these in this order, and treat them as authoritative over anything in this report:

1. [DECISIONS.md](../../DECISIONS.md) — especially D-016 (directed offers do not reserve; re-validate and settle atomically), D-017 (parties-only terms; no public offer book at first playable), D-024 (declared, visible action limits), D-026 (retention), D-027 (k=5 aggregates), D-034 (pair matrix, including rows 3, 4 and 19), D-039 (reroll and unsettled trades).
2. [B-02 — core gameplay loop and turn system](../07_core_gameplay_loop_symbolic_world_and_turn_system.md) — P0–P7, class Q, TR-067…TR-072 (reservation, available balance, income vs obligations), TR-051/TR-060 (re-validation), TR-043/TR-078 (phase failure and recovery).
3. [B-03 — account, nation, reroll and network policy](../09_account_onboarding_nation_creation_and_progression.md) — ACC-001…ACC-016, NET-014…NET-043 (especially NET-029 and the §5.5 matrix), RRL-013…RRL-031, ONB-031/ONB-032 (fresh-nation one-sided transfer rule; provisional 30 days/360 turns; band to be specified).
4. [B-04 — economy, resources, treasury and finances](../10_economy_resources_treasury_and_finances.md) and its [formula register](../10_economic_formula_and_balance_register.md) — the 11-resource roster, ECN-023…ECN-029, ECN-099 (sales and purchases are transfers), ECN-105/106 (austerity, no debt), ECN-109 (fair-value gap), ECN-147a (maintenance order), ECN-158 (deterministic inputs), ECN-191 (hoarding), ECN-207/208 (starter farming; band and window are Prompt 07's), **ECN-211** (the Prompt 07 contract), ECN-227 (limitations).
5. [B-05 — cities, infrastructure, production and research](../11_cities_infrastructure_production_and_research.md) and its [formula register](../11_city_infrastructure_production_and_research_formula_register.md) — warehouse capacity and `planned_batches = M + A ≤ C`, because a purchase must fit storage.
6. [B-06 — population and domestic politics](../12_population_and_domestic_politics.md) §36 — **DMP-262 is a binding market contract**: while `leadership_state` is `TRANSITION` or `CRISIS`, the player may **read** the market and may **not create, accept or cancel** a trade offer or a reservation; existing accepted trades settle normally. 06B imposes no trade tax, tariff, embargo or market fee, and Prompt 07 may not reuse the political stability term for one.
7. [Stage 1 Report 07 §10](../../stage-1/07_economy_design_and_market_structure.md) — the directed-first decision, the G-1…G-6 gate and its six conditions, the fee comparison and the G-5 deferral, and the R-19 atomic-pair / zero-partial invariant.
8. [Requirements register](../03_requirements_traceability.md) — REQ-009 (directed trades validate, settle atomically, are idempotent), REQ-010 (listing market only after the gate), REQ-087 (reroll abuse controls).
9. [Stage 1 Report 08](../../stage-1/08_security_privacy_fair_play_and_trust.md) — trade-related abuse threats, evidence retention and the disclosure posture.

### 14.7 Economic and accounting issues that must be reconciled, not assumed

1. **D-016 versus a listing.** D-016 says a directed offer does not reserve; acceptance re-validates both sides and the transfer is reserved and settled atomically. If a listing reserves at posting, that is a **new object with a new rule**, not an application of D-016. Prompt 07B must state which object it is designing and whether D-016 needs a scoped amendment.
2. **D-017 versus any public book or public price.** D-017 says no public offer book exists at first playable and terms are parties-only. A public board, a public average or a public per-trade history would contradict it unless the gate has passed and D-017 is formally superseded.
3. **REQ-010's gate.** A listing market is **Deferred** until G-1…G-6 pass. Prompt 07B may design the listing foundation, but it must not present it as first-playable, and it must not claim the gate has passed. The gate evidence does not exist.
4. **ECN-211's contract.** A trade must settle at **P4**, both legs or neither, must not change a P3 result, must check the buyer's warehouse space, must write `TRADE_BUY`/`TRADE_SELL` with a shared `transfer_id`, and must not create or destroy value except an explicit fee.
5. **Reservation and the three-figure balance.** B-02 TR-067…TR-069 requires total/reserved/available. A market that holds funds or goods must show the hold and release it exactly once on failure, cancellation or expiry.
6. **Austerity and no debt.** B-04's no-debt rule means a buyer cannot settle with money it does not have; a partial settlement is not allowed. A failed trade must leave both sides unchanged.
7. **Book value versus market value.** ECN-027's reference prices are book values, not market prices. ECN-109's fair-value gap is an accounting estimate. A market price, a daily average and a book value are three different numbers and must not share a label.
8. **The fair-value band and the fresh-nation window.** B-03 ONB-031/ONB-032 and B-04 ECN-208 assign both to Prompt 07. The band needs a base (book value, last trade or an average), a width, a symmetry rule and a review threshold. The window is provisionally 30 days/360 turns. Prompt 07B must decide the band; Prompt 14 validates it.
9. **The pair matrix.** D-034 blocks a directed trade with a restricted pair at offer/accept/settle and blocks a market match at the match point; row 19 allows public market participation with unrelated accounts. The market must check the pair **before reservation**, record the attempt, and not reveal the restriction to the counterparty.
10. **Reroll.** D-039 says a reroll is blocked by an unsettled accepted settlement; offers are withdrawn and accepted trades must settle or cancel first. The market must expose a pre-reroll check.
11. **Retention and aggregates.** D-026's hot/summary/permanent classes and D-027's k = 5 apply to any published market aggregate. The market's own history is a class-P candidate only where it is an audit record; ordinary offers are compactable.
12. **The free-first budget.** Every offer, acceptance, settlement, cancellation and expiry is a write. Stage 3 must measure the row count and read pattern before a listing market is enabled; Prompt 07B should state the minimum row set and what can be bounded.
13. **The political-state contract.** DMP-262 (B-06 §36) freezes **new** market actions during `TRANSITION` and `CRISIS`: read-only, no create/accept/cancel, and existing accepted trades still settle. The market must expose that state without presenting it as a sanction, and it must not add a trade tax, tariff, embargo or fee that reuses the political stability term.

### 14.8 Decisions that must remain open until Prompt 07B

Prompt 07A deliberately does **not** answer any of the following:

- the market model (directed only, listing, hybrid, order book, other);
- whether a listing reserves at posting;
- whether execution is immediate, boundary-settled or hybrid;
- whether matching is manual or automatic, and if automatic, its priority and tie rules;
- whether partial fills are allowed;
- whether offers expire and on what terms;
- the fee posture and any rate;
- the offer cap and its overflow behaviour;
- minimum/maximum order sizes and price increments;
- which of the eleven resources are tradeable, and in which direction;
- whether Credits, military goods or political assets are tradeable;
- whether an alliance market exists and who owns its rules;
- the fair-value band's base, width and review threshold;
- the public/private visibility of offers, trades and aggregates;
- the exact settlement order inside P4 and the failure codes;
- the anti-automation and notification posture (Prompt 12 also has a stake);
- the market's row set, retention and read model;
- any numeric value at all.

### 14.9 Unresolved research questions to carry forward

1. Does a posted Politics & War offer reserve anything, and what exactly happens on a failed acceptance? (`PWR-005`, `PWR-022`)
2. Can a taker accept part of an offer, and does the remainder stay open? (`PWR-006`)
3. Is there any automatic crossing or priority rule, now or historically? (`PWR-002`, `PWR-023`)
4. Do offers expire, and is there a maximum lifetime? (`PWR-004`, `PWR-006`)
5. Is there a trade fee, and how is it displayed and accounted? (`PWR-010`)
6. Did the 2022 per-resource offer cap ship, at what value, and with which overflow rule? (`PWR-008`)
7. Is the ±30% band current, and is it computed from the daily average or the live book? (`PWR-016`)
8. Are the alliance and private surfaces still live, and do they share the global price? (`PWR-001`, `PWR-015`)
9. Does a blockade stop all three channels? (`PWR-015`)
10. How are same-network pairs detected and cleared, and what does a legitimate household experience? (`PWR-017`)
11. What does the trade-price API return with a key? (`PWR-029`)

### 14.10 Handoff checklist for Prompt 07B

- [ ] Read the nine documents in §14.6 before drafting.
- [ ] State the market object being designed (directed offer, listing, both) and its relationship to D-016/D-017.
- [ ] State the gate status honestly: REQ-010 is **Deferred**, G-1…G-6 have **not** passed.
- [ ] Reconcile every settlement rule with B-02 P4 and B-04's ledger/no-debt rules.
- [ ] Reconcile every price with ECN-027's book value and ECN-109's fair-value gap.
- [ ] Decide the fair-value band and the fresh-nation window, or explicitly leave them open with a named owner and validation method.
- [ ] Check the pair matrix before every reservation, including a market match.
- [ ] Declare every visible limit under D-024 (offer cap, order size, rate).
- [ ] Declare what is public, what is parties-only and what is an aggregate under D-027.
- [ ] Declare the minimum row set and the retention class of each record.
- [ ] Do not claim implementation, runtime testing, balance or gate passage.
- [ ] Do not begin Prompt 07C or production code.

### 14.11 Document control

| Item | Value |
|---|---|
| Prompt | Stage 2, Prompt 07A — Politics & War trade-system research |
| Version | 1.0 |
| Created | 2026-10-28 |
| Research access date | 2026-10-28 |
| External game references | Politics & War only |
| Sources | `PWS-001`…`PWS-022` |
| Findings | `PWR-001`…`PWR-030` |
| Nation Supremacy rules approved here | **None** |
| Decision register changes | **None** |
| Requirement register changes | **None** |
| Next task at publication | **Prompt 07B — market foundations**, only after review and authorization (07B completed 2026-10-28; 07C is next) |

**End of report.**

