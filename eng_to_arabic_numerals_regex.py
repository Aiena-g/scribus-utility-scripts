#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this script CONVERTS ENGLISH NUMERALS TO ARABIC
#translation into RTL languages e.g. Arabic. This flips page content. Note: No changes are made to application of master pages

import scribus
import re

# WARNING THIS SCRIPT HAS NOT BEEN TESTED WITH LINKED FRAMES AND MAY/DOES NOT WORK WITH THOSE CURRENTLY
# This script is lazily designed to preserve style only if one style is apply for the whole text frame 

arabic_zero = u'\N{ARABIC-INDIC DIGIT ZERO}'
arabic_one = u'\N{ARABIC-INDIC DIGIT ONE}'
arabic_two = u'\N{ARABIC-INDIC DIGIT TWO}'
arabic_three = u'\N{ARABIC-INDIC DIGIT THREE}'
arabic_four = u'\N{ARABIC-INDIC DIGIT FOUR}'
arabic_five = u'\N{ARABIC-INDIC DIGIT FIVE}'
arabic_six = u'\N{ARABIC-INDIC DIGIT SIX}'
arabic_seven = u'\N{ARABIC-INDIC DIGIT SEVEN}'
arabic_eight = u'\N{ARABIC-INDIC DIGIT EIGHT}'
arabic_nine = u'\N{ARABIC-INDIC DIGIT NINE}'
arabic_dec_sep = u'\N{ARABIC DECIMAL SEPARATOR}'
arabic_perc_sign = u'\N{ARABIC PERCENT SIGN}'

arab_num_list = [arabic_zero, arabic_one, arabic_two, arabic_three, arabic_four, arabic_five, arabic_six, arabic_seven, arabic_eight, arabic_nine]
eng_num_list = ["0","1","2","3","4","5","6","7","8","9"]

decimal_match_re = r"[-+]?\d+(\.\d+)?"

def conv_text(unicodestr):
	#replaces numbers and percent sign the remainder is left untouched for manual cleaning and fixing
	#returns list of indexes where the char was replaced, utf-8 encoded converted string
	conv_pos = [] #index's in the string where the item was converted
	print "regex1 is {}".format(decimal_match_re)
	result = re.sub(decimal_match_re, replace_decimal_number, unicodestr)
	
	return result
	
def get_significant_text_indices(unicodestr):
	result = []
	
	chars_to_search = arab_num_list
	chars_to_search.extend([arabic_dec_sep, arabic_perc_sign])
	search_re = "|".join(chars_to_search)
	print "regex2 is {}".format(search_re)

	for m in re.finditer(search_re, unicodestr):
		# list containing lists of [start index, count] items e.g. [[1,3],[7,2]] etc.
		result.append([m.start(), m.end() -  m.start()])
		
	return result
	

def replace_decimal_number (matchObj):
	matchstr = matchObj.group(0)
	print ("Matchstr is \"{}\"".format(matchstr))
	if matchstr != "":
		strlist = list(matchstr)

		for idx,char in enumerate(strlist):
			if char in eng_num_list:
				strlist[idx] = replace_digit_str(char)
			if char == ".":
				strlist[idx] = arabic_dec_sep
		
		print "replace_decimal_number returning {}".format("".join(strlist))
		return "".join(strlist)
	else:
		return ""
			
	
def replace_digit_str(eng_digit_str):
	switcher = dict(zip(eng_num_list, arab_num_list))
	
	result =  switcher.get(eng_digit_str,"NOT A DIGIT")
	if result == "NOT A DIGIT":
		raise Exception("data \"{}\" given is not a digit. Cannot convert.".format(eng_digit_str))
	else:
		return result

def main():
	cntr = scribus.selectionCount()

	for i in range(0,cntr):
		obj_nm = scribus.getSelectedObject(i)
		print (obj_nm)
		if scribus.getObjectType(obj_nm) == "TextFrame":
			curr_style = scribus.getStyle(obj_nm)
			text = scribus.getText(obj_nm)
			print(repr(text))
			print(repr(type(text)))
			u_text = unicode(text)
			print(repr(type(u_text)))
			
			text = conv_text(u_text)
			scribus.setText(text, obj_nm)
			
			color_idx_lst = get_significant_text_indices(text)
			
			if color_idx_lst is None:
				print("Nothing to highlight found")
				return
			
			print (repr(color_idx_lst))
			
			print(curr_style)
			if (curr_style is not None):
				scribus.setStyle(curr_style,obj_nm)
			
			for i in color_idx_lst:
				# color needs to be set after style
				scribus.selectText(0,0,obj_nm) # clear selection
				scribus.selectText(i[0],i[1],obj_nm)
				scribus.setTextColor("Red",obj_nm)
		


main()