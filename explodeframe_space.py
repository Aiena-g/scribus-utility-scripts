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
 
y, x = scribus.getPosition()

width, _ =  scribus.getSize()

gap = 4 # in mm

margin_bottom = 0 #spacing between new frames 

# delete original
scribus.deleteObject()

# make new ones
for line in lines:
	frame_name = scribus.createText(y, x, width, gap)
	scribus.setText(line, frame_name)
	x += gap + margin_bottom

scribus.setUnit(doc_unit)

# BROKEN TODO TEST