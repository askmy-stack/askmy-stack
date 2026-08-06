# Futuristic Profile Copy Design

## Goal

Polish the content below the profile GIF so it reads like a concise systems manifesto, remains understandable to general visitors, and uses a futuristic technical visual language that GitHub renders reliably.

## Constraints

- Keep the Prism light-ray GIF as the only animated element.
- Add a cache-busting query to the hero image URL so the merged GIF refreshes immediately.
- Do not include the removed paragraph beginning `I work at the layer where intelligence becomes useful`.
- Do not load custom web fonts; GitHub profile Markdown sanitizes unsupported styling.
- Use semantic HTML supported by GitHub: centered headings, `<samp>` for monospace copy, Markdown tables, code labels, and horizontal rules.
- Preserve all five external links: portfolio, LinkedIn, GitHub, Medium, and Hugging Face.
- Remove emoji-led section headings and reduce decorative badge clutter.

## Content Structure

1. Centered identity block: name, `AI SYSTEMS ENGINEER // RESEARCHER`, and the system arc `CONTEXT → ORCHESTRATION → EXECUTION → AUTONOMY`.
2. `01 // PERSPECTIVE`: one quote only—`Models predict. Agents deliver. Systems anchor context.`
3. `02 // OPERATING LAYERS`: a two-column table describing context, orchestration, execution, reliability, and learning in plain language.
4. `03 // SYSTEM STACK`: four compact rows for intelligence, systems, data, and operations.
5. `04 // TRANSMISSION`: existing destinations presented as a restrained static badge row.

## Voice

Short, declarative, systems-oriented, and free of résumé filler. Lead with ideas, explain the working layers, and place tools after the explanation.

## Validation

- Exactly one GIF reference.
- Removed paragraph absent.
- All required headings, labels, and links present.
- No emoji entities in section headings.
- Existing GIF renderer tests continue to pass.
