#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this script CONVERTS ENGLISH NUMERALS TO ARABIC
#translation into RTL languages e.g. Arabic. This flips page content. Note: No changes are made to application of master pages


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

arab_num_list = [arabic_zero, arabic_one, arabic_two, arabic_three, arabic_four, arabic_five, arabic_six, arabic_seven, arabic_eight, arabic_nine]
eng_num_list = ["0","1","2","3","4","5","6","7","8","9"]

import scribus
import subprocess

def conv_text(unicodestr):
	#replaces numbers and percent sign the remainder is left untouched for manual cleaning and fixing
	#returns list of indexes where the char was replaced, utf-8 encoded converted string
	conv_pos = [] #index's in the string where the item was converted
	
	# make the string a list
	u_list = list(unicodestr)
	
	# do in place replace
	for idx,char in enumerate(u_list):
		if char in eng_num_list:
			#print char
			conv_pos.append(idx)
			u_list[idx] = (replace_digit_str(char))
		
		if char in arab_num_list:
			conv_pos.append(idx)
		
		if char == "%":
			conv_pos.append(idx)
			u_list[idx] = arabic_dec_sep
			
		if char == arabic_dec_sep:
			conv_pos.append(idx)
	
	return conv_pos, ''.join(u_list)
	

	
def replace_digit_str(eng_digit_str):
	switcher = {
		eng_num_list[0] : arab_num_list[0],
		eng_num_list[1] : arab_num_list[1],
		eng_num_list[2] : arab_num_list[2],
		eng_num_list[3] : arab_num_list[3],
		eng_num_list[4] : arab_num_list[4],
		eng_num_list[5] : arab_num_list[5],
		eng_num_list[6] : arab_num_list[6],
		eng_num_list[7] : arab_num_list[7],
		eng_num_list[8] : arab_num_list[8],
		eng_num_list[9] : arab_num_list[9]
	}
	
	result =  switcher.get(eng_digit_str,"NOT A DIGIT")
	if result == "NOT A DIGIT":
		raise Exception("data \"{}\" given is not a digit. Cannot convert.".format(eng_digit_str))
	else:
		return result


def get_styles_at_index(string,index_lst):
	pass

def main():
	cntr = scribus.selectionCount()

	for i in range(0,cntr):
		objNm = scribus.getSelectedObject(i)
		print (objNm)
		if scribus.getObjectType(objNm) == "TextFrame":
			curr_style = scribus.getStyle(objNm)
			text = scribus.getText(objNm)
			print(repr(text))
			print(repr(type(text)))
			u_text = unicode(text)
			print(repr(type(u_text)))
			color_idx_lst, text = conv_text(u_text)
			scribus.setText(text, objNm)
			
			print (repr(color_idx_lst))
			
			for i in color_idx_lst:
				scribus.selectText(i,1,objNm)
				scribus.setTextColor("Red",objNm)
				print(curr_style)
				if (curr_style is not None):
					scribus.setStyle(curr_style,objNm)
			


main()
'''

import scribus

scribus.selectText(2,1)
'''