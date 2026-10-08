---
title: "Creating a GitHub Account"
parent: "Tutorials"
nav_order: 8
description: "Step-by-step guide to creating a GitHub account, setting up Git, and creating and using your first repository."
---

# Creating a GitHub Account

GitHub is a website for storing, sharing, and collaborating on projects that are tracked with Git. This guide covers creating a free GitHub account, securing it, setting up Git on your computer, and creating your first repository (repo), both on the GitHub website and from your own computer.

**Why this matters for vibe coding:** Git is the safety net that lets you see and undo every change an AI tool makes (see [03 · Agentic Tools](../03-claude-code-codex.md#2-use-version-control-git)). GitHub adds an online backup and a free way to share your work, including publishing it as a website like this one.

## Rung

**Supports all rungs. Beginner-friendly.** No prior experience with Git or GitHub is required. You should be comfortable using a web browser and pasting a few commands into a terminal.

## Time

**About 30 to 40 minutes.** Creating the account and repository takes about 10 minutes. Installing Git, connecting it to GitHub, and making your first push from your computer takes about 20 to 30 minutes.

## You Will Need

- A computer running Windows, macOS, or Linux
- An email address you can access (GitHub sends a verification message)
- A web browser
- Permission to install software on your computer. **On a work computer, check with your IT office first.**
- A phone with an authenticator app, or a device that supports passkeys, for two-factor authentication
- Optional: a text editor such as [Visual Studio Code](https://code.visualstudio.com/)

## Last Check

**October 7, 2026.** The account and repository steps were checked against the official GitHub documentation on this date. GitHub updates its interface regularly, so button names and menu locations may differ slightly. If something looks different, check the [GitHub Docs](https://docs.github.com/).

## Table of Contents

- [Key Terms](#key-terms)
- [Part 1: Create Your GitHub Account](#part-1-create-your-github-account)
  - [Step 1: Sign Up](#step-1-sign-up)
  - [Step 2: Verify Your Email Address](#step-2-verify-your-email-address)
  - [Step 3: Turn On Two-Factor Authentication](#step-3-turn-on-two-factor-authentication)
  - [Step 4: Set Up Your Profile](#step-4-set-up-your-profile)
- [Part 2: Create Your First Repository](#part-2-create-your-first-repository)
  - [Step 5: Create the Repository](#step-5-create-the-repository)
  - [Step 6: Edit the README and Make Your First Commit](#step-6-edit-the-readme-and-make-your-first-commit)
- [Part 3: Work on Your Repository from Your Computer](#part-3-work-on-your-repository-from-your-computer)
  - [Step 7: Install Git](#step-7-install-git)
  - [Step 8: Configure Git](#step-8-configure-git)
  - [Step 9: Connect Your Computer to GitHub](#step-9-connect-your-computer-to-github)
  - [Step 10: Clone Your Repository](#step-10-clone-your-repository)
  - [Step 11: Make a Change and Push It](#step-11-make-a-change-and-push-it)
- [Alternative: Create a Repository with the GitHub CLI](#alternative-create-a-repository-with-the-github-cli)
- [Publishing Your Repository as a Website with GitHub Pages](#publishing-your-repository-as-a-website-with-github-pages)
- [Everyday Git Commands](#everyday-git-commands)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Key Terms

| Term | Meaning |
|------|---------|
| **Git** | Free software on your computer that tracks changes to files over time |
| **GitHub** | A website that hosts Git repositories online and adds collaboration features |
| **Repository (repo)** | A project folder whose history Git tracks. It lives on GitHub (the *remote*) and, optionally, on your computer (the *local* copy) |
| **Commit** | A saved snapshot of your project at a point in time, with a short message describing the change |
| **Branch** | A separate line of work. New repositories start with a default branch, usually called `main` |
| **Clone** | Download a copy of a GitHub repository to your computer |
| **Push** | Send your local commits up to GitHub |
| **Pull** | Bring new changes from GitHub down to your computer |
| **README** | A file named `README.md` that GitHub displays on your repository's front page |

---

## Part 1: Create Your GitHub Account

### Step 1: Sign Up

1. Go to [github.com](https://github.com/).
2. Click **Sign up**. You can also sign up with a Google or Apple account.
3. Follow the prompts to enter your email address, create a password, and choose a username.

Your **username** becomes part of your public web address (for example, `github.com/yourname`) and is shown on everything you do on GitHub. Choose something you will be comfortable using for a long time, and consider whether you want it to be professional if you will use GitHub for work or job applications.

The free plan is all you need to follow this guide. You can look at paid plans later.

> **Note:** Signing in with Apple creates a **new** GitHub account, even if you have Apple's "Hide My Email" turned on. If you already have a GitHub account, sign in to it rather than creating another.

### Step 2: Verify Your Email Address

During sign-up, GitHub asks you to verify your email address. Open the message GitHub sends and follow its link or enter the code it provides.

This step matters: without a verified email address, you cannot complete some basic tasks, including creating a repository.

If the message does not arrive, check your spam folder, then see GitHub's [email verification troubleshooting](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/verifying-your-email-address#troubleshooting-email-verification).

### Step 3: Turn On Two-Factor Authentication

GitHub strongly recommends two-factor authentication (2FA), an extra layer of security that protects your account even if your password is stolen.

1. Click your profile picture in the upper-right corner and choose **Settings**.
2. In the sidebar, choose **Password and authentication**.
3. Set up an authentication method, such as an authenticator app on your phone, a passkey, or a security key.
4. **Save your recovery codes** somewhere safe, such as a password manager. They are your way back into your account if you lose your phone.

For the full walkthrough, see [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).

### Step 4: Set Up Your Profile

Your profile is optional, but it is a good idea to add a photo and a short description.

1. Click your profile picture and choose **Your profile**, then **Edit profile**.
2. Add your name, a short bio, and a profile picture.
3. Click **Save**.

#### Keep Your Email Address Private (Recommended)

When you make commits, your email address can be attached to them. To avoid publishing your real email address:

1. Go to **Settings > Emails**.
2. Check **Keep my email addresses private**.

GitHub then provides a private `noreply` address you can use in Git (see [Step 8](#step-8-configure-git)).

---

## Part 2: Create Your First Repository

### Step 5: Create the Repository

1. In the upper-right corner of any GitHub page, click the **+** icon, then click **New repository**.
2. Type a short, memorable **Repository name**. For your first repository, `hello-world` is a good choice.
3. Optionally, add a **Description**, such as `My first repository on GitHub.`
4. Choose a **visibility**:
   - **Public:** anyone on the internet can see the repository
   - **Private:** only you, and people you choose, can see it
5. Toggle **Add README** to **On**. This creates a starting `README.md` file so the repository is not empty.
6. Click **Create repository**.

You have now created your first repository.

#### Optional Choices on the Same Page

Depending on the current version of the form, you may also see options to add a `.gitignore` file (a list of files Git should not track, with templates for common languages) and to choose a license. You can leave these off for a practice repository. If you plan to share code publicly, choose a license deliberately: a repository with no license generally means others do not have permission to reuse your work.

#### Naming Tips

- Use lowercase letters, numbers, and hyphens, such as `my-first-repo`
- Avoid spaces. GitHub converts them to hyphens
- Pick a name that describes the project

> **Warning:** Never put passwords, API keys, or other secrets in a public repository, and never put patron or student data, proxy details, or licensed vendor content in **any** repository, public or private. Anything you commit can be seen by anyone who can view the repository, and removing it later can be difficult. See [Guardrails](../guardrails.md).

### Step 6: Edit the README and Make Your First Commit

A **commit** is a snapshot of your project at one point in time. You can make one right in your browser.

1. In your repository's list of files, click **README.md**.
2. In the upper-right corner of the file view, click the **pencil icon** to edit the file.
3. In the text box, type some information about yourself or your project.
4. Click **Preview** above the text to see how it will look. Choose **Show diff** to see your additions in green.
5. Click **Commit changes...**
6. In the **Commit message** field, type a short, meaningful message, such as `Update README with introduction`.
7. Choose where the commit goes. GitHub's documentation recommends creating a new branch and a pull request when you are on the default branch. For a personal practice repository, committing directly to the default branch is fine.
8. Click **Commit changes** (or **Propose changes** if you chose a new branch).

You now have a repository with a commit history. Click the **clock icon** or the **commits** link on the repository page to see it.

---

## Part 3: Work on Your Repository from Your Computer

You can keep working in the browser, but most people work on their own computer and sync with GitHub. This part sets that up.

> **Prefer buttons to commands?** [GitHub Desktop](https://desktop.github.com/) is a free app for Windows and macOS that handles signing in, cloning, committing, and pushing with a point-and-click interface. You can use it instead of Steps 7–11.

### Step 7: Install Git

First check whether Git is already installed. Open a terminal (Terminal on macOS and Linux, PowerShell or Command Prompt on Windows) and run:

```bash
git --version
```

If a version number appears, skip to [Step 8](#step-8-configure-git). Otherwise, install Git:

#### Windows

1. Download **Git for Windows** from [git-scm.com](https://git-scm.com/downloads/win).
2. Run the installer. The default options work for most people.
3. Open a new terminal and run `git --version` to confirm.

Alternatively, with winget:

```powershell
winget install --id Git.Git -e
```

If you use WSL, install Git inside your Linux distribution instead, using the Linux command below. See [Setting Up WSL on Windows](wsl-setup-guide.md).

#### macOS

Running `git --version` in Terminal may prompt you to install Apple's command line developer tools, which include Git. Accept the prompt. Or, if you use Homebrew:

```bash
brew install git
```

#### Linux (Debian/Ubuntu)

```bash
sudo apt update && sudo apt install -y git
```

### Step 8: Configure Git

Tell Git who you are. This information is attached to your commits.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Replace the name and email with your own. If you turned on **Keep my email addresses private** in [Step 4](#step-4-set-up-your-profile), use the `noreply` address GitHub shows under **Settings > Emails** instead of your real email.

Check your settings:

```bash
git config --global --list
```

### Step 9: Connect Your Computer to GitHub

GitHub does not accept your account password for Git commands over HTTPS. You need a way to authenticate. The two easiest options are below. Choose one.

#### Option A: GitHub CLI (Recommended for Beginners)

The GitHub CLI (`gh`) signs you in through your browser and sets up Git to use that sign-in.

1. Install it:

   - **Windows:** `winget install --id GitHub.cli -e`
   - **macOS:** `brew install gh`
   - **Linux:** see the [installation instructions](https://github.com/cli/cli#installation)

2. Open a new terminal and run:

   ```bash
   gh auth login
   ```

3. Choose **GitHub.com**, choose **HTTPS** when asked for your preferred protocol, and agree to authenticate Git with your GitHub credentials. Then follow the browser prompts.

#### Option B: Git Credential Manager

Git for Windows includes Git Credential Manager, which opens a browser sign-in window the first time you push or clone a private repository. On macOS and Linux, you can install it separately. See the [Git Credential Manager project](https://github.com/git-ecosystem/git-credential-manager).

> **Using SSH instead?** You can also connect with SSH keys. See GitHub's guide to [connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### Step 10: Clone Your Repository

Cloning downloads a copy of your repository to your computer.

1. On your repository's page on GitHub, click the green **Code** button.
2. Make sure **HTTPS** is selected and copy the URL, which looks like `https://github.com/yourname/hello-world.git`.
3. In your terminal, move to the folder where you want the project to live, for example:

   ```bash
   cd ~/projects
   ```

   If the folder does not exist yet, create it first with `mkdir ~/projects`. On Windows PowerShell, use a path such as `cd $HOME\Documents`.

4. Clone it:

   ```bash
   git clone https://github.com/yourname/hello-world.git
   ```

5. Move into the new folder:

   ```bash
   cd hello-world
   ```

Replace `yourname` and `hello-world` with your own username and repository name.

### Step 11: Make a Change and Push It

1. Create or edit a file. This example adds a line to your README:

   ```bash
   echo "This line was added from my computer." >> README.md
   ```

2. Check what changed:

   ```bash
   git status
   ```

   Git lists `README.md` as modified.

3. Stage the file, which tells Git to include it in the next commit:

   ```bash
   git add README.md
   ```

4. Commit with a message:

   ```bash
   git commit -m "Add a line from my computer"
   ```

5. Push the commit to GitHub:

   ```bash
   git push
   ```

6. Refresh your repository's page on GitHub. Your change appears in the README, and the commit appears in the history.

Congratulations. You have created a repository, made commits both on GitHub and on your own computer, and synced them.

> **Tip for agentic tools:** once Git is set up, you can ask Claude Code or Codex to do these steps for you: *"Commit my changes with a clear message and push them to GitHub. Explain each command."* Review what it plans to commit before you approve.

---

## Alternative: Create a Repository with the GitHub CLI

If you have installed and signed in with the GitHub CLI ([Step 9](#step-9-connect-your-computer-to-github)), you can create a repository from the terminal.

1. In your terminal, move to the folder where you want to create the project.
2. Run:

   ```bash
   gh repo create
   ```

3. Choose **Create a new repository on GitHub from scratch** and follow the prompts. Confirm **yes** when asked whether to clone the project locally.

To skip the prompts, give the name and visibility directly:

```bash
gh repo create my-project --public --clone
```

You can use `--private` instead of `--public`. To create the repository under an organization instead of your personal account, use `organization-name/project-name` as the name.

---

## Publishing Your Repository as a Website with GitHub Pages

If your repository holds Markdown guides like the ones on this site, you can publish it as a website with GitHub Pages.

1. On your repository's page, click **Settings**.
2. In the sidebar, click **Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Choose your branch (usually `main`) and the folder (`/ (root)` or `/docs`), then click **Save**.
5. After a few minutes, GitHub shows the address of your published site, usually `https://yourname.github.io/repository-name/`.

Pages reads the lines between the `---` markers at the top of each Markdown file (the *front matter*, such as `title` and `description`) when it builds your site. Public repositories can use Pages on the free plan. For themes, custom domains, and troubleshooting, see the [GitHub Pages documentation](https://docs.github.com/en/pages).

> **Remember:** a Pages site is public, even if you think of it as "just a draft." Check it for anything that shouldn't be shared before you turn Pages on.

---

## Everyday Git Commands

| Command | What it does |
|---------|--------------|
| `git status` | Shows which files changed and what is staged |
| `git add <file>` | Stages a file for the next commit |
| `git add .` | Stages all changes in the current folder |
| `git commit -m "message"` | Saves a commit with a message |
| `git push` | Sends your commits to GitHub |
| `git pull` | Downloads and merges new changes from GitHub |
| `git log --oneline` | Shows a short history of commits |
| `git diff` | Shows unstaged changes line by line |
| `git clone <url>` | Copies a GitHub repository to your computer |
| `git branch` | Lists branches |
| `git switch -c <name>` | Creates and switches to a new branch |

A good habit: **pull before you start working and push when you finish**, especially if you edit the same repository from more than one place.

---

## Troubleshooting

### I Cannot Create a Repository

Make sure your email address is verified. GitHub does not let you complete some basic tasks, including creating a repository, until you verify it. See [Step 2](#step-2-verify-your-email-address).

### `git` Is Not Recognized or `command not found: git`

Git is not installed or your terminal does not know about it yet. Install it ([Step 7](#step-7-install-git)), then close and reopen your terminal.

### "Authentication failed" or Password Rejected When Pushing

GitHub no longer accepts your account password for Git operations over HTTPS. Use the GitHub CLI (`gh auth login`) or Git Credential Manager, as described in [Step 9](#step-9-connect-your-computer-to-github), or connect with SSH.

### "Please tell me who you are" When Committing

Git does not know your name and email yet. Run the `git config --global user.name` and `git config --global user.email` commands from [Step 8](#step-8-configure-git).

### Push Rejected: "Updates were rejected because the remote contains work that you do not have locally"

Someone, or you in the browser, changed the repository on GitHub after your last pull. Run:

```bash
git pull
```

Then push again. If Git reports a merge conflict, open the files it lists, resolve the marked sections, then `git add` and `git commit` the result. GitHub's page on [non-fast-forward errors](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors) explains this in more detail.

### Git Keeps Asking for My Credentials

See GitHub's guides to [caching your credentials](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git) and [why Git keeps asking for them](https://docs.github.com/en/get-started/git-basics/why-is-git-always-asking-for-my-credentials).

### I Committed Something I Should Not Have (Like a Password)

Treat any exposed secret as compromised: **change or revoke it immediately** at the service that issued it. Deleting the file in a later commit does not remove it from the repository's history. See GitHub's guide on [removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). If personal data (for example, patron or student information) was exposed, also tell your supervisor or privacy officer, since your institution may have reporting obligations.

### My Branch Is Called `master` Instead of `main`

An older Git configuration may still default to `master` for repositories you create locally. Set the default for future repositories with `git config --global init.defaultBranch main`, as shown in [Step 8](#step-8-configure-git). Repositories you create on GitHub and then clone use the branch name GitHub gave them.

---

## Additional Resources

- [GitHub Docs: Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
- [GitHub Docs: Quickstart for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)
- [GitHub Docs: Set up Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
- [GitHub Docs: Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [GitHub Docs: Git cheatsheet](https://docs.github.com/en/get-started/git-basics/git-cheatsheet)
- [GitHub Docs: Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub Pages documentation](https://docs.github.com/en/pages)
- [GitHub Community discussions](https://github.com/orgs/community/discussions)

---

*Last updated: October 2026. GitHub changes its interface from time to time, so verify steps against the official documentation if something looks different.*

---

[← Previous: Setting Up WSL on Windows](wsl-setup-guide.md) · [Next: Contributing & Feedback →](../CONTRIBUTING.md)
