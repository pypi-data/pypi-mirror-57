#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x920c79cd

# Compiled with Coconut version 1.4.2 [Ernest Scribbler]

"""
A suite of collection classes that emulate a small subset of those in the
Scala standard library.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

#Copyright 2017 Eric T. Anderson
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the license.
#==============================

class Either(object):
    __slots__ = ['_content', '_is_left']
    try:
        from typing import Any
        from typing import Dict
        from typing import Callable
        from typing import Iterable
        from typing import Tuple
        import typing
    except ImportError:
        Any, Dict, Callable, Iterable, Tuple = ["Any", "Dict", "Callable", "Iterable", "Tuple"]

    def __init__(self, value, is_left):
# type: (...) -> None
        super(Either, self).__init__()
        self._content = value
        self._is_left = is_left

    def __eq__(self, other  # type: Any
    ):
# type: (...) -> bool
        return (self.__class__ == other.__class__) and self.get == other.get

    def __ne__(self, other  # type: Any
    ):
# type: (...) -> bool
        return not self.__eq__(other)

    def fold(self, do_left,  # type: Callable[[Any], Any]
     do_right  # type: Callable[[Any], Any]
    ):
# type: (...) -> Any
        return do_left(self._content) if self._is_left else do_right(self._content)

    @property
    def get(self):
# type: (...) -> Any
        return self._content

    @property
    def isLeft(self):
# type: (...) -> bool
        return self._is_left

    @property
    def isRight(self):
# type: (...) -> bool
        return not self._is_left

class Left(Either):

    def __init__(self, value=None):
# type: (...) -> None
        super(Left, self).__init__(value, True)

class Right(Either):

    def __init__(self, value=None):
# type: (...) -> None
        super(Right, self).__init__(value, False)
