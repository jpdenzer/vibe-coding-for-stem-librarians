---
title: "Guardrails"
nav_order: 6
description: "Data privacy, licensing, security-sensitive code, when to get expert review, and a checklist for validating AI-generated code."
---

# Guardrails

Vibe coding is fast. These guardrails keep you, your patrons, and your institution safe while you move quickly. They apply to **every rung**, from a single chat message to an agent working in your files.

---

## Data privacy: what never goes into an AI tool

Anything you paste into a chat, upload, or put in an agent's project folder is sent to the AI company's servers. Depending on your plan and settings, it may be stored, reviewed by people, or used to train future models.

### Never paste or upload

- 🚫 **Patron or student data:** names, IDs, email addresses, circulation records, search histories, consultation notes, grades, or anything that could identify a person. Library privacy is a professional value, and laws such as FERPA and New York's library records law ([CPLR § 4509](https://www.nysenate.gov/legislation/laws/CVP/4509)) may also apply.
- 🚫 **Credentials:** passwords, API keys, tokens, EZproxy or other proxy configuration and secrets, database connection strings, SSH keys.
- 🚫 **Licensed vendor content:** full-text articles, e-book content, proprietary database exports, or vendor admin reports when your license restricts sharing them with third parties.
- 🚫 **Unpublished research data** from faculty or students unless they have explicitly agreed, and their data management plan, IRB protocol, or funder allows it.
- 🚫 **Internal or confidential documents:** budgets, personnel matters, negotiations, security details.

### Do this instead

- ✅ **Make up sample data** that has the same *shape* (same columns, similar formats) but fake values. The demo in [Examples](examples/) shows how.
- ✅ **Describe the structure** instead of pasting it: "a CSV with columns `title`, `issn`, `start_year`."
- ✅ **De-identify** before you share: replace names with `Patron_001`, real URLs with `https://example.org`.
- ✅ **Use your institution's approved AI tool** if there is one. Enterprise or education plans often come with stronger data protections and no-training agreements. Ask IT what's approved.
- ✅ **Check your settings.** Most AI tools let you opt out of having your chats used for training. Find that setting and turn it on.

> **Check the official docs:** Data-use policies and privacy settings differ by product and plan, and they change. See [OpenAI's data controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq), [Anthropic's privacy center](https://privacy.anthropic.com/), and [Gemini Apps privacy hub](https://support.google.com/gemini/answer/13594961).

---

## Licensing and terms of use

### Your vendor licenses

Many database and e-resource licenses restrict text and data mining, automated downloading, or sharing content with third parties, and AI companies count as third parties. Before you build anything that scrapes, bulk-downloads, or feeds licensed content to an AI:

- Read the license or ask your electronic resources librarian.
- Look for clauses on *text and data mining (TDM)*, *automated access*, *systematic downloading*, and *AI*.
- When in doubt, use the vendor's official API or export tools within their terms.

Automated scripts that ignore these terms can get your **whole institution's access suspended**.

### The AI tool's terms

Each AI service has its own terms of use covering who owns the output, acceptable use, and age requirements. Students using these tools for coursework should also follow their instructor's and institution's AI policies.

### Licensing AI-generated code

- AI-generated code can sometimes closely resemble existing open-source code. For anything you'll publish or distribute, ask the AI *"Is any of this copied from a specific open-source project? What license would apply?"*, and be appropriately skeptical of the answer.
- If you share your code (like this repository does), add a clear license. Code here uses [MIT](LICENSE-CODE); written content uses [CC BY 4.0](LICENSE).
- Copyright status of purely AI-generated material is still unsettled. See the [U.S. Copyright Office's AI initiative](https://www.copyright.gov/ai/) for current guidance.

---

## Security-sensitive code

Be extra careful, and get help, when AI-generated code:

- **Handles logins, passwords, or API keys.** Never write a secret directly into code (a "hardcoded" key). Ask the AI to use environment variables or a separate config file that you keep out of version control.
- **Touches institutional systems:** your ILS/LSP, link resolver, proxy server, discovery layer, LibGuides/LibApps admin, or anything that connects with campus single sign-on.
- **Runs on a public web page or server**, e.g. a form that accepts input from users. Web code needs protection against well-known attacks that AI tools don't always guard against.
- **Deletes, moves, or overwrites files** or database records in bulk.
- **Sends data somewhere:** emails, uploads, API calls to outside services.
- **Installs packages** you haven't heard of. AI tools sometimes suggest packages that don't exist, and attackers have registered fake packages under exactly those names. Check the name on [pypi.org](https://pypi.org) and look for real usage before installing.

**Quick self-check:** ask the AI, *"Review this code for security problems. Assume an attacker will try to misuse it. What could go wrong?"* Treat the answer as a starting point, not a sign-off.

---

## When AI output needs expert review

Use vibe-coded tools on your own for **low-stakes, easily checked tasks**: comparing two lists, reformatting a spreadsheet, drafting a chart. Get a qualified person to review the work when:

| Situation | Who to ask |
|:----------|:-----------|
| It will run on institutional systems or a public website | Library IT / systems, campus IT security |
| It handles credentials, personal data, or authentication | IT security, privacy officer |
| Results will be **published**, inform a **grant**, or support a **policy or budget decision** | A colleague who can independently check the method; statistical consulting |
| It involves **statistics or research methods** you can't evaluate yourself | Statistical consulting, a subject expert, or the literature |
| It involves **human-subjects data** | IRB / research compliance |
| It touches **licensed content** in an automated way | Electronic resources librarian, licensing staff |
| It will be **maintained by others** or run unattended for months | Someone who can read and maintain code |

**Rule of thumb:** the more people affected by a mistake, and the harder that mistake is to notice, the more review the work needs.

---

## Checklist: validating AI-generated code before you use it

Copy this list and run through it before trusting a result.

### Understand it
- [ ] I can explain in plain English what the code does, step by step (ask the AI to explain it if needed).
- [ ] I asked the AI to **list its assumptions**, and they match my data and my goal.
- [ ] I know what the code **reads, writes, deletes, or sends**, and nothing surprises me.

### Test it
- [ ] I ran it on a **small test file where I already know the right answer**, and it matched.
- [ ] I **spot-checked** 3–5 real results by hand.
- [ ] The **totals make sense** (row counts, groups adding up to the whole).
- [ ] I tried **edge cases**: blank cells, duplicates, special characters, very long values.

### Make it safe
- [ ] No **passwords, keys, or real personal data** in the code, the prompts, or the project folder.
- [ ] It doesn't use **licensed content** in a way the license forbids.
- [ ] Any packages it installs are **real and widely used**.
- [ ] I ran it on a **copy** of my data, not the original.

### Keep a record
- [ ] I saved the **prompt(s)**, the **tool and model** used, and the **date**.
- [ ] I saved the **working version** of the code (ideally in Git).
- [ ] I wrote down **how I validated** the result.
- [ ] If the stakes are high, someone else has **reviewed** it (see the table above).

---

[← Previous: Helping Students](consultations.md) · [Next: Examples →](examples/)
