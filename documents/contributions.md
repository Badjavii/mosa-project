# Contributions

Your contributions to the repository help the project in various ways. For example, you can fix a code vulnerability, improve the documentation, or add new features.

> Contributions are managed through Git and GitHub. All contributions received will be thoroughly reviewed to determine their feasibility for inclusion in the project.

## Ways to contribute to the project

- **Bug reports:** If you find something that is not working as expected, open an issue describing the problem, the steps to reproduce it, and your environment (OS, browser, versions).
- **Feature requests:** Have an idea that could improve MOSA? Open an issue with the `enhancement` label and describe the use case clearly.
- **Code — bug fixes:** Found a bug and know how to fix it? Fork the repo, apply the fix, and open a pull request referencing the related issue.
- **Code — new features:** Want to implement something new? Open an issue first to discuss it before writing code, so we can align on the approach.
- **Documentation:** Improve existing docs, fix typos, clarify instructions, or write missing sections. Good documentation is as valuable as good code.
- **Translations:** Help make MOSA accessible to more people by translating the documentation or UI strings into other languages.
- **UI/UX design suggestions:** If you have ideas to improve the user experience or the visual design, open an issue with mockups, sketches, or a written description of the improvement.

## How to contribute using Git

1. **Fork** the repository on GitHub.

2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/Badjavii/mosa-project.git
   cd mosa-project
   ```

3. **Create a branch** for your contribution using a descriptive name:
   ```bash
   git checkout -b fix/navbar-mobile-layout
   # or
   git checkout -b feat/dark-mode-toggle
   # or
   git checkout -b docs/improve-installation-guide
   ```

4. **Make your changes.** Follow the existing code style and architecture:
   - Backend: `Router → Service → Repository` — no business logic in routers.
   - Frontend: standalone Angular components, all API calls through `core/services/`.
   - Filenames: `kebab-case` for everything.
   - Commits: follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, etc.).

5. **Test your changes** before submitting:
   ```bash
   # Backend
   cd src/backend && pytest tests/ -v

   # Frontend
   cd src/frontend && ng build
   ```

6. **Push** your branch and open a **Pull Request** against `main`:
   ```bash
   git push origin your-branch-name
   ```
   In the pull request description, explain what you changed and why.

7. **Wait for review.** The maintainer will review your PR and may request changes before merging.

## Reflection and gratitude

The MOSA project team extends its gratitude to those interested in contributing, but we will not accept changes that compromise the project's integrity or make it worse. Therefore, we are notifying you in advance that not all contributions will be approved.

If your contribution is not approved, don't get discouraged and keep trying with other contributions. Be encouraged to improve and strengthen your creativity, but above all, strive for excellence. Effort pays off, and giving your best defines you as a great person.
