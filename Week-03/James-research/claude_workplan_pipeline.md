**Note:**  
How do I use a work plan to to keep Claude 'on-track' as it works on a project? 

**Prompt:**  
can you describe the pipeline in claude for properly generating a work plan and then executing that plan to create a delverable (for example a web app or a .STEP file)? provide a step-by-step guide and save as a .md file to /Claude.

**Model:**  
Claude Code, Opus 4.5, 1/23/2026

**Result:**  

# Using Claude to Create a Work Plan and Execute It to a Deliverable

This guide describes a practical pipeline for using Claude to:
- Turn a vague idea into a clear specification
- Generate a concrete, reviewable work plan
- Execute that plan in iterations to produce a real deliverable (e.g., a web app or a STEP file)

The same pattern works for many project types; only the domain-specific steps change.

---

## Phase 1: Define the Goal and Constraints

1. **Describe the end goal in your own words.**  
   Examples:
   - "A small web app where users can upload a CSV and visualize basic charts."
   - "A parametric 3D bracket, exported as a STEP file, with configurable width/height/thickness."

2. **List constraints and preferences explicitly.**  
   Include, where relevant:
   - Tech stack (e.g., "React + TypeScript + Vite", "Python FastAPI", "Onshape or OpenSCAD for CAD")
   - Performance/scale expectations
   - Deadlines and time budget
   - Non-functional requirements (security, portability, offline use, etc.)

3. **Share current assets and context with Claude.**  
   - Existing repo structure
   - Any design docs, mockups, or CAD references
   - APIs or data sources the project must integrate with

4. **Ask Claude to restate the problem and assumptions.**  
   Prompt example:  
   > "Here are my goals and constraints (paste). Please restate them concisely, list the key assumptions you’re making, and highlight anything that is ambiguous or risky."

5. **Resolve ambiguities before moving on.**  
   Iterate until the problem statement and assumptions look right to you.

---

## Phase 2: Ask Claude for a Structured Work Plan

1. **Request a plan with explicit phases and deliverables.**  
   Prompt example:  
   > "Create a phased work plan to achieve this goal. For each phase, include: objective, concrete deliverables, tasks, approximate ordering, and what I should validate before moving on. Assume I will ask you to help with each step."  

2. **Common phases for a web app project:**
   - Requirements & UX outline
   - Architecture and tech choices
   - Initial scaffolding (frontend/backend/framework setup)
   - Core feature implementation
   - Persistence & integrations
   - Testing & QA
   - Packaging, deployment, and documentation

3. **Common phases for a STEP/CAD project:**
   - Requirements (dimensions, loads, tolerances, interfaces)
   - Parametric model design strategy
   - CAD environment and scripting choice (e.g., Onshape FeatureScript, OpenSCAD, Python + CAD API)
   - Iterative CAD modeling (sketches, constraints, features)
   - Design checks (fit, clearances, export validation)
   - STEP export and verification in target tools

4. **Ask Claude to highlight dependencies and risks.**  
   - External APIs, libraries, or CAD kernels
   - Tooling you must install
   - Unknowns that may affect feasibility or scope

5. **Review and adjust the plan.**  
   - Merge/resize phases so they fit your time budget.
   - Ask Claude to re-balance the plan if one phase looks too big or vague.

---

## Phase 3: Turn the Plan into Executable Tasks

1. **Convert each phase into small, concrete tasks.**  
   Prompt example:  
   > "Take this plan and break Phase 1 into tasks that each take 15–60 minutes. For each task, specify: clear success criteria, files likely to be touched/created, and how I can verify completion (tests, commands, or manual checks)."

2. **Create a prioritized task list.**  
   - Ask Claude to tag tasks as P0/P1/P2 (critical → nice-to-have).
   - Ensure there is a clear first task that unblocks everything else.

3. **Define checkpoints and demo moments.**  
   - For web app: e.g., "first static UI", "first working API call", "MVP uploaded and rendered chart".
   - For CAD/STEP: e.g., "first parametric sketch", "all key constraints modeled", "STEP exported and opened in target tool".

