---
title: "Helping Students"
nav_order: 5
description: "How librarians can support students who are vibe coding, without being programmers. The librarian's role is judgment, not syntax."
---

# Helping Students Who Are Vibe Coding

**Your role is judgment, not syntax.**

More and more students arrive at consultations with code they didn't write: an analysis script from ChatGPT, a data-cleaning notebook from Gemini, a whole project built with an agentic tool. Often they're stuck, or they're not sure the results are right. Sometimes they don't realize they *should* be unsure.

You don't need to read Python to help. The most important questions about AI-generated code aren't about programming at all:

- *Did you ask the right question?*
- *What did the AI assume?*
- *Does the output match reality?*
- *Can you explain and stand behind this result?*

These are information literacy questions, and librarians are trained to ask them.

---

## Start the consultation

Open with curiosity, not judgment. Students may worry they're "cheating" or that you'll disapprove. Normalize it:

> "Lots of people are using AI to write code now. Let's make sure it's doing what you need. Can you show me what you asked it and what you got back?"

Then ask to see three things:

1. **The prompt(s)**, the actual conversation if possible
2. **The data**: a few rows of the input file
3. **The output**: what the code produced, and what they *expected*

---

## Questions to ask about the student's prompt

A vague prompt is the most common root problem, and it's the easiest to spot without any coding knowledge.

| Ask the student… | Why it matters |
|:-----------------|:---------------|
| "What exactly did you ask for? Can I see the prompt?" | Students often remember their request as more specific than it was. |
| "Did you tell it what your data looks like: column names, formats, units?" | Without this, the AI invents a structure that may not match the real file. |
| "Did you tell it what the result is for? A class assignment? A thesis? Publication?" | The level of rigor should match what's at stake. |
| "Did you mention any rules from your field or your instructor?" | E.g., required statistical tests, how to handle missing values, citation style. |
| "Was there anything you weren't sure how to ask?" | Gaps in the prompt often point to gaps in understanding the problem itself. |

**Coaching move:** help the student rewrite their prompt using the five-part structure from [01 · Conversational Prompting](01-chatgpt-gemini-prompting.md#step-1-write-a-good-first-prompt): context, goal, input, output, and where it will run. This is just a reference interview, aimed at a machine.

---

## How to check the AI's assumptions

Every script quietly makes decisions. Help the student bring them to the surface. A great move is to have the student **ask the AI directly, while you watch:**

```text
List every assumption this code makes about my data and my analysis.
For each one, tell me what would happen if the assumption were wrong.
```

Then go through the list together. Common assumptions to look for:

- **What counts as a match or a duplicate?** (Exact text? Ignoring case? Ignoring "The"?)
- **What happens to missing or blank values?** (Dropped silently? Counted as zero? These give very different results.)
- **Units and formats.** (Celsius or Fahrenheit? Dates as MM/DD or DD/MM? Gene names in which nomenclature?)
- **Which rows are included?** (Did a filter drop more than intended?)
- **Which method was chosen, and why?** (Why this statistical test? Why this normalization? Is it standard in the student's field?)

For methods questions, connect the student to the literature or a subject expert. *"The AI chose a t-test. Let's find out what methods papers in your field actually use for this kind of data."* That's a research consultation, and it's squarely your territory.

---

## How to verify output against the actual data

Checking results against reality is what turns a plausible answer into a trustworthy one. You can model this process without touching the code.

### 1. Spot-check by hand

Pick **3–5 specific rows** and work out the right answer by hand (or in a spreadsheet). Does the code agree?

> "Let's find one title you *know* should be unique to list A. Is it in the output?"

### 2. Check the totals

- Does the number of rows in the output make sense given the input?
- If you split the data into groups, do the groups add up to the whole?
- Are there suspiciously round numbers, zeros, or results that are *too* clean?

### 3. Try a known answer

Make a tiny test file (5–10 rows) where the student already knows the correct result. Run the code on it. This is the single most convincing check, and it's easy to explain in a methods section.

### 4. Look at the edges

- What about the first and last rows?
- Blank cells, special characters (é, ü, &), very long values?
- Duplicates in the input?

### 5. Compare with an independent method

Can the same answer be checked another way, such as a pivot table in Excel or a quick count in a spreadsheet? If two methods agree, confidence goes up.

> **A useful rule:** If the student can't describe how they checked the result, they're not ready to use it in a paper, presentation, or decision.

---

## Connections to information literacy instruction

Vibe coding fits naturally into frameworks you already teach. The [ACRL Framework for Information Literacy for Higher Education](https://www.ala.org/acrl/standards/ilframework) maps onto it well:

| Frame | In a vibe coding context |
|:------|:-------------------------|
| **Authority Is Constructed and Contextual** | AI-generated code sounds confident whether it's right or wrong. Authority comes from verification, not fluency. |
| **Information Creation as a Process** | Code goes through drafts, testing, and revision, just like writing. The prompt history is part of the record. |
| **Research as Inquiry** | Iterating with an AI is inquiry: refine the question, test, revise. Debugging is hypothesis testing. |
| **Searching as Strategic Exploration** | Prompting well works like searching well: specific terms, context, and iteration beat one vague query. |
| **Information Has Value** | Data privacy, licensing, and terms of use apply to what students paste into AI tools (see [Guardrails](guardrails.md)). |
| **Scholarship as Conversation** | Methods should be grounded in the field's literature, not just whatever the AI defaulted to. |

### Ideas for instruction

- **"Spot the assumption" activity:** Give students a short AI-generated script and its prompt. In small groups, they list the assumptions the code makes and design one test for each.
- **Prompt makeover:** Show a vague prompt and its mediocre output. Students rewrite the prompt and compare results.
- **Reproducibility and disclosure:** Teach students to save their prompts, note which tool and model they used, and describe their verification steps. Many journals and instructors now require AI-use disclosure. Point students to their course or publisher policy.
- **Citing AI tools:** Show the current guidance from [APA](https://apastyle.apa.org/blog/how-to-cite-chatgpt), [MLA](https://style.mla.org/citing-generative-ai/), or the style the student's field uses.

---

## Knowing your limits, and referring

You don't have to solve every problem. Good referral partners include:

- **Research computing or data services** for programming help, high-performance computing, or complex environments
- **Statistical consulting** for methods choices and interpreting results
- **The student's advisor or instructor** about whether AI use is allowed for this work at all
- **IRB or research compliance** if human-subjects data is involved
- **IT or information security** if credentials, institutional systems, or sensitive data are involved

Saying *"This needs someone who can review the statistics. Let me connect you"* is a good consultation outcome.

---

## Quick reference: consultation checklist

- [ ] Ask to see the **prompt**, the **data**, and the **output**
- [ ] Is the prompt specific about **context, goal, input, output**?
- [ ] Have the student ask the AI to **list its assumptions**
- [ ] **Spot-check** 3–5 rows by hand
- [ ] Check **totals** and **edge cases**
- [ ] Test on a **small file with a known answer**
- [ ] Is the **method** standard in the field? (Literature check)
- [ ] Is any **sensitive data** being pasted into AI tools?
- [ ] Is AI use **allowed** for this assignment or publication? Does it need disclosure?
- [ ] **Refer** when expertise or stakes call for it

---

[← Previous: 03 · Agentic Tools](03-claude-code-codex.md) · [Next: Guardrails →](guardrails.md)
