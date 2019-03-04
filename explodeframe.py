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

width, _ =  scribus.getSize()

style = scribus.getStyle()

linespacing = scribus.getLineSpacing() * 0.352778 # in pts to mm

margin_bottom = 0 #spacing between new frames 

# delete original
scribus.deleteObject()

# make new ones
for line in lines:
	frame_name = scribus.createText(x, y, width, linespacing)
	scribus.setText(line, frame_name)
	scribus.setStyle(style, frame_name)
	y += linespacing + margin_bottom

scribus.setUnit(doc_unit)