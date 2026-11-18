# Local verification transcript

Platform: `linux`. Verdict: **PASS**.

Executed against the pre-commit working tree. The reviewed-content map and candidate-source manifest identify the maintained source files; the final branch commit adds retained evidence.

## verification-cli

Phase: health; status: PASS; exit: 0

```json
["python3", "plugins/factory/scripts/verification.py", "--help"]
```

```text
usage: verification.py [-h] {discover,scaffold,skill,run} ...

Discover verification candidates and run explicit project verification
contracts. Only ``run`` executes project commands. Discovery never treats a
script or CI snippet as approved verification. This module uses only the
Python standard library; command argument vectors are executed without a
shell.

positional arguments:
  {discover,scaffold,skill,run}

options:
  -h, --help            show this help message and exit
```

## discover-project

Phase: interaction; status: PASS; exit: 0

```json
["python3", "plugins/factory/scripts/verification.py", "discover", "."]
```

```text
{
  "version": 1,
  "project": "factory",
  "candidate_only": true,
  "packages": [],
  "workflows": [
    {
      "path": ".github/workflows/checks.yml",
      "clues": [
        {
          "line": 7,
          "text": "runs-on: ${{ matrix.os }}"
        },
        {
          "line": 13,
          "text": "- uses: actions/checkout@v4"
        },
        {
          "line": 14,
          "text": "- uses: actions/setup-python@v5"
        },
        {
          "line": 17,
          "text": "- run: python scripts/check.py"
        },
        {
          "line": 18,
          "text": "- run: python -m unittest discover -s tests -v"
        }
      ]
    }
  ],
  "configs": [],
  "documentation": [
    "README.md"
  ]
}
```

## packaging-contracts

Phase: checks; status: PASS; exit: 0

```json
["python3", "scripts/check.py"]
```

```text
{
  "verdict": "PASS",
  "errors": []
}
```

## contracts-and-behavior

Phase: checks; status: PASS; exit: 0

```json
["python3", "-m", "unittest", "discover", "-s", "tests", "-v"]
```

