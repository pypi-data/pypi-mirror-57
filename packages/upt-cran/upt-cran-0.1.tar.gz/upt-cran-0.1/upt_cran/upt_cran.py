from lxml import etree

import requests
import upt


class CranPackage(upt.Package):
    pass


class CranFrontend(upt.Frontend):
    name = 'cran'

    def _get_version(self):
        xpath = '//td[text()="Version:"]/following-sibling::td/text()'
        return self.tree.xpath(xpath)[0]

    def _get_summary(self):
        # The title of the web page is "{pkgname}: {summary}".
        title = self.tree.xpath('//h2/text()')[0]
        return title[title.index(' ') + 1:]

    def _get_description(self):
        desc = self.tree.xpath('//p[1]/text()')[0]
        desc = desc.replace(' \n', '\n').replace('\n', ' ')
        desc = desc.replace(' ' * 4, '')
        return desc

    def _get_requirements(self):
        # CRAN has 2 kinds of dependencies: "Imports" and "Suggests".
        # There are no build/runtime/test dependencies. Some packages list test
        # dependencies in the "Suggested" dependencies, so we just bundle
        # everything into "runtime" dependencies and hope for the best.
        requirements = []
        for kind in ['Imports:', 'Suggests:']:
            xpath = f'//td[text()="{kind}"]/following-sibling::td'
            xpath += '/descendant-or-self::text()'
            text_requirements = ''.join(self.tree.xpath(xpath))
            for text_req in text_requirements.split(', '):
                try:
                    pkg, specifier = text_req.split(' ', 1)
                    specifier = specifier.replace('≥', '>=')
                    specifier = specifier.replace('≤', '<=')
                    specifier = specifier[1:-1]  # Remove '(' and ')'
                    specifier = specifier.replace(' ', '')
                except ValueError:
                    pkg, specifier = text_req, None
                requirements.append(upt.PackageRequirement(pkg, specifier))
        return {'run': requirements}

    def _get_archives(self):
        xpath = '//td[starts-with(text()," Package")]/following-sibling::td/a/'
        xpath += '@href'
        pkgsrc = self.tree.xpath(xpath)
        pkgsrc = pkgsrc[0].replace('../../../', 'https://cran.r-project.org/')
        return [upt.Archive(pkgsrc)]

    def _get_licenses(self):
        # See this link for more info about licensing in R:
        # https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing  # noqa
        # Instead of implementing the rules described in the above link, we
        # list all license strings found in packages hosted on CRAN.
        r_to_upt = {
            # 'ACM':
            # 'ACM | file LICENSE':
            # 'AGPL':
            'AGPL (>= 3)': upt.licenses.GNUAfferoGeneralPublicLicenseThreeDotZeroPlus, # noqa
            'AGPL-3': upt.licenses.GNUAfferoGeneralPublicLicenseThreeDotZero,
            'AGPL-3 | file LICENSE': upt.licenses.GNUAfferoGeneralPublicLicenseThreeDotZero, # noqa
            # 'AGPL + file LICENSE':
            # 'AGPL | file LICENSE':
            # 'Apache License':
            'Apache License (== 2)': upt.licenses.ApacheLicenseTwoDotZero,
            'Apache License (== 2.0)': upt.licenses.ApacheLicenseTwoDotZero,
            'Apache License (>= 2.0)': upt.licenses.ApacheLicenseTwoDotZero,
            'Apache License 2.0': upt.licenses.ApacheLicenseTwoDotZero,
            'Apache License (== 2.0) | file LICENSE': upt.licenses.ApacheLicenseTwoDotZero, # noqa
            'Apache License (>= 2.0) | file LICENSE': upt.licenses.ApacheLicenseTwoDotZero, # noqa
            'Apache License 2.0 | file LICENSE': upt.licenses.ApacheLicenseTwoDotZero, # noqa
            # 'Apache License | file LICENSE':
            'Apache License Version 2.0': upt.licenses.ApacheLicenseTwoDotZero,
            'Artistic-2.0': upt.licenses.ArtisticLicenseTwoDotZero,
            'Artistic License 2.0': upt.licenses.ArtisticLicenseTwoDotZero,
            # 'BSD':
            'BSD_2_clause + file LICENCE': upt.licenses.BSDTwoClauseLicense,
            'BSD_2_clause + file LICENSE': upt.licenses.BSDTwoClauseLicense,
            'BSD 2-clause License + file LICENSE': upt.licenses.BSDTwoClauseLicense, # noqa
            'BSD_3_clause + file LICENCE': upt.licenses.BSDThreeClauseLicense,
            'BSD_3_clause + file LICENSE': upt.licenses.BSDThreeClauseLicense,
            'BSD_3_clause + file LICENSE | GPL (>= 2)': upt.licenses.BSDThreeClauseLicense, # noqa
            'BSD_3_clause + file LICENSE | GPL-2': upt.licenses.BSDThreeClauseLicense, # noqa
            'BSD 3-clause License': upt.licenses.BSDThreeClauseLicense,
            'BSD 3-clause License + file LICENSE': upt.licenses.BSDThreeClauseLicense, # noqa
            'BSL': upt.licenses.BoostSoftwareLicense,
            'BSL-1.0': upt.licenses.BoostSoftwareLicense,
            # 'CC0':
            # 'CC BY 4.0':
            # 'CC BY-NC 4.0':
            # 'CC BY-NC-ND 3.0 US':
            # 'CC BY-NC-SA 3.0':
            # 'CC BY-NC-SA 4.0':
            # 'CC BY-SA 2.0 + file LICENSE':
            'CC BY-SA 4.0': upt.licenses.CCBYSAFourDotZero,
            'CC BY-SA 4.0 + file LICENSE': upt.licenses.CCBYSAFourDotZero,
            # 'CeCILL':
            'CeCILL-2': upt.licenses.CeCILLTwoDotZero,
            'CeCILL-2 | file LICENSE': upt.licenses.CeCILLTwoDotZero,
            'CeCILL-2 | GPL-2': upt.licenses.CeCILLTwoDotZero,
            'Common Public License Version 1.0': upt.licenses.CommonDevelopmentAndDistributionLicenseOneDotZero, # noqa
            'CPL-1.0': upt.licenses.CommonDevelopmentAndDistributionLicenseOneDotZero, # noqa
            # 'CPL (>= 2)':
            # 'EPL':
            # 'EPL (>= 1.0)':
            # 'EUPL':
            'EUPL (== 1.1)': upt.licenses.EuropeanUnionPublicLicenseOneDotOne,
            'EUPL-1.1': upt.licenses.EuropeanUnionPublicLicenseOneDotOne,
            'EUPL (>= 1.2)': upt.licenses.EuropeanUnionPublicLicenseOneDotTwo,
            # 'file LICENCE':
            # 'file LICENSE':
            # 'FreeBSD':
            # 'FreeBSD | file LICENSE':
            'FreeBSD | GPL-2 | file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            # 'GNU Affero General Public License':
            # 'GNU General Public License':
            'GNU General Public License (>= 2)': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GNU General Public License (>= 3)': upt.licenses.GNUGeneralPublicLicenseThreePlus, # noqa
            'GNU General Public License version 2': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GNU General Public License version 3': upt.licenses.GNUGeneralPublicLicenseThree, # noqa
            # 'GNU Lesser General Public License':
            # 'GPL':
            # 'GPL (>= 1.0)':
            'GPL (<= 2)': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (== 2)': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (> 2)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 2)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL-2': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (<= 2.0)': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (>= 2.0)': upt.licenses.GNUGeneralPublicLicenseTwoPlus,
            'GPL (>= 2.0.0)': upt.licenses.GNUGeneralPublicLicenseTwoPlus,
            'GPL (>= 2.0) | file LICENCE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL (>= 2.0) | file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            # 'GPL (>= 2.1)':
            # 'GPL (>= 2.10)':
            # 'GPL (>= 2.15)':
            # 'GPL (>= 2.15.1)':
            # 'GPL (>= 2.2)':
            'GPL-2 | Artistic-2.0': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (>= 2) | BSD_2_clause + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL (>= 2) | BSD_3_clause + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL (>= 2) | file LICENCE':  upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | file LICENCE': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL (>= 2) | file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL (>= 2) | FreeBSD': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | GPL (>= 2) | GPL-3': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | GPL-3': upt.licenses.GNUGeneralPublicLicenseTwo,
            'GPL-2 | GPL-3 | BSD_3_clause + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL-2 | GPL-3 | file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL-2 | GPL-3 | MIT + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL (>= 2) | LGPL (>= 2)': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | LGPL-2.1 | MPL-1.1': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL-2 | MIT + file LICENCE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL (>= 2) | MIT + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwoPlus, # noqa
            'GPL-2 | MIT + file LICENSE': upt.licenses.GNUGeneralPublicLicenseTwo, # noqa
            'GPL (> 3)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 3)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL-3': upt.licenses.GNUGeneralPublicLicenseThree,
            'GPL (>= 3.0)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 3.0.0)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 3.2)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 3.3.2)': upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'GPL (>= 3) | CC BY 4.0': upt.licenses.GNUGeneralPublicLicenseThreePlus, # noqa
            'GPL (>= 3) | file LICENCE': upt.licenses.GNUGeneralPublicLicenseThreePlus, # noqa
            'GPL-3 | file LICENCE': upt.licenses.GNUGeneralPublicLicenseThree,
            'GPL (>= 3) | file LICENSE': upt.licenses.GNUGeneralPublicLicenseThreePlus, # noqa
            'GPL-3 + file LICENSE': upt.licenses.GNUGeneralPublicLicenseThree,
            'GPL-3 | file LICENSE': upt.licenses.GNUGeneralPublicLicenseThree,
            'GPL-3 | GPL-2': upt.licenses.GNUGeneralPublicLicenseThree,
            'GPL-3 | LGPL-2.1': upt.licenses.GNUGeneralPublicLicenseThree,
            # 'GPL | file LICENSE':
            # 'LGPL':
            'LGPL (>= 2)': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL-2': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZero,
            'LGPL (> 2.0)': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL (>= 2.0)': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL (>= 2.0, < 3)': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL (>= 2.0, < 3) | file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL (>= 2.0, < 3) | Mozilla Public License': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL (>= 2.1)': upt.licenses.GNULesserGeneralPublicLicenseTwoDotOnePlus, # noqa
            'LGPL-2.1': upt.licenses.GNULesserGeneralPublicLicenseTwoDotOne,
            'LGPL-2.1 | file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseTwoDotOne, # noqa
            'LGPL-2 | Apache License 2.0': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZero, # noqa
            'LGPL-2 | BSD_3_clause + file LICENSE': upt.licenses.BSDThreeClauseLicense, # noqa
            'LGPL (>= 2) | file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZeroPlus, # noqa
            'LGPL-2 | LGPL-3 | GPL-2 | GPL-3': upt.licenses.GNULesserGeneralPublicLicenseTwoDotZero, # noqa
            'LGPL (>= 3)': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZeroPlus, # noqa
            'LGPL-3': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZero, # noqa
            'LGPL (>= 3.0)': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZeroPlus, # noqa
            'LGPL-3 | Apache License 2.0': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZero, # noqa
            'LGPL (>= 3) | file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZeroPlus, # noqa
            'LGPL-3 + file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZero, # noqa
            'LGPL-3 | file LICENSE': upt.licenses.GNULesserGeneralPublicLicenseThreeDotZero, # noqa
            'Lucent Public License': upt.licenses.LucentPublicLicenseOneDotZeroTwo, # noqa
            'MIT': upt.licenses.MITLicense,
            'MIT + file LICENCE': upt.licenses.MITLicense,
            'MIT + file LICENSE': upt.licenses.MITLicense,
            'MIT | file LICENSE': upt.licenses.MITLicense,
            'MIT+file LICENSE': upt.licenses.MITLicense,
            'MIT + file LICENSE | Apache License 2.0': upt.licenses.MITLicense,
            'MIT + file LICENSE | Unlimited': upt.licenses.MITLicense,
            'MIT License': upt.licenses.MITLicense,
            'MIT License + file LICENSE': upt.licenses.MITLicense,
            'Mozilla Public License 1.1': upt.licenses.MozillaPublicLicenseOneDotOne, # noqa
            'Mozilla Public License 2.0': upt.licenses.MozillaPublicLicenseTwoDotZero, # noqa
            # 'MPL':
            'MPL-1.1': upt.licenses.MozillaPublicLicenseOneDotOne,
            'MPL (>= 2)': upt.licenses.MozillaPublicLicenseTwoDotZero,
            'MPL (== 2.0)': upt.licenses.MozillaPublicLicenseTwoDotZero,
            'MPL (>= 2.0)': upt.licenses.MozillaPublicLicenseTwoDotZero,
            'MPL-2.0': upt.licenses.MozillaPublicLicenseTwoDotZero,
            'MPL-2.0 | file LICENSE': upt.licenses.MozillaPublicLicenseTwoDotZero, # noqa
            'MPL (>= 2) | file LICENSE': upt.licenses.MozillaPublicLicenseTwoDotZero, # noqa
            'MPL (>= 2) | GPL (>= 2) | file LICENSE': upt.licenses.MozillaPublicLicenseTwoDotZero, # noqa
            # 'Unlimited':
            # 'Unlimited | file LICENSE':
        }
        xpath = '//td[text()="License:"]/following-sibling::td/a/text()'
        r_license = self.tree.xpath(xpath)[0]
        return [r_to_upt.get(r_license, upt.licenses.UnknownLicense)()]

    def parse(self, pkg_name, version=None):
        # TODO: We should download the DESCRIPTION file at
        # https://cran.r-project.org/web/packages/{pkg_name}/DESCRIPTION and
        # parse it using a third-party library that can read files written in
        # the Debian Control Format (DCF). Writing parsers is tricky,
        # time-consuming and error-prone, so we download a web page and parse
        # it using XPath instead.
        url = f'https://cran.r-project.org/web/packages/{pkg_name}/index.html'
        r = requests.get(url)
        if not r.ok:
            raise upt.InvalidPackageNameError(self.name, pkg_name)

        self.tree = etree.HTML(r.text)

        d = {
            'homepage': f'https://cran.r-project.org/package={pkg_name}',
            'summary': self._get_summary(),
            'description': self._get_description(),
            'requirements': self._get_requirements(),
            'archives': self._get_archives(),
            'licenses': self._get_licenses(),
        }
        return CranPackage(pkg_name, self._get_version(), **d)
