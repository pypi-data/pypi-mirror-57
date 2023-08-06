import six

from ...cereal import serializable
from ..core import typecheck_promote
from .primitive import Primitive
from .bool_ import Bool
from .number import Int
from .none import NoneType


def ListType(param):
    # necessary to delay circular imports for typechecks
    from ..containers import List

    return List[param]


@serializable()
class Str(Primitive):
    "Proxy str"
    _pytype = six.string_types

    @typecheck_promote(lambda: Str)
    def __lt__(self, other):
        return Bool._from_apply("lt", self, other)

    @typecheck_promote(lambda: Str)
    def __le__(self, other):
        return Bool._from_apply("le", self, other)

    @typecheck_promote(lambda: Str)
    def __eq__(self, other):
        return Bool._from_apply("eq", self, other)

    @typecheck_promote(lambda: Str)
    def __ne__(self, other):
        return Bool._from_apply("ne", self, other)

    @typecheck_promote(lambda: Str)
    def __gt__(self, other):
        return Bool._from_apply("gt", self, other)

    @typecheck_promote(lambda: Str)
    def __ge__(self, other):
        return Bool._from_apply("ge", self, other)

    @typecheck_promote(lambda: Str)
    def __add__(self, other):
        return self._from_apply("add", self, other)

    @typecheck_promote(Int)
    def __mul__(self, other):
        return self._from_apply("mul", self, other)

    def __reversed__(self):
        return self._from_apply("reversed", self)

    def length(self):
        "The length of the string (returns `Int`)"
        return Int._from_apply("length", self)

    @typecheck_promote(lambda: Str)
    def contains(self, other):
        "Whether this string contains the given substring (returns `Bool`)"
        return Bool._from_apply("contains", self, other)

    def capitalize(self):
        """
        Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.
        """
        return self._from_apply("Str.capitalize", self)

    @typecheck_promote(Int, fillchar=lambda: Str)
    def center(self, width, fillchar=" "):
        """
        Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self._from_apply("Str.center", self, width, fillchar=fillchar)

    @typecheck_promote(lambda: Str)
    def count(self, sub):
        """
        Return an `Int` of the number of non-overlapping occurrences of the substring sub in this string.
        """
        return Int._from_apply("Str.count", self, sub)

    @typecheck_promote(lambda: Str)
    def endswith(self, suffix):
        """
        Return True if S ends with the specified suffix, False otherwise.
        """
        return Bool._from_apply("Str.endswith", self, suffix)

    @typecheck_promote(tabsize=Int)
    def expandtabs(self, tabsize=8):
        """
        Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return self._from_apply("Str.expandtabs", self, tabsize=tabsize)

    @typecheck_promote(lambda: Str)
    def find(self, sub):
        """
        Return the lowest index in S where substring sub is found in this string.

        Return -1 on failure.
        """
        return Int._from_apply("Str.find", self, sub)

    def format(self, *args, **kwargs):
        """
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return self._from_apply("Str.format", self, *args, **kwargs)

    def isalnum(self):
        """
        Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        return Bool._from_apply("Str.isalnum", self)

    def isalpha(self):
        """
        Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        return Bool._from_apply("Str.isalpha", self)

    def isdigit(self):
        """
        Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        return Bool._from_apply("Str.isdigit", self)

    def islower(self):
        """
        Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        return Bool._from_apply("Str.islower", self)

    def isspace(self):
        """
        Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        return Bool._from_apply("Str.isspace", self)

    def istitle(self):
        """
        Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        return Bool._from_apply("Str.istitle", self)

    def isupper(self):
        """
        Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        return Bool._from_apply("Str.isupper", self)

    @typecheck_promote(lambda: ListType(Str))
    def join(self, strings):
        """
        Concatenate a ``List[Str]``.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: ``wf.Str('.').join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'``
        """
        return self._from_apply("Str.join", self, strings)

    @typecheck_promote(Int, fillchar=lambda: Str)
    def ljust(self, width, fillchar=" "):
        """
        Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self._from_apply("Str.ljust", self, width, fillchar=fillchar)

    def lower(self):
        """
        Return a copy of the string converted to lowercase.
        """
        return self._from_apply("Str.lower", self)

    @typecheck_promote(chars=lambda: (Str, NoneType))
    def lstrip(self, chars=None):
        """
        Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self._from_apply("Str.lstrip", self, chars)

    @typecheck_promote(lambda: Str)
    def partition(self, sep):
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string.  If the separator is found,
        returns a ``Tuple[Str, Str, Str]`` containing the part before the separator,
        the separator itself, and the part after it.

        If the separator is not found, returns a ``Tuple[Str, Str, Str]``
        containing the original string and two empty strings.
        """
        from ..containers import Tuple

        return Tuple[Str, Str, Str]._from_apply("Str.partition", self, sep)

    @typecheck_promote(lambda: Str, lambda: Str, count=Int)
    def replace(self, old, new, count=-1):
        """
        Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        return self._from_apply("Str.replace", self, old, new, count=count)

    @typecheck_promote(lambda: Str)
    def rfind(self, sub):
        """
        Return the highest index in S where substring sub is found.

        Return -1 on failure.
        """
        return Int._from_apply("Str.rfind", self, sub)

    @typecheck_promote(Int, fillchar=lambda: Str)
    def rjust(self, width, fillchar=" "):
        """
        Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self._from_apply("Str.rjust", self, width, fillchar=fillchar)

    @typecheck_promote(lambda: Str)
    def rpartition(self, sep):
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        from ..containers import Tuple

        return Tuple[Str, Str, Str]._from_apply("Str.rpartition", self, sep)

    @typecheck_promote(sep=lambda: (Str, NoneType), maxsplit=Int)
    def rsplit(self, sep=None, maxsplit=-1):
        """
        Return a list of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.

        Splits are done starting at the end of the string and working to the front.
        """
        from ..containers import List

        return List[Str]._from_apply("Str.rsplit", self, sep=sep, maxsplit=maxsplit)

    @typecheck_promote(chars=lambda: (Str, NoneType))
    def rstrip(self, chars=None):
        """
        Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self._from_apply("Str.rstrip", self, chars=chars)

    @typecheck_promote(sep=lambda: (Str, NoneType), maxsplit=Int)
    def split(self, sep=None, maxsplit=-1):
        """
        Return a ``List[Str]`` of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        from ..containers import List

        return List[Str]._from_apply("Str.split", self, sep=sep, maxsplit=maxsplit)

    def splitlines(self):
        """
        Return a ``List[Str]`` of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting strings.
        """
        from ..containers import List

        return List[Str]._from_apply("Str.splitlines", self)

    @typecheck_promote(lambda: Str)
    def startswith(self, prefix):
        """
        Return True if S starts with the specified prefix, False otherwise.
        """
        return Bool._from_apply("Str.startswith", self, prefix)

    @typecheck_promote(chars=lambda: (Str, NoneType))
    def strip(self, chars=None):
        """
        Return a copy of the string with leading and trailing whitespace remove.

        If chars is given and not None, remove characters in chars instead.
        """
        return self._from_apply("Str.strip", self, chars=chars)

    def swapcase(self):
        """
        Convert uppercase characters to lowercase and lowercase characters to uppercase.
        """
        return self._from_apply("Str.swapcase", self)

    def title(self):
        """
        Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        return self._from_apply("Str.title", self)

    def upper(self):
        """
        Return a copy of the string converted to uppercase.
        """
        return self._from_apply("Str.upper", self)

    @typecheck_promote(Int)
    def zfill(self, width):
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """
        return self._from_apply("Str.zfill", self, width)
