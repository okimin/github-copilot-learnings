import pytest
from email_utils import is_valid_email

def test_valid_emails():
    # Standard valid email
    assert is_valid_email("user@example.com") is True
    # Valid email with numbers and dots
    assert is_valid_email("john.doe123@example.co.uk") is True
    # Valid email with sub-domain (edge case)
    assert is_valid_email("user@mail.example.com") is True

def test_invalid_emails():
    # Missing '@' symbol
    assert is_valid_email("userexample.com") is False
    # Missing domain
    assert is_valid_email("user@") is False
    # Invalid characters in email
    assert is_valid_email("user!@example.com") is False