## Research-to-Blog Agent Prompt

### Goal
Turn the first idea in `Ideas/ideas.json` into a research-backed blog content package:
- A comprehensive research markdown file: `{name}.md`
- A short brief markdown file: `brief.md`

Both files must be created in a new topic folder under `Research and Content/`.

### Inputs
1. Source ideas file: `Ideas/ideas.json`
2. Use **only the first record** in the JSON array (index `0`).

### Output location and naming
1. Create a new folder under `Research and Content/` for this topic.
2. Folder name: use a clean, filesystem-safe slug derived from the idea title/topic.
	- Lowercase
	- Replace spaces with hyphens
	- Remove special characters
3. Inside that folder, create two files:
	- Primary research file: `{name}.md` (where `{name}` matches the same slug used for the folder)
	- Brief file: `brief.md`

### Required workflow
#### Step 1 — Extract the idea
- Read `Ideas/ideas.json` and load the first idea object.
- Determine the “topic” / “title” and any supporting fields available (e.g., audience, problem statement, angle, keywords).
- If the schema is unclear, infer the topic from the most descriptive fields.

#### Step 2 — Generate research questions
Create a set of **parallel research questions** that fully cover the topic.
Include (when relevant):
- Definitions / basics (what it is, how it works)
- “Why it matters” (benefits, value, tradeoffs)
- Use cases (who uses it, when, and why)
- How-to / process (steps, best practices)
- Comparisons (alternatives, competitors, build vs buy)
- Pricing / cost drivers (if applicable)
- Common pitfalls / FAQs / misconceptions
- Trends, recent changes, or 2024–2025 context when relevant

Keep the questions specific enough to research, not generic.

#### Step 3 — Research
- Use the available research tooling as much as possible.
- Collect facts, examples, frameworks, and numbers **only when reasonably verifiable**.
- Prefer primary/authoritative sources when possible (official docs, vendor pricing pages, reputable publications).
- When information is uncertain or varies, explicitly say so and provide ranges or multiple viewpoints.

#### Step 4 — Write the primary research file (`{name}.md`)
The primary file must include:
1. **Topic + one-line thesis**
2. **List of research questions** (the ones you generated)
3. **Research findings** organized by question (or by themes that clearly answer the questions)
4. **Actionable takeaways** (what the blog should emphasize)
5. **Potential outline for the blog post** (H2/H3 level)
6. **Source notes**
	- Add links or citations when available.
	- If you cannot provide links, describe the type of source and what it supports.

Write in clean markdown with clear headings.

#### Step 5 — Write the brief (`brief.md`)
In the same folder, create `brief.md` containing:
- **Intent / objective** of the blog
- **Target audience** (as inferred from the idea)
- **Key points to cover** (bulleted)
- **Interesting facts / hooks** (bulleted)
- **Suggested CTA** (call to action)

### Constraints
- Do not create extra folders/files beyond the topic folder, `{name}.md`, and `brief.md`.
- Keep outputs focused on the chosen idea only.
- Use markdown headings and bullet lists for readability.

### Completion checklist
- [ ] Read first record from `Ideas/ideas.json`
- [ ] Generated a thorough set of parallel research questions
- [ ] Completed research and synthesized findings
- [ ] Created `Research and Content/<topic-slug>/{name}.md`
- [ ] Created `Research and Content/<topic-slug>/brief.md`


