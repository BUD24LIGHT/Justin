# CLAUDE.md - AI Assistant Development Guide

## Repository Overview

**Repository Name:** Justin
**Type:** Node.js/npm Package
**Status:** Early Development
**Last Updated:** 2025-12-08

This repository is set up as a Node.js package intended for publication to GitHub Packages. Currently in its initial stages, the repository contains foundational CI/CD infrastructure but minimal source code.

## Repository Structure

```
Justin/
├── .github/
│   └── workflows/
│       └── npm-publish-github-packages.yml  # GitHub Actions workflow for publishing
├── .git/                                     # Git repository data
├── README.md                                 # Basic repository description
└── CLAUDE.md                                 # This file - AI assistant guide
```

### Expected Structure (As Project Grows)

Based on the npm publishing workflow, the following structure is anticipated:

```
Justin/
├── .github/
│   └── workflows/
├── src/                    # Source code files
├── test/                   # Test files
├── dist/                   # Built/compiled output (gitignored)
├── node_modules/           # Dependencies (gitignored)
├── package.json            # npm package configuration
├── tsconfig.json          # TypeScript configuration (if using TS)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── CLAUDE.md              # This file
└── LICENSE                # License file
```

## Development Workflow

### Git Branch Strategy

This repository uses a structured branching strategy for AI-assisted development:

- **Feature Branches:** Follow the pattern `claude/claude-md-<identifier>-<session-id>`
- **Current Branch:** `claude/claude-md-miwn554vdwilt653-01SFGXNYQHWpbbXSZ7pfGFps`
- **Main Branch:** (Not yet specified - likely `main` or `master`)

#### Branch Naming Rules
- All AI-generated branches MUST start with `claude/`
- Branch names must end with the matching session ID
- This naming convention is enforced - pushes to incorrectly named branches will fail with 403 errors

### Commit Workflow

1. **Make Changes:** Develop features on the designated feature branch
2. **Commit:** Use clear, descriptive commit messages
3. **Push:** Always use `git push -u origin <branch-name>`
4. **Retry Logic:** If push fails due to network errors, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)

### Current Git State

**Recent Commits:**
- `7090f7c` - Create npm-publish-github-packages.yml
- `d50b77e` - first commit

**Current Status:** Clean working directory

## CI/CD Pipeline

### GitHub Actions Workflow

**File:** `.github/workflows/npm-publish-github-packages.yml`

**Trigger:** On release creation

**Jobs:**

1. **Build Job**
   - Runs on: `ubuntu-latest`
   - Node version: `20`
   - Steps:
     - Checkout code
     - Setup Node.js
     - Install dependencies (`npm ci`)
     - Run tests (`npm test`)

2. **Publish Job**
   - Runs after: Build job succeeds
   - Runs on: `ubuntu-latest`
   - Permissions: Read contents, write packages
   - Registry: `https://npm.pkg.github.com/`
   - Steps:
     - Checkout code
     - Setup Node.js with GitHub Packages registry
     - Install dependencies (`npm ci`)
     - Publish package (`npm publish`)

### Required Files for CI/CD

Before the workflow can succeed, the following must be created:

- [ ] `package.json` - Must include name, version, repository, publishConfig
- [ ] Test files and test script in package.json
- [ ] Source code files

## Development Conventions

### Code Quality Standards

1. **Testing Requirements**
   - All code must have corresponding tests
   - Tests must pass before publishing
   - Use `npm test` to run test suite

2. **Dependencies**
   - Use `npm ci` for reproducible builds (not `npm install`)
   - Keep `package-lock.json` in version control

3. **Node.js Version**
   - Target Node.js version: 20
   - Ensure compatibility with this version

### File Organization

1. **Source Files**
   - Place source code in `src/` directory
   - Use clear, descriptive file names
   - Follow consistent naming conventions (camelCase or kebab-case)

2. **Tests**
   - Place tests in `test/` or `__tests__/` directories
   - Name test files with `.test.js` or `.spec.js` suffix

3. **Configuration**
   - Keep configuration files in repository root
   - Document any environment variables required

### Security Best Practices

1. **Avoid Security Vulnerabilities**
   - No command injection
   - No XSS vulnerabilities
   - No SQL injection
   - Follow OWASP Top 10 guidelines

2. **Secrets Management**
   - Never commit secrets or API keys
   - Use environment variables for sensitive data
   - Leverage GitHub Secrets for CI/CD

3. **Dependency Security**
   - Regularly update dependencies
   - Run `npm audit` to check for vulnerabilities

## AI Assistant Guidelines

### When Working on This Repository

1. **Always Read Before Modifying**
   - Never propose changes to code you haven't read
   - Understand existing code before suggesting modifications

