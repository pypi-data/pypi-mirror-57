# This file is part of tiny_gnupg, a small-as-possible solution for
# handling GnuPG ECC keys.
#
# Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html
# Copyright © 2019-2020 Gonzo Investigatory Journalism Agency, LLC
#             <gonzo.development@protonmail.ch>
#           © 2019-2020 Richard Machado <rmlibre@riseup.net>
# All rights reserved.
#

from setuptools import setup, find_packages

description = """
tiny_gnupg - A small-as-possible solution for handling GnuPG ECC keys.
""".replace("\n", "")

with open("README.rst", "r") as readme:
    long_description = readme.read()

setup(
    name="tiny_gnupg",
    license="GPLv3",
    version="0.2.1",
    description=description,
    long_description=long_description,
    author="Gonzo Investigatory News Agency, LLC",
    author_email="gonzo.development@protonmail.ch",
    maintainer="Gonzo Investigatory News Agency, LLC",
    maintainer_email="gonzo.development@protonmail.ch",
    classifiers=['Programming Language :: Python :: 3'],
    packages=find_packages(),
)
