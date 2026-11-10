# Contributing

Thanks for considering an improvement. CreativeCode is intentionally lightweight: readable instructions, verifiable criteria and a dependency-free scoring tool. Please preserve its honest feature boundaries.

## Good contributions

- Better prompts with concrete examples of meaningful structural design differences.
- Accessibility, keyboard/touch and reduced-motion review improvements.
- Clearer documentation, translations or stronger scorecard validation.
- Small tests for real bugs, or clearly labelled proposals for future automation.

## Workflow

1. Open an issue explaining the problem and expected behavior before a large rewrite.
2. Fork the repository, create a branch, and make small scoped changes.
3. Run `python3 -m unittest discover -s tools -p 'test_*.py' -v` and the sample calculator.
4. Explain what you tested. Never call untested visual behavior verified.
5. Send a pull request linking the issue and include before/after examples for design-rule changes.

Avoid copyrighted asset uploads, secrets, private user data, fabricated testimonials, and code that silently deploys or uses a paid API. Contributions are provided under the repository's MIT license.
