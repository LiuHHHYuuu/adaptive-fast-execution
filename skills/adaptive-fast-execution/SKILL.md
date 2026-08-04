---
name: adaptive-fast-execution
description: Use this skill for coding implementation, modification, bug-fix, or small build tasks whenever the user asks to "implement directly", "just do it", "skip the plan", "move fast", or similar, and also when the task appears finishable within about one hour. It selects a fast path only for local, reversible, low-risk work and falls back immediately for long, complex, cross-system, architectural, production, security, data, permission, billing, publishing, or irreversible work. Do not use for pure explanation, review-only, research-only, or planning-only requests.
---

# Adaptive Fast Execution

Reduce ceremony for small safe implementation tasks without removing the evidence needed to trust the result.

## Decide fast eligibility

Use the fast path only when every statement below is true:

- The work is likely to finish within about one hour.
- The goal is singular, clear enough, and locally scoped.
- The change is easy to revert.
- It does not coordinate multiple core modules, services, or subsystems.
- It does not change core architecture, public interfaces, persistent data models, or critical algorithms.
- A reasonable minimal assumption can resolve any remaining ambiguity without substantial rework.
- None of the strict-exclusion conditions apply.

Treat user phrases such as “直接实现”, “直接改”, “不用写方案”, “不用设计文档”, “别问了，先做”, “快速执行”, “简单处理一下”, “修好并测试”, “按你的判断完成”, “implement directly”, “just do it”, and “skip the plan” as strong preferences for the fast path. They do not override the exclusions below.

If eligibility is uncertain, follow the normal rigorous workflow instead.

## Strict exclusions

Do not use the fast path when any of these apply:

- The task is likely to exceed one hour, span sessions, or require multiple implementation stages.
- It crosses core modules, services, repositories, or subsystems.
- It changes architecture, public APIs, persistent schemas, critical algorithms, or project-wide behavior.
- A local mistake could propagate broadly through the project.
- Ambiguity could change product direction or cause substantial rework.
- It touches production, deployment, public publishing, credentials, permissions, security, privacy, data deletion, database migrations, billing, or other external side effects.
- The action is destructive, difficult to reverse, or changes evaluation, security, permission, or merge rules.

On an exclusion, stop applying this skill and use the normal rigorous process. Do not restate that entire process here.

## Fast path

Use this compact loop:

```text
minimum necessary inspection -> implement -> targeted verification -> concise handoff
```

### Minimum necessary inspection

- Read only the files, nearby implementation, repository guidance, and tests needed to locate the change.
- Do not create a formal design document, large execution plan, or task decomposition for an eligible fast task.
- Do not pause for routine implementation choices that are reversible and do not change the requested behavior.
- Make the smallest reasonable assumption for low-impact ambiguity and disclose it briefly at handoff.

### Implement

- Keep the diff local and minimal.
- Do not perform opportunistic refactors, cleanup, dependency upgrades, or unrelated edits.
- Preserve existing conventions and user-owned changes.

### Targeted verification

- Run the narrowest deterministic check that proves the changed behavior: a directly related test, lint/type check for touched files, a local build, or a minimal runtime reproduction.
- Do not run unrelated project-wide evaluations merely for ceremony.
- Never gain speed by skipping all verification when a relevant check is available.

### Concise handoff

Report only:

- what changed;
- what verification passed or failed;
- any important assumption or unverified limitation.

## Exit the fast path

Exit immediately when investigation reveals broader scope, a public contract or architecture change, material ambiguity, difficult rollback, or any strict exclusion.

A first failed targeted check does not by itself require escalation. Diagnose and fix it within the original local scope. Escalate when the failure shows that the task is broader or riskier than initially classified.

When escalating, preserve useful findings and give a concise reason. Do not continue expanding a supposedly fast task silently.

## Interaction with design workflows

For an eligible fast task, do not invoke a full brainstorming/specification workflow merely because implementation involves a small creative choice. Use such a workflow only after the task fails fast eligibility or exits the fast path.

System, developer, repository, safety, sandbox, and approval rules always take precedence over this skill.

