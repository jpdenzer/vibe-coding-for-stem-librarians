---
title: "Setting Up Codex on Windows"
parent: "Tutorials"
nav_order: 3
description: "Step-by-step guide to installing and configuring OpenAI Codex on Windows, using the desktop app, the command line, or WSL."
---

# Setting Up Codex on Windows

Codex is OpenAI's coding agent. It can read your project, make changes, and run commands on your behalf. On Windows you can use it in the ChatGPT desktop app, in the command line (CLI), in an editor extension, or inside Windows Subsystem for Linux (WSL). This guide walks through the desktop app and the CLI, then covers the Windows sandbox, WSL, and troubleshooting.

**New to agentic tools?** Read [03 · Agentic Tools](../03-claude-code-codex.md) first. It explains what Codex does and why the safety habits matter.

## Rung

**High (agentic). Beginner-friendly** for the desktop app path. The command-line and WSL paths are optional and assume you can open PowerShell and paste a command into it.

## Time

**About 15 to 20 minutes** for the desktop app, including the sandbox setup. Allow **an extra 15 to 30 minutes** if you also install the command-line tool, developer tools, or WSL.

## You Will Need

- A computer running **Windows 11** (recommended) or a recent, fully updated **Windows 10** (version 1809 or newer, best effort)
- Administrator approval on the machine, because the recommended sandbox setup asks for it. **On a work computer, check with your IT office first.** The sandbox setup creates local users and firewall rules, which many institutions restrict.
- `winget` (Windows Package Manager), which comes with current versions of Windows
- A **ChatGPT account** to sign in with. OpenAI's [pricing page](https://learn.chatgpt.com/codex/pricing) lists which plans include Codex. You can also use Codex with an API key, but some features might not be available that way.
- An internet connection
- A project folder to work in (any folder with a few files works for a first test)
- Optional: [Git](creating-a-github-account.md#step-7-install-git) installed, so Codex can show and revert changes

## Last Check

**October 7, 2026.** Commands and options were checked against OpenAI's Codex documentation on this date. Codex changes quickly, so verify against the [official Codex docs](https://learn.chatgpt.com/codex/quickstart) if something looks different on your system.

## Table of Contents

- [Choose Your Setup](#choose-your-setup)
- [Prerequisites](#prerequisites)
- [Path A: The ChatGPT Desktop App](#path-a-the-chatgpt-desktop-app)
  - [Step 1: Install the Desktop App](#step-1-install-the-desktop-app)
  - [Step 2: Sign In](#step-2-sign-in)
  - [Step 3: Set Up the Agent Sandbox](#step-3-set-up-the-agent-sandbox)
  - [Step 4: Open a Project and Start a Task](#step-4-open-a-project-and-start-a-task)
  - [Step 5: Install Useful Developer Tools](#step-5-install-useful-developer-tools)
- [Path B: The Codex CLI](#path-b-the-codex-cli)
- [Understanding the Windows Sandbox](#understanding-the-windows-sandbox)
- [Using Codex with WSL](#using-codex-with-wsl)
- [Customizing the Desktop App](#customizing-the-desktop-app)
- [Staying Safe While Using Codex](#staying-safe-while-using-codex)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Choose Your Setup

| Option | Best for | Where it runs |
|--------|----------|---------------|
| **ChatGPT desktop app** | Most people. A graphical app with projects, parallel chats, review panel, and built-in browser | Natively on Windows (PowerShell with a Windows sandbox), or in WSL2 if you choose |
| **Codex CLI** | People who prefer the terminal, scripting, or automation | In your terminal, natively on Windows or inside WSL |
| **IDE extension** | Working inside an editor such as VS Code | Inside the editor |
| **WSL (Windows Subsystem for Linux)** | Linux-native tools, or when your projects already live in WSL | Inside your Linux distribution |

If you are unsure, start with the **desktop app** (Path A). OpenAI recommends using the native Windows sandbox by default, and choosing WSL when you need Linux-native tooling, your workflow already lives in WSL2, or neither native sandbox mode meets your needs.

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Windows 11 | Recommended. The best baseline for Codex on Windows |
| Windows 10 | Best effort. Needs version 1809 or newer, because Codex depends on modern console support (ConPTY). Older builds are not recommended |
| `winget` | Should be available. If it is missing, update Windows or install the Windows Package Manager first |
| Administrator approval | The recommended native sandbox depends on an administrator-approved setup step |
| Managed devices | Some company-managed computers block the required setup steps even when the Windows version is fine. See [Troubleshooting](#troubleshooting) |

To check your Windows version, press **Win + R**, type `winver`, and press **Enter**.

---

## Path A: The ChatGPT Desktop App

### Step 1: Install the Desktop App

Use either method.

**Option 1: Microsoft Store download**

Download the [ChatGPT desktop app for Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) and run the installer.

**Option 2: Command line**

Open PowerShell and run:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

For company-wide rollouts, see OpenAI's [Windows app deployment guide](https://learn.chatgpt.com/codex/enterprise/windows-deployment).

### Step 2: Sign In

1. Open the ChatGPT desktop app from the Start menu.
2. Sign in with your ChatGPT account.

You can also use Codex with an API key, but some features might not be available. See OpenAI's [authentication options](https://learn.chatgpt.com/codex/auth) for details.

### Step 3: Set Up the Agent Sandbox

When you first use Codex natively on Windows, the app asks you to **set up the agent sandbox**. A sandbox keeps Codex inside your working folder and blocks network access unless you approve it.

1. When you see **Set up Agent sandbox to continue**, click **Set up**.
2. **Approve the Windows administrator (UAC) prompt.** The recommended sandbox needs this to create low-privilege sandbox users and apply firewall and permission rules.

If setup succeeds, you are using the stronger **elevated** sandbox. If it cannot finish, Codex may fall back to the weaker **unelevated** sandbox. See [Understanding the Windows Sandbox](#understanding-the-windows-sandbox) and [Troubleshooting](#troubleshooting).

> **Important:** To apply sandbox protections, select **Ask for approval** beneath the message box before you send messages to Codex.

### Step 4: Open a Project and Start a Task

1. In the app, select **Codex** from the ChatGPT dropdown. (The same app also offers **ChatGPT** for chat and **Work** for documents and research.)
2. Start a chat, create a project, or open a folder. Codex can read and modify files in the folder you choose. For your first time, use a new, empty **practice folder** (for example, `Documents\codex-practice`), never your whole Documents folder or Desktop.
3. Send a first message such as:

   ```text
   Tell me about this project
   ```

To add a project from WSL, click **Add new project** (or press `Ctrl + O`) and type `\\wsl$\` into the file window. For details, see [Using Codex with WSL](#using-codex-with-wsl).

> **Tip:** Create Git checkpoints (commits) before and after a task so you can revert changes. See the [Creating a GitHub Account](creating-a-github-account.md) tutorial if you are new to Git.

### Step 5: Install Useful Developer Tools

Codex works best when a few common tools are installed. OpenAI suggests these, installed with `winget`. Paste the lines you want into PowerShell, or into the app's integrated terminal:

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

| Tool | Why it helps |
|------|--------------|
| **Git** | Powers the review panel and lets you inspect or revert changes |
| **Node.js** | A common tool the agent uses to work efficiently |
| **Python** | A common tool the agent uses to work efficiently |
| **.NET SDK** | Useful if you build native Windows apps |
| **GitHub CLI** | Powers GitHub features in the app |

After installing the GitHub CLI, run:

```powershell
gh auth login
```

This turns on the app's GitHub features. If you need a different Python or .NET version, change the package ID to the version you want. You only need the tools your projects use. Git is the most important one.

---

## Path B: The Codex CLI

The Codex CLI runs in your terminal. It works against your local repository, and you choose the model, permissions, and commands.

### Step 1: Install Codex

Open a **new PowerShell window** and run the standalone installer for Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

**Alternative: install with npm**

If you already have Node.js installed:

```bash
npm install -g @openai/codex
```

### Step 2: Run Codex and Sign In

1. In PowerShell, move to a project folder. For your first time, make a new, empty **practice folder** so Codex can't touch anything important:

   ```powershell
   mkdir "$env:USERPROFILE\Documents\codex-practice"
   cd "$env:USERPROFILE\Documents\codex-practice"
   ```

2. Start Codex:

   ```powershell
   codex
   ```

3. The first time you run it, choose **Sign in with ChatGPT** or another available sign-in method, and follow the prompts.

### Step 3: Start Your First Task

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
| `/permissions` | Inside a session, choose when Codex can edit files or run commands without asking |

### Updating the CLI

Re-run the same install command you used originally. For example, for the standalone installer:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

For npm installs, run `npm install -g @openai/codex` again.

---

## Understanding the Windows Sandbox

When you run Codex natively on Windows, agent mode uses a **Windows sandbox**. It blocks file writes outside your working folder and prevents network access without your explicit approval.

There are two native modes:

| Mode | What it does | When to use it |
|------|--------------|----------------|
| `elevated` | Uses dedicated lower-privilege sandbox users, filesystem permission boundaries, firewall rules, and local policy changes | **Preferred.** Use this whenever it works |
| `unelevated` | Runs commands with a restricted Windows token derived from your user, with permission-list file boundaries and weaker offline controls | **Fallback** when administrator-approved setup is blocked by local or company policy |

If both are available, use `elevated`.

### Choose a Mode in the Config File

The mode is controlled in Codex's `config.toml` file with this setting:

```toml
[windows]
sandbox = "elevated"   # or "unelevated"
```

The Windows app uses the same Codex home folder as native Codex on Windows, which is `%USERPROFILE%\.codex` by default. Look for `config.toml` there, or see OpenAI's [config basics](https://learn.chatgpt.com/codex/config-file/config-basic) for the exact location on your version.

### Give the Sandbox Access to Another Folder

If a command fails because the sandbox cannot read a folder, run this inside Codex, using a real absolute path:

```text
/sandbox-add-read-dir C:\absolute\directory\path
```

The folder must already exist. After it succeeds, later sandboxed commands can read it for the rest of the current session.

---

## Using Codex with WSL

Choose WSL when you need Linux-native tooling, your projects already live in WSL2, or neither native sandbox mode works for you.

> **Note:** WSL1 is not supported. WSL1 worked through Codex 0.114. Starting with Codex 0.115, the Linux sandbox moved to bubblewrap, so you need **WSL 2**.

If you have not installed WSL yet, follow the [Setting Up WSL on Windows](wsl-setup-guide.md) tutorial.

### Option 1: Keep the Windows App, Run the Agent in WSL

1. Open the desktop app's **Settings**.
2. Switch the agent from **Windows native** to **WSL**.
3. **Restart the app.** The change does not take effect until you restart. Your projects stay in place.

You choose the integrated terminal separately. You can keep the agent in WSL and still use PowerShell in the terminal, or use WSL for both.

### Option 2: Use the Codex CLI Inside WSL

From an elevated PowerShell, install WSL and open a shell (skip this if WSL is already set up):

```powershell
wsl --install
wsl
```

Then, inside your WSL shell, install and run Codex:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex
```

### Where to Keep Your Projects

| Situation | Recommendation |
|-----------|----------------|
| Agent runs inside WSL | Keep repositories under your Linux home folder, such as `~/code/my-app`. This is faster and avoids symlink and permission issues. Avoid `/mnt/c/...` for heavy work |
| Agent runs natively on Windows, and you also use WSL | Keep projects on your Windows drive and open them from WSL through `/mnt/<drive>/...`. This is more reliable than opening projects from the WSL filesystem |

For example, to clone a repository inside WSL:

```bash
mkdir -p ~/code && cd ~/code
git clone https://github.com/your/repo.git
cd repo
```

### Open a WSL Project in VS Code

With the VS Code WSL extension installed, run this from your WSL terminal:

```bash
cd ~/code/your-project
code .
```

You should see **WSL: your-distro** in the bottom-left status bar. For editor setup, see [Use Visual Studio Code with WSL](wsl-setup-guide.md#use-visual-studio-code-with-wsl) in the WSL tutorial.

### Share Settings Between the Windows App and WSL

The Windows app keeps its settings, sign-in, and session history in `%USERPROFILE%\.codex`. The CLI in WSL uses your Linux home folder by default, so the two do not share anything automatically. To make WSL use the Windows folder, set `CODEX_HOME` in your WSL shell:

```bash
export CODEX_HOME=/mnt/c/Users/<windows-user>/.codex
```

Replace `<windows-user>` with your Windows username. To make it permanent, add that line to `~/.bashrc` or `~/.zshrc`.

---

## Customizing the Desktop App

### Preferred Editor

Choose a default app for the **Open** button, such as Visual Studio, VS Code, or another editor. You can override this for individual projects.

### Integrated Terminal

Choose the default terminal. Options depend on what you have installed and can include PowerShell, Command Prompt, Git Bash, and WSL. This applies only to new terminal sessions, so restart the app or start a new chat to see the change.

### Run Codex with Elevated Permissions

If you need Codex to run commands with administrator rights, start the desktop app itself as an administrator: open the Start menu, find the app, and choose **Run as administrator**. The Codex agent inherits that permission level. Use this sparingly.

> **Caution:** An agent running as administrator can change anything on your computer. Avoid this on work computers, and never combine it with full access mode.

---

## Staying Safe While Using Codex

- **Keep the sandbox on.** Select **Ask for approval** before sending messages so sandbox protections apply.
- **Be careful with full access mode.** Running Codex in full access mode means it is not limited to your project folder and might perform unintentional destructive actions that lead to data loss. For safer automation, keep sandbox boundaries and use [rules](https://learn.chatgpt.com/codex/agent-configuration/rules) for specific exceptions.
- **Work in a copy.** Point Codex at a copy of your project folder, never the original.
- **Use Git checkpoints.** Commit before and after tasks so you can revert.
- **Review changes before you accept them,** especially on projects that matter to you.
- **Do not share secrets.** Do not paste passwords or keys into prompts or commit them to a repository.
- **Keep sensitive data out of the folder.** No patron or student data, proxy details, or licensed vendor files. See [Guardrails](../guardrails.md).

See OpenAI's [agent approvals and security guide](https://learn.chatgpt.com/codex/agent-approvals-security) for how to tune approvals.

---

## Troubleshooting

### Sandbox Setup Failed

The `elevated` setup usually fails for one of these reasons:

- You declined the Windows administrator (UAC) prompt
- The machine does not allow local user or group creation
- The machine does not allow firewall rule changes
- The machine blocks the logon rights the sandbox users need
- A company policy blocks part of the setup

Try these in order:

1. Run the `elevated` sandbox setup again and approve the administrator prompt.
2. On a work computer, ask IT whether the device allows administrator-approved setup for local user and group creation, firewall configuration, and the required sandbox-user logon rights.
3. If it still fails, use the `unelevated` sandbox so you can keep working while the problem is investigated.

### Codex Switched Me to the Unelevated Sandbox

This means the stronger `elevated` setup could not finish on your machine. Codex still runs sandboxed, but with weaker network isolation and without the separate sandbox-user boundary. Treat it as a fallback. On a work computer, the best long-term fix is usually to get `elevated` working with your IT team's help.

### Windows Error 1385

Windows is denying the logon type the sandbox user needs to start a command. Codex probably created the sandbox users, but a Windows policy is blocking them from launching commands. Ask IT whether the device policy grants the required logon rights to the Codex-created sandbox users. Use the `unelevated` sandbox in the meantime.

### Warning: Some Folders Are Writable by Everyone

The Windows permissions on those folders are too broad for the sandbox to fully protect them. Review the folders Codex lists, remove `Everyone` write access if that is appropriate, and restart Codex or re-run the sandbox setup. Ask IT if you are unsure how to change permissions.

### Sandboxed Commands Cannot Reach the Network

Some chats intentionally run without outbound network access, depending on the permissions mode. Check whether the task was meant to run with network disabled. If you expected access, restart Codex and try again.

### The Sandbox Worked Before and Then Stopped

This can happen after moving a repository, changing machine permissions, or a Windows policy change. Restart Codex, try the `elevated` setup again, and use `unelevated` as a temporary fallback if needed.

### PowerShell Blocks Commands (Execution Policy Error)

If you have not used tools such as Node.js or `npm` in PowerShell before, you may see an error like:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

A common fix is to set the execution policy to `RemoteSigned` for your own user account. Adding `-Scope CurrentUser` means you don't need administrator rights and the change doesn't affect other users:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Read Microsoft's [execution policy guide](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) before changing this setting. On a work computer, this may be controlled by IT policy.

### Git Features Are Unavailable

If Git is not installed natively on Windows, the app cannot use some features. Install it:

```powershell
winget install Git.Git
```

### Git Is Not Detected for Projects Opened from `\\wsl$`

If you use the Windows-native agent with a project that is also reachable from WSL, the most reliable workaround is to store the project on your Windows drive and access it from WSL through `/mnt/<drive>/...`.

### The IDE Extension Is Installed but Unresponsive

Your system may be missing C++ development tools that some native dependencies need. Install:

- Visual Studio Build Tools (C++ workload)
- Microsoft Visual C++ Redistributable (x64)

With `winget`:

```powershell
winget install --id Microsoft.VisualStudio.2022.BuildTools -e
```

Then fully restart VS Code.

### `codex` Is Not Found

- **In PowerShell:** Close PowerShell and open a new window so it picks up the install location, then try `codex --version`.
- **In WSL or VS Code in WSL:** Check whether the program is on your path:

  ```bash
  which codex || echo "codex not found"
  ```

  If it is not found, reinstall it inside WSL with the command in [Using Codex with WSL](#using-codex-with-wsl).

### Large Repositories Feel Slow in WSL

Make sure the repository is not under `/mnt/c`. Move it into your Linux home folder, such as `~/code/...`. Update WSL if needed:

```powershell
wsl --update
wsl --shutdown
```

### Sending Diagnostics to OpenAI

If you still have problems, send OpenAI the file `CODEX_HOME/.sandbox/sandbox.log`. It also helps to include:

- A short description of what you were trying to do
- Whether the `elevated` sandbox failed or the `unelevated` sandbox was used
- Any error message from the app, including `1385` or another Windows or PowerShell error
- Whether you are on Windows 11 or Windows 10

**Do not send** the contents of `CODEX_HOME/.sandbox-secrets/`. Before sending any log, skim it for patron data, file names, or other details you shouldn't share.

---

## Additional Resources

- [Codex quickstart](https://learn.chatgpt.com/codex/quickstart)
- [ChatGPT desktop app for Windows](https://learn.chatgpt.com/codex/windows/windows-app)
- [Windows sandbox](https://learn.chatgpt.com/codex/windows/windows-sandbox)
- [Codex with WSL](https://learn.chatgpt.com/codex/windows/wsl)
- [Codex CLI](https://learn.chatgpt.com/codex/cli)
- [Codex IDE extension](https://learn.chatgpt.com/codex/ide)
- [Agent approvals and security](https://learn.chatgpt.com/codex/agent-approvals-security)
- [Authentication options](https://learn.chatgpt.com/codex/auth)
- [Codex pricing](https://learn.chatgpt.com/codex/pricing)
- [Codex changelog](https://learn.chatgpt.com/codex/changelog)

---

*Last updated: October 2026. Codex is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Claude Code on macOS](claude-code-macos-setup-guide.md) · [Next: Setting Up Codex on macOS →](codex-macos-setup-guide.md)
