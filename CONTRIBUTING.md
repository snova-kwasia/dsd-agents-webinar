<div align="center">

<img src="assets/sambanova_logo.png" alt="SambaNova" width="300">

# Contributing to Deep Agents from Scratch

</div>

Thank you for your interest in contributing! This document outlines how to contribute to this project.

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

## Development Setup

```bash
# Install dependencies
uv sync

# Copy environment template
cp .env.example .env

# Add your API keys to .env
```

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code
- Use meaningful variable and function names
- Keep lines under 100 characters when practical
- Add docstrings to public functions

## Testing

Run tests before submitting a PR:

```bash
# Run a specific test file
pytest tests/your_test_file.py

# Run with verbose output
pytest tests/ -v
```

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep the first line under 72 characters
- Reference issues when applicable

## Pull Request Process

1. **Update** documentation if needed
2. **Ensure** tests pass
3. **Push** your branch to your fork
4. **Open** a pull request against `main`
5. **Describe** your changes and why they're needed

## Resources

- [SambaNova](https://sambanova.ai/) — Company homepage
- [SambaNova Cloud](https://cloud.sambanova.ai/) — API documentation and keys
- [SambaNova Documentation](https://docs.sambanova.ai/) — Full platform docs
- [Data Science Dojo](https://datasciencedojo.com/) — Webinar series host

## Questions?

Open an issue for questions about contributing.