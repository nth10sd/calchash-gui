# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Tests for oneplus3t.py"""

from __future__ import annotations

from calchashgui.devices.oneplus3t import OP3T


def test_op3t() -> None:
    """Test the OP3T class."""
    assert OP3T()
