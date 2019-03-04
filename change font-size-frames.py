import scribus

#iterate thrown all selected text objects and set font size
cntr = scribus.selectionCount()
newFontSz = float(scribus.valueDialog("Font size","Enter the new font size"))

for i in range(0,cntr):
	objNm = scribus.getSelectedObject(i)
	print (objNm)
	if scribus.getObjectType(objNm) == "TextFrame":
		scribus.setFontSize(newFontSz,objNm)