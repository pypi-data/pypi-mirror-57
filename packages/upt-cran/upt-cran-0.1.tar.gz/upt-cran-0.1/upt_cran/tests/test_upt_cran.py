# Copyright 2019      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import unittest

from lxml import etree
import requests_mock

import upt
from upt_cran.upt_cran import CranFrontend
from upt_cran.tests.fake_html import ellipsis_html


class TestCranFrontend(unittest.TestCase):
    def setUp(self):
        self.frontend = CranFrontend()
        self.frontend.tree = etree.HTML(ellipsis_html)

    @requests_mock.mock()
    def test_invalid_package_name(self, requests):
        pkg_name = 'invalid'
        url = f'https://cran.r-project.org/web/packages/{pkg_name}/index.html'
        requests.get(url, status_code=404)
        with self.assertRaises(upt.InvalidPackageNameError):
            self.frontend.parse(pkg_name)

    def test_get_version(self):
        self.assertEqual(self.frontend._get_version(), '0.3.0')

    def test_get_summary(self):
        self.assertEqual(self.frontend._get_summary(),
                         'Tools for Working with ...')

    def test_get_description(self):
        description = '''The ellipsis is a powerful tool for extending \
functions. Unfortunately this power comes at a cost: misspelled arguments \
will be silently ignored. The ellipsis package provides a collection of \
functions to catch problems and alert the user.'''
        self.assertEqual(self.frontend._get_description(), description)

    def test_get_requirements(self):
        self.maxDiff = None
        expected_requirements = {
            'run': [
                upt.PackageRequirement('rlang', '>=0.3.0'),
                upt.PackageRequirement('covr'),
                upt.PackageRequirement('testthat'),
            ],
        }
        self.assertEqual(self.frontend._get_requirements(),
                         expected_requirements)

    def test_get_archives(self):
        url = 'https://cran.r-project.org/src/contrib/ellipsis_0.3.0.tar.gz'
        expected_archives = [
            upt.Archive(url),
        ]
        archives = self.frontend._get_archives()
        self.assertEqual(len(archives), len(expected_archives))
        self.assertEqual(archives[0].url, expected_archives[0].url)

    def test_get_licenses(self):
        self.assertEqual(self.frontend._get_licenses(),
                         [upt.licenses.GNUGeneralPublicLicenseThree()])
