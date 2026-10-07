---
title: "Real-World Examples"
parent: "Examples"
nav_order: 1
permalink: /examples/real-world/
description: "The author's own vibe-coded library projects, documented from prompt to validation."
---

# Real-World Examples

> 🚧 **Author's examples coming soon.**
>
> This page will collect real projects built by vibe coding for library work, documented honestly, including what went wrong.

---

## Format for each example

Each example gets its own folder inside `examples/real-world/`, e.g. `examples/real-world/az-list-migration-check/`, with a `README.md` that follows this structure:

### 1. The task
- What library problem was being solved, and why
- Which rung of the spectrum was used (1: conversational, 2: iterative, 3: agentic), plus the tool and model and the date

### 2. The original prompt
- The **exact** first prompt used, copied as-is (after removing sensitive details; see below)
- Any important follow-up prompts

### 3. What the AI produced
- The code, or a link to a file in the same folder
- A short plain-English summary of what it does

### 4. What went wrong or needed fixing
- Errors, wrong results, bad assumptions, things that looked right but weren't
- How each was found and how it was fixed (more prompting, a manual edit, a different approach)
- How many rounds it took

### 5. How the result was validated
- Spot checks, known-answer tests, comparisons with another method
- Who else reviewed it, if anyone
- Remaining limitations or known issues

### 6. Takeaways
- What you'd do differently next time
- Whether it was worth it compared to doing the task by hand

### Folder template

```text
examples/real-world/short-project-name/
├── README.md          # the six sections above
├── prompt.md          # full prompt history (optional)
├── script.py          # the final code (placeholders only, no secrets)
└── sample_data/       # FAKE data with the same shape as the real data
```

When you add a new example, also add front matter at the top of its `README.md` so it appears in the site menu:

```yaml
---
title: "Short Project Name"
parent: "Real-World Examples"
grand_parent: "Examples"
---
```

and add `has_children: true` to the front matter of this page.

---

## ⚠️ Before adding any example: scrub it

Every real-world example **must** have all sensitive details replaced with placeholders **before** it's committed. Git keeps history, so something committed once and deleted later can still be recovered.

| Replace this… | …with a placeholder like |
|:--------------|:-------------------------|
| Real library data (patron info, usage stats, holdings exports, consultation notes) | Fake data with the same columns, e.g. `fake_data/usage_fake.csv` |
| Vendor names and database titles from licensed lists | `Example Publisher One`, `Database A` |
| Vendor URLs, admin portal links, SUSHI/COUNTER endpoints | `https://vendor.example.com/...` |
| Proxy details (EZproxy or other proxy hostnames, stanzas, config files) | `https://proxy.example.edu/login?url=` |
| Credentials: passwords, API keys, tokens, customer IDs, requestor IDs | `YOUR_API_KEY_HERE`, or read from an environment variable |
| Institution-specific hostnames, IP ranges, internal server names | `library.example.edu`, `192.0.2.0/24` |
| Names or emails of colleagues, students, or patrons | `Librarian A`, `student@example.edu` |

**Final check before committing:** search the folder for `@`, `http`, `key`, `token`, `password`, `secret`, `proxy`, and your institution's name and domain.

See [Guardrails](../../guardrails.md) for the full privacy and licensing guidance.

---

[← Previous: Examples](../) · [Next: Contributing & Feedback →](../../CONTRIBUTING.md)