2. **Avoid Over-Engineering**
   - Only make changes that are directly requested or clearly necessary
   - Keep solutions simple and focused
   - Don't add features, refactor code, or make "improvements" beyond what was asked
   - Don't add error handling for scenarios that can't happen

3. **Minimal Changes Philosophy**
   - A bug fix doesn't need surrounding code cleaned up
   - A simple feature doesn't need extra configurability
   - Don't add docstrings, comments, or type annotations to unchanged code
   - Three similar lines of code is better than a premature abstraction

4. **Delete Unused Code**
   - Avoid backwards-compatibility hacks
   - If something is unused, delete it completely
   - No `_vars` renaming, re-exporting types, or `// removed` comments

5. **Task Management**
   - Use TodoWrite tool for multi-step tasks
   - Mark todos as completed immediately after finishing
   - Only one task should be in_progress at a time
   - Keep todos updated in real-time

### Git Operations for AI Assistants

1. **Pushing Code**
   - Always use: `git push -u origin <branch-name>`
   - Branch must follow `claude/*-<session-id>` pattern
   - Retry on network failures: up to 4 times with exponential backoff

2. **Fetching/Pulling**
   - Prefer: `git fetch origin <branch-name>`
   - For pulls: `git pull origin <branch-name>`
   - Apply same retry logic on network failures

3. **Commits**
   - Use clear, descriptive messages
   - Focus on "why" rather than "what"
   - Follow existing commit message style
   - Use heredoc for commit messages:
     ```bash
     git commit -m "$(cat <<'EOF'
     Commit message here.
     EOF
     )"
     ```

4. **Pull Requests**
   - Create PRs using `gh pr create` (if available)
   - Include comprehensive summary with bullet points
   - Add test plan checklist
   - Reference all commits in the PR, not just the latest

### Communication Style

1. **Output Format**
   - Responses displayed on CLI interface
   - Keep responses short and concise
   - Use GitHub-flavored markdown for formatting
   - Output text directly; never use bash echo or comments to communicate

2. **Tone**
   - Professional and objective
   - Prioritize technical accuracy over validation
   - Avoid emojis unless explicitly requested
   - No excessive praise or superlatives

3. **Code References**
   - Use pattern: `file_path:line_number`
   - Example: "Error handling occurs in src/services/process.ts:712"

## Project-Specific Conventions

### Package Configuration

When creating `package.json`, ensure it includes:

```json
{
  "name": "@BUD24LIGHT/justin",
  "version": "0.1.0",
  "repository": {
    "type": "git",
    "url": "https://github.com/BUD24LIGHT/Justin.git"
  },
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  },
  "scripts": {
    "test": "npm test command here"
  }
}
```

### Release Process

1. Ensure all tests pass
2. Update version in `package.json`
3. Commit changes
4. Create a GitHub release
5. GitHub Actions will automatically build and publish

## Common Tasks

### Setting Up the Project

```bash
# Install dependencies
npm ci

# Run tests
npm test

# Build (if applicable)
npm run build
```

### Making Changes

```bash
# Check current status
git status

# Stage changes
git add <files>

# Commit
git commit -m "descriptive message"

# Push to feature branch
git push -u origin claude/claude-md-miwn554vdwilt653-01SFGXNYQHWpbbXSZ7pfGFps
```

### Creating a Pull Request

```bash
# Ensure branch is up to date
git fetch origin main
git merge origin/main

# Push changes
git push -u origin <branch-name>

# Create PR (if gh CLI available)
gh pr create --title "PR title" --body "$(cat <<'EOF'
## Summary
- Change 1
- Change 2

## Test plan
- [ ] Test item 1
- [ ] Test item 2
EOF
)"
```

## Troubleshooting

### Common Issues

1. **Push fails with 403**
   - Verify branch name follows `claude/*-<session-id>` pattern
   - Ensure branch name ends with correct session ID

2. **npm ci fails**
   - Ensure `package.json` and `package-lock.json` exist
   - Check Node.js version (should be 20)

3. **Tests fail**
   - Ensure test files are properly configured
   - Check that test script is defined in `package.json`

4. **Workflow fails**
   - Verify all required files exist
   - Check that package.json has correct publishConfig
   - Ensure tests pass locally before pushing

## Resources

- **Repository:** https://github.com/BUD24LIGHT/Justin
- **GitHub Actions:** https://docs.github.com/en/actions
- **npm Publishing:** https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-npm-registry

## Maintenance

This CLAUDE.md file should be updated when:
- Project structure changes significantly
- New conventions or workflows are established
- CI/CD pipeline is modified
- New development tools are introduced
- Project reaches new milestones (e.g., first release)

---

**Note to AI Assistants:** This is a living document. Keep it updated as the project evolves. When making significant changes to the repository structure or workflow, update this file accordingly.
