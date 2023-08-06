"""
 pyfuzzylite (TM), a fuzzy logic control library in Python.
 Copyright (C) 2010-2017 FuzzyLite Limited. All rights reserved.
 Author: Juan Rada-Vilela, Ph.D. <jcrada@fuzzylite.com>

 This file is part of pyfuzzylite.

 pyfuzzylite is free software: you can redistribute it and/or modify it under
 the terms of the FuzzyLite License included with the software.

 You should have received a copy of the FuzzyLite License along with
 pyfuzzylite. If not, see <http://www.fuzzylite.com/license/>.

 pyfuzzylite is a trademark of FuzzyLite Limited
 fuzzylite is a registered trademark of FuzzyLite Limited.
"""

import unittest
from typing import Optional, Type, TypeVar


class A:

    def __init__(self) -> None:
        pass


class B:

    def __init__(self) -> None:
        pass

    def do_something(self) -> None:
        print("B: Doing something")


class Experimental:
    T = TypeVar('T', 'A', 'B')

    def create_component_a(self) -> Optional['A']:
        return self.create_component(A)
        # error: Value of type variable "T" of "create_component" of
        # "Experimental" cannot be "Optional[A]

    def create_component(self, cls: Type['T']) -> Optional['T']:
        result = cls()
        if hasattr(result, "do_something"):
            getattr(result, "do_something")()
        return result


class TestFllImporter(unittest.TestCase):

    def test_experimental(self) -> None:
        # optional_a: Optional[A] = None
        # reveal_type(optional_a)
        # error: Revealed type is 'Union[tests.test_experimental.A, None]'

        # a = A()
        # reveal_type(a)
        # error: Revealed type is 'tests.test_experimental.A'

        # constructed_a = Experimental().create_component_a()
        # reveal_type(constructed_a)
        # error: Revealed type is 'Union[tests.test_experimental.A, None]'

        # component_a = Experimental().create_component(A)
        # reveal_type(component_a)
        # error: Revealed type is 'Union[tests.test_experimental.A*, None]'
        pass


if __name__ == '__main__':
    unittest.main()
