import scribus
 
# "Warning", "Utility script to arrange pg frame for "MOH Executive summary only" adapt for other docs"

if not scribus.haveDoc():
	scribus.messageBox('Usage Error', 'You need a Document open')
	sys.exit(1)
 
if scribus.selectionCount() != 1:
	scribus.messageBox('Usage Error', 'Please, select one single frame')
	sys.exit(1)
 
if (scribus.getObjectType() != 'ImageFrame'):
	scribus.messageBox('Usage Error', 'Please, select an image frame')
	sys.exit(1)

# set dpi of image to 300dpi (32% scale)
scribus.setImageScale(0.32, 0.32)
 
# fit frame to image
scribus.setScaleFrameToImage()
 
# align the object to top right corner of pg
scribus.moveObjectAbs(0,0)
scribus.setImageOffset(0,0)