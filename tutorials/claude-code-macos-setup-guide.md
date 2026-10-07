---
title: "Setting Up Claude Code on macOS"
parent: "Tutorials"
nav_order: 2
description: "Step-by-step guide to installing, authenticating, and updating Claude Code on a Mac."
---

# Setting Up Claude Code on macOS

Claude Code is Anthropic's agentic coding tool that runs in your terminal. It can read your project, edit files, and run commands on your behalf. This guide covers installing Claude Code on macOS, signing in, verifying the setup, and keeping it up to date.

**New to agentic tools?** Read [03 · Agentic Tools](../03-claude-code-codex.md) first. It explains what Claude Code does and why the safety habits matter.

## Rung

**High (agentic). Beginner-friendly.** No prior experience with Claude Code is required. You should be able to open the Terminal app and paste a command into it.

## Time

**About 10 to 15 minutes.** Most of that is signing in through your browser and confirming the install. No restart is required.

## You Will Need

- A Mac running macOS 13.0 or later
- At least 4 GB of RAM (Apple silicon or Intel)
- An internet connection
- A Claude **Pro, Max, Team, or Enterprise** account, or an Anthropic **Console** account. The free claude.ai plan does not include Claude Code access. See [current plans and pricing](https://claude.com/pricing).
- **Permission to install software.** On a work computer, check with your IT office first. You don't need administrator rights for the recommended installer, but your institution may have rules about AI tools.
- A web browser, for the sign-in step
- A project folder you want to work in (optional for installation, needed for your first session)
- Optional: [Homebrew](https://brew.sh/), if you prefer to install with it

## Last Check

**October 7, 2026.** Commands and options were checked against the official Claude Code documentation on this date. Claude Code changes frequently, so verify against the [official setup page](https://code.claude.com/docs/en/setup) if something behaves differently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Open Terminal](#step-1-open-terminal)
- [Step 2: Install Claude Code](#step-2-install-claude-code)
- [Step 3: Verify the Installation](#step-3-verify-the-installation)
- [Step 4: Sign In](#step-4-sign-in)
- [Step 5: Start Your First Session](#step-5-start-your-first-session)
- [Keeping Claude Code Up to Date](#keeping-claude-code-up-to-date)
- [Alternative: The Desktop App](#alternative-the-desktop-app)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [Before You Use It on a Real Project](#before-you-use-it-on-a-real-project)
- [Additional Resources](#additional-resources)

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Operating system | macOS 13.0 or later |
| Hardware | 4 GB or more of RAM; Apple silicon (ARM64) or Intel (x64) |
| Network | Internet connection required |
| Shell | Zsh (the macOS default) or Bash |
| Account | Claude Pro, Max, Team, or Enterprise, or an Anthropic Console account |
| Location | A [supported country](https://www.anthropic.com/supported-countries) |

To check your macOS version, click the **Apple menu** in the top-left corner and choose **About This Mac**.

You do **not** need to install Node.js to use the recommended installer.

---

## Step 1: Open Terminal

1. Press **Command + Space** to open Spotlight.
2. Type `Terminal` and press **Return**.

A window opens with a prompt where you can type commands. You can also find Terminal in **Applications > Utilities**.

---

## Step 2: Install Claude Code

Choose **one** of the following methods. The native installer is recommended.

### Option A: Native Installer (Recommended)

Paste this command into Terminal and press **Return**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Benefits of this method:

- No dependencies to install
- Updates itself automatically in the background
- Places the `claude` launcher at `~/.local/bin/claude`

When it finishes, **close Terminal and open a new window** so your shell picks up the change.

### Option B: Homebrew

If you already use Homebrew:

```bash
brew install --cask claude-code
```

Homebrew offers two casks:

| Cask | Channel | Behavior |
|------|---------|----------|
| `claude-code` | Stable | Typically about a week behind the latest release and skips releases with major regressions |
| `claude-code@latest` | Latest | Receives new versions as soon as they ship |

> **Note:** Homebrew installations do **not** auto-update. See [Keeping Claude Code Up to Date](#keeping-claude-code-up-to-date).

### Option C: npm

The npm package requires [Node.js 22 or later](https://nodejs.org/en/download):

```bash
npm install -g @anthropic-ai/claude-code
```

> **Warning:** Do **not** use `sudo npm install -g`. It can cause permission problems and security risks. If you hit permission errors, see [Troubleshooting](#troubleshooting).

---

## Step 3: Verify the Installation

In a **new** Terminal window, run:

```bash
claude --version
```

A working installation prints a version number followed by `(Claude Code)`.

For a more detailed health check, run:

```bash
claude doctor
```

`claude doctor` prints read-only diagnostics without starting a session. It reports install health, settings validation errors, and warnings with suggested fixes.

If you see `command not found: claude`, go to [Troubleshooting](#troubleshooting).

---

## Step 4: Sign In

1. In Terminal, move to a project folder. For your first time, use a new, empty **practice folder** so Claude Code can't touch anything important:

   ```bash
   mkdir -p ~/Documents/claude-practice
   cd ~/Documents/claude-practice
   ```

   Never start Claude Code in your whole home folder, Documents, or Desktop. It works on whatever folder you start it in.

2. Start Claude Code:

   ```bash
   claude
   ```

3. Follow the prompts. Claude Code opens your browser so you can sign in with your Claude account.
4. Approve the sign-in, then return to Terminal.

Notes:

- If the `ANTHROPIC_API_KEY` environment variable is already set on your machine, Claude Code asks you once to approve using that key instead of opening a browser.
- Claude Code can also be used through Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry. See the [authentication documentation](https://code.claude.com/docs/en/authentication) for those and for team setup options.

> **Shortcut for later projects:** in Terminal, type `cd ` (with a space), then drag your project folder from Finder into the Terminal window and press **Return**.

---

## Step 5: Start Your First Session

With Claude Code running inside your project folder, try a plain-language request such as:

```text
Give me an overview of this project.
```

In an empty practice folder, try building something small instead:

```text
Create a file called hello.html with a simple web page that says
"Hello from the library!" in large text. Explain what you did.
```

Claude Code reads files in the current folder as it works and asks for your permission before taking actions such as editing files or running commands.

Helpful habits:

- **Start Claude Code from the folder you want to work in.** It treats that folder as the project.
- **Review what it proposes** before approving changes.
- **Press `Esc`** to interrupt Claude while it's working.
- **Type `/config`** inside a session to view and change settings.
- **Exit** a session with `Ctrl + C` twice, or by typing `/exit`.

For a guided walkthrough of your first session, see the [quickstart](https://code.claude.com/docs/en/quickstart). To try the A–Z list demo, copy this site's `examples` folder into your practice folder and use the [Rung 3 prompts](../examples/#rung-3-agentic-tools).

---

## Keeping Claude Code Up to Date

How updates work depends on how you installed.

| Install method | Updates |
|----------------|---------|
| Native installer | Automatic, in the background. Takes effect the next time you start Claude Code |
| Homebrew | Manual: `brew upgrade claude-code` (or `brew upgrade claude-code@latest` if you installed that cask) |
| npm | Manual: `npm install -g @anthropic-ai/claude-code@latest` |

To apply an update immediately instead of waiting for the next background check:

```bash
claude update
```

If you installed with Homebrew, run `brew cleanup` occasionally to reclaim disk space from old versions.

### Choose a Release Channel

Claude Code supports two release channels:

- `latest` (default): new features as soon as they are released
- `stable`: a version that is typically about a week old, skipping releases with major regressions

Set the channel from inside a session with `/config`, or add it to `~/.claude/settings.json`:

```json
{
  "autoUpdatesChannel": "stable"
}
```

Homebrew users choose a channel by cask name instead of this setting.

### Turn Off Auto-Updates

To stop background updates, add this to `~/.claude/settings.json`:

```json
{
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

You can still update manually with `claude update`. Run `claude doctor` to confirm the setting took effect.

---

## Alternative: The Desktop App

If you would rather not use the terminal, the Claude desktop app lets you use Claude Code through a graphical interface. See the [desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart) for download and setup instructions.

---

## Uninstalling

Follow the section that matches how you installed.

### Native Installation

```bash
rm -f ~/.local/bin/claude
rm -rf ~/.local/share/claude
```

### Homebrew

```bash
brew uninstall --cask claude-code
```

If you installed the latest cask:

```bash
brew uninstall --cask claude-code@latest
```

### npm

```bash
npm uninstall -g @anthropic-ai/claude-code
```

### Remove Settings and Cached Data (Optional)

> **Warning:** This deletes all your settings, allowed tools, MCP server configurations, and session history.

```bash
# User settings and state
rm -rf ~/.claude
rm ~/.claude.json

# Project-specific settings (run from your project folder)
rm -rf .claude
rm -f .mcp.json
```

If the Claude desktop app, VS Code extension, or JetBrains plugin is still installed, `~/.claude/` is recreated the next time one of them runs. Uninstall those first for a complete removal.

---

## Troubleshooting

### `command not found: claude`

The install location is probably not on your `PATH` yet. First, close Terminal and open a new window, then try again. If it still fails and you used the native installer, add the install folder to your `PATH` in `~/.zshrc`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
claude --version
```

If you use Bash instead of Zsh, add the same line to `~/.bash_profile`.

### The Install Command Fails

If you see `syntax error near unexpected token '<'`, a `403` error, or another `curl` error, the script may not have downloaded correctly, often because of a network, proxy, or VPN restriction. Try again on a different network or without a VPN, or install with Homebrew (Option B) instead. See the [installation troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install) for matching specific errors to fixes.

> **On a work computer:** if the download is blocked by your institution's network or security software, contact your IT office rather than trying to work around it.

### Permission Errors with npm

Do not use `sudo`. Use the native installer or Homebrew instead, or see the [permission errors section](https://code.claude.com/docs/en/troubleshoot-install#permission-errors-during-installation) of the troubleshooting guide.

### Claude Code Still Runs After Uninstalling

You may have a second installation, such as one from npm plus one from the native installer, or a leftover shell alias. See [Check for conflicting installations](https://code.claude.com/docs/en/troubleshoot-install#check-for-conflicting-installations).

### Search Does Not Work Inside a Session

Claude Code normally includes the search tool (ripgrep) it needs. If searches fail, see the [search troubleshooting section](https://code.claude.com/docs/en/troubleshooting#search-and-discovery-issues).

### Sign-In Does Not Complete

- Confirm you are using an account on a plan that includes Claude Code (Pro, Max, Team, Enterprise, or Console). The free plan does not.
- Make sure your default browser can open and that you finish the approval in the browser window.
- Run `claude doctor` for diagnostics.

---

## Before You Use It on a Real Project

- ✅ Work in a **copy** of your project folder, never the original.
- ✅ Set up **Git** so you can undo changes. Just ask Claude: *"Set up git in this folder and make a first commit. Explain each command."*
- ✅ **Read permission prompts** before approving them.
- 🚫 No patron or student data, passwords, API keys, proxy details, or licensed vendor files in the folder. See [Guardrails](../guardrails.md).

---

## Additional Resources

- [Claude Code advanced setup](https://code.claude.com/docs/en/setup)
- [Claude Code quickstart](https://code.claude.com/docs/en/quickstart)
- [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
- [Authentication options](https://code.claude.com/docs/en/authentication)
- [Terminal guide for first-time users](https://code.claude.com/docs/en/terminal-guide)
- [Claude Code on npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)

---

*Last updated: October 2026. Claude Code is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Claude Code on Windows](claude-code-windows.md) · [Next: Setting Up Codex on Windows →](codex-windows-setup-guide.md)
