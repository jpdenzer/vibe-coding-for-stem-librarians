---
title: Home
nav_order: 1
description: "A practical, jargon-light guide to vibe coding for STEM and science librarians."
permalink: /
---

# Vibe Coding for STEM Librarians

**What it really is and how it can help you**

Welcome! This site goes with the talk *Vibe Coding for STEM Librarians: What It Really Is and How It Can Help You*, given at the Upstate New York Science Librarians (NYSCILIB) meeting on October 16, 2026.

You do **not** need to be a programmer to use anything here. Every guide assumes you have never opened a terminal, and each one tells you what to type and what to click.

---

## What is "vibe coding"?

"Vibe coding" means describing what you want in plain English and letting an AI tool write the code. You judge the result by whether it *does the right thing*, not by reading every line. Andrej Karpathy coined the term in early 2025, and it quickly came to cover any AI-assisted coding by people who don't consider themselves programmers.

For librarians, that might look like:

- Comparing two database A–Z lists to find titles unique to each
- Cleaning up a messy spreadsheet of journal titles or ISSNs
- Turning a CSV export into a quick chart for an annual report
- Building a small web page or LibGuide widget
- Helping a student who built an analysis script and isn't sure it's right

The "vibe" part is both the appeal and the risk. You can build useful things fast, but **someone still has to check that the result is right.** That someone is you, and checking is something librarians are already good at.

---

## Vibe coding as a spectrum

The talk treats vibe coding as a ladder. Each rung needs a bit more setup and gives the AI more independence.

| Rung | What it looks like | Setup needed | Guide |
|:-----|:-------------------|:-------------|:------|
| **Low** | Chat with ChatGPT or Gemini, copy the code, paste it somewhere to run it | None (just a browser) | [01 · Conversational Prompting](01-chatgpt-gemini-prompting.md) |
| **Mid** | Go back and forth: paste errors back in, refine the request, build something a bit bigger | None (just a browser) | [02 · Iterating & Debugging](02-iterating-and-debugging.md) |
| **High** | Agentic tools like Claude Code and ChatGPT Codex read your files, run commands, edit code, and keep going on their own | Install a tool; usually a paid plan | [03 · Agentic Tools](03-claude-code-codex.md) |

Two more sections apply to every rung:

- [Helping Students (Consultations)](consultations.md): your role is judgment, not syntax
- [Guardrails](guardrails.md): privacy, licensing, security, and a checklist for checking AI-written code

---

## Which rung should I start on?

Answer the first question that fits you:

1. **"I've never written or run any code."**
   Start at **[01 · Conversational Prompting](01-chatgpt-gemini-prompting.md)**. You'll write a prompt, get a short Python script, and run it in your browser with Google Colab. Nothing to install.

2. **"I've gotten code from ChatGPT before, but it broke and I got stuck."**
   Go to **[02 · Iterating & Debugging](02-iterating-and-debugging.md)**. It covers what to do with error messages and how to tell when the AI is going in circles.

3. **"I have a project folder with several files, and copy-and-paste is getting painful."**
   You're ready for **[03 · Agentic Tools](03-claude-code-codex.md)**. Read the safety section first, then follow a step-by-step [tutorial](tutorials/) to install a tool.

4. **"I don't want to code. I want to help students who are."**
   Go straight to **[Helping Students](consultations.md)** and **[Guardrails](guardrails.md)**.

Not sure? Start at 01. It takes about 20 minutes, and every later rung builds on it.

---

## Try the demo

The [Examples](examples/) section has sample prompts for every rung and a small Python demo. The demo compares two **fake** STEM database A–Z lists and reports which titles appear in only one of them. You can run it in Google Colab without installing anything.

---

## All sections

- [01 · Conversational Prompting (ChatGPT & Gemini)](01-chatgpt-gemini-prompting.md)
- [02 · Iterating & Debugging](02-iterating-and-debugging.md)
- [03 · Agentic Tools (Claude Code & Codex)](03-claude-code-codex.md)
- [Helping Students (Consultations)](consultations.md)
- [Guardrails](guardrails.md)
- [Examples](examples/)
  - [Real-World Examples](examples/real-world/)
- [Tutorials](tutorials/): step-by-step walkthroughs, like [setting up Claude Code on Windows](tutorials/claude-code-windows.md)
- [Contributing & Feedback](CONTRIBUTING.md)

> **A note on dates and prices:** AI tools change monthly. Model names, free-tier limits, prices, and install commands on this site were checked in October 2026. Each page links to the official docs. If those docs disagree with this site, trust the docs.

---

**Next:** [01 · Conversational Prompting →](01-chatgpt-gemini-prompting.md)
