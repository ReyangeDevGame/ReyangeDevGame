# Operational Protocols

## 1. Universal Startup Protocol
**Trigger**: Every time you are activated (New Conversation or Role Switch).
**Action**:
1. **Check State**: Read `task.md`. Is the previous task marked `[x]`?
   - **NO**: Ask User: "Previous task incomplete. Should I continue it or switch context?"
   - **YES**: Proceed.
2. **Context Injection**: Read `docs/governance/roles.md` & `protocols.md` & `README.md`.
3. **Environment Scan**: Check if `docs/system_context.md` exists. If NOT, trigger "Setup Phase" (ask user for OS/Shell details).
4. **Standby Rule**: If `task.md` defines an Active Feature, and the assigned agent is NOT YOU, output "Standby: Waiting for [Agent]" and STOP.

## 2. Hybrid Workflow (Fast Lane vs Slow Lane)
### A. Slow Lane (Standard)
- **Use Case**: New Features, Logic Refactors, Complex UI.
- **Flow**: Plan -> Code -> QA.

### B. Fast Lane (Trivial Fixes)
- **Use Case**: Typos, Missing Imports, One-line CSS.
- **Action**: 
  1. **Fix it** immediately (Skip Plan).
  2. **Log it**: Mention action in final summary (e.g., *"Fast Lane: Fixed typo"*).
  3. **Proceed**: Continue with primary task.

### C. QA Triage Rule
- **Blocking/Critical**: Push back to Coder (Current Sprint).
- **Minor/Polish**: Log in Backlog (Next Sprint).
- **Unclear**: Ask [BA] to Triage.

## 3. Strict Path & Persistence Protocol
- **Paths**: ALWAYS use Relative Paths (e.g., `src/utils.ts` not `C:\Users...`).
- **Archive**: `docs/archive/` contains subfolders `sprint_01`, `sprint_02`, etc.
- **Persistence**: 
  - `task.md` items are NEVER deleted.
  - [ARCHITECT] Plans -> `docs/specs/[id]_[name].md`
  - [CODER] Task Breakdowns -> `docs/specs/[id]_task_breakdown.md` (Optional, but persistent if created).


## 4. The "Conch Shell" Protocol (Task.md)
- Only the **Active Agent** (assigned in `task.md`) should modify `task.md`.

## 5. Verification Protocol (QA)
1. **Automated**: Run tests.
2. **Manual**: Create `docs/reports/[id]_walkthrough.md`. This is the MANDATORY "Proof of Readiness".
3. **Server**: Explicitly START the test server -> Wait for User Validation -> STOP the server.
4. **Constraint**: QA NEVER closes the sprint or moves items to "Completed".

## 6. Sprint Transition Protocol (The Virtual Meeting)
**Trigger**: Features complete, or Sprint Duration reached.
**Phase 1: Freeze (DEVOPS ONLY)**
1. Ensure all code is committed.
2. Create/Finish the Sprint Branch (e.g., `git checkout -b release/sprint-01` or merge to main).
3. Archive current `task.md` AND any sprint-specific specs (`docs/specs/*`) to `docs/archive/sprint_XX/`.

**Phase 2: The Round Table (BA & TEAM)**
1. **[BA]** creates `docs/meetings/YYYY-MM-DD_sprint_retro.md` from Template.
2. **[USER]** activates agents sequentially to fill out the meeting doc.
   - **Topic 1**: Retrospective (Risks & Failures).
   - **Topic 2**: Process Review (Amend Protocols?).
   - **Topic 3**: Next Scope (What Features?).
3. **Flexibility**: [BA] or [USER] can add extra agenda items to this file as needed.

**Phase 3: Activation (DEVOPS)**
1. Read the finalized Meeting Doc.
2. Setup new `task.md`.
3. Create new Sprint Branch `sprint/XX`.
