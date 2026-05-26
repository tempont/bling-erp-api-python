"""Tests for BaseResource docstring auto-population."""

from __future__ import annotations

from bling_erp_api.resources.base import BaseResource, is_substantive_docstring


class TestIsSubstantiveDocstring:
    """Tests for the heuristic that detects already-good docstrings."""

    def test_empty_docstring_is_not_substantive(self) -> None:
        """Empty string is not substantive."""
        assert not is_substantive_docstring("")

    def test_none_like_docstring_is_not_substantive(self) -> None:
        """Whitespace-only string is not substantive."""
        assert not is_substantive_docstring("   ")

    def test_short_one_liner_is_not_substantive(self) -> None:
        """Short one-line docstring is not substantive."""
        assert not is_substantive_docstring("Obtém um produto pelo ID.")

    def test_compatibility_alias_is_not_substantive(self) -> None:
        """Compatibility alias docstring is not substantive."""
        assert not is_substantive_docstring("Compatibility alias for ``obter()``.")

    def test_multiline_docstring_is_substantive(self) -> None:
        """Multi-line docstring is substantive."""
        doc = "First line.\n\nSecond line.\n\nThird line."
        assert is_substantive_docstring(doc)

    def test_docstring_with_args_is_substantive(self) -> None:
        """Docstring with Args section is substantive."""
        doc = "Summary.\n\nArgs:\n    x: Something."
        assert is_substantive_docstring(doc)

    def test_docstring_with_returns_is_substantive(self) -> None:
        """Docstring with Returns section is substantive."""
        doc = "Summary.\n\nReturns:\n    Something."
        assert is_substantive_docstring(doc)

    def test_long_one_liner_is_substantive(self) -> None:
        """Long one-line docstring is substantive."""
        doc = "A" * 61
        assert is_substantive_docstring(doc)


class TestAutoPopulation:
    """Tests for the auto-population of docstrings via __init_subclass__."""

    def test_subclass_triggers_autopopulate(self) -> None:
        """Creating a subclass calls _autopopulate_docstrings."""
        called: list[str] = []

        class _FakeBase(BaseResource):
            @classmethod
            def _autopopulate_docstrings(cls) -> None:
                called.append(cls.__name__)

        class TestResource(_FakeBase):
            """Test resource."""

            def some_method(self) -> None:
                """Short doc."""

        _ = TestResource  # Used through __init_subclass__ side effects
        assert "TestResource" in called

    def test_method_with_substantive_docstring_is_preserved(self) -> None:
        """A method with a multi-line docstring keeps it."""

        class TestResource2(BaseResource):
            """Test resource."""

            def preserved_method(self) -> None:
                """First line.

                Second line.

                Third line.
                """

        # The original docstring should be preserved (no key match, no override)
        assert TestResource2.preserved_method.__doc__ is not None
        assert "First line" in (TestResource2.preserved_method.__doc__ or "")
