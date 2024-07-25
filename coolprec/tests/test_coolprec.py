"""
Unit and regression test for the coolprec package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import coolprec


def test_coolprec_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "coolprec" in sys.modules
