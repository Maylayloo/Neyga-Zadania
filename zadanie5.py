import pytest
from unittest.mock import Mock


def user_exists(db, email):
    user = db.find_user_by_email(email)
    return user is not None


def test_user_exists_found():
    mock_db = None  # make Mock
    # your code goes here
    assert user_exists(mock_db, "test@example.com") is True


def test_user_exists_not_found():
    mock_db = None  # make Mock
    # your code goes here
    assert user_exists(mock_db, "notfound@example.com") is False
