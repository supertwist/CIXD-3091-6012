**Note:**  
As artists/designers, we make drawings, think visually, and with our hands, not just in verbal/written language. Can we use our *native abilities* as prompt inputs for tools like Claude?

**Prompt:**  
Can claude generate a .STEP file from a hand-drawn sketch?

**Model:**  
Claude Code, Opus 4.5, 1/23/2026

**Response:**  

# Can Claude Generate a STEP File from a Hand-Drawn Sketch?

Short answer: not *directly* as a one-click “image → STEP” converter, but it can realistically get you from a hand sketch to a valid `.STEP` file using a CAD tool in the loop.

---

## What Claude Can and Cannot Do

### Can Do
- Read a scanned/photographed hand sketch (if you give it as an image).
- Infer a likely 2D/3D geometry from the sketch.
- Ask for missing info (dimensions, thickness, fillet radii, holes, constraints, etc.).
- Generate **parametric CAD code** (e.g. OpenSCAD, CadQuery/FreeCAD Python, Onshape FeatureScript) based on that interpretation.
- Generate or refine a **STEP export pipeline** in those tools.

### Cannot (Reliably) Do
- Magically infer precise dimensions or tolerances from a sketch without you specifying them.
- Guarantee manufacturability or mechanical correctness without your review.
- Directly act as a CAD kernel: you still need a CAD system to *open* geometry and export `.STEP`.

---

## Practical Pipeline: Hand Sketch → `.STEP` with Claude’s Help

### 1. Capture the Sketch Clearly
- Take a high-res photo or scan.
- If possible, include at least one reference dimension or grid so scaling is obvious.

### 2. Give Claude the Sketch and Intent
- Upload the image.
- Describe in text:
  - What the part is for (use case).
  - Any key dimensions (overall size, thicknesses, hole diameters, etc.).
  - Symmetries or constraints (“centered holes”, “mirror across this plane”, etc.).
- Ask Claude:
  > "Interpret this sketch as a 3D part. List all assumptions and ask any questions you need before generating a CAD model."

### 3. Clarify Dimensions and Constraints
- Answer its questions: missing dimensions, chamfers/fillets, fit with other parts, tolerances if relevant.
- Iterate until you agree on:
  - A simple dimensioned drawing (Claude can restate this as a table or text spec).
  - The parametric variables you care about (e.g. `width`, `height`, `thickness`, `hole_diam`, etc.).

### 4. Have Claude Generate CAD Code (Recommended Path)
- Pick a stack you’re comfortable running, e.g.:
  - **OpenSCAD** (simple, script-based; STEP via FreeCAD or other tools).
  - **CadQuery in FreeCAD** (Python scripts, native STEP export).
  - **Onshape FeatureScript** (cloud CAD, STEP export from the UI).
- Ask something like:
  > "Generate an OpenSCAD (or CadQuery / FeatureScript) model for this part, with these parameters. Assume I will then use [FreeCAD / Onshape / etc.] to export a STEP file."

### 5. Run the Script in Your CAD Environment
- Paste the generated script into the chosen tool.
- Regenerate the model; fix any syntax or geometry errors (Claude can help if you paste the error).
- Visually inspect: dimensions, clearances, alignment, feature order.

### 6. Iterate on the Geometry
- If features look wrong, send screenshots or descriptions back to Claude and ask for corrections to the script.
- Repeat until the model matches the sketch and your intent.

### 7. Export to `.STEP`
- From your CAD tool:
  - Select the solid body.
  - Use its "Export → STEP (.step / .stp)" function.
- Optionally open the `.STEP` in another tool (e.g. a CAM program or different CAD system) to verify.

---

## When It Won’t Work Well

- Sketch has **no dimensions** and you’re not willing to specify them.
- Very complex, freeform/organic surfaces where parametric scripting is awkward.
- Tight engineering requirements (fatigue, fits, GD&T) that are not clearly specified.

---

If you pick a specific CAD stack you’d like to use (OpenSCAD, FreeCAD/CadQuery, Onshape, Fusion 360 scripting, etc.), you can then ask Claude to produce a concrete example prompt and a minimal script for turning your particular sketch into a `.STEP` file.
