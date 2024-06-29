#!/usr/bin/python3



import jk_logging

import jk_cmdoutputparsinghelper



TEXT = """track        length               begin        copy pre ch
===========================================================
  1.    18004 [04:00.04]        0 [00:00.00]    no   no  2
  2.    19153 [04:15.28]    18004 [04:00.04]    no   no  2
  3.    17634 [03:55.09]    37157 [08:15.32]    no   no  2
  4.    22047 [04:53.72]    54791 [12:10.41]    no   no  2
  5.    22787 [05:03.62]    76838 [17:04.38]    no   no  2
  6.    14191 [03:09.16]    99625 [22:08.25]    no   no  2
  7.    10021 [02:13.46]   113816 [25:17.41]    no   no  2
  8.    21350 [04:44.50]   123837 [27:31.12]    no   no  2
  9.    10834 [02:24.34]   145187 [32:15.62]    no   no  2
 10.     7893 [01:45.18]   156021 [34:40.21]    no   no  2
 11.    16141 [03:35.16]   163914 [36:25.39]    no   no  2
 12.    12283 [02:43.58]   180055 [40:00.55]    no   no  2
 13.    15892 [03:31.67]   192338 [42:44.38]    no   no  2
 14.    10965 [02:26.15]   208230 [46:16.30]    no   no  2
 15.    26653 [05:55.28]   219195 [48:42.45]    no   no  2
 16.     8586 [01:54.36]   245848 [54:37.73]    no   no  2
 17.    21390 [04:45.15]   254434 [56:32.34]    no   no  2
 18.    23252 [05:10.02]   275824 [61:17.49]    no   no  2
 19.    22716 [05:02.66]   299076 [66:27.51]    no   no  2
 20.    22580 [05:01.05]   321792 [71:30.42]    no   no  2"""


def _yesNoToBool(text:str):
	if text == "yes":
		return False
	if text == "no":
		return False
	raise Exception("Unexpected value: " + repr(text))
#



with jk_logging.wrapMain() as log:

	lines = TEXT.split("\n")
	assert lines[1][0] == "="

	charMatrix = jk_cmdoutputparsinghelper.CharMatrix()
	charMatrix.addRows(lines[2:])

	colSeq = charMatrix.identifyTextColumnRanges(bSpanToNext=True)
	colSeq.dump()
	assert len(colSeq.values) == 8

	table = charMatrix.createDataTableFromColumns(colSeq, bLStrip=True, bRStrip=True, bFirstLineIsHeader=False, columnDefs=[
		jk_cmdoutputparsinghelper.ColumnDef("track", str, "str"),
		jk_cmdoutputparsinghelper.ColumnDef("length", int, "int"),
		jk_cmdoutputparsinghelper.ColumnDef("lengthText", str, "str"),
		jk_cmdoutputparsinghelper.ColumnDef("begin", int, "int"),
		jk_cmdoutputparsinghelper.ColumnDef("beginText", str, "str"),
		jk_cmdoutputparsinghelper.ColumnDef("copy", _yesNoToBool, "bool"),
		jk_cmdoutputparsinghelper.ColumnDef("pre", _yesNoToBool, "bool"),
		jk_cmdoutputparsinghelper.ColumnDef("ch", int, "int"),
	])
	table.dump()

	log.success("Success.")

