---
title: "Setting Up Codex on macOS"
parent: "Tutorials"
nav_order: 4
description: "Step-by-step guide to installing and configuring OpenAI Codex on a Mac, using the ChatGPT desktop app or the command line."
---

# Setting Up Codex on macOS

Codex is OpenAI's coding agent. It can read your project, make changes, and run commands on your behalf. On a Mac you can use it in the ChatGPT desktop app, in the command line (CLI), or in an editor extension. This guide walks through the desktop app and the CLI, explains how sandboxing and permissions work on macOS, and covers troubleshooting.

**New to agentic tools?** Read [03 · Agentic Tools](../03-claude-code-codex.md) first. It explains what Codex does and why the safety habits matter.

## Rung

**High (agentic). Beginner-friendly** for the desktop app path. The command-line path is optional and assumes you can open Terminal and paste a command into it.

## Time

**About 10 to 15 minutes** for the desktop app. Allow **an extra 10 minutes** if you also install the command-line tool and developer tools.

## You Will Need

- A Mac with a version of macOS supported by the current ChatGPT desktop app. The download page lists the current requirements. As of October 2026, OpenAI's docs list the desktop app for **Apple silicon** Macs. On an older Intel Mac, use the [Codex CLI](#path-b-the-codex-cli) instead.
- A **ChatGPT account** to sign in with. OpenAI's [pricing page](https://learn.chatgpt.com/codex/pricing) lists which plans include Codex. You can also use Codex with an API key, but some features might not be available that way.
- An internet connection
- A project folder to work in (any folder with a few files works for a first test)
- **Permission to install apps on your Mac.** On a work computer, check with your IT office first. Your institution may also have rules about which AI tools can be used.
- Optional: [Homebrew](https://brew.sh/), if you prefer to install with it
- Optional: [Git](creating-a-github-account.md#step-7-install-git), so Codex can show and revert changes

## Last Check

**October 7, 2026.** Commands and options were checked against OpenAI's Codex documentation on this date. Codex changes quickly, so verify against the [official Codex docs](https://learn.chatgpt.com/codex/quickstart) if something looks different on your system.

## Table of Contents

- [Choose Your Setup](#choose-your-setup)
- [Path A: The ChatGPT Desktop App](#path-a-the-chatgpt-desktop-app)
  - [Step 1: Install the Desktop App](#step-1-install-the-desktop-app)
  - [Step 2: Sign In](#step-2-sign-in)
  - [Step 3: Open a Project and Start a Task](#step-3-open-a-project-and-start-a-task)
  - [Step 4: Check Your Permissions Setting](#step-4-check-your-permissions-setting)
  - [Step 5: Install Useful Developer Tools](#step-5-install-useful-developer-tools)
- [Path B: The Codex CLI](#path-b-the-codex-cli)
- [How Sandboxing and Permissions Work on macOS](#how-sandboxing-and-permissions-work-on-macos)
- [Setting Defaults in config.toml](#setting-defaults-in-configtoml)
- [Using Codex in an Editor](#using-codex-in-an-editor)
- [Staying Safe While Using Codex](#staying-safe-while-using-codex)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Choose Your Setup

| Option | Best for | Where it runs |
|--------|----------|---------------|
| **ChatGPT desktop app** | Most people. A graphical app for working across projects, running parallel chats, creating files, and reviewing results | On your Mac |
| **Codex CLI** | People who prefer the terminal, scripting, or automation | In Terminal, on your Mac |
| **IDE extension** | Working inside an editor such as VS Code | Inside the editor |

If you are unsure, start with the **desktop app** (Path A). You can add the CLI later.

---

## Path A: The ChatGPT Desktop App

### Step 1: Install the Desktop App

1. Go to [chatgpt.com/download](https://chatgpt.com/download/) and download the app for **macOS**.
2. Open the downloaded file and follow the on-screen steps to install the app. If it arrives as a disk image, drag the app into your **Applications** folder.
3. Open the app from **Applications** or Spotlight (`Cmd + Space`, then type `ChatGPT`).
4. If macOS asks whether you want to open an app downloaded from the internet, choose **Open**.

### Step 2: Sign In

1. Open the ChatGPT desktop app.
2. Sign in with your ChatGPT account.

You can also use Codex with an API key, but some features might not be available. See OpenAI's [authentication options](https://learn.chatgpt.com/codex/auth) for details.

### Step 3: Open a Project and Start a Task

1. In the app, start a chat, create a project, or open a folder. Codex can read and modify files in the folder you choose. For your first time, use a new, empty **practice folder** (for example, `Documents/codex-practice`), never your whole home folder, Documents, or Desktop.
2. Choose **Codex** rather than **ChatGPT** for software development with codebase context and developer tools. (The same app also offers **ChatGPT** for chat and **Work** for documents and research.)
3. Start with **New chat**. For a quick question, point to **New chat** and select the **Quick chat** icon on its right.
4. Send a first message such as:

   ```text
   Tell me about this project
   ```

> **Tip:** Create Git checkpoints (commits) before and after a task so you can revert changes. See the [Creating a GitHub Account](creating-a-github-account.md) tutorial if you are new to Git.

### Step 4: Check Your Permissions Setting

Beneath the message box, the app has a permissions control. Depending on your configuration, the menu can include:

| Option | What it does |
|--------|--------------|
| **Ask for approval** | Codex works inside the sandbox and stops to ask when it needs to go beyond it |
| **Approve for me** | Eligible approval requests are reviewed automatically instead of by you |
| **Full access** | Codex runs without sandbox restrictions. Use only when you understand the risk |
| Named or custom profiles | Permission profiles you or your organization have set up |

For your first sessions, choose **Ask for approval** and review what Codex asks to do. See [How Sandboxing and Permissions Work on macOS](#how-sandboxing-and-permissions-work-on-macos) for what this means.

### Step 5: Install Useful Developer Tools

Codex works best when common developer tools are installed. These are my suggestions for a Mac, installed with Homebrew. If you do not have Homebrew, see [brew.sh](https://brew.sh/) first.

```bash
brew install git
brew install node
brew install python
brew install gh
```

| Tool | Why it helps |
|------|--------------|
| **Git** | Lets Codex and the app track, show, and revert changes |
| **Node.js** | A common tool used by many projects and by agents working on them |
| **Python** | A common tool used by many projects and by agents working on them |
| **GitHub CLI** | Powers GitHub-related workflows from the terminal |

After installing the GitHub CLI, sign in:

```bash
gh auth login
```

You only need the tools your projects use. Git is the most important one.

---

## Path B: The Codex CLI

The Codex CLI runs in Terminal. It works against your local repository, and you choose the model, permissions, and commands.

### Step 1: Open Terminal

Press `Cmd + Space`, type `Terminal`, and press **Return**.

### Step 2: Install Codex

Choose **one** of these methods.

**Option A: Standalone installer**

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

**Option B: Homebrew**

```bash
brew install --cask codex
```

**Option C: npm**

If you already have Node.js installed:

```bash
npm install -g @openai/codex
```

When the install finishes, close Terminal and open a new window so your shell picks up the change.

### Step 3: Run Codex and Sign In

1. In Terminal, move to a project folder. For your first time, make a new, empty **practice folder** so Codex can't touch anything important:

   ```bash
   mkdir -p ~/Documents/codex-practice
   cd ~/Documents/codex-practice
   ```

2. Start Codex:

   ```bash
   codex
   ```

3. The first time you run it, choose **Sign in with ChatGPT** or another available sign-in method, and follow the prompts.

### Step 4: Start Your First Task

Describe what you want in plain language:

```text
Tell me about this project
```

In an empty practice folder, try building something small instead:

```text
Create a file called hello.html with a simple web page that says
"Hello from the library!" in large text. Explain what you did.
```

### Useful CLI Commands

| Command | What it does |
|---------|--------------|
| `codex` | Starts an interactive session in the current folder |
| `codex resume` | Reopens a recent chat from the current repository |
| `codex --search` | Switches a run to live web search |
| `codex --image <file>` | Passes an image, such as an error screenshot, with your first prompt |
| `codex exec` | Runs Codex non-interactively, for scripts and automation |
| `codex mcp` | Adds and manages MCP servers that connect Codex to external tools |
| `codex completion` | Generates shell completions |
| `/permissions` | Inside a session, opens the permissions picker to change when Codex can edit files or run commands without asking |

### Updating the CLI

| Installed with | Update command |
|----------------|----------------|
| Standalone installer | Re-run the install command from [Step 2](#step-2-install-codex) |
| Homebrew | `brew upgrade --cask codex` |
| npm | `npm install -g @openai/codex` |

---

## How Sandboxing and Permissions Work on macOS

The sandbox is the boundary that lets Codex act on its own without unrestricted access to your Mac. When Codex runs commands in the desktop app, the CLI, or the IDE extension, those commands run inside a constrained environment instead of with full access.

On macOS, sandboxing works out of the box using Apple's built-in **Seatbelt** framework. You do not need to install anything extra or approve an administrator prompt.

Two controls work together:

| Control | What it decides |
|---------|-----------------|
| **Sandbox** | The technical limits: which files commands can change and whether they can use the network |
| **Approval policy** | When Codex must stop and ask before crossing those limits |

The sandbox applies to the commands Codex starts, not just its built-in file operations. If Codex runs `git`, a package manager, or a test runner, those commands inherit the same limits.

### Sandbox Modes

| Mode | Behavior |
|------|----------|
| `read-only` | Codex can inspect files but cannot edit files or run commands without approval |
| `workspace-write` | Codex can read files, edit inside the workspace, and run routine local commands inside that boundary. This is the default low-friction mode for local work |
| `danger-full-access` | Codex runs with no sandbox restrictions. This removes the filesystem and network boundaries |

### Approval Policies

| Policy | Behavior |
|--------|----------|
| `on-request` | Codex works inside the sandbox and asks when it needs to go beyond it |
| `never` | Codex does not stop for approval prompts |

**Full access** means `danger-full-access` together with `never`. The lower-risk setup for local work is `workspace-write` together with `on-request`.

> **Tip:** When an approval offers different scopes, such as approving once or for the whole session, choose the narrowest scope that lets the task continue. Use separate projects or Git worktrees instead of broadening access across unrelated repositories.

---

## Setting Defaults in config.toml

To start with the same behavior every time, set defaults in Codex's `config.toml` file. The settings that control sandboxing are:

```toml
sandbox_mode = "workspace-write"
approval_policy = "on-request"
approvals_reviewer = "user"
```

| Key | What it controls |
|-----|------------------|
| `sandbox_mode` | `read-only`, `workspace-write`, or `danger-full-access` |
| `approval_policy` | `on-request` or `never` |
| `approvals_reviewer` | `user` (you review approval prompts, the default) or `auto_review` (eligible prompts go to a reviewer agent) |
| `sandbox_workspace_write.writable_roots` | Extra folders Codex may write to, without removing the sandbox entirely |

The Codex home folder is where Codex keeps its configuration. On a Mac this is typically `~/.codex`, so the file is usually `~/.codex/config.toml`. See OpenAI's [config basics](https://learn.chatgpt.com/codex/config-file/config-basic) to confirm the location on your version, and the [configuration reference](https://learn.chatgpt.com/codex/config-file/config-reference) for exact keys.

To open the folder from Terminal:

```bash
open ~/.codex
```

If you need to allow a specific exception, use [rules](https://learn.chatgpt.com/codex/agent-configuration/rules), which let you allow, prompt for, or forbid particular command prefixes outside the sandbox. This is usually better than broadly widening access.

---

## Using Codex in an Editor

Codex also has an IDE extension. See OpenAI's [IDE extension guide](https://learn.chatgpt.com/codex/ide) for installation and settings. If you use VS Code, download it from [code.visualstudio.com](https://code.visualstudio.com/) first.

You can also run `codex` in an editor's integrated terminal. In VS Code, open it with `` Ctrl + ` `` (the backtick key, usually above Tab).

---

## Staying Safe While Using Codex

- **Keep the sandbox on.** Use **Ask for approval** (or the `workspace-write` plus `on-request` setup) while you are learning.
- **Be careful with full access.** `danger-full-access` with `never` removes the filesystem and network limits, so Codex can act on anything your account can reach.
- **Work in a copy.** Point Codex at a copy of your project folder, never the original.
- **Use Git checkpoints.** Commit before and after tasks so you can revert.
- **Review changes before you accept them,** especially on projects that matter to you.
- **Do not share secrets.** Do not paste passwords or keys into prompts or commit them to a repository.
- **Keep sensitive data out of the folder.** No patron or student data, proxy details, or licensed vendor files. See [Guardrails](../guardrails.md).

See OpenAI's [agent approvals and security guide](https://learn.chatgpt.com/codex/agent-approvals-security) for more on tuning approvals.

---

## Troubleshooting

### `codex: command not found`

- Close Terminal and open a new window so your shell picks up the install location, then run:

  ```bash
  codex --version
  ```

- Check whether the program is on your path:

  ```bash
  which codex || echo "codex not found"
  ```

- If it is still not found, reinstall with one of the methods in [Path B](#path-b-the-codex-cli).

### The Install Command Fails

If the `curl` command fails, the download may be blocked by your network, proxy, or VPN. Try again on a different network or without a VPN, or install with Homebrew or npm instead. On a work computer, contact your IT office rather than trying to work around a block.

### macOS Says the App Cannot Be Opened

If macOS blocks the app because it was downloaded from the internet, open **System Settings > Privacy & Security**, scroll down to the message about the blocked app, and click **Open Anyway**. On older versions of macOS, you can instead hold **Control**, click the app in **Applications**, and choose **Open**. Only do this for a download you got from OpenAI's official download page.

### Codex Keeps Asking for Approval

That is the sandbox working as designed. When a task goes beyond the sandbox, Codex stops and asks. To reduce prompts safely:

- Approve at the narrowest scope that lets the task continue
- Add specific exceptions with [rules](https://learn.chatgpt.com/codex/agent-configuration/rules)
- Add extra writable folders with `sandbox_workspace_write.writable_roots`

Avoid switching to full access just to stop the prompts.

### Codex Cannot Write to a Folder

By default, Codex can edit inside the workspace (the project folder you opened). To let it change other folders, add them as writable roots in `config.toml`, or work from a project folder that contains everything it needs.

### Sandboxed Commands Cannot Reach the Network

Some local chats intentionally run without outbound network access, depending on your permissions settings. Check your permissions mode. If a task needs the network, Codex asks for approval.

### I Updated Codex and It Behaves Differently

Check the [Codex changelog](https://learn.chatgpt.com/codex/changelog) for recent changes.

### Homebrew Cannot Find the Cask

Update Homebrew and try again:

```bash
brew update
brew install --cask codex
```

### I Cannot Sign In

- Confirm you are signing in with the right ChatGPT account and that your plan includes Codex. See the [pricing page](https://learn.chatgpt.com/codex/pricing).
- Make sure your default browser opens so you can complete the sign-in.
- Review OpenAI's [authentication options](https://learn.chatgpt.com/codex/auth).

---

## Additional Resources

- [Codex quickstart](https://learn.chatgpt.com/codex/quickstart)
- [ChatGPT desktop app](https://learn.chatgpt.com/codex/app)
- [Codex CLI](https://learn.chatgpt.com/codex/cli)
- [Codex IDE extension](https://learn.chatgpt.com/codex/ide)
- [Sandboxing](https://learn.chatgpt.com/codex/sandboxing)
- [Agent approvals and security](https://learn.chatgpt.com/codex/agent-approvals-security)
- [Config basics](https://learn.chatgpt.com/codex/config-file/config-basic)
- [Authentication options](https://learn.chatgpt.com/codex/auth)
- [Codex pricing](https://learn.chatgpt.com/codex/pricing)
- [Codex changelog](https://learn.chatgpt.com/codex/changelog)

---

*Last updated: October 2026. Codex is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Codex on Windows](codex-windows-setup-guide.md) · [Next: Setting Up WSL on Windows →](wsl-setup-guide.md)
