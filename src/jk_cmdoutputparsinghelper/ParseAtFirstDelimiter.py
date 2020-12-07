



class ParseAtFirstDelimiter(object):

	################################################################################################################################
	## Constructors
	################################################################################################################################

	def __init__(self, delimiter:str = ":", valueCanBeWrappedInDoubleQuotes:bool = False, keysReplaceSpacesWithUnderscores:bool = False):
		self.delimiter = delimiter
		self.keysReplaceSpacesWithUnderscores = keysReplaceSpacesWithUnderscores
		self.valueCanBeWrappedInDoubleQuotes = valueCanBeWrappedInDoubleQuotes
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

	def parseLines(self, lines):
		assert isinstance(lines, (tuple, list))

		ret = {}
		for line in lines:
			k, v = self.parseLine(line)
			if k:
				ret[k] = v
		#
		return ret
	#

	def parseLine(self, line:str):
		assert isinstance(line, str)

		pos = line.find(self.delimiter)
		if pos > 0:
			k = line[:pos].strip()
			v = line[pos+1:].strip()
			if self.valueCanBeWrappedInDoubleQuotes:
				if v.startswith("\"") and v.endswith("\""):
					v = v[1:-1]
					v = v.replace("\\\"", "\"")
			if self.keysReplaceSpacesWithUnderscores:
				k = k.replace(" ", "_")
			return k, v
		else:
			return None, None
	#

#







