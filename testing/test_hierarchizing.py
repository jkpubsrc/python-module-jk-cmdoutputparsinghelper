#!/usr/bin/python3



import jk_logging

import jk_cmdoutputparsinghelper



TEXT = """This is text line
	a descended text line
		some nested data
		more nested data
			even more more nested data
	another descended text line
	even another descended text line
		and more nested data
Another main text line
	below the main text line
		even more below
		and another line
"""




with jk_logging.wrapMain() as log:

	lineList = jk_cmdoutputparsinghelper.LineList(TEXT)
	assert len(lineList) == 12

	lineList.dump(printFunc=log.debug)

	log.debug("getLeadingSpaceCounts() = " + str(lineList.getLeadingSpaceCounts()))

	rootNode = lineList.groupByIndentation()
	rootNode.dump(printFunc=log.info)

	log.success("Success.")

