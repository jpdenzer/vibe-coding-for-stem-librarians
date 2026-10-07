---
title: "03 · Agentic Tools"
nav_order: 4
description: "What agentic coding tools are, how to install and start Claude Code and ChatGPT Codex, and how to use them safely."
---

# 03 · Agentic Tools: Claude Code and ChatGPT Codex

**Rung: High** · **Setup: install a tool and sign in (usually a paid plan)** · **Time: about 45 minutes the first time**

On rungs 01 and 02, *you* are the go-between: you copy code out of the chat, run it, copy errors back in. **Agentic coding tools** cut out that middle step. You give them a folder and a goal, and they can:

- **Read** the files in your project folder
- **Edit** those files or create new ones
- **Run commands**, like running your Python script or installing a package
- **Look at the result and keep going**: if a test fails, they read the error and try a fix, often several times, before reporting back

That's powerful, and it's also why this rung needs the most care. An agent that can edit files can also edit the *wrong* files. Read [Safe practices](#safe-practices) before your first real project.

---

## Is this rung right for you?

**Move up to agentic tools when:**
- Your project has more than one file, or one file that's getting long
- You're tired of copy-and-paste
- You want the AI to test its own work before showing you

**Stay on rungs 01–02 if:**
- Your task is a one-off script under about 50 lines
- You can't install software on your work computer (ask IT first, see below)
- You don't have a paid plan and don't want one

> **Ask before you install:** Many institutions restrict installing software on work computers or limit which AI services may be used with institutional data. Check with your IT or information security office first. This is also a good chance to ask whether your institution already has an approved license.

---

## The two tools covered here

| | **Claude Code** (Anthropic) | **Codex** (OpenAI) |
|:--|:--|:--|
| **What you sign in with** | A Claude account (Pro, Max, Team, or Enterprise plan) or an Anthropic Console (API) account | A ChatGPT account (Plus, Pro, Business, Edu, or Enterprise plan) or an OpenAI API key |
| **Free plan included?** | No, the free Claude plan doesn't include Claude Code | Check current terms; access by plan changes often |
| **Ways to use it** | Terminal, desktop app, VS Code / JetBrains extensions, web | Terminal, desktop app, IDE extension, web (Codex cloud) |
| **Official docs** | [code.claude.com/docs](https://code.claude.com/docs/en/overview) | [Codex docs](https://developers.openai.com/codex) |

> **Check the official docs:** Plans, prices, usage limits, and which plans include these tools change frequently. The install commands below were checked against the official docs in October 2026. Before your first install, compare them with [Claude Code setup](https://code.claude.com/docs/en/setup) and the [Codex CLI docs](https://developers.openai.com/codex/cli).

Other tools work in a similar way (for example GitHub Copilot's agent mode, Cursor, Gemini CLI, and Windsurf). The habits on this page apply to all of them.

---

## Step 0: The bare minimum about the terminal

Both tools are mostly used from a **terminal**, a text window where you type commands. (Both also have desktop apps; see [the no-terminal option](#the-no-terminal-option-desktop-apps) below.) You only need three things:

**1. Open a terminal**
- **Mac:** press **⌘ Command + Space**, type `Terminal`, press **Return**.
- **Windows:** click **Start**, type `PowerShell`, click **Windows PowerShell**.

**2. Go to your project folder** with `cd` ("change directory"). The easy way: type `cd` and a space, then **drag your project folder from Finder or File Explorer into the terminal window**. The folder's location appears. Press **Enter**.

```bash
cd /Users/yourname/Documents/my-project
```

**3. Paste and run commands.** Paste with **⌘ Command + V** (Mac) or **right-click** (Windows terminal), then press **Enter**.

> **New to all of this?** Anthropic has a beginner-friendly [terminal guide](https://code.claude.com/docs/en/terminal-guide) that walks through opening a terminal and pasting commands on each operating system.

---

## Installing and starting Claude Code

> **On Windows?** The [Set Up Claude Code on Windows](tutorials/claude-code-windows.md) tutorial walks through every screen, with troubleshooting.

### 1. Install

Open a terminal and paste the command for your computer:

**Mac, Linux, or Windows Subsystem for Linux (WSL):**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Other options include **Homebrew** on Mac (`brew install --cask claude-code`) and **WinGet** on Windows (`winget install Anthropic.ClaudeCode`). On Windows, installing [Git for Windows](https://git-scm.com/downloads/win) is recommended but optional.

### 2. Check that it worked

Close the terminal, open a **new** one, and run:

```bash
claude --version
```

If you see a version number, you're set. If you see "command not found" or "not recognized," see Anthropic's [installation troubleshooting](https://code.claude.com/docs/en/troubleshoot-install).

### 3. Start it in your project folder and sign in

```bash
cd path/to/your/project-copy
claude
```

The first time, a browser window opens so you can sign in to your Claude account. After that, you'll see a prompt where you type requests in plain English.

> **Check the official docs:** [Claude Code setup](https://code.claude.com/docs/en/setup) · [Quickstart](https://code.claude.com/docs/en/quickstart) · [Plans and pricing](https://claude.com/pricing)

---

## Installing and starting Codex

### 1. Install

**Mac or Linux:**
```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

**Windows PowerShell:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Other options: **npm** (`npm install -g @openai/codex`, requires Node.js) or **Homebrew** on Mac (`brew install --cask codex`).

### 2. Start it in your project folder and sign in

```bash
cd path/to/your/project-copy
codex
```

The first time, choose **Sign in with ChatGPT** and finish signing in in your browser.

> **Check the official docs:** [Codex CLI](https://developers.openai.com/codex/cli) · [Codex on GitHub](https://github.com/openai/codex) · [ChatGPT plans](https://openai.com/chatgpt/pricing/)

---

## The no-terminal option: desktop apps

If the terminal is a dealbreaker, both companies offer **desktop apps** that let you pick a folder and chat with the agent in a normal window:

- **Claude Code:** the [Claude desktop app](https://claude.com/download) has a Code tab. See the [desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart).
- **Codex:** see the [Codex app docs](https://developers.openai.com/codex/app).

Both also have extensions for **Visual Studio Code**, a free code editor that many beginners find friendlier than the terminal because you can see your files and the changes side by side.

---

## Giving the agent a project folder

The agent works on **whatever folder you start it in**, and that folder becomes its workspace. Set it up on purpose:

1. **Make a new folder just for this project**, e.g. `Documents/az-list-comparison/`.
2. **Put in only what the agent needs:** your script (if you have one), **fake or de-identified** sample data, and a short notes file.
3. **Don't start it in a big folder** like your whole `Documents` or `Desktop`. The agent could read anything in there.
4. **Write a short project description.** Both tools read a plain-text instructions file automatically: `CLAUDE.md` for Claude Code and `AGENTS.md` for Codex. Put a few lines in it, for example:

   ```markdown
   # Project: compare two A–Z database lists
   - I'm a librarian, not a programmer. Explain changes in plain English.
   - Use Python's standard library only.
   - Sample data is in fake_data/. Never invent or download real data.
   - Ask before deleting any file.
   ```

### Your first session

Start the tool in your project folder and try:

```text
Look at the files in this folder and explain what's here in plain English.
Don't change anything yet.
```

Then:

```text
Before writing any code, give me a step-by-step plan for comparing the
two CSV files in fake_data/ and listing titles unique to each.
Wait for me to approve the plan.
```

Asking for a **plan first** is one of the best habits on this rung. You can catch a wrong assumption ("it's going to match on ISSN, but half my rows don't have one") before any code exists. Claude Code has a dedicated **plan mode** for this. Codex lets you control what it can do without asking via its `/permissions` command.

More starter prompts: [Examples → Rung 3 prompts](examples/#rung-3-agentic-tools).

---

## Safe practices

These habits matter more than any single prompt.

### 1. Work in a copy

Never point an agent at your only copy of something. Copy the folder first, then start the agent in the **copy**. If anything goes wrong, you can delete the copy and start over.

### 2. Use version control (Git)

**Git** takes snapshots of your folder so you can see exactly what changed and undo it. It's the safety net that makes agentic tools safe to use.

**The easy way:** ask the agent to do it.

```text
Set up git version control in this folder and make a first commit
called "Starting point before any AI changes." Explain each command you run.
```

**Or do it yourself** (after [installing Git](https://git-scm.com/downloads) if needed):

```bash
git init
git add .
git commit -m "Starting point before any AI changes"
```

**Prefer buttons to commands?** [GitHub Desktop](https://desktop.github.com/) is a free app that does the same thing with a point-and-click interface, and it works without a GitHub account for local-only projects.

After each step that works, commit again (or ask the agent to). Then you can always get back to the last good version.

### 3. Review changes before accepting them

- **Read the permission prompts.** By default, both tools ask before editing files or running commands. Read what it wants to do before you say yes. If you don't understand a command, answer *"Explain what that command does first."*
- **Look at the diff.** A *diff* shows exactly which lines were added (often green) and removed (often red). Ask: *"Show me a summary of every change you made and why."* or run `git diff` yourself.
- **Run it yourself.** Don't take "All tests pass ✅" on faith. Run the script on data where you already know the right answer.
- **Avoid "skip all permissions" or "full access" modes** until you're experienced, and even then only in a throwaway copy. These modes let the agent run any command without asking.

### 4. Keep secrets and sensitive data out of the folder

The agent can read everything in the folder you give it, and what it reads is sent to the AI company's servers. **No passwords, API keys, proxy credentials, patron or student data, or licensed vendor files.** See [Guardrails](guardrails.md).

### 5. Watch your usage

Agents can use a lot of your plan's usage on one task, especially if they get stuck in a loop. If it's been working for a long time without progress, interrupt it (press **Esc** in both tools) and use the advice from [going in circles](02-iterating-and-debugging.md#how-to-tell-when-the-ai-is-going-in-circles).

---

## Quick reference

- **Agentic = reads files, runs commands, edits code, iterates on its own.**
- **Ask IT before installing.** Check what's approved.
- Install → `claude` or `codex` in your **project copy** → sign in in your browser.
- **Small, dedicated project folder** with fake data and a `CLAUDE.md` / `AGENTS.md` notes file.
- **Plan first, then code.**
- **Git commit before and after each change.** Review the diff. Run it yourself.

---

[← Previous: 02 · Iterating & Debugging](02-iterating-and-debugging.md) · [Next: Helping Students →](consultations.md)
