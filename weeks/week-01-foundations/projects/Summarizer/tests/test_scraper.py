import pytest
from app.tools.scraper import _validate_url


def test_validate_url_rejects_invalid_scheme() -> None:
    with pytest.raises(ValueError):
        _validate_url("ftp://example.com")


def test_validate_url_accepts_https() -> None:
    _validate_url("https://example.com")
