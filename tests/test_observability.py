import os
import pytest
from unittest.mock import patch, MagicMock


class TestObservabilityConfig:
    """Tests for observability configuration (Langfuse and LangSmith)."""

    def test_langsmith_env_vars_in_example(self):
        """Verify LangSmith environment variables are documented in .env.example."""
        env_example_path = os.path.join(os.path.dirname(__file__), "..", ".env.example")
        with open(env_example_path) as f:
            content = f.read()
        
        assert "LANGSMITH_TRACING" in content
        assert "LANGSMITH_API_KEY" in content

    def test_langfuse_env_vars_in_example(self):
        """Verify Langfuse environment variables are documented in .env.example."""
        env_example_path = os.path.join(os.path.dirname(__file__), "..", ".env.example")
        with open(env_example_path) as f:
            content = f.read()
        
        assert "LANGFUSE_PUBLIC_KEY" in content
        assert "LANGFUSE_SECRET_KEY" in content
        assert "LANGFUSE_BASE_URL" in content

    def test_langsmith_import(self):
        """Verify langsmith package can be imported."""
        try:
            from langsmith import traceable
            assert callable(traceable)
        except ImportError:
            pytest.skip("langsmith not installed")

    def test_langsmith_config_detection(self):
        """Test LangSmith configuration detection logic."""
        with patch.dict(os.environ, {"LANGSMITH_TRACING": "true", "LANGSMITH_API_KEY": "test-key"}):
            langsmith_enabled = os.environ.get("LANGSMITH_TRACING") == "true" and bool(os.environ.get("LANGSMITH_API_KEY"))
            assert langsmith_enabled is True

    def test_langsmith_config_disabled(self):
        """Test LangSmith configuration detection when disabled."""
        with patch.dict(os.environ, {"LANGSMITH_TRACING": "false", "LANGSMITH_API_KEY": ""}, clear=True):
            langsmith_enabled = os.environ.get("LANGSMITH_TRACING") == "true" and bool(os.environ.get("LANGSMITH_API_KEY"))
            assert langsmith_enabled is False

    def test_langsmith_config_missing_key(self):
        """Test LangSmith configuration detection when key is missing."""
        with patch.dict(os.environ, {"LANGSMITH_TRACING": "true"}, clear=True):
            langsmith_enabled = os.environ.get("LANGSMITH_TRACING") == "true" and bool(os.environ.get("LANGSMITH_API_KEY"))
            assert langsmith_enabled is False


class TestDependencies:
    """Tests for project dependencies."""

    def test_langsmith_in_dependencies(self):
        """Verify langsmith is in pyproject.toml dependencies."""
        pyproject_path = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
        with open(pyproject_path) as f:
            content = f.read()
        
        assert "langsmith" in content

    def test_langfuse_in_dependencies(self):
        """Verify langfuse is in pyproject.toml dependencies."""
        pyproject_path = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
        with open(pyproject_path) as f:
            content = f.read()
        
        assert "langfuse" in content