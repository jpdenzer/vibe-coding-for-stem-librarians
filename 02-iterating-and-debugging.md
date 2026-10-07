---
title: "02 · Iterating & Debugging"
nav_order: 3
description: "Paste errors back in, ask better follow-up questions, and recognize when the AI is going in circles."
---

# 02 · Iterating & Debugging

**Rung: Mid** · **Setup: none (same browser tools as rung 01)** · **Time: about 30 minutes**

Code from the AI rarely works perfectly on the first try. That's normal, and it's not a sign you did something wrong. This rung is about the **conversation that comes after the first answer**: fixing errors, refining the request, and building something a bit bigger one step at a time.

---

## The core loop

Almost all vibe coding at this level follows one loop:

1. **Ask** for a small, specific piece.
2. **Run** it (in Colab or wherever you're working).
3. **Look** at what happened. Did it work? Is the output right?
4. **Report back** exactly what happened, including the full error or a sample of the wrong output.
5. **Repeat.**

The key word is *small*. Asking for "a complete dashboard that pulls our usage stats, charts them, and emails a report" in one prompt usually produces something that almost works and is hard to fix. Asking for "read this CSV and print the first five rows" first, then adding one feature at a time, works much better.

---

## Pasting errors back in

When code fails, Python prints an **error message** (also called a *traceback*). It looks intimidating, but it's the most useful thing you can give the AI.

### What an error looks like

```text
Traceback (most recent call last):
  File "/content/compare.py", line 12, in <module>
    titles_a = {row["title"] for row in reader_a}
KeyError: 'title'
```

How to read it, bottom-up:

- **Last line** (`KeyError: 'title'`): *what* went wrong. Here, the code looked for a column called `title` and didn't find it.
- **Lines above it**: *where* it went wrong (file name and line number).

You don't need to fix it yourself. You just need to pass it along well.

### A good error report

Don't just say "it didn't work." Copy the **entire** error, and add what you did and what you expected:

```text
I ran the script in Colab and got this error:

[paste the full error here, every line]

My CSV file's first line is:  Title,Provider,Subject
I expected it to print the titles that are only in list A.

Please explain what caused the error in plain English, then give me
the corrected code.
```

In this example, the extra detail (the CSV's first line) gives the answer away: the column is `Title` with a capital T, not `title`. The AI can only spot that if you show it.

> **Privacy check:** Error messages sometimes include pieces of your data, such as a row that failed to load. If you're working with anything sensitive, look over the error before you paste it and replace real values with fake ones. See [Guardrails](guardrails.md).

---

## Asking better follow-up questions

When the code runs but the **result** looks off, your follow-up questions matter even more. Some patterns that work well:

### Describe the gap between expected and actual

```text
The script says 40 titles are only in list A. I checked by hand and
"Annals of Pretend Biology" is in both lists, but it's being reported
as unique to list A. In list B it's written "The Annals of Pretend Biology".
Why is that happening, and how should we handle titles that start with "The"?
```

### Ask for one change at a time

```text
That works. Now, without changing anything else, add one feature:
save the three lists to a CSV file I can download.
```

"Without changing anything else" helps more than you'd think. AI tools sometimes "improve" parts of the code you didn't ask about, which can break things that were working.

### Ask it to check its own work

```text
Before I run this, walk through what the code would do with these three
test rows, step by step, and tell me the exact output you expect:
[paste 3 fake rows]
```

Then run it and compare. If the AI's prediction and the real output disagree, you've found a problem.

### Ask for options, not just an answer

```text
There are a few ways to decide whether two titles are "the same."
Give me 3 options (from strict to loose), explain the trade-offs for a
library collection comparison, and recommend one.
```

This turns the AI from an order-taker into a consultant. **You** stay in charge of the decisions that affect whether the answer is right.

---

## How to tell when the AI is going in circles

Sometimes the conversation stops making progress. Warning signs:

- 🔁 **The same error keeps coming back**, or two errors take turns: fixing A brings back B, and fixing B brings back A.
- 🩹 **Each fix is a patch on a patch.** The code keeps growing with special cases, but the problem doesn't go away.
- 🙇 **Lots of apologizing, little changing.** "You're absolutely right, I apologize. Here's the corrected version…" followed by nearly identical code.
- 🧪 **It invents things.** It suggests a library, function, or setting that doesn't exist, or "fixes" an error by deleting the part of the code that was doing the actual work.
- 📏 **The conversation is very long.** After many rounds, the AI can lose track of details from early in the chat.

### What to do instead

1. **Stop and summarize.** Ask: *"Summarize what we've tried so far, what worked, and what's still broken."* Reading that summary often shows you the real problem.
2. **Start a fresh chat.** Paste in your *latest working* code (or the original goal) plus a short summary. A clean conversation often solves in one try what a long one couldn't.
3. **Shrink the problem.** Make a tiny test file with 3–5 rows that shows the bug. Small examples are easier for both you and the AI.
4. **Ask a different way.** *"Forget the current approach. What's a simpler way to do this?"* or *"What information do you need from me to solve this?"*
5. **Try a different tool.** ChatGPT and Gemini have different strengths. A second opinion is free.
6. **Know when to stop.** If something important is at stake (security, money, research data that will be published), see [when output needs expert review](guardrails.md#when-ai-output-needs-expert-review).

---

## Keeping track of versions

As your project grows, you'll lose track of which version of the code worked. A few simple habits help:

- **Save working versions.** When something works, copy it to a text file or a new Colab cell called "WORKING v1" before asking for changes.
- **Name your files with dates**, e.g. `compare_lists_2026-10-01.py`.
- **Keep a short log** of what you asked for and what changed. This is also exactly what you'd want to show a colleague, or include in a [real-world example](examples/real-world/).

If you find yourself juggling several files and many versions, that's a sign you're ready for the next rung, where tools like Claude Code and Codex work directly with your files and version control keeps track of changes for you.

---

## Quick reference

- **Small steps.** One feature per request.
- **Paste the full error**, plus what you did and what you expected.
- **Describe the gap** between expected and actual output, with a specific example.
- **"Without changing anything else"** protects working code.
- **Going in circles?** Summarize → fresh chat → smaller test case.
- **Save working versions** before asking for changes.

---

[← Previous: 01 · Conversational Prompting](01-chatgpt-gemini-prompting.md) · [Next: 03 · Agentic Tools →](03-claude-code-codex.md)
