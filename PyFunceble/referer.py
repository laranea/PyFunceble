# pylint:disable=line-too-long
"""
The tool to check the availability or syntax of domains, IPv4 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This submodule will provide the referer extraction interface.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.github.io/special-thanks.html

Contributors:
    https://pyfunceble.github.io/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/master/

Project homepage:
    https://pyfunceble.github.io/

License:
::


    MIT License

    Copyright (c) 2017, 2018, 2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
# pylint: enable=line-too-long
import PyFunceble
from PyFunceble.logs import Logs


class Referer:  # pragma: no cover pylint: disable=too-few-public-methods
    """
    Get the WHOIS server (referer) of the current domain extension according to
    the IANA database.

    :param str subject: The subject we are working with.
    """

    # We create a list of ignored extension.
    # Note: We need the following because those extension does
    # not have a centralized whois server (yet).
    ignored_extension = [
        "ad",
        "al",
        "an",
        "ao",
        "aq",
        "arpa",
        "az",
        "ba",
        "bb",
        "bd",
        "bf",
        "bh",
        "bl",
        "boots",
        "bq",
        "bs",
        "bt",
        "bv",
        "cg",
        "chloe",
        "ck",
        "cu",
        "cv",
        "cw",
        "cy",
        "dj",
        "doosan",
        "eg",
        "eh",
        "er",
        "et",
        "fk",
        "flsmidth",
        "fm",
        "gb",
        "gm",
        "gn",
        "goodhands",
        "gp",
        "gr",
        "gt",
        "gu",
        "gw",
        "htc",
        "iinet",
        "jm",
        "jo",
        "kh",
        "km",
        "kp",
        "lb",
        "lr",
        "mc",
        "meo",
        "mf",
        "mh",
        "mil",
        "mm",
        "mt",
        "mv",
        "mw",
        "ne",
        "ni",
        "np",
        "nr",
        "pa",
        "pamperedchef",
        "panerai",
        "pg",
        "ph",
        "pk",
        "pn",
        "py",
        "sd",
        "sj",
        "spiegel",
        "sr",
        "ss",
        "sv",
        "sz",
        "telecity",
        "tj",
        "tp",
        "tt",
        "um",
        "va",
        "vi",
        "vista",
        "vn",
        "xn--0zwm56d",
        "xn--11b5bs3a9aj6g",
        "xn--54b7fta0cc",
        "xn--80akhbyknj4f",
        "xn--9t4b11yi5a",
        "xn--deba0ad",
        "xn--g6w251d",
        "xn--hgbk6aj7f53bba",
        "xn--hlcj6aya9esc7a",
        "xn--hlcj6aya9esc7a",
        "xn--jxalpdlp",
        "xn--kgbechtv",
        "xn--l1acc",
        "xn--mgbai9azgqp6j",
        "xn--mgbayh7gpa",
        "xn--mgbc0a9azcg",
        "xn--mgbpl2fh",
        "xn--pgbs0dh",
        "xn--qxam",
        "xn--zckzah",
        "xperia",
        "ye",
        "zw",
    ]

    def __init__(self, subject):
        # Note: A URL testing or an IP testing does not come around
        # here. So there is no need to be scared by the following.

        if subject:
            if not isinstance(subject, str):
                raise ValueError("`subject` must be a string.")

            self.subject = subject
        else:
            raise ValueError("`subject` must be given.")

        try:
            # We get the extension of the currently tested element.
            # We basically get everything after the last point.
            self.domain_extension = subject[subject.rindex(".") + 1 :]

            if not self.domain_extension and subject.endswith("."):
                self.domain_extension = [x for x in subject.split(".") if x][-1]
        except (ValueError, IndexError):
            # There was not point, so no extension to work with.
            self.domain_extension = None

    def get(self):
        """
        Return the referer aka the WHOIS server of the current domain extension.

        :return:

            - :code:`None` if there is no referer.

            - :code:`False` if the extension is unknown which implicitly means
               that the subject is :code:`INVALID`

        :rtype: None|False|str
        """

        if not PyFunceble.CONFIGURATION["local"]:
            # We are not running a test in a local network.

            if self.domain_extension not in self.ignored_extension:
                # The extension of the domain we are testing is not into
                # the list of ignored extensions.

                if self.domain_extension in PyFunceble.INTERN["iana_db"]:
                    # The domain extension is in the iana database.

                    if not PyFunceble.CONFIGURATION["no_whois"]:
                        # We are authorized to use WHOIS for the test result.

                        # We get the referer from the database.
                        referer = PyFunceble.INTERN["iana_db"][self.domain_extension]

                        if not referer:
                            # The referer is not filled.

                            # We log the case of the current extension.
                            Logs().referer_not_found(
                                self.subject, self.domain_extension
                            )

                            # And we handle and return None status.
                            return None

                        # The referer is into the database.

                        # We return the extracted referer.
                        return referer

                    # We are not authorized to use WHOIS for the test result.

                    # We return None.
                    return None

                # The domain extension is not in the iana database.

                # We return False, it is an invalid domain.
                return False

            # The extension of the domain we are testing is not into
            # the list of ignored extensions.

            # We return None, the domain does not have a whois server.
            return None

        # We are running a test in a local network.

        # We return None.
        return None
