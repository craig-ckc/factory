# Factory

Shared agent plugin for building and shipping software: one orchestrator skill (`factory`), sixteen capability skills across Understand, Engineer, Design, Verify, and Deliver, seven task playbooks, and shared code/design references.

This repository starts from the installed Factory **2.1.1** shared marketplace. The skills, playbooks, references, and plugin manifests are preserved from that base. Specification: [Factory V2.1](https://craigchihururu.notion.site/Factory-V2-1-3f851dc3a8b481cf918ce864bb2741ea).

Each harness reads its own manifest over the same `plugins/factory` tree:

| Harness | Marketplace | Plugin manifest |
| --- | --- | --- |
| Claude Code | `.claude-plugin/marketplace.json` | `plugins/factory/.claude-plugin/plugin.json` |
| Codex | `.agents/plugins/marketplace.json` | `plugins/factory/plugin.json` |
| Cursor | `.cursor-plugin/marketplace.json` | `plugins/factory/.cursor-plugin/plugin.json` |

The marketplace identifier remains `factory-local` for compatibility with existing installations. Its name is independent of the GitHub repository name.

## Install from this repository

Clone the repository, then register the checkout with the agents you use:

```sh
gh repo clone craig-ckc/factory ~/Developer/Projects/factory
```

Claude Code:

```sh
claude plugin marketplace add ~/Developer/Projects/factory
claude plugin install factory@factory-local --scope user
```

Codex:

```sh
codex plugin marketplace add ~/Developer/Projects/factory
codex plugin add factory@factory-local
```

For Cursor, use `.cursor-plugin/marketplace.json` as the marketplace manifest for this checkout.

The Codex marketplace uses repository-relative plugin paths, as described in the [official plugin format documentation](https://learn.chatgpt.com/docs/enterprise/plugin-management#supported-formats).

## Develop and update

Make changes under `plugins/factory`. For a plugin release, keep `version` synchronized in all three manifests:

- `plugins/factory/plugin.json`
- `plugins/factory/.claude-plugin/plugin.json`
- `plugins/factory/.cursor-plugin/plugin.json`

Use this checkout as the shared authoring location and register it as the marketplace source in each harness that should receive updates. Harness-specific cache folders are generated installations. The visual and interface acceptance gate in `plugins/factory/skills/factory/SKILL.md` applies across every playbook.

After editing the registered source, refresh the installed copy:

```sh
claude plugin marketplace update factory-local
claude plugin update factory@factory-local
codex plugin add factory@factory-local
```

## Contents

- `plugins/factory/skills/`: Factory orchestration and sixteen capability skills.
- `plugins/factory/playbooks/`: feature, bug fix, refactor, migration, investigation, performance, and shipping workflows.
- `plugins/factory/references/`: shared code quality and interface design guidance.
- `.agents/`, `.claude-plugin/`, `.cursor-plugin/`: marketplace manifests for the supported agents.
