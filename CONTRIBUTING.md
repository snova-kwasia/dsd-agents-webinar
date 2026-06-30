<div align="center">

<img src="assets/sambanova_logo.png" alt="SambaNova" width="300">

# Contributing to Deep Agents from Scratch

</div>

We welcome contributions! This project is a collaborative educational series on building AI agents with LangGraph and SambaNova Cloud. Please read these guidelines before contributing.

## Before You Start

**Open an issue first** for significant changes. This lets us discuss the direction before you invest time in code or notebooks. For minor fixes (typos, small bugs), feel free to submit directly.

## Notebooks

This project is notebook-first. When contributing notebooks or modifying existing ones:

- **Execute all cells** before committing — no empty outputs or "todo" placeholders
- **Clear outputs** if you're submitting a template/demo notebook that shows code without running it
- **Restart and run all** (`Kernel → Restart & Run All`) to verify the notebook runs end-to-end
- **Test with different inputs** — notebooks should demonstrate realistic, educational examples
- **Keep cells focused** — one concept or logical step per cell
- **Add cell comments** for non-obvious code sections
- **Update the table** in README.md if adding a new session notebook

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/dsd-agents-webinar.git
   cd dsd-agents-webinar
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies**:
   ```bash
   uv sync
   ```

## Development Setup

```bash
# Copy environment template
cp .env.example .env
```

## Environment Variables

Never commit API keys or secrets. The `.env` file is gitignored. Use `.env.example` as a template for required variables.

When adding new features that require environment variables:
- Update `.env.example` with the new variable and a comment
- Document the variable in the README setup section

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code
- Use meaningful variable and function names (no single letters except loop counters)
- Keep lines under 100 characters when practical
- Add docstrings to public functions and classes
- Type hints are encouraged for complex functions

For notebooks:
- Prefer explicit imports over `from module import *`
- Use consistent naming conventions across related notebooks
- Add `# %%` cell markers for portability with IDEs

## Documentation

Good documentation is required, not optional:

- **README.md**: Update if you add new features, notebooks, or dependencies
- **Docstrings**: Required for new functions and classes
- **Comments**: Explain *why*, not *what* — the code shows what, comments should clarify intent
- **Examples**: Include usage examples for non-trivial utility functions

## Testing

Run tests before submitting a PR:

```bash
# Run a specific test file
pytest tests/your_test_file.py -v

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=.
```

**Test requirements:**
- New features require tests
- Bug fixes should include a test that reproduces the bug
- All tests must pass before merging
- Aim for meaningful test coverage, not just line coverage

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb: `Add`, `Fix`, `Update`, `Remove`, `Refactor`
- Keep the first line under 72 characters
- Reference issues when applicable: `Closes #123` or `Refs #456`

**Format:**
```
Short summary (under 72 chars)

Optional longer explanation if needed. Wrap at 72 characters.
Explain the *why* not the *what* when relevant.
```

## Pull Request Process

1. **Open an issue first** for significant changes (optional for small fixes)
2. **Create** a feature branch from `main`
3. **Make your changes** — commit early and often
4. **Add tests** for new functionality
5. **Update documentation** — README, docstrings, comments
6. **Run tests** and ensure they pass
7. **Push** your branch to your fork
8. **Open a PR** against `main` with:
   - Clear title describing the change
   - Description of what changed and why
   - Link to related issues
   - Note any breaking changes

**PR titles** follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions/updates
- `refactor:` Code restructuring without behavior change
- `chore:` Maintenance tasks

## Code Review

We review PRs for:
- Correctness and maintainability
- Test coverage
- Documentation completeness
- Adherence to these guidelines

Be responsive to review feedback. Small, focused PRs get reviewed faster.

## Resources

- [SambaNova](https://sambanova.ai/) — Company homepage
- [SambaNova Cloud](https://cloud.sambanova.ai/) — API documentation and keys
- [SambaNova Documentation](https://docs.sambanova.ai/) — Full platform docs
- [Data Science Dojo](https://datasciencedojo.com/) — Webinar series host
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) — Agent framework used in this project

## Questions?

Open an issue for questions about contributing. For quick questions, check existing issues first.
