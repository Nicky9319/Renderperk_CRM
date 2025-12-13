## Blog Layout and Image Planning Agent Prompt

### Goal
Given a completed research markdown file and its brief, design a detailed blog layout and image plan for the topic.

### Inputs
1. The main research markdown file (`{name}.md`) and its brief (`brief.md`) in a topic folder under `Research and Content/`.

### Output location and naming
1. Inside the topic folder, create a subfolder named `blog`.
2. In `blog/`, create:
	- `{name}_blog.md`: Contains the full blog outline/layout, section structure, and image references (no full text content).
	- `content.md`: Contains the detailed, ground-level content for each section/heading in the outline, ready to be posted.
	- `images.md`: Contains detailed descriptions and tags for each image reference.

### Required workflow
#### Step 1 — Analyze research and brief
- Read the `{name}.md` and `brief.md` files to understand the topic, key points, and intended audience.

#### Step 2 — Design blog layout (in `{name}_blog.md`)
- Create a clear, sectioned outline for the blog post (H1/H2/H3 structure).
- For each section, specify:
	- Section/heading title
	- Where images/visuals should be placed (with reference IDs, e.g., `IMG1`, `IMG2`)
	- The type of image or visual (photo, diagram, chart, etc.)
- Include suggested CTAs (calls to action) in appropriate places.
- Optionally, include sequence or line diagrams (in markdown or mermaid) to illustrate layout or flow.

#### Step 3 — Write `{name}_blog.md` (blog outline)
This file must include:
1. Blog title and one-line summary
2. Full blog outline with all sections and subsections (H1/H2/H3 structure)
3. For each section:
	- Section/heading title
	- Image reference(s) with placement notes (e.g., “Insert IMG1 here: [caption]”)
	- CTA placement if relevant
4. At the end, a list of all image references used

#### Step 4 — Write `content.md` (full blog content)
For each section/heading in the outline, provide:
- The complete, ready-to-publish content for that section (not just a summary)
- Use markdown formatting for headings, lists, images (with reference IDs), and CTAs
- Ensure the structure matches the outline in `{name}_blog.md`

#### Step 5 — Write `images.md`
For every image reference (e.g., `IMG1`, `IMG2`):
- Provide a detailed description of the image needed for that spot
- List relevant tags/keywords for stock image search
- If possible, suggest the style (photo, illustration, diagram, etc.)

### Constraints
- Do not create extra folders/files beyond `blog/`, `{name}_blog.md`, `content.md`, and `images.md`.
- All image references in `{name}_blog.md` and `content.md` must be described in `images.md`.
- Limit the total number of images used in the blog to **3–5** maximum.
- Write in clear markdown with headings, bullet lists, and diagrams as appropriate.

### Completion checklist
- [ ] Read `{name}.md` and `brief.md` in the topic folder
- [ ] Created `blog/` subfolder
- [ ] Wrote `{name}_blog.md` with full outline/layout and image references (max 3–5 images)
- [ ] Wrote `content.md` with full, ready-to-publish content for each section
- [ ] Wrote `images.md` with detailed image descriptions and tags (max 3–5 images)