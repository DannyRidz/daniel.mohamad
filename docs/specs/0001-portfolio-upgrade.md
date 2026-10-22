# 0001. Portfolio presentation upgrade

**Date**: 2026-10-22
**Status**: Accepted
**Delivery**: Implemented and verified locally. Not published.
**Authorization**: The supplied brief delegates routine design and implementation decisions and requests completion without deployment.

## Summary

Keep the working static website and rebuild its presentation around verifiable projects. Visitors should understand Daniel's role quickly and reach evidence, resume and contact details without hunting through a long biography.

## Context

The existing HTML and CSS are sufficient for a content focused portfolio on GitHub Pages. There are no application data flows or client routing requirements. See [the original audit](../audit.md).

## Requirements

- **AC-1**: Introduce Daniel as a Brunei based full stack and AI application developer, with project, contact and resume actions.
- **AC-2**: Feature Cartograph and RidzTalk with verified implementation, preview images, source availability, technical decisions and appropriate public links.
- **AC-3**: Include concise About, categorized verified skills and working contact links. Additional projects must add distinct evidence.
- **AC-4**: Support 320px, mobile, tablet and desktop layouts without horizontal overflow, with keyboard navigation, visible focus, semantic headings and reduced motion support.
- **AC-5**: Preserve static GitHub Pages delivery, relative assets, the existing public URL and resume. Add search and social metadata and efficient images.
- **AC-6**: Deliver updated documentation, screenshots, factual research, test evidence and ranked remaining recommendations. Do not publish.

## Options considered

Retaining HTML and CSS avoids a build toolchain and preserves existing hosting. A component framework could help a larger application, but this page has no state that justifies its runtime or maintenance cost.

## Decision

Use static semantic HTML and CSS, native `details` for expanded engineering notes, and no JavaScript runtime. Use the Swiss visual direction from the frontend design skill: neutral white, Helvetica typography, one blue accent, asymmetric grid and fine rules. A large typographic introduction paired with a compact index of actual projects provides the distinctive composition.

## Rationale

The brief prioritizes credibility, loading efficiency and simplicity. Native navigation and disclosures remain usable without script. Real screenshots communicate more than invented product mockups.

## Feature design

Page order: header, introduction and project index, selected work, About, capabilities, contact, footer. Keep the existing home, projects, about, contact and main-content anchors. Use always visible navigation that wraps on narrow screens, avoiding unnecessary menu state. Keep captions clear that Cartograph is a recorded preview and RidzTalk source is private.

| Displayed value                                  | Source                                                          |
| ------------------------------------------------ | --------------------------------------------------------------- |
| Identity, location, career intent and background | User brief; original portfolio                                  |
| Email, LinkedIn, GitHub and CV                   | Existing checked in HTML and assets                             |
| Project stack, implementation and limits         | Repository source and documentation, recorded in ../research.md |
| RidzTalk availability                            | Public Google Play listing                                      |
| Cartograph preview                               | Public repository showcase screenshot at a pinned commit        |
| Additional project contribution                  | Public README explicitly credits Daniel with app development    |

No APIs, storage, authentication or environment variables belong to this portfolio. Public project summaries may describe verified private implementation, but must never reproduce credentials or private source code.

## Build plan

1. Record audit and project evidence (AC-2, AC-6).
2. Build the recruiter journey from introduction to project evidence and contact (AC-1, AC-2, AC-3).
3. Apply responsive presentation, accessibility, image optimization and metadata (AC-4, AC-5).
4. Validate actual browser behavior and update README and results (AC-4, AC-5, AC-6).

## Consequences

Content remains manually maintained. There is no dark theme switch or animated navigation. The site remains small and works without installation or a build step.

## Follow-up

Publication requires the owner's approval. Future project edits should recheck public status and technical evidence.
