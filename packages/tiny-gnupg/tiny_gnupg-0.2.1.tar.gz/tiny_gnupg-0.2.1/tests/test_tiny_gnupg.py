# This file is part of tiny_gnupg, a small-as-possible solution for
# handling GnuPG ECC keys.
#
# Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html
# Copyright © 2019-2020 Gonzo Investigatory Journalism Agency, LLC
#             <gonzo.development@protonmail.ch>
#           © 2019-2020 Richard Machado <rmlibre@riseup.net>
# All rights reserved.
#

import os
import sys

sys.path.append(os.getcwd() + "/../")

import pytest
import tiny_gnupg
from tiny_gnupg import GnuPG


username = "testing_user"
email = "testing.user@tests.net"
passphrase = "test_passphrase"
relative_gpg_path = "../tiny_gnupg/gpghome/gpg2"


@pytest.fixture(scope="module")
def gpg():
    print("setup".center(15, "-"))
    gpg = GnuPG(username, email, passphrase)
    gpg.path = gpg.format_homedir(relative_gpg_path)
    yield gpg
    print("teardown".center(18, "-"))


def test_encode_inputs(gpg):
    inputs = ["1", "y", "q"]
    encoded_inputs = gpg.encode_inputs(*inputs)
    assert type(encoded_inputs) == bytes
    assert encoded_inputs.endswith(b"\n")
    for element in inputs:
        assert bytes(element, "utf-8") in encoded_inputs


def test_command(gpg):
    options = ["--list-keys"]
    command = gpg.command(*options)
    passphrase_command = gpg.command(*options, with_passphrase=True)
    for option in options:
        assert option in command
        assert option in passphrase_command
