---
title: "Examples"
nav_order: 7
has_children: true
permalink: /examples/
description: "Sample prompts for each rung, plus a demo Python script that compares two fake STEM A-Z database lists."
---

# Examples

This section has two parts:

1. **[Sample prompts](#sample-prompts)** for each rung of the spectrum, ready to copy, paste, and adapt
2. **[A demo script](#demo-compare-two-az-database-lists)** that compares two **fake** STEM A–Z database lists

There's also a [Real-World Examples](real-world/) page, where the author's own projects will be added.

> **All data here is fake.** The titles, providers, and subjects in `fake_data/` are made up. When you adapt these prompts, use fake or de-identified data too. See [Guardrails](../guardrails.md).

---

## Sample prompts

Replace anything in `[square brackets]` with your own details.

### Rung 1: Conversational prompting

*Use with ChatGPT or Gemini. See [01 · Conversational Prompting](../01-chatgpt-gemini-prompting.md).*

**Compare two lists**
```text
I'm a science librarian with no programming experience. Write a Python
script I can run in Google Colab that compares two CSV files, list_a.csv
and list_b.csv. Each has a column called "title". Treat titles as the same
if they differ only in capitalization or extra spaces. Print the titles
only in A, only in B, and in both, sorted alphabetically with counts.
Use only Python's standard library and explain each step in comments.
Then tell me exactly how to upload the files and run it in Colab.
```

**Clean up a messy column**
```text
I have a spreadsheet column of ISSNs that are formatted inconsistently:
some have hyphens, some don't, some have spaces, and a few have an "X"
at the end. Here are 6 made-up examples: [paste fake examples].
Write a Python script for Google Colab that standardizes them to the
format 1234-567X and flags any that aren't 8 characters long.
Explain what the code assumes about valid ISSNs.
```

**Make a quick chart**
```text
I have a CSV with columns "year" and "downloads" (made-up example rows:
2022,1200 / 2023,1450 / 2024,1610). Write Python code for Google Colab
that makes a simple, readable bar chart with labeled axes and a title,
and saves it as a PNG I can download. Keep it beginner-friendly.
```

**Understand code someone gave you**
```text
Explain this code to me line by line as if I've never programmed.
Then list every assumption it makes about the input data, and anything
it deletes, overwrites, or sends anywhere.

[paste code]
```

### Rung 2: Iterating and debugging

*See [02 · Iterating & Debugging](../02-iterating-and-debugging.md).*

**Report an error**
```text
I ran the script and got this error:

[paste the FULL error message]

The first line of my CSV is: [paste header row]
I expected: [what you expected to happen]
Explain the cause in plain English, then give me the corrected code.
```

**Report a wrong result**
```text
The script runs, but the result looks wrong. It reports
"[specific title]" as only in list A, but it's also in list B,
spelled "[spelling in list B]". Why? Suggest 2-3 ways to handle this
kind of difference, explain the trade-offs, and recommend one.
```

**Add one feature safely**
```text
This version works. Without changing anything else, add one feature:
[describe it]. Show me only the lines that changed and explain why.
```

**Break out of a loop**
```text
We've been going back and forth without fixing this. Stop and summarize:
what we're trying to do, what we've tried, what worked, and what's still
broken. Then suggest a simpler approach.
```

**Check before running**
```text
Before I run this, walk through what the code would do with these 3
made-up rows, step by step, and tell me the exact output you expect:
[paste 3 fake rows]
```

### Rung 3: Agentic tools

*Use with Claude Code or Codex, started in a **copy** of your project folder. See [03 · Agentic Tools](../03-claude-code-codex.md).*

**Get oriented (no changes)**
```text
Look at the files in this folder and explain in plain English what's
here and what each file does. Don't change anything.
```

**Set up a safety net**
```text
Set up git in this folder and make a first commit called
"Starting point before AI changes." Explain each command you run.
```

**Plan before coding**
```text
I want to compare the two CSV files in fake_data/ and report titles
unique to each list. Before writing any code, give me a step-by-step
plan, list the assumptions you'd make about matching titles, and wait
for my approval.
```

**Build and test**
```text
Go ahead with the plan. Also create a tiny test file with 5 rows where
the correct answer is obvious, run the script on it, and show me the
output so I can confirm it's right. Commit when it works.
```

**Review what changed**
```text
Summarize every file you created or changed in this session, what you
changed, and why. Point out anything I should double-check by hand.
```

**Security review**
```text
Review this project for security and privacy problems. Check for
hardcoded passwords or keys, code that sends data anywhere, and code
that deletes or overwrites files. Assume someone will try to misuse it.
```

---

## Demo: compare two A–Z database lists

[`compare_az_lists.py`](https://github.com/jpdenzer/vibe-coding-for-stem-librarians/blob/main/examples/compare_az_lists.py) is a short Python script (standard library only) that is a simplified stand-in for a common library task: comparing two database A–Z lists, for example before and after a migration, or two campuses' lists, to see which titles are unique to each.

It reads two fake CSV files:

- [`fake_data/list_a_fake.csv`](https://github.com/jpdenzer/vibe-coding-for-stem-librarians/blob/main/examples/fake_data/list_a_fake.csv)
- [`fake_data/list_b_fake.csv`](https://github.com/jpdenzer/vibe-coding-for-stem-librarians/blob/main/examples/fake_data/list_b_fake.csv)

### The fake data has deliberate "traps"

The two lists contain the kinds of messiness real lists have:

| List A | List B | Same title? |
|:-------|:-------|:------------|
| Journal of Imaginary Chemistry | journal of imaginary chemistry | Capitalization differs |
| Fictional Physics Letters | Fictional Physics Letters**.** | Trailing period |
| **The** Annals of Pretend Biology | Annals of Pretend Biology | Leading "The" |
| Made-Up Materials **&** Methods | Made-Up Materials **and** Methods | "&" vs. "and" |
| `␣␣`Demo Data Science Digest`␣` | Demo Data Science Digest | Extra spaces |
| (column named `title`) | (column named `Title`) | Header capitalization |
| | *(a blank row)* | Missing value |
| | Placeholder Mathematics Review (listed twice) | Duplicate |

A naive exact-match comparison would report most of these as "unique" titles, which is wrong. The script's `normalize()` function handles each one, and **those rules are assumptions you should question**. For example, is ignoring a leading "The" always safe? (What about *The Lancet*?) This is exactly the kind of judgment call covered in [Helping Students](../consultations.md#how-to-check-the-ais-assumptions).

### Run it in Google Colab (no install)

1. Open [colab.research.google.com](https://colab.research.google.com) and click **New notebook**.
2. Paste this into the first cell and press **▶** (or Shift + Enter). It downloads the script and the fake data from this repository:

   ```python
   !mkdir -p fake_data
   !wget -q https://raw.githubusercontent.com/jpdenzer/vibe-coding-for-stem-librarians/main/examples/compare_az_lists.py
   !wget -q -P fake_data https://raw.githubusercontent.com/jpdenzer/vibe-coding-for-stem-librarians/main/examples/fake_data/list_a_fake.csv
   !wget -q -P fake_data https://raw.githubusercontent.com/jpdenzer/vibe-coding-for-stem-librarians/main/examples/fake_data/list_b_fake.csv
   ```

3. In a new cell, run the script:

   ```python
   !python compare_az_lists.py
   ```

4. To save results as a CSV you can download from the folder icon in the sidebar:

   ```python
   !python compare_az_lists.py --out comparison_results.csv
   ```

### Run it on your own computer

If you have Python 3 installed (see the setup tutorials for [Windows](../tutorials/python-windows-setup-guide.md) and [macOS](../tutorials/python-macos-setup-guide.md)), download this repository (green **Code** button → **Download ZIP** on GitHub), unzip it, open a terminal in the `examples` folder, and run:

```bash
python compare_az_lists.py
```

(On some Macs, use `python3` instead of `python`.)

To compare your own files, which should be de-identified and contain a `title` column:

```bash
python compare_az_lists.py my_list_a.csv my_list_b.csv --out comparison_results.csv
```

### Expected output

After a few lines naming the input files and a note about a duplicate in list B, you should see:

```text
List A has 12 unique titles; list B has 10.

Only in list A (6)
------------------
  Hypothetical Geoscience Index
  Invented Ecology Archive
  Mock Marine Science Database
  Notional Neuroscience Abstracts
  Pseudo Pharmacology Portal
  Simulated Statistics Quarterly

Only in list B (4)
------------------
  Example Engineering Encyclopedia
  Fabricated Food Science Files
  Sample Soil Science Collection
  Speculative Astronomy Abstracts

In both lists (6)
-----------------
  Demo Data Science Digest
  Fictional Physics Letters
  Journal of Imaginary Chemistry
  Made-Up Materials & Methods
  Placeholder Mathematics Review
  The Annals of Pretend Biology
```

### Things to try (practice for every rung)

- **Rung 1:** Paste the script into ChatGPT or Gemini and ask, *"What assumptions does this code make about what counts as the same title?"*
- **Rung 2:** Add a row to list B like `Journal of Imaginary Chemistry (Online)`. Is it treated as a match? Ask the AI how to handle it, then decide whether you agree.
- **Rung 3:** Start Claude Code or Codex in a copy of the `examples` folder and ask it to *"add an ISSN column to both fake files and match on ISSN when available, falling back to title."* Review the diff before accepting.
- **Validation:** Before trusting any change, check 3–5 titles by hand against the expected output above.

---

[← Previous: Guardrails](../guardrails.md) · [Next: Real-World Examples →](real-world/)
