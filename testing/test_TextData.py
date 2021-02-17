#!/usr/bin/python3



import jk_logging

from jk_cmdoutputparsinghelper import *





with jk_logging.wrapMain() as log:

	t = TextData("foo\nbar\n")
	assert len(t.lines) == 3

	t = TextData("foo\nbar")
	assert len(t.lines) == 2

	t = TextData("foo")
	assert len(t.lines) == 1

	t = TextData("")
	assert len(t.lines) == 0

	log.success("Success.")

