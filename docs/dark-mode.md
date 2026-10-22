# Light and dark themes

Added on 22 October 2026 at the owner's request, extending the initial light-only portfolio. The owner also authorized publication and asked for current screenshots in the GitHub README.

## Behavior

The header's theme button names the action it will perform: Light mode in the dark theme, and Dark mode in the light theme. Its visible label, accessible name, tooltip and sun/moon icon update together. It is a native action button with visible keyboard focus, rather than a pressed-state toggle with a changing name. It works with pointer input, Enter and Space. On small phones, the visible text is hidden while the accessible label and 44px target remain.

The initial theme follows the device preference. An explicit choice is stored as `portfolio-theme` in localStorage and applied on the next visit. Invalid values are ignored. If reading or writing storage throws, the button still changes the theme for the current visit. System theme changes are followed until a visitor chooses a theme.

`theme.js` runs before the stylesheet, so the root theme attribute is available for the first styled render. Browser theme-color metadata follows the choice. CSS supplies a device-theme fallback when JavaScript is unavailable, and the unused button stays hidden. Print styles always use the light palette. Project screenshots and the resume PDF are not recolored.

## Checks executed

- `node --check theme.js`, `node scripts/check_theme.cjs`, `python3 scripts/check_site.py`, HTML validation and `git diff --check` passed.
- The Node check exercises automatic selection, a saved override, reload state, OS changes, invalid preferences, blocked storage, visible and accessible action labels and browser theme color.
- CSS Tree parsed the stylesheet and checked declaration grammar without errors.
- Browser checks in Chrome confirmed pointer toggling, Enter and Space operation, and persistence across a real page reload.
- Both themes had document width equal to viewport width at 320, 390, 768, 1024 and 1440px.
- A rendered text contrast scan inspected 132 visible text-bearing elements in each theme and reported no failures against normal and large text contrast thresholds. This is a focused contrast check, not a full WCAG conformance evaluation or a new axe scan.
- The mobile toggle measured 44px by 44px. Final desktop and phone captures were reviewed in both themes.

Updated README images include the current light desktop and mobile views plus new dark desktop and mobile views. Social sharing artwork remains a deliberately authored card, rather than a screenshot, and needs no change for this feature.

No runtime libraries, framework or build step were added. Browser testing used Chrome; other browsers and screen readers were not independently tested for this change.
