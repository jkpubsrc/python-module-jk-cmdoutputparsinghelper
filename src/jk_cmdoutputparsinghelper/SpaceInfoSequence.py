

import typing

import jk_typing
import jk_prettyprintobj

from .TextSpanInfo import TextSpanInfo
from .TextSpanInfoSequence import TextSpanInfoSequence






#
# This class represents space/non-space information sequence.
# Each space is represented as value `True` while non-space characters are represented as `False`.
#
class SpaceInfoSequence(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self,
			values:typing.Iterable[bool],
		):

		if isinstance(values, list):
			self.values = values
		else:
			self.values = list(values)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dump(self, ctx:jk_prettyprintobj.DumpCtx):
		tf = [ "^" if x else "." for x in self.values ]
		# tf = [ "1" if x else "0" for x in self.values ]
		ctx.dumpVar("values", "".join(tf))
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __iter__(self):
		yield from self.values
	#

	def __len__(self):
		return len(self.values)
	#

	def __str__(self) -> str:
		return "SpaceInfoSequence<( {} )>".format(self.values)
	#

	def __repr__(self) -> str:
		return self.__repr__()
	#

	#
	# Converts a sequence of boolens to TextSpanInfo objects.
	#
	def compact(self) -> TextSpanInfoSequence:
		ret:typing.List[TextSpanInfo] = []

		_currentValue = None
		_temp = []
		pos = 0
		for b in self.values:
			if _currentValue != b:
				if _temp:
					ret.append(TextSpanInfo(_currentValue, pos-len(_temp), len(_temp)))
				_currentValue = b
				_temp = []
			_temp.append(b)
			pos += 1

		if _temp:
			ret.append(TextSpanInfo(_currentValue, pos-len(_temp), len(_temp)))

		return TextSpanInfoSequence(ret)
	#

#







