import scribus
 
if not scribus.haveDoc():
	scribus.messageBox('Usage Error', 'You need a Document open')
	sys.exit(1)
 
if scribus.selectionCount() != 1:
	scribus.messageBox('Usage Error', 'Please, select one single frame')
	sys.exit(1)
 
if (scribus.getObjectType() != 'TextFrame'):
	scribus.messageBox('Usage Error', 'Please, select a text frame')
	sys.exit(1)
 
doc_unit = scribus.getUnit()

scribus.setUnit(scribus.UNIT_MILLIMETERS)

scribus.selectText(0, 0)

content = scribus.getText()
 
lines = content.split('\r')
 
x, y = scribus.getPosition()
w,h = scribus.getSize()

#get current applied style
style = scribus.getStyle()

new_content = ""
for line in lines:
	if line != "":
		new_content = new_content + line + "%" + "\r\n"
	else:
		new_content = new_content + "\r\n"
		
	
scribus.setText(new_content)
scribus.setStyle(style)

scribus.setUnit(doc_unit)
