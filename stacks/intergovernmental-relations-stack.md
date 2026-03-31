# Intergovernmental Relations Stack

## Best for
Regional partnerships, state and federal legislative engagement, COG and MPO participation, interlocal agreements, and coordinated advocacy on legislation affecting the city.

## When to activate
Pull this stack when a state legislative session opens and bills affecting the city need tracking, when a regional COG or MPO agenda item requires a city position, when an interlocal agreement is being negotiated or renewed, when a federal agency comment period opens on a rule that affects city operations, or when the City Manager needs a coordinated intergovernmental strategy memo for Council.

## Combine
- Agent: `agents/executive-office/city-manager.md`
- Agent: `agents/departments/grants-and-intergovernmental-affairs-director.md`
- Agent: `agents/executive-office/assistant-city-manager.md`
- Prompt folder: `prompts/intergovernmental/`
- Skills: `legislative-tracker`, `kpi-dashboard-narrative`

## Sequence
1. **Grants/IGR Director agent + legislative-tracker** — at the start of each legislative session or when a significant bill is introduced, run the tracker to categorize bills by impact area, track status, and flag bills that need a city position. Attach the bill text and any league of cities or state association analysis.
2. **City Manager agent** — develop the city's position on priority bills. Attach the legislative tracker output and any prior Council resolutions or policy positions relevant to the subject matter. Draft a position letter or testimony outline.
3. **Assistant City Manager agent + kpi-dashboard-narrative** — for COG or MPO participation, prepare a data narrative showing the city's regional context (population, infrastructure investment, service levels) that supports the city's position in regional forums. Attach the relevant regional plan or study data.
4. **Grants/IGR Director agent** — for interlocal agreements, draft the scope, term, and financial framework sections. Attach the existing or model agreement, the service description, and any cost-sharing data. City Attorney review is required before negotiation.
5. **City Manager agent** — for federal comment letters or agency engagement, draft the city's comment. Attach the proposed rule or agency document, the city's operational data on the subject matter, and any prior correspondence with the agency.

## Watch for
- **Position without Council authorization**: City staff can analyze bills and flag impacts, but taking an official advocacy position typically requires Council direction. AI-drafted position letters should be clearly labeled as staff analysis or draft until Council has authorized the city's position.
- **Interlocal agreement scope creep**: Interlocal agreements drafted or expanded with AI assistance can accumulate obligations that exceed what either party's Council authorized. City Attorney should confirm that every material obligation in a draft agreement is within the city's legal authority and that the counterparty has equivalent authorization.
- **Legislative session speed**: State legislative sessions move fast. A bill can pass committee, floor, and conference in days. The legislative-tracker output needs to be refreshed frequently; a stale position memo can send staff to testify on a bill that has already been amended to remove the provision they are opposing.
- **Regional forum political dynamics**: COG and MPO decisions often reflect long-standing regional relationships and power balances that AI analysis cannot capture. Use the kpi-dashboard-narrative to build the factual case; rely on human relationship knowledge to read the room and time advocacy correctly.
