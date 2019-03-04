#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus

def list_unicode_names(unicodestr):
	#replaces numbers and percent sign the remainder is left untouched for manual cleaning and fixing
	#returns list of indexes where the char was replaced, utf-8 encoded converted string
	conv_pos = [] #index's in the string where the item was converted
	
	# make the string a list
	u_list = list(unicodestr)
	
	# do in place replace
	for idx,char in enumerate(u_list):
		
	
	return conv_pos, ''.join(u_list)
	


def main():
	cntr = scribus.selectionCount()

	for i in range(0,cntr):
		objNm = scribus.getSelectedObject(i)
		print (objNm)
		if scribus.getObjectType(objNm) == "TextFrame":
			text = scribus.getText(objNm)
			print(repr(text))
			print(repr(type(text)))
			u_text = unicode(text)
			print(repr(type(u_text)))
			result = list_unicode_names(u_text)
			scribus.messageBox("unicode names:", result)
			


main()
