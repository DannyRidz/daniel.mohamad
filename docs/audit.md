# Portfolio audit and improvement plan

Reviewed 22 October 2026, starting from commit `51cabd0`.

## First impression

The original page explains Daniel's identity and contact options, but reads as a course portfolio rather than an engineering showcase. The only project is below the lengthy background and skills sections. A recruiter can identify technologies, but cannot quickly inspect architecture, decisions, source evidence, or Cartograph.

## Findings

| Area                     | Original evidence                                                                           | Priority and response                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Positioning              | Clear role and Brunei location; full name absent                                            | Keep the concise identity, add the full name in About and bring career intent forward       |
| Information architecture | About and a long skills list precede the single project                                     | P1: move selected work immediately after the introduction                                   |
| Project evidence         | Cartograph absent; RidzTalk has a feature list without decisions or source status           | P1: two detailed showcases with verified architecture, boundaries and direct evidence links |
| Visual design            | Uniform navy surfaces, similar text weights, generic rounded container                      | P2: deliberate white editorial grid, blue accent, strong type scale and section rules       |
| Typography               | Readable Arial; little distinction between introduction and supporting content              | P2: fluid Helvetica stack, narrower body measure and stronger heading hierarchy             |
| Responsive layout        | Existing 48rem breakpoint stacks header and project; 1080px app image served at small sizes | P2: inspect 320px to desktop; optimize image and retain visible navigation                  |
| Accessibility            | Good landmarks, skip link, alt text, focus styles and 44px link targets                     | Preserve these; add reduced motion support and test keyboard, contrast and disclosures      |
| Interaction              | Basic hover underline, no motion preference handling                                        | P3: small hover transitions, native case study disclosures; no required JavaScript          |
| Performance              | No scripts, fonts or package dependencies, but 1.3MB app screenshot                         | Preserve static delivery; resize image, lazy load previews and declare dimensions           |
| SEO and sharing          | Title and description exist; canonical, social preview and favicon absent                   | P2: add canonical, Open Graph, Twitter metadata and local favicon                           |
| Contact                  | Email, GitHub, LinkedIn and actual local CV available                                       | Keep all; expose resume in hero and display the email address                               |
| Maintainability          | Small readable source; duplicate body and h1 rules                                          | P2: consolidate CSS into tokens, shared layouts and explicit responsive rules               |
| Deployment               | Relative assets, static index, no deployment workflow tracked                               | Preserve repository subpath and hosting settings; no automatic publication                  |
| README                   | Useful startup steps; showcase and screenshot cover previous site only                      | Refresh screenshots, project descriptions, evidence, validation and deployment notes        |

## Implementation order

1. Verify actual repositories and record evidence and limitations.
2. Keep the static architecture and document the visual and content plan.
3. Build the complete introduction, projects, About, skills and contact journey.
4. Test real browser layouts, links, accessibility and metadata; fix findings.
5. Update README and record remaining recommendations. Leave deployment to the owner.

## Audience review

Software recruiters need source links and concrete application architecture before the skills inventory. AI recruiters need the distinction between parser facts and model output in Cartograph, and audio orchestration in RidzTalk. Clients need plain descriptions of what each application does, with a direct contact route. The new information order serves these three needs while keeping employment the primary goal.