```text
test_acceptance_rejects_advanced_base_even_when_patch_is_unchanged (test_delivery_guard.DeliveryGuardTests.test_acceptance_rejects_advanced_base_even_when_patch_is_unchanged) ... ok
test_acceptance_rejects_advanced_head (test_delivery_guard.DeliveryGuardTests.test_acceptance_rejects_advanced_head) ... ok
test_acceptance_rejects_dirty_checkout (test_delivery_guard.DeliveryGuardTests.test_acceptance_rejects_dirty_checkout) ... ok
test_acceptance_rejects_open_prerequisite (test_delivery_guard.DeliveryGuardTests.test_acceptance_rejects_open_prerequisite) ... ok
test_acceptance_rejects_retarget_to_equal_sha_alias (test_delivery_guard.DeliveryGuardTests.test_acceptance_rejects_retarget_to_equal_sha_alias) ... ok
test_acceptance_requires_verdict_reviewer_and_evidence (test_delivery_guard.DeliveryGuardTests.test_acceptance_requires_verdict_reviewer_and_evidence) ... ok
test_active_topic_worktree_blocks_cleanup (test_delivery_guard.DeliveryGuardTests.test_active_topic_worktree_blocks_cleanup) ... ok
test_clean_merged_topic_is_eligible_without_mutating_git (test_delivery_guard.DeliveryGuardTests.test_clean_merged_topic_is_eligible_without_mutating_git) ... ok
test_cli_blocks_malformed_records_and_has_nonzero_status (test_delivery_guard.DeliveryGuardTests.test_cli_blocks_malformed_records_and_has_nonzero_status) ... ok
test_current_acceptance_allows_exact_committed_patch (test_delivery_guard.DeliveryGuardTests.test_current_acceptance_allows_exact_committed_patch) ... ok
test_dirty_or_untracked_original_checkout_is_preserved (test_delivery_guard.DeliveryGuardTests.test_dirty_or_untracked_original_checkout_is_preserved) ... ok
test_dirty_other_worktree_blocks_cleanup (test_delivery_guard.DeliveryGuardTests.test_dirty_other_worktree_blocks_cleanup) ... ok
test_integration_target_must_match_record_and_cannot_be_topic (test_delivery_guard.DeliveryGuardTests.test_integration_target_must_match_record_and_cannot_be_topic) ... ok
test_missing_remote_branch_is_allowed_but_unreachable_remote_blocks (test_delivery_guard.DeliveryGuardTests.test_missing_remote_branch_is_allowed_but_unreachable_remote_blocks) ... ok
test_new_useful_topic_commit_is_preserved (test_delivery_guard.DeliveryGuardTests.test_new_useful_topic_commit_is_preserved) ... ok
test_only_named_canonical_integration_branch_aliases_are_accepted (test_delivery_guard.DeliveryGuardTests.test_only_named_canonical_integration_branch_aliases_are_accepted) ... ok
test_open_or_unknown_dependencies_block_cleanup (test_delivery_guard.DeliveryGuardTests.test_open_or_unknown_dependencies_block_cleanup) ... ok
test_remote_topic_advance_blocks_even_without_fetch (test_delivery_guard.DeliveryGuardTests.test_remote_topic_advance_blocks_even_without_fetch) ... ok
test_sha_tag_and_revision_expression_cannot_self_prove_unmerged_topic (test_delivery_guard.DeliveryGuardTests.test_sha_tag_and_revision_expression_cannot_self_prove_unmerged_topic) ... ok
test_squash_merge_requires_attributed_exact_head_evidence (test_delivery_guard.DeliveryGuardTests.test_squash_merge_requires_attributed_exact_head_evidence) ... ok
test_unknown_ownership_original_default_and_protected_branches_are_preserved (test_delivery_guard.DeliveryGuardTests.test_unknown_ownership_original_default_and_protected_branches_are_preserved) ... ok
test_unmerged_topic_is_preserved (test_delivery_guard.DeliveryGuardTests.test_unmerged_topic_is_preserved) ... ok
test_candidate_regression_cannot_pass (test_evaluations.EvaluationReceiptTests.test_candidate_regression_cannot_pass) ... ok
test_changed_output_invalidates_receipt (test_evaluations.EvaluationReceiptTests.test_changed_output_invalidates_receipt) ... ok
test_changed_requests_invalidate_comparison (test_evaluations.EvaluationReceiptTests.test_changed_requests_invalidate_comparison) ... ok
test_duplicate_task_ids_cannot_hide_missing_coverage (test_evaluations.EvaluationReceiptTests.test_duplicate_task_ids_cannot_hide_missing_coverage) ... ok
test_empty_task_set_cannot_vacuously_pass (test_evaluations.EvaluationReceiptTests.test_empty_task_set_cannot_vacuously_pass) ... ok
test_inconclusive_is_not_promoted (test_evaluations.EvaluationReceiptTests.test_inconclusive_is_not_promoted) ... ok
test_missing_case_cannot_pass (test_evaluations.EvaluationReceiptTests.test_missing_case_cannot_pass) ... ok
test_paired_content_bound_pass (test_evaluations.EvaluationReceiptTests.test_paired_content_bound_pass) ... ok
test_broken_migration_link_is_rejected (test_packaging.PackagingTests.test_broken_migration_link_is_rejected) ... ok
test_broken_skill_reference_is_rejected (test_packaging.PackagingTests.test_broken_skill_reference_is_rejected) ... ok
test_missing_entry_skill_is_rejected (test_packaging.PackagingTests.test_missing_entry_skill_is_rejected) ... ok
test_repository_contracts (test_packaging.PackagingTests.test_repository_contracts) ... ok
test_version_drift_is_rejected (test_packaging.PackagingTests.test_version_drift_is_rejected) ... ok
test_wrong_marketplace_source_is_rejected (test_packaging.PackagingTests.test_wrong_marketplace_source_is_rejected) ... ok
test_absent_git_identity_is_inconclusive (test_verification.VerificationTests.test_absent_git_identity_is_inconclusive) ... ok
test_argv_is_not_interpreted_by_a_shell (test_verification.VerificationTests.test_argv_is_not_interpreted_by_a_shell) ... ok
test_cleanup_failure_outranks_unsupported_launch (test_verification.VerificationTests.test_cleanup_failure_outranks_unsupported_launch) ... ok
test_cli_requires_evidence_and_reports_nonpass_exit (test_verification.VerificationTests.test_cli_requires_evidence_and_reports_nonpass_exit) ... ok
test_command_timeout_preserves_evidence_and_cleans_up (test_verification.VerificationTests.test_command_timeout_preserves_evidence_and_cleans_up) ... ok
test_discovery_inventories_without_executing (test_verification.VerificationTests.test_discovery_inventories_without_executing) ... ok
test_evidence_is_not_overwritten (test_verification.VerificationTests.test_evidence_is_not_overwritten) ... ok
test_explicit_cleanup_may_stop_launched_service (test_verification.VerificationTests.test_explicit_cleanup_may_stop_launched_service) ... ok
test_failure_stops_proof_but_always_runs_all_cleanup (test_verification.VerificationTests.test_failure_stops_proof_but_always_runs_all_cleanup) ... ok
test_git_identity_does_not_execute_diff_drivers (test_verification.VerificationTests.test_git_identity_does_not_execute_diff_drivers) ... ok
test_git_identity_records_modes_even_when_git_ignores_filemode (test_verification.VerificationTests.test_git_identity_records_modes_even_when_git_ignores_filemode) ... ok
test_git_identity_uses_repository_root_for_nested_project (test_verification.VerificationTests.test_git_identity_uses_repository_root_for_nested_project) ... ok
test_incomplete_scaffold_is_rejected_before_commands (test_verification.VerificationTests.test_incomplete_scaffold_is_rejected_before_commands) ... ok
test_launch_and_descendant_are_stopped (test_verification.VerificationTests.test_launch_and_descendant_are_stopped) ... ok
test_launch_failure_still_runs_cleanup (test_verification.VerificationTests.test_launch_failure_still_runs_cleanup) ... ok
test_malformed_commands_are_rejected_before_execution (test_verification.VerificationTests.test_malformed_commands_are_rejected_before_execution) ... ok
test_platform_and_ci_exceptions_are_not_passes (test_verification.VerificationTests.test_platform_and_ci_exceptions_are_not_passes) ... ok
test_readiness_timeout_stops_launch_descendants_and_runs_cleanup (test_verification.VerificationTests.test_readiness_timeout_stops_launch_descendants_and_runs_cleanup) ... ok
test_skill_is_self_contained_and_overwrite_requires_force (test_verification.VerificationTests.test_skill_is_self_contained_and_overwrite_requires_force) ... ok
test_source_change_during_run_is_inconclusive (test_verification.VerificationTests.test_source_change_during_run_is_inconclusive) ... ok
test_success_records_each_phase_and_output (test_verification.VerificationTests.test_success_records_each_phase_and_output) ... ok
test_unconfirmed_launch_descendant_cleanup_is_inconclusive (test_verification.VerificationTests.test_unconfirmed_launch_descendant_cleanup_is_inconclusive) ... ok
test_unsupported_health_blocks_dependent_interaction (test_verification.VerificationTests.test_unsupported_health_blocks_dependent_interaction) ... ok

----------------------------------------------------------------------
Ran 59 tests in 4.772s

OK
```

## cli-no-service-cleanup

Phase: cleanup; status: PASS; exit: 0

```json
["python3", "-c", "print('No persistent service or temporary project data; evidence retained')"]
```

```text
No persistent service or temporary project data; evidence retained
```
