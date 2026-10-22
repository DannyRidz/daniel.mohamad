# Verification record

Executed 22 October 2026 against the local static site under its real repository subpath:
`http://127.0.0.1:8000/Project-Building-Your-Personal-Website/`.

## Results

| Check                     | Executed method                                                                                                | Result                                                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTML                      | html-validate 9.7.1, recommended rules plus the existing lowercase doctype and self closing void element style | Passed, no errors                                                                                                                                                                               |
| CSS                       | CSS Tree parser and declaration grammar matching                                                               | Passed, 121 top level rules, 481 declarations, no reported errors; variable dependent values resolved by the browser                                                                            |
| Static links and metadata | `python3 scripts/check_site.py`                                                                                | Passed, 29 link elements, 17 unique IDs, 2 project images; local files, anchor destinations, dimensions, social assets, canonical and Pages paths present                                       |
| Whitespace                | `git diff --check`                                                                                             | Passed                                                                                                                                                                                          |
| Responsive layouts        | Chromium through Playwright CLI, uncached loads at 320, 375, 390, 768, 1024, 1440 and 1920px                   | Document width equaled viewport width at all seven sizes                                                                                                                                        |
| Expanded notes            | All three native disclosures opened at 320px                                                                   | No horizontal overflow                                                                                                                                                                          |
| Touch targets             | Measured visible links and summaries at 320px with all notes open                                              | No targets below 44px in either dimension                                                                                                                                                       |
| Automated accessibility   | axe WCAG 2 A/AA and 2.1 AA tags at 1440px, 390px and 320px with expanded notes                                 | Each scan: 22 passed rules, zero violations, zero incomplete results                                                                                                                            |
| Keyboard                  | Tab to skip link, Enter to main; Enter and Space on all three disclosures                                      | Skip link focused main-content; all disclosures opened and closed                                                                                                                               |
| Internal navigation       | Clicked Work, About, Skills, Contact and Back to top                                                           | Correct hash destinations; script also confirms every local anchor target exists                                                                                                                |
| Focus                     | Browser inspected focused skip link                                                                            | Visible 3px focus outline and link within viewport; links and summaries share the focus rule                                                                                                    |
| Reduced motion            | Emulated reduced motion in Chromium                                                                            | Computed scrolling changed to auto; transitions disabled by the media rule                                                                                                                      |
| Local assets and CV       | Actual HTTP requests below the repository subpath                                                              | CSS, favicon, two project images, existing CV and social preview returned HTTP 200                                                                                                              |
| External links            | Redirect following GET requests                                                                                | GitHub profile, Cartograph source, walkthrough, evidence anchor page, public RidzTalk showcase, Crop Health Assistant source and app, Google Play and existing live portfolio returned HTTP 200 |
| LinkedIn                  | Automated HTTP request                                                                                         | HTTP 999, LinkedIn blocked automated access. Original user supplied profile URL retained; verify manually                                                                                       |
| Console and runtime       | Playwright console inspection and pageerror listener                                                           | Zero errors on the redesigned page; no page errors during final checks                                                                                                                          |
| Visual inspection         | Captured and viewed desktop and mobile layouts, tablet layout, phone preview and social card                   | Confirmed typography, project images, captions, wrapping, contact and section hierarchy                                                                                                         |
| Deployment compatibility  | Static serving at the repository subpath, relative link inspection                                             | Passed locally. No hosting settings, repository name, branch or workflow changes                                                                                                                |
| Content                   | Reconciled page with source files, documentation and the user brief                                            | Public/private source status, team contribution and project limits recorded in research.md                                                                                                      |

The axe script was injected only by the verification tool. It is not included in the delivered page. No JavaScript is required for navigation, disclosures or content.

## Issues found and fixed

- The browser reused the original dark stylesheet. Added a CSS query version and ran final checks with the browser cache disabled.
- Corrected figure caption ordering and removed unnecessary list labels flagged by HTML validation.
- Rewrote RidzTalk alternative text to match the actual promotional image rather than describing absent conversation messages.
- Increased narrow navigation and evidence links to at least 44px targets; adjusted mobile navigation spacing.
- Added the public RidzTalk technical showcase after discovering its separate case study repository. Production source remains private.

## Performance observations

The served RidzTalk image is 69,671 bytes, compared with 1,408,678 bytes for the original PNG, a reduction of about 95%. The unmodified original remains available for provenance but is not requested by the page. Cartograph's screenshot is 101,449 bytes. Both previews have explicit intrinsic dimensions, lazy loading and asynchronous decoding.

The HTML is about 23KB and the CSS about 16KB before transport compression. There are no runtime packages, remote fonts, analytics or application scripts. These are measured file sizes and implementation observations, not a Lighthouse score or a claim about real visitor latency.

## Evidence and reproducing checks

The repository includes current desktop and mobile preview images in `assets/images/`. Full desktop, mobile, tablet, expanded 320px and original screenshots plus the final browser check log are in local `output/playwright/` (ignored by Git). The browser checks used installed Playwright CLI and axe tools. HTML/CSS validators were installed temporarily under `/private/tmp/daniel-portfolio-validation`; no runtime dependencies or package manifest were added to this site.

You can repeat the dependency free checks with:

```sh
python3 scripts/check_site.py
git diff --check
```

Optional HTML validation:

```sh
npx --yes html-validate@9.7.1 index.html
```

See the README for serving both the root and the Pages subpath. The implementation plan's six acceptance criteria were covered by the checks above. All four build steps were implemented; no existing scope row was present to update.

## Limits

Browser checks ran in Chromium. Safari, Firefox, physical devices and a screen reader were not tested. Automated axe results do not establish complete WCAG conformance. No Lighthouse run, real network performance benchmark, AI accuracy evaluation, payment test, email delivery test or test suite from the featured applications was run. The existing resume was preserved, not rewritten. Remote publication and social crawler rendering remain untested until the owner approves deployment.

## Remaining recommendations, in priority order

1. Review the finished page and the existing CV together before approving publication. If the CV predates Cartograph or the public RidzTalk showcase, update it to match the verified projects. Publication has not been performed.
2. Manually open LinkedIn, then try keyboard and screen reader navigation in Safari or Firefox and on a physical phone.
3. After approved deployment, check the live Pages subpath, PDF and social image, and run Lighthouse on the hosted page. Measure before adding performance tools or dependencies.
4. Keep project evidence current. Replace the store promotional image with a recent application capture if one becomes available, and record any new outcomes only after they are measured.
