# CLAUDE.md - AI Assistant Guide for Justin Repository

Last Updated: 2025-12-08

## Repository Overview

**Repository Name**: Justin
**Current State**: Minimal/Skeleton Repository
**Intended Purpose**: Node.js package with GitHub Packages publishing support

This repository is currently in its initial state with minimal infrastructure. It appears to be set up as a Node.js package intended for distribution via GitHub Packages.

## Repository Structure

```
Justin/
├── .github/
│   └── workflows/
│       └── npm-publish-github-packages.yml  # GitHub Actions workflow
├── .git/                                     # Git repository
└── README.md                                 # Basic repository documentation
```

### Missing Components (Expected to be Added)

Based on the GitHub Actions workflow configuration, the following components are expected but not yet present:

- `package.json` - Node.js package configuration
- `src/` or `lib/` - Source code directory
- `test/` or `__tests__/` - Test files directory
- `.gitignore` - Git ignore configuration
- `tsconfig.json` - If using TypeScript
- Additional documentation files

## GitHub Actions Workflow

### npm-publish-github-packages.yml

**Trigger**: On release creation
**Node Version**: 20
**Registry**: GitHub Packages (https://npm.pkg.github.com/)

**Jobs**:
1. **build**
   - Runs `npm ci` (requires package-lock.json)
   - Runs `npm test` (requires test script in package.json)

2. **publish-gpr**
   - Depends on successful build
   - Publishes package to GitHub Packages
   - Uses GITHUB_TOKEN for authentication

## Development Guidelines for AI Assistants

### When Creating New Files

1. **package.json**: Must include:
   - Name scoped to GitHub username/org (e.g., `@BUD24LIGHT/justin`)
   - Version number (start with `0.1.0` or `1.0.0`)
   - `test` script (required by workflow)
   - `publishConfig` pointing to GitHub Packages registry
   - Repository, author, and license information

2. **Source Code**:
   - Use `src/` for source files (TypeScript preferred) or `lib/` for JavaScript
   - Follow standard Node.js module patterns
   - Include proper exports in package.json (`main`, `module`, `types`)

3. **.gitignore**: Should include:
   - `node_modules/`
   - Build output directories (`dist/`, `build/`)
   - Environment files (`.env`)
   - IDE configurations (`.vscode/`, `.idea/`)
   - OS files (`.DS_Store`, `Thumbs.db`)

4. **Tests**:
   - Use a testing framework (Jest, Mocha, or Vitest recommended)
   - Place tests in `test/` or `__tests__/` directories
   - Ensure `npm test` command works before any release

### Git Workflow

**Current Branch**: `claude/claude-md-miwn6ocowhp6sns6-016C9X2j6WqCGWSLLiWeNHDf`

#### Branch Naming Convention
- Feature branches created by Claude should follow: `claude/claude-md-{random-id}`
- All development should occur on feature branches
- Never push directly to main/master

#### Commit Message Guidelines
- Use conventional commits format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `test:` for test additions/changes
  - `chore:` for maintenance tasks
  - `refactor:` for code refactoring

#### Push Protocol
- Always use `git push -u origin <branch-name>`
- Branch names must start with `claude/` and match session ID
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) on network failures

### Code Style and Conventions

Since the repository is in its initial state, establish conventions early:

1. **Language**: Determine if JavaScript or TypeScript will be used
2. **Linting**: Consider ESLint for code quality
3. **Formatting**: Consider Prettier for code formatting
4. **Module System**: Use ES modules (ESM) for modern Node.js compatibility

### Testing Requirements

- All code should have corresponding tests
- Minimum test coverage threshold should be defined
- Tests must pass before creating releases
- Use `npm test` as the standard test command

### Documentation Standards

1. **README.md**: Should include:
   - Project description and purpose
   - Installation instructions
   - Usage examples
   - API documentation (if applicable)
   - Contributing guidelines
   - License information

2. **Code Comments**:
   - Use JSDoc for function documentation
   - Add comments only where logic isn't self-evident
   - Avoid over-commenting obvious code

3. **CHANGELOG.md**: Track version changes and updates

### Release Process

1. Ensure all tests pass locally with `npm test`
2. Update version in package.json (follow semver)
3. Update CHANGELOG.md with changes
4. Create a git tag matching the version
5. Create a GitHub release
6. GitHub Actions will automatically build and publish to GitHub Packages

### Security Considerations

- Never commit sensitive information (API keys, tokens, passwords)
- Use environment variables for configuration
- Regularly update dependencies to patch vulnerabilities
- Review dependency security with `npm audit`

### Performance Guidelines

- Keep the package lightweight and focused
- Minimize dependencies when possible
- Use peer dependencies for optional features
- Tree-shakeable exports for better bundle sizes

### AI Assistant Specific Notes

1. **Before Making Changes**:
   - Always read existing files before modifying
   - Check for package.json to understand project dependencies
   - Review existing code patterns and follow them

2. **When Adding Features**:
   - Create tests alongside implementation
   - Update documentation (README, JSDoc comments)
   - Consider backward compatibility
   - Keep changes focused and minimal

3. **Error Handling**:
   - Avoid over-engineering error handling
   - Only validate at system boundaries
   - Trust internal code and framework guarantees

4. **Avoid Over-Engineering**:
   - Don't add features beyond what's requested
   - Don't create abstractions for one-time operations
   - Keep solutions simple and focused
   - Three similar lines of code is better than premature abstraction

5. **Git Operations**:
   - Always develop on the designated feature branch
   - Commit with clear, descriptive messages
   - Push to the specified branch when complete
   - Create the branch locally if it doesn't exist

## Current Status Summary

As of 2025-12-08, this repository contains:
- ✅ GitHub Actions workflow for npm publishing
- ✅ Basic README.md
- ❌ No package.json
- ❌ No source code
- ❌ No tests
- ❌ No .gitignore

**Next Steps for Development**:
1. Create package.json with proper configuration
2. Set up project structure (src/, test/, etc.)
3. Add .gitignore file
4. Implement core functionality
5. Add comprehensive tests
6. Update README.md with usage documentation
7. Create first release

## Additional Resources

- [GitHub Packages Documentation](https://docs.github.com/en/packages)
- [npm Documentation](https://docs.npmjs.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Note**: This document should be updated as the repository evolves and new conventions are established.
