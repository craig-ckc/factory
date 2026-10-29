# Project verification

Use when a project lacks reusable verification instructions or its launch/check commands are unclear. Reuse established project tooling first; a one-off change does not require a new skill.

## Discover and select

Read repository instructions, package scripts, CI workflows, tool versions, fixtures, and service dependencies. Identify commands for launch (or explicitly no persistent service), readiness/health, a real consumer interaction, evidence, and cleanup. Map each CI job to its local command and prerequisites, or record the platform/credential/hosted dependency that prevents local execution. Workflow inventory is advisory: inspect job conditions, matrices, services, actions, and secrets before deciding equivalence. Discovered commands are candidates, never automatically trusted or executed.

The bundled standard-library helper inventories candidates and scaffolds a contract:

```sh
python3 plugins/factory/scripts/verification.py discover /path/to/project
python3 plugins/factory/scripts/verification.py scaffold /path/to/project --output /path/to/project/verification.json
```

Inspect and complete the scaffold before running it. A contract contains `version: 1`, `project`, optional `launch` (a command or `null`), nonempty `health`, `interaction`, `checks`, and `cleanup` command lists, and `ci_exceptions` (job/reason records). Each command has `name`, `argv` (an argument array), and bounded `timeout_seconds`; optional `platforms` uses Python platform identifiers (`darwin`, `linux`, `win32`). Explicitly record a no-op cleanup command when the CLI starts no service and creates no temporary project data. Do not disguise an unavailable check as a no-op.

## Run and retain evidence

```sh
python3 plugins/factory/scripts/verification.py run /path/to/project --manifest /path/to/project/verification.json --evidence /path/to/evidence
python3 plugins/factory/scripts/verification.py skill /path/to/project --manifest /path/to/project/verification.json --output /path/to/project/.agents/skills/project-verification
```

Generate a project skill only when repeated verification warrants it; inspect the generated instructions and commit them according to the project's conventions. Existing files require an explicit overwrite choice. The skill records project commands and does not depend on the original plugin's absolute install path.

The runner executes explicit argument arrays without a shell, bounds commands, retains revision/dirty-state metadata and command logs, and attempts cleanup even after failures. Its PASS establishes the selected contract only. Missing/unsupported CI stays INCONCLUSIVE; a failing command is FAIL. CLI exit codes are 0/1/2 respectively. Logs and `report.json` identify the observed content, including a dirty checkout; a dirty-run result is not automatically acceptance of a later commit.

POSIX process-group teardown is exercised with live child processes. Windows uses `taskkill`; descendants cannot be proven stopped after their process leader has already exited. That launch condition is INCONCLUSIVE, and Windows CI does not stand in for the POSIX-specific descendant tests. Inspect the runner report and platform coverage for the actual flow.

Keep Testing, Code Review, Interface Review and Product Validation conclusions distinct. For a user flow, record the original finish condition and actual observed result. Green contract checks cannot approve a feature that misses the original request. Any visual/UI behavior still requires the Factory interface gate and rendered evidence. Choose and inspect evidence before attaching it to an external record.
