# pylint:disable=line-too-long
"""
The tool to check the availability or syntax of domains, IPv4, IPv6 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

Tests of the PyFunceble.output.prints

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.github.io/special-thanks.html

Contributors:
    https://pyfunceble.github.io/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/dev/

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

from collections import OrderedDict
from datetime import datetime
from unittest import main as launch_tests
from unittest.mock import Mock, patch

from colorama import Back, Fore

import PyFunceble
from PyFunceble.output import Prints
from stdout_base import StdoutBase
from time_zone import TZ


class TestPrints(StdoutBase):
    """
    Tests of the PyFunceble.helpers.command.
    """

    def setUp(self):
        """
        Setups everything needed for the tests.
        """

        PyFunceble.load_config()

        StdoutBase.setUp(self)

        self.file = "the_file_is_a_ghost"
        self.to_print = {
            "basic": {"hello": 5, "world": 6, "here": 7, "is": 8, "PyFunceble": 10},
            "size_constructor": [5, 6, 7, 8, 9, 10],
            "basic_string": "Hello, World!",
            "hosts": {"0.0.0.0": 7, "hello.world": 11},
        }

        self.file_instance = PyFunceble.helpers.File(self.file)
        self.file_instance.delete()

    def tearDown(self):
        """
        Setups everything we need after the tests.
        """

        self.file_instance.delete()

        StdoutBase.tearDown(self)

    @patch("datetime.datetime")
    def test_before_header(self, datetime_patch):
        """
        Tests the method which prints some information before
        the generation of the content of a file.
        """

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        datetime_patch = Mock(wraps=datetime)
        datetime_patch.now = Mock(
            return_value=datetime(1970, 1, 1, 1, 0, 2, 0, tzinfo=TZ("+", hours=1).get())
        )
        patch("PyFunceble.output.prints.datetime", new=datetime_patch).start()

        # pylint: disable=line-too-long
        expected = f"""# File generated by {PyFunceble.NAME} (v{PyFunceble.VERSION.split()[0]}) / {PyFunceble.LINKS.repo}
# Date of generation: {datetime_patch.now().isoformat()}

"""

        Prints(
            None, None, output_file=self.file_instance.path, only_on_file=False
        ).before_header()

        self.assertEqual(expected, self.file_instance.read())

        self.file_instance.delete()

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        # pylint: disable=line-too-long
        expected = f"""# File generated by {PyFunceble.NAME} (v{PyFunceble.VERSION.split()[0]}) / {PyFunceble.LINKS.repo}
# Date of generation: {datetime_patch.now().isoformat()}

Hello World
"""

        printer = Prints(
            None,
            "Generic_File",
            output_file=self.file_instance.path,
            only_on_file=False,
        )

        printer.currently_used_header = OrderedDict(
            zip(
                [
                    "Hello",
                    "World",
                    "Expiration Date",
                    "Source",
                    "HTTP Code",
                    "Analyze Date",
                ],
                [5, 5],
            )
        )

        printer.before_header()

        self.assertEqual(expected, self.file_instance.read())

    def test_header_constructor_with_separator(self):
        """
        Tests the header constructor when a table separator is needed.
        """

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        expected = [
            "hello world  here    is       PyFunceble",
            "----- ------ ------- -------- ----------",
        ]

        actual = Prints(
            None, None, output_file=None, only_on_file=False
        ).header_constructor(self.to_print["basic"])

        self.assertEqual(expected, actual)

    def test_header_constructor_without_separator(self):
        """
        Tests the header constructor when a table separator is not needed.
        """

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        expected = ["hello world  here    is       PyFunceble"]
        actual = Prints(
            None, None, output_file=None, only_on_file=False
        ).header_constructor(self.to_print["basic"], None)

        self.assertEqual(expected, actual)

        # Test of the case that we want to print the hosts file format.
        expected = [" ".join(self.to_print["hosts"].keys())]

        actual = Prints(
            None, None, output_file=None, only_on_file=False
        ).header_constructor(self.to_print["hosts"], None)

        self.assertEqual(expected, actual)

    def test_data_constructor(self):
        """
        Tests the data constructor.
        """

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        expected = OrderedDict()
        to_print = []

        chars = ["H", "E", "L", "L", "O", "!"]

        for i, size in enumerate(self.to_print["size_constructor"]):
            index = chars[i] * size
            expected[index] = size
            to_print.append(index)

        actual = Prints(
            to_print, None, output_file=None, only_on_file=False
        ).data_constructor(self.to_print["size_constructor"])

        self.assertEqual(expected, actual)

        # Test the case that there is an issue.
        expected = OrderedDict()
        to_print = []

        chars = ["H", "E", "L", "L", "O", "!"]

        for i, size in enumerate(self.to_print["size_constructor"]):
            index = chars[i] * size
            expected[index] = size
            to_print.append(index)

        del to_print[-1]

        self.assertRaisesRegex(
            Exception,
            "Inputed: %d; Size: %d"
            % (
                len(self.to_print["size_constructor"]) - 1,
                len(self.to_print["size_constructor"]),
            ),
            lambda: Prints(
                to_print, None, output_file=None, only_on_file=False
            ).data_constructor(self.to_print["size_constructor"]),
        )

    def test_size_from_header(self):
        """
        Tests the method which extracts the sizes from the declared
        headers.
        """

        # pylint: disable=protected-access

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        expected = [element for _, element in self.to_print["basic"].items()]

        actual = Prints(
            None, None, output_file=None, only_on_file=False
        )._size_from_header(self.to_print["basic"])

        self.assertEqual(expected, actual)

    def test_colorify(self):
        """
        Tests the method which colors a line depending of the status.
        """

        # pylint: disable=protected-access

        expected = False
        actual = self.file_instance.exists()

        self.assertEqual(expected, actual)

        # Test with a template that is not designed for colorify
        expected = self.to_print["basic_string"]
        actual = Prints(None, "Hehehe", output_file=None, only_on_file=False)._colorify(
            self.to_print["basic_string"]
        )

        self.assertEqual(expected, actual)

        # Test with a template that is designed for colorify + Status is UP
        expected = Fore.BLACK + Back.GREEN + self.to_print["basic_string"]
        actual = Prints(
            ["This is a test", PyFunceble.STATUS.official.up],
            "Generic",
            output_file=None,
            only_on_file=False,
        )._colorify(self.to_print["basic_string"])

        self.assertEqual(expected, actual)

        # Test with a template that is designed for colorify + Status is DOWN
        expected = Fore.BLACK + Back.RED + self.to_print["basic_string"]
        actual = Prints(
            ["This is a test", PyFunceble.STATUS.official.down],
            "Generic",
            output_file=None,
            only_on_file=False,
        )._colorify(self.to_print["basic_string"])

        self.assertEqual(expected, actual)

        # Test with a template that is designed for colorify + Status is
        # UNKNOWN or INVALID
        expected = Fore.BLACK + Back.CYAN + self.to_print["basic_string"]
        actual = Prints(
            ["This is a test", PyFunceble.STATUS.official.invalid],
            "Generic",
            output_file=None,
            only_on_file=False,
        )._colorify(self.to_print["basic_string"])

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()