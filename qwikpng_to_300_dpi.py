# This script is only for photoshop exported images with the quick export to PNG operation

import scribus
 
# "Warning", "Utility script to arrange pg frame for "MOH Executive summary only" adapt for other docs"

if not scribus.haveDoc():
	scribus.messageBox('Usage Error', 'You need a Document open')
	sys.exit(1)

cntr = scribus.selectionCount()

for i in range(0,cntr):
	objNm = scribus.getSelectedObject(i)
	print (objNm)
	if scribus.getObjectType(objNm) == "ImageFrame":
		# set dpi of image to 300dpi (32% scale)
		scribus.setImageScale(0.32, 0.32, objNm)
		# fit frame to image
		scribus.setScaleFrameToImage(objNm)