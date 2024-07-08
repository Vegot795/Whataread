import pytest
import unittest.mock as mock
import App.AppMod as AppMod

@mock.patch("App.AppMod.delete_book")
def test_delete_book(mock_delete_book):
    mock_delete_book.return_value = "Book deleted"
    