4. **Align on your workflow with Claude.**  
   For example:  
   - You run shell commands locally; Claude suggests commands and code edits.
   - After each logical change, you show diffs or errors; Claude helps fix or refactor.

---

## Phase 4: Implementation Loop (Task-by-Task Execution)

Repeat the following loop for each task or small cluster of tasks.

1. **Select the next task and restate it to Claude.**  
   Prompt example:  
   > "Next task: Implement user sign-up and login using email + password in this React + FastAPI app. Here is the current repo structure and relevant files (paste tree or snippets). Help me design the approach and then write the code step by step."

2. **Have Claude propose an approach before writing code.**  
   - Data models, components, or CAD feature sequence
   - Interfaces between modules
   - Any required library choices

3. **Ask for concrete code or model changes in small batches.**  
   - For web app: one component/file or small feature at a time.
   - For CAD: one sketch or feature group at a time, with clear parameters.

4. **Apply the suggested changes locally and run checks.**  
   Examples:
   - Web app:
     - `npm test`, `npm run lint`, `npm run dev`
     - Manual UI testing in a browser
   - CAD/STEP:
     - Regenerate the model
     - Inspect dimensions, clearances, and constraints
     - Re-export STEP and open it in downstream tools

5. **Report results back to Claude.**  
   - Paste error messages, test failures, or screenshots/descriptions of incorrect behavior.
   - Ask for fixes or refactors.

6. **Iterate until the task’s success criteria are met.**  
   - Once done, mark the task complete and choose the next one.

---

## Phase 5: Integration, Testing, and Hardening

1. **Ask Claude to design a verification strategy.**  
   - Unit tests, integration tests, or end-to-end tests for a web app
   - Parametric checks and interference checks for CAD models

2. **Implement tests with Claude’s help.**  
   - Provide current code/model; ask for specific test cases and implementations.
   - Run tests and iterate on failures.

3. **Perform integration reviews.**  
   - For web app: review routing, error handling, API boundaries, and data flow.
   - For CAD: ensure parametric changes don’t break the model and interfaces remain correct.

4. **Ask Claude for a final pre-release checklist.**  
   Examples:
   - Web app: env config, logging, minimal docs, deployment steps.
   - CAD: naming conventions, configuration presets, export settings, versioning.

---

## Phase 6: Packaging and Deliverables

1. **Define the exact deliverables you need.**  
   Examples:
   - Web app:
     - Source repo in a clean state
     - Build artifacts or deployed URL
     - `README` with setup, run, and deployment instructions
   - STEP file project:
     - Source CAD model (scripts/documents)
     - Exported `.step` file(s)
     - Notes on parameters and how to regenerate/export

2. **Ask Claude to help you create or polish these artifacts.**  
   - Generate or refine `README`, architecture notes, API docs.
   - Describe CAD parameters, dependencies, and regeneration steps.

3. **Standardize the project layout.**  
   - Ask Claude to review your file structure and suggest improvements for clarity.

4. **Create a short final summary with Claude.**  
   - What was built
   - How to run or use it
   - Known limitations and future work

---

## Phase 7: Iteration and Maintenance

1. **Capture feedback and new requirements.**  
   - Ask Claude to turn feedback into new tasks or a v2 plan.

2. **Use the same pipeline for improvements.**  
   - Start again from a mini-Phase 1 (updated goals) and go through planning → execution → packaging.

3. **Refactor with Claude’s help periodically.**  
   - For web apps: architecture cleanups, performance improvements, UX refinements.
   - For CAD: feature tree simplification, robustness improvements, better parameterization.

---

## Example: Minimal Prompt Template

You can reuse this pattern to drive the workflow:

> "You are helping me build a [web app / STEP-based CAD model].
> 1) Restate my goal and assumptions.
> 2) Propose a phased plan with concrete deliverables.
> 3) Break the first phase into 15–60 minute tasks with success criteria.
> I’ll then ask you to help me implement each task step by step, and I will run commands/tests locally and report back results."

Use this loop consistently and keep Claude informed of your project state (files, errors, screenshots, and decisions). That is what turns the high-level plan into a concrete, working deliverable.
