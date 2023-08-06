# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import logging
import re

import requests
import semver
import upt


class RubyGemsPackage(upt.Package):
    pass


class RubyGemsFrontend(upt.Frontend):
    name = 'rubygems'

    def __init__(self):
        self.logger = logging.getLogger('upt')

    @staticmethod
    def _guess_licenses(json_licenses):
        # There is no 'official' list of 'valid' strings in RubyGems. Package
        # authors are free to write whatever they want in the 'licenses' field.
        # Let's take care of the most common license strings.
        ruby_to_upt = {
            'Apache-2.0': upt.licenses.ApacheLicenseTwoDotZero,
            'Artistic-2.0': upt.licenses.ArtisticLicenseTwoDotZero,
            '2-clause BSDL': upt.licenses.BSDTwoClauseLicense,
            'BSD 2-Clause': upt.licenses.BSDTwoClauseLicense,
            'BSD-2-Clause': upt.licenses.BSDTwoClauseLicense,
            'BSD-2': upt.licenses.BSDTwoClauseLicense,
            'BSD 3-Clause': upt.licenses.BSDThreeClauseLicense,
            'BSD-3-Clause': upt.licenses.BSDThreeClauseLicense,
            'BSD-3': upt.licenses.BSDThreeClauseLicense,
            'GPL-2': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL-2.0': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL-2.0+': upt.licenses.GNUGeneralPublicLicenseTwoPlus,
            'LGPLv2': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZero,
            'LGPLv2+':
                upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus,
            'LGPL-2.1':
                upt.licenses.GNULesserGeneralPublicLicenseTwoDotOne,
            'LGPLv3+': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'MIT': upt.licenses.MITLicense,
            'MPL-2.0': upt.licenses.MozillaPublicLicenseTwoDotZero,
            'Ruby': upt.licenses.RubyLicense,
        }

        return [ruby_to_upt.get(l, upt.licenses.UnknownLicense)()
                for l in json_licenses]

    @staticmethod
    def _fix_twiddle_wakka_expr(expr):
        """Replaces '~> <version>' with a more usual expression.

        Ruby uses the twiddle-wakka operator to handle 'pessimistic
        version constraints'. Basically:

        '~> 1'      => '>=1,<2'
        '~> 2.2'    => '>=2.2,<3.0'
        '~> 2.2.0'  => '>=2.2.0<2.3.0'

        This method converts a specifier that uses the twiddle-wakka and turns
        it into an expression using only '>=' and '<'. If the given version
        specifier does not use the twiddle-wakka operator, it is returned
        as-is.

        Should this method not manage to parse the given expression, it will
        raise a ValueError.

        See:
        http://guides.rubygems.org/patterns/#pessimistic-version-constraint
        """
        m = re.match(r'~>\s*(.*)', expr)
        if m is None:
            return expr

        # The semver library cannot handle versions such as 'X' or 'X.Y': it
        # needs versions to be valid SemVer versions. To work around this, we
        # add '.0' or '.0.0' to the version we matched earlier. The returned
        # result does not contain extra digits, though.
        version = m.group(1)
        if re.match(r'^\d+$', version):
            version += '.0.0'
            return f'>={version[:-4]},<{semver.bump_major(version)[:-4]}'
        elif re.match(r'^\d+\.\d+$', version):
            version += '.0'
            return f'>={version[:-2]},<{semver.bump_major(version)[:-2]}'
        elif re.match(r'^\d+\.\d+\.\d+$', version):
            return f'>={version},<{semver.bump_minor(version)}'
        else:
            raise ValueError(f'Cannot handle version "{version}".')

    def _convert_specifier(self, specifier):
        # Turn '=' into '=='
        if specifier.startswith('='):
            specifier = f'={specifier}'

        # There is no twiddle-wakka in Python, so we have to replace it with a
        # combination of specifiers.
        specifier = self._fix_twiddle_wakka_expr(specifier)
        return specifier

    def _get_requirements(self, json_dependencies):
        """Return a list of upt.PackageRequirement instances.

        json_dependencies: the dependencies as specified in the JSON returned
                           by RubyGems
        """
        reqs = {}
        kinds = {
            'runtime': 'run',
            'development': 'test'
        }
        for ruby_kind, upt_kind in kinds.items():
            kind_reqs = []
            for requirement in json_dependencies.get(ruby_kind, []):
                name = requirement['name']
                specifiers = requirement['requirements'].split(',')
                try:
                    specifiers = [self._convert_specifier(specifier.strip())
                                  for specifier in specifiers]
                except ValueError:
                    # Yeah, for some reason, we failed to handle the
                    # twiddle-wakka. Let's just skip this dependency.
                    self.logger.warning('Could not parse requirement '
                                        f'{name} ({specifiers}), skipping it.')
                    continue
                pkg_req = upt.PackageRequirement(name, ','.join(specifiers))
                kind_reqs.append(pkg_req)
            if kind_reqs:
                reqs[upt_kind] = kind_reqs

        return reqs

    def _get_archives(self, json):
        try:
            return [
                upt.Archive(json['gem_uri'], sha256=json.get('sha'),
                            archive_type=upt.ArchiveType.RUBYGEM)
            ]
        except KeyError:
            return []

    def _get_latest_version(self, pkg_name):
        # There is no way to find the latest version of a given package using
        # v2, so we resort to using v1 here.
        url = f'https://rubygems.org/api/v1/gems/{pkg_name}.json'
        r = requests.get(url)
        if not r.ok:
            raise upt.InvalidPackageNameError(self.name, pkg_name)
        return r.json()['version']

    def _get_metadata(self, pkg_name, version):
        url = f'https://rubygems.org/api/v2/rubygems/{pkg_name}/'
        url += f'/versions/{version}.json'
        r = requests.get(url)
        if not r.ok:
            raise upt.InvalidPackageVersionError(self.name, pkg_name, version)
        return r.json()

    def parse(self, pkg_name, version=None):
        if version is None:
            version = self._get_latest_version(pkg_name)
        meta = self._get_metadata(pkg_name, version)

        d = {
            'homepage': meta.get('homepage_uri',
                                 f'https://rubygems.org/gems/{pkg_name}'),
            'summary': meta.get('summary', ''),
            'description': meta.get('description', ''),
            'requirements': self._get_requirements(meta.get('dependencies',
                                                            {})),
            'licenses': self._guess_licenses(meta.get('licenses', []) or []),
            'archives': self._get_archives(meta),
        }
        return RubyGemsPackage(pkg_name, version, **d)
