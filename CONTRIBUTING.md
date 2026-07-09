# Contributing Guide

Thank you for contributing to the **Lead Management System**! We appreciate your time and effort.

This guide explains our development workflow, branching strategy, and the process for contributing code.

## Repository

Repository: `https://github.com/leadvecto/lead_management_system`

---

# Branching Strategy

We maintain two primary branches:

* **`main`** – Production-ready, stable code.
* **`develop`** – Active development branch.

### Development Flow

1. All new work starts from the **`develop`** branch.
2. Create a separate feature or bugfix branch from `develop`.
3. Open a Pull Request **into `develop`**.
4. After review and approval, the PR is merged into `develop`.
5. Once `develop` reaches a stable milestone, it is merged into `main`.

> **Do not open Pull Requests directly to `main`.**

---

# Contribution Workflow

## 1. Create or Find an Issue

Before writing any code:

* Search existing issues to avoid duplicate work.
* If your issue doesn't exist, create a new one.
* Wait for discussion if the change is significant.

---

## 2. Assign Yourself

Assign yourself to the issue before starting work.

This helps everyone know the issue is already being worked on.

---

## 3. Clone the Repository

```bash
git clone https://github.com/leadvecto/lead_management_system.git
cd lead_management_system
```

---

## 4. Checkout the Develop Branch

```bash
git checkout develop
git pull origin develop
```

---

## 5. Create a Feature Branch

Always create your branch from `develop`.

Examples:

```text
feature/user-authentication
feature/dashboard
bugfix/login-error
docs/update-contributing
refactor/api-cleanup
```

Command:

```bash
git checkout -b feature/your-feature-name
```

---

## 6. Make Your Changes

Implement your feature or fix.

Please ensure:

* Code follows project conventions.
* Keep commits focused.
* Update documentation if required.
* Add tests where applicable.

---

## 7. Commit Your Changes

```bash
git add .
git commit -m "feat: add lead filtering"
```

Examples of commit messages:

```text
feat: add lead filtering
fix: resolve duplicate lead issue
docs: update API documentation
refactor: simplify authentication logic
test: add lead service tests
```

---

## 8. Push Your Branch

```bash
git push origin feature/your-feature-name
```

---

# Creating a Pull Request

Open a Pull Request with:

* **Base branch:** `develop`
* **Compare branch:** your feature branch

### Pull Request Title

Use a clear, descriptive title.

Example:

```text
feat: add lead filtering
```

### Pull Request Description

**Link the related GitHub Issue in the PR description** so GitHub automatically closes it after the PR is merged.

For example:

```text
Closes #42
```

or

```text
Fixes #42
```

or

```text
Resolves #42
```

Replace `42` with the actual issue number.

> **Important:** Adding one of these keywords in the PR description (not just in a comment) ensures the linked issue is automatically closed when the PR is merged.

You should also briefly describe:

* What was changed
* Why it was changed
* Any screenshots (if UI changes)
* Any additional notes for reviewers

---

# Code Review

Every Pull Request is reviewed before merging.

You may be asked to:

* Improve the implementation
* Address review comments
* Resolve merge conflicts
* Update documentation

Push additional commits to the same branch until the review is complete.

---

# Keeping Your Branch Updated

If `develop` has new commits:

```bash
git checkout develop
git pull origin develop

git checkout feature/your-feature-name
git merge develop
```

Resolve any conflicts and push again:

```bash
git push origin feature/your-feature-name
```

---

# After Your Pull Request Is Merged

Delete your local branch:

```bash
git branch -d feature/your-feature-name
```

Delete the remote branch:

```bash
git push origin --delete feature/your-feature-name
```

Update your local `develop` branch:

```bash
git checkout develop
git pull origin develop
```

---

# Branch Rules

* ❌ Never commit directly to `main`.
* ❌ Never commit directly to `develop`.
* ✅ Always branch from `develop`.
* ✅ Always submit Pull Requests to `develop`.
* ✅ Reference the related issue in your PR description (`Closes #<issue-number>`).
* ✅ Wait for review and approval before merging.

---

# Quick Workflow

```bash
# Clone the repository
git clone https://github.com/leadvecto/lead_management_system.git
cd lead_management_system

# Get latest develop
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/my-feature

# Make changes...

git add .
git commit -m "feat: add new feature"

git push origin feature/my-feature
```

Then:

1. Open a Pull Request to **`develop`**.
2. Add `Closes #<issue-number>` (or `Fixes #<issue-number>`) in the PR description.
3. Request a review.
4. Once approved, your PR will be merged into `develop`.
