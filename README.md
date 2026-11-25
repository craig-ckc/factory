# Factory

Six agent skills for turning a request into verified software. Two inner loops—spec/review and build/verify—feed back into each other when an assumption fails, then hand off the requested result.

| Skill | Purpose |
| --- | --- |
| [factory](skills/factory/SKILL.md) | Coordinate the loops and the authorized handoff. |
| [spec](skills/spec/SKILL.md) | Define the outcome, constraints, and proof. |
| [design](skills/design/SKILL.md) | Shape, build, and inspect the actual interface. |
| [review](skills/review/SKILL.md) | Challenge specs and implementations; coordinate a council when needed. |
| [verify](skills/verify/SKILL.md) | Prove the original outcome and route failures. |
| [deliver](skills/deliver/SKILL.md) | Hand off a branch, PR, merge, or deployment within scope. |

Skills live directly in `skills/`. The root manifests let Claude Code, Codex, and Cursor install that same source as `factory@factory`. Model preferences and project-specific tooling belong in the project using Factory.

## Install

Claude Code and Codex install straight from this repository.

Claude Code:

```sh
claude plugin marketplace add craig-ckc/factory
claude plugin install factory@factory --scope user
```

For Claude Code cloud sessions, add the marketplace `craig-ckc/factory` at claude.ai/customize/plugins and install `factory` from it.

Codex:

```sh
codex plugin marketplace add craig-ckc/factory
codex plugin add factory@factory
```

Cursor registers a local checkout:

```sh
git clone https://github.com/craig-ckc/factory.git
```

Then use `.cursor-plugin/marketplace.json` from that checkout.

After pushing changes, refresh existing installations (`claude plugin marketplace update factory`, `codex plugin marketplace upgrade`) and confirm that the six skills are discovered.

## Maintaining Factory

Edit the skills directly and keep versions aligned in the three plugin manifests. Run checks and evaluations in the local or cloud environment doing the work. Use commits and PRs for rationale, review, and results; this repository contains no separate docs, evaluation suite, scripts, or tests.
