# Project evidence

Reviewed 22 October 2026 through connected GitHub access, actual source files, and the public Google Play listing. No unrelated repository was modified. These are implementation observations, not claims that another project's tests or live AI behavior were independently rerun.

## Selection

The account inventory returned 45 repositories, including course exercises, full stack applications and private projects. Shortlisted Cartograph, RidzTalk, Crop Health Assistant, Messaging App and Blog API. Read the README for each shortlist candidate, then inspected implementation for the selected projects. Course exercises and basic interfaces were not added merely to increase the project count. Private projects unrelated to the requested showcase were not investigated further.

Cartograph and RidzTalk provide complementary evidence in developer tooling and mobile delivery. Crop Health Assistant adds multimodal integration, a documented team contribution and a deployed product. A fourth project would add length with less distinct evidence. Messaging App and Blog API remain useful supporting repositories, particularly for conventional backend roles.

## Cartograph

Public source: [DannyRidz/Cartograph](https://github.com/DannyRidz/Cartograph).
Snapshot inspected: `c96ec55512f980cea461e3edbefb6d058390424c`.

- Problem: understand an unfamiliar public JavaScript or TypeScript repository and follow structural dependencies.
- Functionality: real import maps, incoming and outgoing traversal, coverage reporting, explanations and repository questions.
- Stack: Next.js, React, TypeScript, ts-morph, React Flow, dagre, Supabase Postgres and Realtime, Clerk, OpenAI, Managed Deep Agents, LangChain and LangSmith.
- Implementation: `lib/parser/parse.ts` creates source files with ts-morph, resolves modules through TypeScript configuration, and distinguishes resolved, external, excluded and unresolved imports. `lib/canvas/graph.ts` indexes and walks edges. `lib/agent/queries.ts` imports those same graph functions for lookup tools.
- Access: `supabase/migrations/20261022035500_agent_tool_grants.sql` enables row level security and restricts temporary grants to a completed analysis within the issuing organization. This supports the scoped access description, not a claim of independent security certification.
- Decision: calculate graph structure independently of a model, then explain the result. Report coverage gaps rather than guess connections.
- Preview: [public screenshot walkthrough](https://github.com/DannyRidz/Cartograph/tree/main/docs/showcase). The source explicitly states there is no public deployed service. The portfolio therefore links a walkthrough, not a live demo.
- Image: `docs/showcase/images/dependency-map.jpg`, copied unchanged from the pinned public snapshot. It shows saved Redux Toolkit parser output, not a new analysis or model call.
- Limits: public JS/TS source only; change impact means graph reachability, not predicted runtime failure. Recorded agent cases are a limited behavior sample, not a general accuracy score.

Sources: [README](https://github.com/DannyRidz/Cartograph/blob/main/README.md), [showcase and engineering decisions](https://github.com/DannyRidz/Cartograph/blob/main/docs/showcase/README.md), [parser](https://github.com/DannyRidz/Cartograph/blob/main/lib/parser/parse.ts), [shared graph traversal](https://github.com/DannyRidz/Cartograph/blob/main/lib/canvas/graph.ts), [agent queries](https://github.com/DannyRidz/Cartograph/blob/main/lib/agent/queries.ts).

## RidzTalk / PolyTalk

Public product: [RidzTalk on Google Play](https://play.google.com/store/apps/details?id=com.polytalk.app).
Public evidence: [RidzTalk showcase](https://github.com/DannyRidz/RidzTalk-showcase).
The production repository is private and was inspected through authorized connected access. No private source or credentials were copied into this portfolio.

- Problem: let two people speak across a language barrier without typing messages.
- Functionality: audio capture, source transcription, translation, spoken playback, language selection, account access and usage/subscription handling.
- Stack: private `package.json` and README confirm React, TypeScript, Vite, Tailwind, Capacitor, Supabase, OpenAI, RevenueCat, AdMob, Vitest and Testing Library.
- Implementation: `src/lib/realtimeSession.ts` tracks source and translation identities, validates session selection and builds translation instructions. `supabase/functions/create-realtime-session/index.ts` resolves identity, checks usage, rate limits requests and issues ephemeral provider credentials. Its main provider key is read from the server environment.
- Challenge: transcript and translation events arrive asynchronously. Pairing source and response identities avoids confusing conversation turns. The public showcase additionally explains queue reservations for out of order transcripts and provides an isolated runnable sample.
- Delivery: Android availability is verified by Google Play. Capacitor iOS and Android projects are present; an App Store release is not asserted.
- Source status: the public showcase is a case study and code sample, not the full production source. Public links point to it and Google Play.
- Image: the preexisting repository image came from Google Play. `ridztalk-preview.jpg` is a resized JPEG derivative of it, not a new app screenshot.
- Limits: current source can differ from the published store binary. Saved audio playback is not evidence of offline live translation. No latency, language accuracy, revenue or user impact figures are claimed.

Sources: original portfolio; inspected private README, manifest and files named above; [public technical case study](https://github.com/DannyRidz/RidzTalk-showcase/blob/main/README.md); [engineering decisions](https://github.com/DannyRidz/RidzTalk-showcase/blob/main/ENGINEERING.md); public Google Play product information.

## Crop Health Assistant

Public source: [DannyRidz/Crop-Health-Assistant](https://github.com/DannyRidz/Crop-Health-Assistant).
Snapshot inspected: `53022785c676e3b00e7e1993408f8dfaf510b53f`.
Public app: [coffee-leaf-check.web.app](https://coffee-leaf-check.web.app).

- Problem: help coffee farmers understand visible leaf changes and practical next checks.
- Contribution: the README explicitly credits Daniel with app development in team J2D, alongside Jeremiah Ewande as team leader and resource coordinator. The portfolio does not imply sole ownership of the team project.
- Stack: Next.js, React, TypeScript, the official Gemini SDK, Zod, sharp, pdf-lib, Firebase Hosting and Cloud Run. Manifest and source support these choices.
- Architecture: browser uploads and questions reach server routes; Gemini returns structured observations and tentative causes; a sourced regional catalogue constrains care suggestions; the device receives a downloadable PDF.
- Implementation: `src/lib/server/gemini.ts` validates structured model responses, restricts invented citations and unsupported certainty, and translates generated text into Tok Pisin. `src/lib/pdf.ts` implements reports. The README explains temporary processing rather than permanent case storage.
- Limits: coffee leaves only, tentative screening rather than confirmed diagnoses, no custom model training or measured disease accuracy. Broader agricultural evaluation remains pending.

Sources: [README and contributor credits](https://github.com/DannyRidz/Crop-Health-Assistant/blob/main/README.md), [Gemini integration](https://github.com/DannyRidz/Crop-Health-Assistant/blob/main/src/lib/server/gemini.ts), [report export](https://github.com/DannyRidz/Crop-Health-Assistant/blob/main/src/lib/pdf.ts).

## Skills and identity

Name, Brunei location, curriculum completion, previous industry background and career intent come from the supplied brief. Email, LinkedIn, GitHub and CV path are preserved from the original portfolio. No employment history, availability date or numeric outcomes were invented. Prisma, Express and JWT are also supported by the Blog API README; PostgreSQL and Express are supported by Messaging App documentation.

The only newly authored brand asset is the typographic `dm.` monogram. The social card and portfolio preview images describe this portfolio, rather than pretending to be product evidence.
