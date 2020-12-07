#!/usr/bin/python3




import jk_json

from jk_cmdoutputparsinghelper import *








INPUT_FILE = "input__systemctl_list_units.txt"



with open(INPUT_FILE, "r") as f:
	inputData = f.read()

lines = LineList(inputData)
#lines.dump()

lineNumbers = lines.getLineNumbersOfEmptyLines()
#print(lineNumbers)
del lines[lineNumbers[0]:]
#lines.dump()

wordPos = getPositionsOfWords(lines[0])
#print(wordPos)

#lines2 = LineList(lines.extractColumn(0, wordPos[0]))
#lines2.dump()

wordPos = [ 0 ] + wordPos
columns = lines.extractColumns(wordPos)
#jk_json.prettyPrint(columns)
table = lines.createDataTableFromColumns(wordPos, bFirstLineIsHeader=True)
#jk_json.prettyPrint(table)

m = table.toDataMatrix()
m.orderByColumn("ACTIVE")
m.orderByColumn("LOAD")
m.dump()








