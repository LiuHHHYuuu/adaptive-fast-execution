---
name: brainstorming
description: Use this before implementation when the work is long, complex, multi-stage, cross-system, architectural, product-defining, materially ambiguous, difficult to reverse, or high risk. It turns consequential ideas into an approved design. Do not use it for a well-scoped, low-risk, reversible task likely to finish within about one hour, especially when the user asks to implement directly; let adaptive-fast-execution evaluate those tasks first.
---

# Brainstorming Consequential Work

Use design work where an incorrect decision would create meaningful rework, risk, or long-term cost. Do not turn routine implementation details into artificial user participation.

## Design gate

Require an approved design before implementation when any of these apply:

- Work is likely to exceed one hour, span sessions, or require multiple stages.
- Multiple core modules, services, repositories, or subsystems must coordinate.
- Architecture, public APIs, persistent schemas, critical algorithms, product behavior, or evaluation truth may change.
- Requirements contain ambiguity that could materially alter the result.
- The work is hard to reverse or involves production, deployment, publishing, credentials, permissions, security, privacy, deletion, migration, billing, or external side effects.

If none apply and the task is local, reversible, and clear enough, do not impose this design gate. Use the adaptive fast-execution workflow when available.

## Workflow

### 1. Explore first

- Inspect the current project, repository guidance, architecture, tests, relevant docs, and recent changes.
- Continue all safe read-only discovery until the consequential decisions are isolated.
- Do not ask the user to gather information that is already available to the agent.

### 2. Clarify only material uncertainty

Ask one concise question at a time only when the answer could change architecture, product intent, safety, cost, reversibility, or success criteria.

For routine syntax, glue code, file placement within established conventions, or other reversible implementation choices, make a reasonable decision yourself.

### 3. Compare approaches

Present two or three viable approaches when meaningful alternatives exist. Lead with a recommendation and explain the consequential trade-offs.

Do not manufacture alternatives for a task with one obvious implementation.

### 4. Use one high-value approval gate

Present a consolidated design containing:

- objective and non-goals;
- proposed architecture or behavior;
- important constraints and boundaries;
- error and rollback behavior;
- verification and acceptance criteria;
- unresolved human decisions, if any.

Ask for approval once. After approval, write the durable design and implementation plan, then execute without asking the user to re-approve the same content in a different format.

Pause again only when new evidence creates a materially different decision.

### 5. Persist long-running state

For work that may cross sessions, record the approved design, progress, decisions, failed approaches, verification evidence, and remaining work in repository files.

Do not rely on chat-only memory for a long project.

## Human and agent responsibilities

Use human attention for product intent, architecture, algorithm hypotheses, evaluation truth, safety boundaries, irreversible actions, and long-term trade-offs.

The agent owns investigation, code, tests, documentation, integrations, debugging, verification, and routine implementation after those decisions are clear.

## Interaction with adaptive fast execution

User wording such as “直接实现” or “skip the plan” is a preference for speed, not permission to ignore consequential risk.

- If the task qualifies for the fast path, do not use this workflow.
- If it fails fast eligibility or expands during execution, use this workflow or the normal rigorous process.
- System, developer, repository, safety, sandbox, and approval rules always take precedence.

