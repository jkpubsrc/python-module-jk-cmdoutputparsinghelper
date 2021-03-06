


class ValueParserDef(object):

	__slots__ = (
		"matchKey",
		"outputKey",
		"parseFunc",
	)

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, matchKey:str, outputKey:str, parseFunc):
		assert isinstance(matchKey, str)
		assert matchKey
		if outputKey is None:
			outputKey = matchKey
		else:
			assert isinstance(outputKey, str)
			assert outputKey
		if parseFunc:
			assert callable(parseFunc)

		self.matchKey = matchKey
		self.outputKey = outputKey
		self.parseFunc = parseFunc
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

#








