# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import unittest

import requests_mock

import upt
from upt_rubygems.upt_rubygems import RubyGemsFrontend


class TestRubyGemsFrontend(unittest.TestCase):
    def setUp(self):
        self.frontend = RubyGemsFrontend()

    @requests_mock.mock()
    def test_get_latest_version(self, fake_requests):
        url = 'https://rubygems.org/api/v1/gems/rails.json'
        fake_requests.get(url, json={'name': 'rails', 'version': '1.2'})
        self.assertEqual(self.frontend._get_latest_version('rails'), '1.2')

    @requests_mock.mock()
    def test_get_latest_version_invalid_name(self, fake_requests):
        url = 'https://rubygems.org/api/v1/gems/fake-package.json'
        fake_requests.get(url, status_code=404)
        with self.assertRaises(upt.InvalidPackageNameError):
            self.frontend._get_latest_version('fake-package')

    @requests_mock.mock()
    def test_get_metadata(self, fake_requests):
        url = f'https://rubygems.org/api/v2/rubygems/rails/'
        url += f'/versions/6.0.1.json'
        fake_json = {'name': 'rails', 'version': '6.0.1'}
        fake_requests.get(url, json=fake_json)
        self.assertEqual(self.frontend._get_metadata('rails', '6.0.1'),
                         fake_json)

    @requests_mock.mock()
    def test_get_metadata_invalid_version(self, fake_requests):
        url = f'https://rubygems.org/api/v2/rubygems/rails/'
        url += f'/versions/12.12.12.json'
        fake_requests.get(url, status_code=404)
        with self.assertRaises(upt.InvalidPackageVersionError):
            self.frontend._get_metadata('rails', '12.12.12')


class TestLicenses(unittest.TestCase):
    def setUp(self):
        self.frontend = RubyGemsFrontend()

    def test_no_license(self):
        out = self.frontend._guess_licenses([])
        expected = []
        self.assertListEqual(out, expected)

    def test_one_license(self):
        out = self.frontend._guess_licenses(['Ruby'])
        expected = [upt.licenses.RubyLicense()]
        self.assertListEqual(out, expected)

        out = self.frontend._guess_licenses(['same as Ruby'])
        expected = [upt.licenses.UnknownLicense()]
        self.assertListEqual(out, expected)

    def test_multiple_licenses(self):
        out = self.frontend._guess_licenses(['Ruby', 'same as Ruby'])
        expected = [upt.licenses.RubyLicense(), upt.licenses.UnknownLicense()]
        self.assertListEqual(out, expected)


class TestRequirements(unittest.TestCase):
    def setUp(self):
        self.frontend = RubyGemsFrontend()

    def test_empty_requirements(self):
        expected = {}
        out = self.frontend._get_requirements({})
        self.assertEqual(out, expected)

    def test_runtime_requirements(self):
        json_reqs = {
            'runtime': [{
                'name': 'foo',
                'requirements': '> 0.12',
            }, {
                'name': 'bar',
                'requirements': '>= 13.37',
            }]
        }
        expected = {
            'run': [upt.PackageRequirement('foo', '> 0.12'),
                    upt.PackageRequirement('bar', '>= 13.37')]
        }
        out = self.frontend._get_requirements(json_reqs)
        self.assertDictEqual(out, expected)

    def test_development_requirements(self):
        json_reqs = {
            'development': [{
                'name': 'baz',
                'requirements': '> 42',
            }]
        }
        expected = {
            'test': [upt.PackageRequirement('baz', '> 42')]
        }
        out = self.frontend._get_requirements(json_reqs)
        self.assertDictEqual(out, expected)

    def test_runtime_development_requirements(self):
        json_reqs = {
            'runtime': [{
                'name': 'foo',
                'requirements': '> 0.12',
            }, {
                'name': 'bar',
                'requirements': '>= 13.37',
            }],
            'development': [{
                'name': 'baz',
                'requirements': '> 42',
            }]
        }
        expected = {
            'run': [upt.PackageRequirement('foo', '> 0.12'),
                    upt.PackageRequirement('bar', '>= 13.37')],
            'test': [upt.PackageRequirement('baz', '> 42')],
        }
        out = self.frontend._get_requirements(json_reqs)
        self.assertDictEqual(out, expected)

    def test_requirements_with_twiddle_wakka(self):
        json_reqs = {
            'runtime': [{
                'name': 'foo',
                'requirements': '~> 0.12',
            }, {
                'name': 'bar',
                'requirements': '>= 1.0.1, ~> 1.0'
            }]
        }
        expected = {
            'run': [upt.PackageRequirement('foo', '>=0.12,<1.0'),
                    upt.PackageRequirement('bar', '>= 1.0.1,>=1.0,<2.0')]
        }
        out = self.frontend._get_requirements(json_reqs)
        self.assertDictEqual(out, expected)

    def test_requirements_with_bugged_twiddle_wakka(self):
        json_reqs = {
            'runtime': [{
                'name': 'foo',
                'requirements': '~> 0.12.1.a',
            }]
        }
        expected = {}
        out = self.frontend._get_requirements(json_reqs)
        self.assertDictEqual(out, expected)

    def test_fix_twiddle_wakka_expr(self):
        results = [
            ('>= 1.2', '>= 1.2'),
            ('~> 0', '>=0,<1'),
            ('~> 2.2', '>=2.2,<3.0'),
            ('~> 2.2.0', '>=2.2.0,<2.3.0'),
        ]
        for specifier, expected in results:
            self.assertEqual(self.frontend._fix_twiddle_wakka_expr(specifier),
                             expected)

    def test_convert_specifier(self):
        results = [
            ('> 1.2', '> 1.2'),
            ('>= 1.2', '>= 1.2'),
            ('< 1.2', '< 1.2'),
            ('<= 1.2', '<= 1.2'),
            ('= 1.2', '== 1.2'),
            ('~> 2.2', '>=2.2,<3.0'),
        ]
        for ruby_specifier, python_specifier in results:
            self.assertEqual(self.frontend._convert_specifier(ruby_specifier),
                             python_specifier)

    def test_fix_twiddle_wakka_bugged_expr(self):
        # Pre-releases are not allowed when using the twiddle-wakka operator.
        with self.assertRaises(ValueError):
            self.frontend._fix_twiddle_wakka_expr('~> 2.0.0.a')


class TestArchives(unittest.TestCase):
    def setUp(self):
        self.frontend = RubyGemsFrontend()

    def test_no_archive(self):
        self.assertEqual(self.frontend._get_archives({}), [])

    def test_no_sha(self):
        json = {
            'gem_uri': 'some_uri',
        }
        archives = self.frontend._get_archives(json)
        self.assertEqual(len(archives), 1)
        self.assertEqual(archives[0].url, 'some_uri')


if __name__ == '__main__':
    unittest.main()
