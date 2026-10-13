---
title: "Tools & Tips"
nav_order: 9
permalink: /tools-and-tips/
description: "Recommended software, hardware, and small habits that make vibe coding easier, all chosen for people with little or no programming background."
---

# Tools & Tips

The guides and tutorials cover the main tools: ChatGPT, Gemini, Claude Code, Codex, Python, and Git. This page collects the **extras**: helpful software, what kind of computer you need, and small habits that save time and frustration.

None of this is required. You can start vibe coding today with only a web browser (see [01 · Conversational Prompting](../01-chatgpt-gemini-prompting.md)).

> **Recommendations, not endorsements:** Software listed here is free (or has a free plan) or comes with your computer. Hardware costs money. Check with your IT department before installing software on a work computer. Tools change often. These suggestions were last checked in **October 2026**.

---

## Recommended software

### A code editor: Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) (VS Code) is a free editor for Windows, macOS, and Linux. Even if the AI writes all the code, it helps to have a comfortable place to **open, read, and compare files**.

- It shows your project's files in a sidebar, so you can see what an AI tool changed.
- Both Claude Code and Codex have VS Code extensions (see [03 · Agentic Tools](../03-claude-code-codex.md)).
- It previews Markdown files and colors code to make it easier to read.

### Version control: Git and GitHub Desktop

Git lets you see and undo every change, which matters most when an AI tool is editing your files. If you'd rather click buttons than type commands, [GitHub Desktop](https://desktop.github.com/) is a free point-and-click app. See [Creating a GitHub Account](../tutorials/creating-a-github-account.md) to get set up.

### A terminal you like

You'll need a terminal for agentic tools and for running Python on your own computer.

- **Windows:** Windows Terminal is included with Windows 11 and is available free from the Microsoft Store for Windows 10. It can open PowerShell and (if you install it) WSL in tabs.
- **macOS:** The built-in **Terminal** app (in Applications → Utilities) is all you need.

### Running code without installing anything: Google Colab

[Google Colab](https://colab.research.google.com/) runs Python in your browser. It's the easiest way to test a script an AI wrote before you install anything. See [01 · Conversational Prompting](../01-chatgpt-gemini-prompting.md#step-3-run-a-simple-python-script-with-google-colab).

### Cleaning messy data: OpenRefine

[OpenRefine](https://openrefine.org/) is a free tool, already popular with librarians, for cleaning and transforming spreadsheet data. It pairs well with vibe coding: sometimes OpenRefine is a faster answer than a script, and it's a good way to double-check what a script produced.

### Dictating prompts: Wispr Flow

[Wispr Flow](https://wisprflow.ai/) is a voice dictation app for Windows, macOS, iPhone, and Android. You speak, and it types cleaned-up text into whatever app you're using: a chat window, a terminal, or an editor. It removes filler words like "um" and fixes punctuation, which makes it well suited to long, detailed prompts. It works with any microphone, including the one built into your laptop (see [A microphone for dictating prompts](#a-microphone-for-dictating-prompts)).

- **Cost:** There is a free plan with a weekly word limit and a paid plan with no limit. Check the website for current prices.
- **Privacy:** Wispr Flow sends your speech to its servers to turn it into text, so it doesn't work offline. Look in the app's settings for the option that controls whether your data can be used to improve its AI models. As with any AI tool, don't dictate patron information or anything else you couldn't paste into a chatbot (see [Guardrails](../guardrails.md)).

### Keeping secrets safe: a password manager

If you use API keys or passwords in a project, store them in a password manager (ask your IT department which one your institution supports), **never** in your code or in a prompt. See [Guardrails](../guardrails.md).

---

## Recommended hardware

### You probably don't need a new computer

The AI models behind ChatGPT, Gemini, Claude Code, and Codex run on the companies' servers, not on your computer. Any reasonably current laptop or desktop that runs a modern web browser well is enough for every rung on this site.

| | Minimum | More comfortable |
|:--|:--|:--|
| **Memory (RAM)** | 8 GB | 16 GB or more, if you keep a browser, an editor, and an agentic tool open at once |
| **Operating system** | A version that still gets security updates | The version listed in each [tutorial](../tutorials/)'s requirements |
| **Internet** | A steady connection | Same. The AI tools don't work offline. |

> **Running AI models on your own computer** (sometimes called "local models") is a different story. It typically needs much more memory and a powerful graphics chip or Apple silicon Mac. It's an advanced topic that this site doesn't cover yet.

### A second monitor

This is the single most useful upgrade. Put the AI chat (or terminal) on one screen and your data, code, or results on the other. You'll spend much less time switching windows, and it's easier to compare what you asked for with what you got.

### A microphone for dictating prompts

Good prompts are often long and detailed, and talking is faster than typing. Both Windows and macOS have free built-in dictation:

- **Windows:** press **Windows key + H** to start voice typing.
- **macOS:** turn on **Dictation** in **System Settings → Keyboard**, then use the shortcut shown there.

For more accurate, polished results, try [Wispr Flow](#dictating-prompts-wispr-flow).

Your laptop's built-in microphone is usually fine. For clearer audio, especially in a shared or noisy office, a small clip-on wireless microphone like the [DJI Mic Mini](https://www.dji.com/mic-mini) makes a big difference:

- **What it is:** a tiny transmitter that clips to your shirt and a small receiver that plugs into your laptop's USB-C port.
- **Why it helps:** the microphone stays close to your mouth, so dictation picks up your voice instead of the room. You can also move around while you talk.
- **Before you buy:** make sure your computer has a USB-C port, or plan on an adapter. After you plug in the receiver, choose it as your input device in your computer's sound settings.

Read the dictated text before you send it, since dictation makes mistakes too.

---

## Small habits that help

### Show file extensions

Computers hide the end of file names (like `.py` or `.csv`) by default. That causes a common beginner problem: a file that looks like `script.py` is really `script.py.txt` and won't run. Turn extensions on:

- **Windows 11:** in File Explorer, choose **View → Show → File name extensions**.
- **macOS:** in Finder, choose **Finder → Settings → Advanced** and check **Show all filename extensions**.

### Take screenshots of errors (carefully)

When something breaks, a screenshot is a quick way to show the AI the problem.

- **Windows:** **Windows key + Shift + S**
- **macOS:** **Command + Shift + 4**

Before you share a screenshot, check it for **patron names, emails, or other private information**. Copying and pasting the error text is often better, because the AI can read it exactly.

### Keep a practice folder

Make one folder, for example `vibe-coding-practice`, for experiments. Only put **copies** of data and fake or sample files in it. This is especially important with agentic tools, which can edit any file in the folder you give them.

### Keep a prompt log

Keep a simple document with the date, the tool and model, your prompt, and whether it worked. It helps you reuse good prompts, and it's the record the [Guardrails checklist](../guardrails.md) asks you to keep.

---

## Have a favorite tool or tip?

This page will grow over time. If something has made vibe coding easier for you, please share it. See [Contributing & Feedback](../CONTRIBUTING.md).

---

[← Previous: Tutorials](../tutorials/) · [Next: Contributing & Feedback →](../CONTRIBUTING.md)
