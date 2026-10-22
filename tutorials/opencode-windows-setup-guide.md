---
title: "Setting Up OpenCode on Windows"
parent: "Tutorials"
nav_order: 5
description: "Step-by-step guide to installing and configuring OpenCode on Windows, connecting a model, and running a first task safely in PowerShell or WSL."
---

# Setting Up OpenCode on Windows

OpenCode is a free, open-source coding agent. Like Claude Code and Codex, it can read your project, make changes, and run commands on your behalf. The difference is that OpenCode is not tied to one AI company: you connect it to the model you want, such as a free OpenCode model, an OpenAI or Anthropic account, or a model running on your own computer. This guide walks through installing the OpenCode command-line tool on Windows, connecting a model, setting safe permissions, and running your first task. It also covers WSL, the desktop app, and troubleshooting.

**New to agentic tools?** Read [03 · Agentic Tools](../03-claude-code-codex.md) first. It explains what these tools do and why the safety habits matter. Everything there about Claude Code and Codex applies to OpenCode too.

## Rung

**High (agentic). Beginner-friendly** if you can open PowerShell and paste a command into it. The [WSL section](#using-opencode-with-wsl) is optional.

## Time

**About 20 minutes**, including installing Node.js and Git. Allow **an extra 20 to 30 minutes** if you also set up WSL.

## You Will Need

- A computer running **Windows 10 or 11**, 64-bit (x64 or ARM64)
- **Permission to install software.** On a work computer, check with your IT office first. Your institution may also have rules about which AI tools and AI providers can be used.
- `winget` (Windows Package Manager), which comes with current versions of Windows
- An internet connection
- **A model to connect.** OpenCode itself is free. You can start with OpenCode's free models, or connect an account you already have. See [Step 5](#step-5-start-opencode-and-connect-a-model) for the options and what they cost.
- Optional: [Windows Terminal](https://aka.ms/terminal), which shows OpenCode's colors and layout better than the older PowerShell window. It comes with Windows 11.

## Last Check

**October 22, 2026.** Commands and options were checked against the official [OpenCode 2 documentation](https://opencode.ai/v2/docs/) on this date. At that time the latest version was **2.1.3**. OpenCode changes quickly, so verify against the official docs if something looks different on your system.

## Table of Contents

- [Choose Your Setup](#choose-your-setup)
- [OpenCode 1 and OpenCode 2](#opencode-1-and-opencode-2)
- [Step 1: Install Node.js and Git](#step-1-install-nodejs-and-git)
- [Step 2: Install OpenCode](#step-2-install-opencode)
- [Step 3: Verify the Installation](#step-3-verify-the-installation)
- [Step 4: Make a Practice Folder with Safe Permissions](#step-4-make-a-practice-folder-with-safe-permissions)
- [Step 5: Start OpenCode and Connect a Model](#step-5-start-opencode-and-connect-a-model)
- [Step 6: Plan, Then Build Your First Task](#step-6-plan-then-build-your-first-task)
- [Useful Commands and Shortcuts](#useful-commands-and-shortcuts)
- [Using OpenCode with WSL](#using-opencode-with-wsl)
- [The OpenCode Desktop App](#the-opencode-desktop-app)
- [Keeping OpenCode Up to Date](#keeping-opencode-up-to-date)
- [Uninstalling](#uninstalling)
- [Staying Safe While Using OpenCode](#staying-safe-while-using-opencode)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Choose Your Setup

| Option | Best for | Where it runs |
|--------|----------|---------------|
| **OpenCode CLI in PowerShell** | Most people. This guide's main path | Natively on Windows |
| **OpenCode CLI in WSL** | Linux tools, or projects that already live in WSL | Inside your Linux distribution |
| **OpenCode Desktop** | People who prefer a graphical app | Natively on Windows |

If you are unsure, follow the steps in order. You can add WSL or the desktop app later.

---

## OpenCode 1 and OpenCode 2

OpenCode 2 was released in October 2026. Both versions use the same `opencode` command, so you can only have one installed at a time. This guide is for **OpenCode 2**.

> **Important:** Many videos, blog posts, and AI answers still describe OpenCode 1. Its install package is named `opencode-ai`, and it was also offered through Chocolatey and Scoop. Those commands install the **old** version. Use the commands in this guide instead. If you already have OpenCode 1, see OpenCode's [migration guide](https://opencode.ai/v2/docs/migrate-v1/) before installing.

---

## Step 1: Install Node.js and Git

OpenCode 2 does not support Windows package managers such as Chocolatey or Scoop, so the simplest native install uses **npm**, which comes with Node.js. **Git** lets OpenCode undo file changes and lets you review what it did.

1. Open **PowerShell**: press the **Windows** key, type `PowerShell`, and press **Enter**.
2. Install both tools:

   ```powershell
   winget install --id OpenJS.NodeJS.LTS
   winget install --id Git.Git
   ```

3. Accept any prompts. When both finish, **close PowerShell and open a new window** so it can find the new programs.
4. Check that they work:

   ```powershell
   node --version
   git --version
   ```

Each command should print a version number. If you already have Node.js and Git, you can skip this step.

---

## Step 2: Install OpenCode

In PowerShell, run:

```powershell
npm install -g @opencode/cli
```

The `-g` means "install globally," so the `opencode` command works from any folder. The install downloads the right OpenCode program for your computer.

> **Note:** If you see an error saying `npm.ps1 cannot be loaded because running scripts is disabled on this system`, see [PowerShell Blocks Commands](#powershell-blocks-commands-execution-policy-error) in Troubleshooting.

**Alternative: standalone program.** If you cannot install Node.js, OpenCode also offers a standalone `opencode` program for Windows (x64, ARM64, and "baseline" x64 for older processors) on its [docs home page](https://opencode.ai/v2/docs/). You need to put that file in a folder on your `PATH` yourself, so the npm method is easier for most people.

---

## Step 3: Verify the Installation

Open a **new** PowerShell window, then run:

```powershell
opencode --version
```

A working installation prints a version number that starts with **2**, for example:

```text
2.1.3
```

If the version starts with **1**, you have the old OpenCode. If you see `opencode is not recognized`, see [Troubleshooting](#troubleshooting).

---

## Step 4: Make a Practice Folder with Safe Permissions

> **Warning:** Out of the box, OpenCode's main **Build** agent can edit files and run commands **without asking you first**. The only thing it asks about is reading `.env` files, which often hold passwords. Before your first session, set it up to ask before it changes anything.

For your first sessions, work in a new, empty **practice folder**, never your whole Documents folder or Desktop.

1. Create the folder and move into it:

   ```powershell
   mkdir "$env:USERPROFILE\Documents\opencode-practice"
   cd "$env:USERPROFILE\Documents\opencode-practice"
   ```

2. Turn it into a Git repository. OpenCode's `/undo` command can only restore files inside a Git repository:

   ```powershell
   git init
   ```

3. Create a settings file named `opencode.jsonc` that tells OpenCode to ask before it edits files, runs commands, or touches anything outside this folder. Copy and paste the whole block:

   ```powershell
   @'
   {
     "$schema": "https://opencode.ai/config.json",
     "permissions": [
       { "action": "edit", "resource": "*", "effect": "ask" },
       { "action": "shell", "resource": "*", "effect": "ask" },
       { "action": "external_directory", "resource": "*", "effect": "ask" }
     ]
   }
   '@ | Set-Content -Path opencode.jsonc -Encoding ascii
   ```

4. Check that the file exists:

   ```powershell
   Get-Content opencode.jsonc
   ```

This file only applies to this folder. To use the same rules in every project, see [Make Safe Permissions Your Default](#make-safe-permissions-your-default).

---

## Step 5: Start OpenCode and Connect a Model

1. In the practice folder, start OpenCode:

   ```powershell
   opencode
   ```

   OpenCode opens a full-screen interface in your terminal, called the TUI (terminal user interface). Type at the bottom and press **Enter** to send.

2. Type `/connect` and press **Enter**. Pick a provider from the list and follow the prompts. Some providers ask you to paste an API key (a long secret code from your account page). Others open a sign-in page in your browser.
3. Type `/models` and press **Enter** to choose which model to use.

Choose a provider:

| Option | Cost | Good to know |
|--------|------|--------------|
| **OpenCode free models** | Free | Good for trying OpenCode. The list changes often. OpenCode's docs say data sent to some free models **may be used to improve the model**, so use them only with practice files |
| **An account you already have**, such as OpenAI or Anthropic | Depends on your plan or API usage | Pick it in `/connect` and sign in or paste an API key. Check your institution's rules about which providers you may use |
| **OpenCode Go** | $10 or $40 per month | A subscription to open models tested by the OpenCode team |
| **OpenCode Console** | Pay as you go | Add credits and use many models through one account |
| **A local model** | Free | Runs on your own computer through a tool such as LM Studio. Needs a powerful computer, and results are usually weaker |

> **Check the official docs:** Prices, free models, and privacy terms change often. See [Providers](https://opencode.ai/v2/docs/providers/), [OpenCode Go](https://opencode.ai/v2/docs/console/go/), and the [Console models list](https://opencode.ai/v2/docs/console/models/), which includes a privacy section for each model.

> **Tip:** You can also log in from PowerShell without opening the TUI: `opencode auth login`.

---

## Step 6: Plan, Then Build Your First Task

OpenCode has two main **agents** (modes):

| Agent | What it does |
|-------|--------------|
| **Build** | The default. Writes files and runs commands |
| **Plan** | Explores and suggests a plan, but does not edit your project files |

Press **Shift + Tab** to switch between them. The current agent is shown on screen.

1. Press **Shift + Tab** until you are in **Plan**.
2. Describe what you want:

   ```text
   I want a file called hello.html with a simple web page that says
   "Hello from the library!" in large text. Plan how you would do it.
   ```

3. Read the plan. Ask questions or suggest changes if something looks wrong.
4. Press **Shift + Tab** to switch back to **Build**, then send:

   ```text
   Sounds good. Go ahead and make the file. Explain what you did.
   ```

5. Because of the settings file from Step 4, OpenCode stops and asks before it creates the file. Read the request, then approve it.
6. Open the practice folder in File Explorer and double-click `hello.html` to see the result.

If you don't like a change, type `/undo`. OpenCode restores the files and puts your last message back in the box so you can reword it. `/redo` brings the change back.

> **Tip:** Type `@` and start typing a file name to point OpenCode at a specific file, for example `Explain @hello.html`.

> **Tip:** Commit to Git before and after a task so you have a checkpoint you can return to. See the [Creating a GitHub Account](creating-a-github-account.md) tutorial if you are new to Git.

### Give OpenCode Project Instructions

OpenCode reads a plain-text file named `AGENTS.md` in your project folder at the start of every session. Put a few lines in it about the project, such as what it is for and what to avoid. You can ask OpenCode to write a first draft for you. OpenCode 2 reads only `AGENTS.md`, not Claude Code's `CLAUDE.md`. See [Instructions](https://opencode.ai/v2/docs/instructions/).

---

## Useful Commands and Shortcuts

Type `/` inside OpenCode to see every command. Press **Ctrl + P** for the command palette.

| Command or key | What it does |
|----------------|--------------|
| `/connect` | Connect or manage a model provider |
| `/models` | Choose a model |
| `/agents` or **Shift + Tab** | Choose or switch agents (Build, Plan) |
| `/undo` and `/redo` | Revert the last message and its file changes, or bring them back |
| `/new` | Start a new session |
| `/sessions` | Go back to an earlier session |
| `@` | Attach a file to your message |
| `!` | At the start of an empty message, runs a command such as `!git status` yourself |
| **Ctrl + C** | Exit OpenCode |

From PowerShell:

| Command | What it does |
|---------|--------------|
| `opencode` | Starts OpenCode in the current folder |
| `opencode run "..."` | Sends one message and prints the reply, without opening the TUI |
| `opencode auth list` | Shows connected providers |
| `opencode models` | Lists available models |

---

## Using OpenCode with WSL

OpenCode's [Windows guide](https://opencode.ai/docs/windows-wsl/) recommends WSL (Windows Subsystem for Linux) for the best performance and compatibility. You don't need it to get started, but it is worth trying if OpenCode feels slow or a Linux tool doesn't work in PowerShell.

If you have not installed WSL yet, follow the [Setting Up WSL on Windows](wsl-setup-guide.md) tutorial. Then, in your WSL (Ubuntu) terminal, install OpenCode 2 with its install script:

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

Close the terminal, open a new one, and check:

```bash
opencode --version
```

| Situation | Recommendation |
|-----------|----------------|
| Most work in WSL | Keep projects in your Linux home folder, such as `~/code/my-project`. This is faster |
| Projects on your Windows drive | Reach them through `/mnt/c/...`, for example `cd /mnt/c/Users/<your-username>/Documents/opencode-practice` |

> **Note:** OpenCode in WSL is a separate install with its own settings and sign-ins. You need to run `/connect` again inside WSL. Repeat [Step 4](#step-4-make-a-practice-folder-with-safe-permissions) with the macOS/Linux version of the settings command from the [Setting Up OpenCode on macOS](opencode-macos-setup-guide.md#step-4-make-a-practice-folder-with-safe-permissions) guide.

---

## The OpenCode Desktop App

OpenCode also has a desktop app for people who prefer windows and buttons to a terminal. Download the Windows installer (x64 or ARM64) from [opencode.ai/download](https://opencode.ai/download). You still need to connect a model provider, and the same safety habits apply: open a practice folder and check the permission settings before your first task.

> **Note:** This guide focuses on the command-line tool. The desktop app's menus may change, so follow the [official docs](https://opencode.ai/v2/docs/) for its current steps.

---

## Keeping OpenCode Up to Date

| Installed with | How to update |
|----------------|---------------|
| npm | `npm install -g @opencode/cli@latest` |
| Install script (in WSL) | Re-run `curl -fsSL https://opencode.ai/v2/install \| bash` |
| Desktop app | Download the latest installer from [opencode.ai/download](https://opencode.ai/download) |

After an update, OpenCode shows what's new the first time you open it. Type `/highlights` to see it again.

---

## Uninstalling

OpenCode has a built-in uninstaller. First, preview what will be removed:

```powershell
opencode uninstall --dry-run
```

Then remove it:

```powershell
opencode uninstall
```

For npm installs, it uses npm to remove the program. Your sessions, settings, and saved sign-ins are **not** deleted. Delete your practice folder yourself when you no longer need it.

---

## Staying Safe While Using OpenCode

- **Make it ask first.** Use the `opencode.jsonc` settings from [Step 4](#step-4-make-a-practice-folder-with-safe-permissions) while you are learning. Out of the box, the Build agent doesn't ask before editing files or running commands.
- **Plan before you build.** Use the **Plan** agent to catch a wrong assumption before any code exists.
- **Work in a copy.** Point OpenCode at a copy of your project folder, never the original.
- **Use Git checkpoints.** Commit before and after tasks. `/undo` is a convenience, not a backup: it can't undo commands that changed things outside your files.
- **Review changes before you accept them,** especially on projects that matter to you.
- **Know where your data goes.** Each provider has its own privacy terms, and some free models may use your data for training. Check before you send anything you care about.
- **Do not share secrets.** Do not paste passwords or API keys into messages or commit them to a repository.
- **Keep sensitive data out of the folder.** No patron or student data, proxy details, or licensed vendor files. See [Guardrails](../guardrails.md).

### Make Safe Permissions Your Default

To use the ask-first rules in every project, put the same `opencode.jsonc` content in OpenCode's global settings file, `~/.config/opencode/opencode.jsonc` (on Windows, `~` is your user folder, such as `C:\Users\<your-username>`). See [Config](https://opencode.ai/v2/docs/config/) and [Permissions](https://opencode.ai/v2/docs/permissions/) for the exact locations and more rules, such as always allowing `git status`.

---

## Troubleshooting

### `opencode` Is Not Recognized

1. Close PowerShell and open a new window, then try `opencode --version` again.
2. Check that npm's install folder is on your `PATH`. Run `npm config get prefix` and make sure that folder appears in the output of `$env:Path`.
3. If it is still not found, reinstall with `npm install -g @opencode/cli`.

### PowerShell Blocks Commands (Execution Policy Error)

If you have not used `npm` in PowerShell before, you may see:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

A common fix is to set the execution policy to `RemoteSigned` for your own user account. Adding `-Scope CurrentUser` means you don't need administrator rights and the change doesn't affect other users:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Read Microsoft's [execution policy guide](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) before changing this setting. On a work computer, this may be controlled by IT policy.

### The Version Starts with 1, or Instructions Online Don't Match

You have OpenCode 1, or you are following a guide written for it. For example, in OpenCode 1 the **Tab** key switched to Plan mode; in OpenCode 2 it is **Shift + Tab**. Remove the old version and install OpenCode 2 with the commands in [Step 2](#step-2-install-opencode). See [OpenCode 1 and OpenCode 2](#opencode-1-and-opencode-2).

### No Models Appear, or OpenCode Says It Has No Provider

Run `/connect` and finish connecting a provider, then run `/models`. To check from PowerShell, run `opencode auth list`.

### OpenCode Edits Files Without Asking

Make sure `opencode.jsonc` is in the folder you started OpenCode from, and that you copied the whole block in [Step 4](#step-4-make-a-practice-folder-with-safe-permissions). Restart OpenCode after creating or changing the file.

### `/undo` Did Not Restore My Files

File restore only works inside a Git repository. Run `git init` in the project folder. Also, `/undo` can't reverse what a command did outside your files, such as installing a program.

### The Screen Looks Garbled or Colors Look Wrong

Use [Windows Terminal](https://aka.ms/terminal) instead of the older PowerShell window. OpenCode also suggests terminals such as WezTerm and Alacritty.

### The Install Is Blocked on a Work Computer

Contact your IT office rather than trying to work around the block. Ask whether npm installs or the OpenCode desktop app are allowed, and which AI providers your institution approves.

### I Am Still Stuck

You can ask OpenCode to help debug itself: describe the problem and point it at the [troubleshooting page](https://opencode.ai/v2/docs/troubleshooting/). To report a bug, open an issue on [GitHub](https://github.com/anomalyco/opencode/issues) and include the output of `opencode --version`, your Windows version, and the exact error message. Remove API keys, file contents, and personal details from anything you post publicly.

---

## Additional Resources

- [OpenCode 2 docs](https://opencode.ai/v2/docs/)
- [Download OpenCode](https://opencode.ai/download)
- [Using the TUI](https://opencode.ai/v2/docs/cli/tui/)
- [Providers](https://opencode.ai/v2/docs/providers/)
- [Agents](https://opencode.ai/v2/docs/agents/)
- [Permissions](https://opencode.ai/v2/docs/permissions/)
- [Snapshots (undo and redo)](https://opencode.ai/v2/docs/snapshots/)
- [Migrate from OpenCode 1](https://opencode.ai/v2/docs/migrate-v1/)
- [OpenCode on Windows with WSL](https://opencode.ai/docs/windows-wsl/)
- [Troubleshooting](https://opencode.ai/v2/docs/troubleshooting/)
- [OpenCode on GitHub](https://github.com/anomalyco/opencode)

---

*Last updated: October 2026. OpenCode is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Codex on macOS](codex-macos-setup-guide.md) · [Next: Setting Up OpenCode on macOS →](opencode-macos-setup-guide.md)
