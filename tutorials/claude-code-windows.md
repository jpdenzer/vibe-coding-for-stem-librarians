---
title: "Setting Up Claude Code on Windows"
parent: "Tutorials"
nav_order: 1
description: "Step-by-step: install Claude Code on Windows 10 or 11 with PowerShell, sign in, and run a first session safely."
---

# Setting Up Claude Code on Windows

**Rung:** High (agentic) · **Time:** about 20 minutes · **Last checked:** October 2026

By the end of this tutorial you'll have Claude Code installed on a Windows computer, signed in, and running in a practice folder where it can't touch anything important.

> **Check the official docs:** These steps follow Anthropic's [setup guide](https://code.claude.com/docs/en/setup) and [terminal guide for new users](https://code.claude.com/docs/en/terminal-guide#windows) as of October 2026. If anything on your screen looks different, those pages are the source of truth.

**New to agentic tools?** Read [03 · Agentic Tools](../03-claude-code-codex.md) first. It explains what Claude Code does and why the safety habits matter.

---

## Before you start

Check these four things:

- [ ] **Windows 10 (version 1809 or newer) or Windows 11, 64-bit.** Almost any Windows computer from the last several years qualifies. To check, press **Windows key**, type `About your PC`, and look at **System type** (should say *64-bit*) and **Version**.
- [ ] **A paid Claude plan**: Pro, Max, Team, or Enterprise, or an Anthropic Console (API) account. The free Claude plan does **not** include Claude Code. See [current plans and pricing](https://claude.com/pricing).
- [ ] **Permission to install software.** On a work computer, check with your IT office first. You don't need administrator rights for this install, but your institution may still have rules about AI tools.
- [ ] **An internet connection** and a web browser for signing in.

---

## Step 1 (optional): Install Git for Windows

Git for Windows gives Claude Code a better set of tools for running commands, and you'll want Git later for [version control](../03-claude-code-codex.md#2-use-version-control-git). You don't have to learn Git yourself to use it. Without it, Claude Code still works and uses PowerShell instead.

1. Go to [git-scm.com/downloads/win](https://git-scm.com/downloads/win) and download the installer.
2. Run it and click **Next** on every screen to accept the defaults. There are many screens, but you don't need to change anything.
3. When you see **"Adjusting your PATH environment,"** keep the recommended option.
4. Click **Install**, then **Finish**.

Not sure if you already have it? Installing again won't cause problems.

---

## Step 2: Open PowerShell

PowerShell is a text window for typing commands. It's built into Windows.

1. Press **Windows key + X** (or right-click the Start button).
2. Choose **Terminal** or **Windows PowerShell** from the menu.

A window opens with a blinking cursor and a line like this:

```text
PS C:\Users\YourName>
```

The **`PS`** at the start means you're in PowerShell. 👍

> **Watch out for two look-alikes:**
> - If the line starts with `C:\Users\YourName>` **without `PS`**, you're in **Command Prompt (CMD)**. Close it and try again.
> - Don't pick **Windows PowerShell (x86)**. That's the 32-bit version, and Claude Code won't install there.

**How to paste in PowerShell:** press **Ctrl + V** or simply **right-click** inside the window.

---

## Step 3: Install Claude Code

Copy this line, paste it into PowerShell, and press **Enter**:

```powershell
irm https://claude.ai/install.ps1 | iex
```

**What this does:** `irm` downloads Anthropic's installer script from claude.ai, and `iex` runs it. You'll see text scroll by. When it's done, you'll see:

```text
Claude Code successfully installed!
```

You don't need to run PowerShell as Administrator.

> **Alternative: WinGet.** If you prefer Windows' built-in package manager, you can run `winget install Anthropic.ClaudeCode` instead. Note that WinGet installs don't update themselves; you'd run `winget upgrade Anthropic.ClaudeCode` now and then. The command above updates automatically, which is easier.

---

## Step 4: Check that it worked

1. **Close PowerShell and open a new window** (repeat Step 2). This step matters: the new window picks up the newly installed program.
2. Type this and press **Enter**:

   ```powershell
   claude --version
   ```

3. You should see a version number, something like `2.1.211 (Claude Code)`. The exact number will differ, and that's fine.

If you see **`'claude' is not recognized`**, jump to [Troubleshooting](#troubleshooting).

---

## Step 5: Make a practice folder

Claude Code works on **whatever folder you start it in**. Never start it in your whole Documents folder or Desktop. Give it a small, dedicated folder.

In PowerShell, run these two lines (one at a time):

```powershell
mkdir "$env:USERPROFILE\Documents\claude-practice"
cd "$env:USERPROFILE\Documents\claude-practice"
```

The first line creates a folder called `claude-practice` inside your Documents folder. The second moves PowerShell into it. Your prompt now ends with `\Documents\claude-practice>`.

> **Shortcut for later projects:** open any folder in **File Explorer**, click in the **address bar** at the top, type `powershell`, and press **Enter**. PowerShell opens already inside that folder. On Windows 11 you can also right-click inside a folder and choose **Open in Terminal**.

---

## Step 6: Start Claude Code and sign in

In the same PowerShell window (inside `claude-practice`), type:

```powershell
claude
```

The first time, Claude Code walks you through a short setup:

1. **Pick a color theme.** Use the arrow keys and press **Enter**. Any choice is fine.
2. **Sign in.** A **browser window opens**. Sign in to your Claude account and approve the connection. Then switch back to PowerShell.
   - If no browser opens, Claude Code shows a link. Copy it into your browser, and if it shows a code afterward, paste that back into PowerShell.
3. **Trust the folder.** Claude Code asks whether you trust the files in this folder. Since it's your new empty practice folder, choose **Yes**.

You'll then see a welcome screen and a prompt where you can type. 🎉

---

## Step 7: Your first conversation

Type a request in plain English and press **Enter**. Try:

```text
Create a file called hello.html with a simple web page that says
"Hello from the library!" in large text. Explain what you did.
```

Claude Code will ask **permission** before creating the file. Read what it plans to do, then press **Enter** to approve. Afterward, open your `claude-practice` folder in File Explorer and double-click `hello.html` to see it in your browser.

### Keys to know

| Do this | To… |
|:--------|:----|
| Type and press **Enter** | Send a message |
| **Esc** | Interrupt Claude while it's working |
| **Arrow keys** + **Enter** | Choose options in menus (you can't click in the terminal) |
| Type `/help` | See available commands |
| Type `exit` (or **Ctrl + D** twice) | Leave Claude Code |

---

## Step 8 (optional): Try the A–Z list demo

1. Go to the [repository on GitHub](https://github.com/jpdenzer/vibe-coding-for-stem-librarians), click the green **Code** button, and choose **Download ZIP**.
2. Unzip it, and **copy** the `examples` folder into `Documents\claude-practice`.
3. In PowerShell:

   ```powershell
   cd "$env:USERPROFILE\Documents\claude-practice\examples"
   claude
   ```

4. Use the [Rung 3 prompts](../examples/#rung-3-agentic-tools), starting with: *"Look at the files in this folder and explain in plain English what's here. Don't change anything."*

---

## Troubleshooting

| What you see | What to do |
|:-------------|:-----------|
| **`'irm' is not recognized`** | You're in Command Prompt, not PowerShell. Close it and open PowerShell (Step 2). |
| **`The token '&&' is not a valid statement separator`** | You pasted the CMD command into PowerShell. Use the PowerShell command from Step 3. |
| **`'claude' is not recognized`** after installing | First, close PowerShell and open a **new** window. If it still fails, see the PATH fix below. |
| **`Could not create SSL/TLS secure channel`** | Common on older Windows 10. Run `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12` then run the Step 3 command again. |
| **`Claude Code does not support 32-bit Windows`** | You opened *Windows PowerShell (x86)*. Close it and open the one without "(x86)". |
| **Blocked by antivirus or a work policy** | Contact your IT office. Don't try to work around institutional security controls. |
| Sign-in fails or says your plan doesn't include Claude Code | Check that you're on a Pro, Max, Team, or Enterprise plan; the free plan doesn't include it. |

### PATH fix for "'claude' is not recognized"

This tells Windows where Claude Code was installed. Paste these **two lines** into PowerShell, pressing **Enter** after each:

```powershell
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Close PowerShell, open a new window, and try `claude --version` again.

For anything else, see Anthropic's [installation troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install).

---

## Prefer not to use the terminal?

The **Claude desktop app** includes Claude Code in a regular window. You pick a folder with a normal folder picker and chat with it, with no PowerShell needed.

1. Download the app from [claude.com/download](https://claude.com/download) and install it.
2. Sign in, then follow Anthropic's [desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart) to open the Code tab and choose a folder.

All the same safety habits apply: use a dedicated practice folder or a copy of your project.

**Want a Linux environment instead?** Claude Code also runs inside Windows Subsystem for Linux. See [Setting Up WSL on Windows](wsl-setup-guide.md).

---

## Keeping it updated, or removing it

- **Updates:** Claude Code installed with the Step 3 command **updates itself automatically** in the background. To update right away, run `claude update`.
- **Uninstall:** in PowerShell, run:

  ```powershell
  Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
  Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
  ```

  See [Uninstall Claude Code](https://code.claude.com/docs/en/setup#uninstall-claude-code) for removing settings too.

---

## Before you use it on a real project

- ✅ Work in a **copy** of your project folder, never the original.
- ✅ Set up **Git** so you can undo changes. Just ask Claude: *"Set up git in this folder and make a first commit. Explain each command."*
- ✅ **Read permission prompts** before approving them.
- 🚫 No patron or student data, passwords, API keys, proxy details, or licensed vendor files in the folder. See [Guardrails](../guardrails.md).

---

[← Back to Tutorials](./) · [Next: Setting Up Claude Code on macOS →](claude-code-macos-setup-guide.md)
