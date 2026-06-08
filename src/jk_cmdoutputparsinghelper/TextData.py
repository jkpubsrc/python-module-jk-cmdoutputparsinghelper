


import typing

from .LineList import LineList
from .CharMatrix import CharMatrix







#
# This class represents text. It converts text automatically to a LineList or to string as required.
# So if you access the stored data via <c>text</c> you will receive the text content as a single string.
# If you access the stored data via <c>lines</c> you will receive the text content as a set of text lines.
# Conversion occurs automatically depending on which property you use.
#
# This mechanism provided by this class
# allows you to work efficiently with text data as a string or a string list, depending on the current
# requirements, while avoiding unnecessary intermediate conversions.
#
class TextData(object):

	__slots__ = (
		"__dataStr",
		"__dataLines",
	)

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#

	def __init__(self, data:str|tuple[str]|list[str]|LineList):
		self.__dataStr:str|None = None
		self.__dataLines:LineList|None = None

		if isinstance(data, str):
			self.text = data
		elif isinstance(data, (tuple,list,LineList)):
			self.lines = data
		else:
			raise TypeError(str(type(data)))
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def lines(self) -> LineList:
		if self.__dataLines is None:
			# convert to lines
			self.__dataLines = LineList(self.__dataStr.split("\n"))

		return self.__dataLines
	#

	@lines.setter
	def lines(self, value:tuple[str]|list[str]|LineList):
		if isinstance(value, (tuple, list)):
			for x in value:
				assert isinstance(x, str)
			self.__dataLines = LineList(value)
		elif isinstance(value, LineList):
			self.__dataLines = value
		else:
			raise TypeError(str(type(value)))
		self.__dataStr = None
	#

	@property
	def text(self) -> str:
		if self.__dataStr is None:
			# convert to text
			self.__dataStr = "\n".join(self.__dataLines)
		return self.__dataStr
	#

	@text.setter
	def text(self, value:str):
		if isinstance(value, str):
			self.__dataStr = value
		else:
			raise TypeError(str(type(value)))
		self.__dataLines = None
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self):
		if self.__dataStr is None:
			self.__dataStr = "\n".join(self.__dataLines)
		return self.__dataStr
	#

	def __repr__(self):
		return repr(self.__str__())
	#

	def __bool__(self):
		return bool(self.text)
	#

	def toCharMatrix(self) -> CharMatrix:
		ret = CharMatrix()
		if self.__dataLines is None:
			self.__dataLines = LineList(self.__dataStr.split("\n"))
		for line in self.__dataLines:
			ret.addRow(line)
		return ret
	#

#










