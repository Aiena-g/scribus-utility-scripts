import scribus
 
if not scribus.haveDoc():
	scribus.messageBox('Usage Error', 'You need a Document open')
	sys.exit(1)
 
if scribus.selectionCount() < 2:
	scribus.messageBox('Usage Error', 'Please, select atleast 2 objects')
	sys.exit(1)
 
 
doc_unit = scribus.getUnit()

scribus.setUnit(scribus.UNIT_MILLIMETERS)

_ , first_y =    scribus.getPosition(scribus.getSelectedObject(i))

for i in range(scribus.selectionCount()):
	currobjname = scribus.getSelectedObject(i)
	x, y = scribus.getPosition(currobjname)
	width, _ =  scribus.getSize(currobjname)
	


# make new ones
for line in lines:
	frame_name = scribus.createText(x, y, width, linespacing)
	scribus.setText(line, frame_name)
	y += linespacing + margin_bottom

scribus.setUnit(doc_unit)