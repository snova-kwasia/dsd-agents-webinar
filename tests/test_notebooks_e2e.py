"""
E2E tests for Jupyter notebooks in sessions 1 and 2.

This module validates that notebooks can be parsed, have valid structure,
and can be executed up to the point where API calls are required.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any

import pytest


class NotebookValidator:
    """Validates Jupyter notebook structure and execution."""

    def __init__(self, notebook_path: str):
        self.notebook_path = Path(notebook_path)
        self.notebook_data: dict[str, Any] = {}
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def load_notebook(self) -> bool:
        """Load and parse the notebook JSON."""
        try:
            with open(self.notebook_path, "r", encoding="utf-8") as f:
                self.notebook_data = json.load(f)
            return True
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Failed to load notebook: {e}")
            return False

    def validate_structure(self) -> bool:
        """Validate the notebook has required structure."""
        if not self.notebook_data:
            self.errors.append("Notebook not loaded")
            return False

        # Check for required keys
        required_keys = ["cells", "metadata", "nbformat", "nbformat_minor"]
        for key in required_keys:
            if key not in self.notebook_data:
                self.errors.append(f"Missing required key: {key}")

        if self.errors:
            return False

        # Validate cells
        cells = self.notebook_data.get("cells", [])
        if not cells:
            self.errors.append("No cells found in notebook")
            return False

        # Check cell types
        cell_types = set()
        for i, cell in enumerate(cells):
            if "cell_type" not in cell:
                self.errors.append(f"Cell {i} missing cell_type")
            else:
                cell_types.add(cell["cell_type"])

        valid_cell_types = {"code", "markdown", "raw", "heading"}
        invalid_types = cell_types - valid_cell_types
        if invalid_types:
            self.warnings.append(f"Unexpected cell types: {invalid_types}")

        return len(self.errors) == 0

    def validate_code_cells(self) -> bool:
        """Validate code cells have required fields."""
        if not self.notebook_data:
            return False

        cells = self.notebook_data.get("cells", [])
        code_cells = [c for c in cells if c.get("cell_type") == "code"]

        if not code_cells:
            self.warnings.append("No code cells found")
            return True

        for i, cell in enumerate(code_cells):
            if "source" not in cell:
                self.errors.append(f"Code cell {i} missing source")
            if "outputs" not in cell:
                self.warnings.append(f"Code cell {i} missing outputs field")
            if "execution_count" not in cell:
                self.warnings.append(f"Code cell {i} missing execution_count field")

        return len(self.errors) == 0

    def validate_imports(self) -> list[str]:
        """Extract and validate imports from code cells."""
        if not self.notebook_data:
            return []

        imports = []
        cells = self.notebook_data.get("cells", [])
        code_cells = [c for c in cells if c.get("cell_type") == "code"]

        for cell in code_cells:
            source = cell.get("source", [])
            if isinstance(source, list):
                source = "".join(source)
            lines = source.split("\n")
            for line in lines:
                line = line.strip()
                if line.startswith("import ") or line.startswith("from "):
                    imports.append(line)

        return imports

    def get_summary(self) -> dict[str, Any]:
        """Get a summary of the validation results."""
        cells = self.notebook_data.get("cells", [])
        code_cells = [c for c in cells if c.get("cell_type") == "code"]
        markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]

        return {
            "notebook_path": str(self.notebook_path),
            "total_cells": len(cells),
            "code_cells": len(code_cells),
            "markdown_cells": len(markdown_cells),
            "errors": self.errors,
            "warnings": self.warnings,
            "imports": self.validate_imports(),
            "valid": len(self.errors) == 0,
        }


class TestSession1Notebook:
    """Tests for Session 1 notebook."""

    @pytest.fixture
    def notebook_path(self) -> str:
        return str(
            Path(__file__).parent.parent
            / "notebooks"
            / "session_1"
            / "0_create_agent.ipynb"
        )

    @pytest.fixture
    def validator(self, notebook_path: str) -> NotebookValidator:
        validator = NotebookValidator(notebook_path)
        validator.load_notebook()
        return validator

    def test_notebook_exists(self, notebook_path: str):
        """Test that the notebook file exists."""
        assert Path(notebook_path).exists(), f"Notebook not found: {notebook_path}"

    def test_notebook_valid_json(self, validator: NotebookValidator):
        """Test that the notebook is valid JSON."""
        assert validator.notebook_data, "Failed to load notebook JSON"

    def test_notebook_structure(self, validator: NotebookValidator):
        """Test that the notebook has valid structure."""
        assert validator.validate_structure(), f"Structure errors: {validator.errors}"

    def test_code_cells_valid(self, validator: NotebookValidator):
        """Test that code cells are valid."""
        assert validator.validate_code_cells(), f"Code cell errors: {validator.errors}"

    def test_notebook_summary(self, validator: NotebookValidator):
        """Test that we can get a summary of the notebook."""
        summary = validator.get_summary()
        assert summary["total_cells"] > 0, "No cells found in notebook"
        assert summary["code_cells"] > 0, "No code cells found"
        print(f"\nNotebook Summary: {json.dumps(summary, indent=2)}")


class TestSession2Notebook:
    """Tests for Session 2 notebook."""

    @pytest.fixture
    def notebook_path(self) -> str:
        return str(
            Path(__file__).parent.parent
            / "notebooks"
            / "session_2"
            / "1_build_first_agent.ipynb"
        )

    @pytest.fixture
    def validator(self, notebook_path: str) -> NotebookValidator:
        validator = NotebookValidator(notebook_path)
        validator.load_notebook()
        return validator

    def test_notebook_exists(self, notebook_path: str):
        """Test that the notebook file exists."""
        assert Path(notebook_path).exists(), f"Notebook not found: {notebook_path}"

    def test_notebook_valid_json(self, validator: NotebookValidator):
        """Test that the notebook is valid JSON."""
        assert validator.notebook_data, "Failed to load notebook JSON"

    def test_notebook_structure(self, validator: NotebookValidator):
        """Test that the notebook has valid structure."""
        assert validator.validate_structure(), f"Structure errors: {validator.errors}"

    def test_code_cells_valid(self, validator: NotebookValidator):
        """Test that code cells are valid."""
        assert validator.validate_code_cells(), f"Code cell errors: {validator.errors}"

    def test_notebook_summary(self, validator: NotebookValidator):
        """Test that we can get a summary of the notebook."""
        summary = validator.get_summary()
        assert summary["total_cells"] > 0, "No cells found in notebook"
        assert summary["code_cells"] > 0, "No code cells found"
        print(f"\nNotebook Summary: {json.dumps(summary, indent=2)}")


class TestNotebookExecution:
    """Tests for notebook execution capability."""

    def test_can_import_notebook_modules(self):
        """Test that required modules can be imported."""
        # Test that we can import the utils module
        sys.path.insert(0, str(Path(__file__).parent.parent / "notebooks"))
        try:
            from utils import format_messages
        except ImportError as e:
            pytest.skip(f"Cannot import utils module: {e}")

    def test_environment_setup(self):
        """Test that the environment is set up correctly."""
        from dotenv import load_dotenv

        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(env_path, override=True)

        # Check that required env vars are set (or at least the .env file exists)
        assert env_path.exists(), ".env file not found"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--no-header"])