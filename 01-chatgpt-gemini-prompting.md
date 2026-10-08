---
title: "01 · Conversational Prompting"
nav_order: 2
description: "The zero-setup starting point: write a good first prompt, get the AI to explain code, and run Python in your browser."
---

# 01 · Conversational Prompting with ChatGPT or Gemini

**Rung: Low** · **Setup: none (just a web browser)** · **Time: about 20 minutes**

This is the bottom rung. You describe what you want in a chat window, the AI writes code, and you copy that code into a place where it can run. Nothing to install, nothing to configure.

---

## What you need

- A web browser (a laptop works best, but a tablet is fine for reading along)
- A free account with one of these chat tools:
  - **ChatGPT**: [chatgpt.com](https://chatgpt.com)
  - **Google Gemini**: [gemini.google.com](https://gemini.google.com)
- A free Google account for **Google Colab**, the place you'll run your code: [colab.research.google.com](https://colab.research.google.com)

> **Check the official docs:** Both ChatGPT and Gemini have free tiers, but which models you get, how many messages you can send, and which features are included all change often. See [ChatGPT pricing](https://openai.com/chatgpt/pricing/) and [Gemini plans](https://gemini.google/subscriptions/) for current details. Your institution may also offer an approved AI tool (such as Microsoft Copilot or Gemini through a campus Google Workspace) with better privacy terms. Ask your IT office.

> **Before you start:** Don't paste patron data, student records, passwords, or licensed vendor content into any AI chat. Make up sample data instead. See [Guardrails](guardrails.md) for details.

---

## Step 1: Write a good first prompt

The biggest mistake beginners make is asking for too little. "Write a Python script to compare two lists" will get you *a* script, but probably not the one you need. The AI fills every gap with a guess.

A good first prompt answers five questions:

| Question | Example |
|:---------|:--------|
| **Who are you / what's the context?** | "I'm a science librarian with no programming experience." |
| **What's the goal?** | "I want to compare two lists of database names and see which names are only on one list." |
| **What does the input look like?** | "Each list is a CSV file with a column called `title`. Here are 3 example rows: …" |
| **What should the output look like?** | "Print three lists: only in A, only in B, and in both. Sort them alphabetically." |
| **Where will it run?** | "I'll run it in Google Colab. Use only standard Python libraries if possible." |

### A weak prompt

```text
Write code to compare two database lists.
```

### A strong prompt

```text
I'm a science librarian with no programming experience. I want a Python
script I can run in Google Colab.

I have two CSV files, list_a.csv and list_b.csv. Each has a column called
"title" with names of STEM databases. Here are a few made-up example rows:

title
Journal of Imaginary Chemistry
Fictional Physics Letters
The Annals of Pretend Biology

Please write a script that:
1. Reads both files.
2. Treats titles as the same even if capitalization or extra spaces differ.
3. Prints titles that are only in list A, only in list B, and in both,
   each sorted alphabetically, with a count for each group.

Use only Python's standard library. Add short comments explaining each
step in plain English, and tell me exactly how to run it in Colab.
```

Notice what the strong prompt does:

- **Uses fake sample rows.** The AI can see the shape of the data without seeing any real data.
- **States the rules.** "Treat capitalization differences as the same" is a decision *you* made, so the AI doesn't have to guess.
- **Asks for comments and run instructions.** You'll need both.

More ready-to-use prompts are on the [Examples](examples/) page.

---

## Step 2: Ask the AI to explain the code

You don't need to understand every line, but you should understand **what the code is doing and what it assumes**. Once you get code back, ask questions like these:

```text
Explain this script to me line by line, as if I've never programmed before.
```

```text
What assumptions does this code make about my data? What would happen if
a title had a typo, an extra space, or "&" instead of "and"?
```

```text
What could go wrong when I run this? What error messages might I see, and
what would each one mean?
```

```text
Is there anything in this code that deletes, overwrites, or sends data
anywhere? Point to the exact lines.
```

The second question is the most important one on this page. Every script makes assumptions, such as which column to read, what counts as a match, and what to do with blank rows. **Those assumptions are where wrong answers come from**, and you are the one who knows whether they fit your data.

---

## Step 3: Run a simple Python script with Google Colab

[Google Colab](https://colab.research.google.com) is a free website that runs Python in your browser. You don't install anything on your computer.

### Your first run

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with a Google account.
2. Click **New notebook** (or **File → New notebook**).
3. You'll see an empty box called a **code cell**. Click inside it and paste this:

   ```python
   titles = ["Fictional Physics Letters", "Journal of Imaginary Chemistry", "Annals of Pretend Biology"]
   for t in sorted(titles):
       print(t)
   print("Total:", len(titles))
   ```

4. Click the **▶ play button** on the left of the cell (or press **Shift + Enter**).
5. The output appears below the cell: three titles in alphabetical order, then `Total: 3`.

That's it. You just ran Python.

### Running code that uses files

Most library tasks need a file, such as a CSV export. In Colab:

1. Click the **folder icon** in the left sidebar.
2. Click the **upload icon** (a page with an up arrow) and choose your file. Use a **fake or de-identified** file while you're learning.
3. The file now appears in the file list. Your code can open it by name, e.g. `list_a.csv`.

> **Good to know:** Files you upload to Colab are deleted when your session ends (usually after you close the tab or stay idle for a while). Download any results you want to keep: right-click the file in the sidebar and choose **Download**.

### Try the demo in Colab

The [Examples](examples/) page has a ready-made demo that compares two fake A–Z lists. It includes copy-and-paste Colab instructions.

### Other no-install options

- **Gemini in Colab:** Colab has a built-in Gemini assistant that can write or explain code right inside the notebook. Look for the Gemini or "Generate" button in a cell.
- **ChatGPT's built-in code running:** ChatGPT can sometimes run Python itself and show you the result, for example when you upload a CSV and ask a question about it. This is handy for quick answers, but you see less of what happened, so ask it to show you the code it ran.
- **Python on your own computer:** You can install Python if your institution allows it. See the tutorials for [Windows](tutorials/python-windows-setup-guide.md) and [macOS](tutorials/python-macos-setup-guide.md). You don't need to yet.

> **Check the official docs:** Colab's free tier has usage limits, and its built-in AI features change regularly. See the [Colab FAQ](https://research.google.com/colaboratory/faq.html).

---

## What this rung is good for

**Good fits:**
- Short scripts under about 50 lines
- One-off data cleanup (deduplicating, reformatting, splitting columns)
- Spreadsheet formulas, regular expressions, and small text transformations
- Learning what code *can* do

**Signs you've outgrown it:**
- You're copying and pasting the same code back and forth more than five or six times
- Your project has more than one file
- You keep losing track of which version of the code is the latest

When that happens, move on to [02 · Iterating & Debugging](02-iterating-and-debugging.md).

---

## Quick reference

- Give **context, goal, input shape, output shape, and where it will run.**
- Use **fake sample rows**, never real data.
- Ask **"What does this code assume about my data?"**
- Run it in **Google Colab**: New notebook → paste → ▶.
- **Check the output against a few rows you know the answer to.**

---

[← Previous: Home](index.md) · [Next: 02 · Iterating & Debugging →](02-iterating-and-debugging.md)
