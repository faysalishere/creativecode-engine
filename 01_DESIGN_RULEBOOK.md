# 01 — Design Rulebook (v1.0)

## A. Design should be intentional

Design is not a palette selection. Before layout, name the audience, top user job, visual hierarchy, brand personality, primary action, constraints and real content. Every visual choice must answer **why this arrangement is useful**.

**Rule precedence** (highest first):
1. Explicit instructions and approvals for the current request.
2. Current project's approved roadmap, existing architecture and verified state.
3. Existing project design system, real content/assets and any explicitly supplied project-specific design requirements.
4. This cross-project rulebook's defaults and model suggestions.

Example: if a project already has an approved monochrome visual identity, do not silently replace it with a generic gradient. Likewise, a blanket rule should not invalidate an explicitly approved font or animation choice. Use skill-specific typography/spacing defaults where compatible; do not silently impose a marketing landing-page structure on a dashboard or app.

## B. Ban obvious AI-pattern shortcuts

| Avoid | Replace with |
|---|---|
| Arbitrary emoji icons | Consistent vetted icon family or meaningful custom illustration |
| A hero + three equal glowing feature cards for every product | Information architecture selected for the actual user journey |
| Recycled purple gradients, generic glass panels, giant pill buttons | Brand-led restrained materials and meaningful depth |
| Decorative animation on every element | Choreography that guides attention or signals feedback |
| Placeholder copy masquerading as facts | Verified copy, or visible `{{placeholder}}` tokens |
| Same layout with three new colors presented as three concepts | Different hierarchy, composition, navigation and interaction model |
| Endless large blocks on mobile | Content density tuned for thumb use and screen constraints |
| Expensive visual effects without measurement | Fast first render, fluid scrolling, accessible motion settings |

No forced originality through novelty alone. Familiar patterns are permitted when they measurably improve comprehension.

## C. Design decisions before code

For each concept provide:
- Concept name, user promise, main user task and why the concept exists.
- Page architecture: list of sections and purpose, without generic filler.
- Three signature layout moves (not merely color or shadow choices).
- Primary + secondary navigation and interaction map.
- Content model with source provenance for real assets.
- Typography roles, spacing rhythm, constraints and motion intent.
- A short comparison against the other two concepts to demonstrate meaningful differences.

## D. Typography / visual hierarchy

- Define named roles (`Heading 1`, `Heading 2`, `Title`, `Body`, `Caption`, `Button`) and implement as reusable tokens.
- Prefer one primary type family within the approved project's system; additional family only when editorial or technical purpose justifies it.
- Use a deliberate scale and line heights, not arbitrary numbers per component.
- Visible order must be clear in 3 seconds: identity → value → next action.
- No single-word orphans when preventable; keep Bangla and English line breaks readable.
- Don't hide essential information inside low-contrast decorative copy.

**Optional landing-page starting values (only where compatible with the approved project):** type sizes on Tailwind's standard scale; default typeface Geist, Manrope or Poppins; spacing tokens 0 / 2 / 4 / 8 / 12 / 16 / 24 / 32 / 40 / 48 / 64 / 80 / 96 px; hero maximum text measure about 680 px. Reuse existing app tokens instead of replacing its whole type system.

## E. Composition and brand identity

- Create a 12-column desktop or appropriate project grid; mobile should reflow meaningfully, not merely shrink.
- Use alignment, content density, asymmetric composition and negative space intentionally.
- A page should have visual rhythm: focal area, information grouping, variation, quiet space.
- Color is for identification, state and emphasis, not decoration by default.
- Photographs, project previews and logos must be genuine or labelled as mockups. No fabricated 'live site' screenshots.
- Icon style and stroke weight must be consistent, regardless of icon library.

## F. Interaction, accessibility and motion

- Keyboard-focus visibility, sensible focus order, semantic roles, linked labels and proper error feedback are required.
- Aim for WCAG 2.2 AA: normal text contrast >= 4.5:1; large text >= 3:1, with applicable exceptions. Text sizing must remain readable when zoomed.
- Core actions must work by mouse, keyboard and touch; hover-only functionality is unacceptable.
- Default landing-page motion uses restrained transforms/opacity. Respect `prefers-reduced-motion` and deliver the final readable state without movement.
- Use IntersectionObserver or a throttled requestAnimationFrame for scroll-responsive effects; never rely on expensive unthrottled scroll callbacks.
- Micro-interactions should communicate state, not delay access. Audio never auto-plays without appropriate user initiation; provide clear mute/stop controls.
- A word-by-word benefit reveal may fit some landing-page briefs; it is not required in utility apps, dashboards or project UI unless requested.

## G. Responsive quality and state coverage

Test real or emulated viewport widths: 390 px mobile, ~768 px tablet, 1440 px desktop (plus representative small device when available). Test both EN and BN when a project is bilingual. Verify no horizontal overflow, truncation of key content, obstructed CTA or broken fixed navigation.

Required interaction states: default, hover/touch, active, focus, loading, empty, error, validation and completed. Every back button, menu, toggle, footer link and form must have a meaningful result.

## H. Performance and engineering

- Do not trade away core usability for cinematic effects.
- Aim for field Core Web Vitals LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1 at the 75th percentile; these are **targets**, not claimed test results.
- Audit images and fonts; compress, size, lazy-load noncritical media and prevent layout shifts.
- Inspect existing code and dependencies before editing. Prefer narrow diffs, no duplicate snippets or CSS overrides. Preserve route behavior, auth rules and content.
- Build and test in local/staging first. Keep previous production untouched unless explicitly approved for deployment.

## I. Anti-generic originality test (mandatory)

For two concepts A and B, ignore color and font and ask:
1. Are the hero composition and information priority different?
2. Is the navigation and page structure meaningfully different?
3. Are project/content presentations visibly different?
4. Is the interaction model appropriate and distinct?
5. Can a reviewer explain why each choice fits the audience?

**Fail originality** if fewer than three answers are substantively yes. 'Different' means observable in a grayscale wireframe, not just in a styling screenshot. A concept may still be rejected despite passing this test if its usability is worse.

## J. Definition of done

No unsupported '100/100 professional' claim. Report exactly what is built, what is reviewed, what is browser-tested, what remains unverified, and any exceptions. A visually attractive screenshot alone is insufficient evidence of a working app.
