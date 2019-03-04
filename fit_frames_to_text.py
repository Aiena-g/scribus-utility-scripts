# This script is only for photoshop exported images with the quick export to PNG operation

import scribus
 
# "Warning", "Utility script to arrange pg frame for "MOH Executive summary only" adapt for other docs"

if not scribus.haveDoc():
	scribus.messageBox('Usage Error', 'You need a Document open')
	sys.exit(1)


def main():
	cntr = scribus.selectionCount()
	
	while(True):
		along_dim = scribus.valueDialog("How to fit text?", 'Enter "w" to fit alog width. "h" to fit along height. Enter "b" to fit along both width first. Type "c" to cancel operation',"w")
		along_dim = along_dim.lower()
		if along_dim in ("c"):
			sys.exit(0)
		if along_dim in ("w","h", "b"):
			break
		else:
			scribus.messageBox("Error","Invalid option specified. Please try again")

	for i in range(0,cntr):
		objNm = scribus.getSelectedObject(i)
		print (objNm)
		if along_dim in ("w","h"):
			fit_frame_to_text(objNm, along_dim)
		elif along_dim == "b":
			fit_frame_to_text(objNm, "w")
			fit_frame_to_text(objNm, "h")
			

def fit_frame_to_text(frame,dim):
	if dim not in ["h","w"]:
		raise Exception("Invalid dimension specified. Please speficy the dimension as \"h\" for height or \"w\" for width.")

	if scribus.getObjectType(frame) != "TextFrame":
		print "Object with name \"{}\" is not a text frame - skipping".format(objNm)
		return

	char_n = scribus.getTextLength(frame)

	if char_n == 0 :
		scribus.messageBox('Warning:', 'Cannot adjust \"{}\" as it is an empty frame.'.format(frame));
		return

	# get some frame measures	
	x, y = scribus.getPosition(frame)
	w, h = scribus.getSize(frame)

	steps_coarse = 0.393701 # 10mm in inches
	steps_fine = 0.0393701 # 1 mm = 0.0393701 in
	
	if dim == "h":
		# if the frame doesn't overflow, shorten it to make it overflow
		while ((scribus.textOverflows(frame) == 0) and (h > 0)):
			h -= steps_coarse
			scribus.sizeObject(w, h, frame)

		# resize the frame in steps_coarse pt steps
		while (scribus.textOverflows(frame) > 0):
			h += steps_coarse
			scribus.sizeObject(w, h, frame)
			
		print ("dim after making it overflow is ({},{})".format(w,h))

		# undo the latest steps_coarse pt step and fine adjust in steps_fine pt steps
		h -= steps_coarse
		scribus.sizeObject(w, h, frame)
		print ("dim after making undoing last overflow resolution is ({},{})".format(w,h))

		while (scribus.textOverflows(frame) > 0):
			h += steps_fine
			scribus.sizeObject(w, h, frame)
		print ("dim after making overflow resolution is ({},{})".format(w,h))
	
	if dim == "w":
		# if the frame doesn't overflow, shorten it to make it overflow
		while ((scribus.textOverflows(frame) == 0) and (w > 0)) :
			w -= steps_coarse
			scribus.sizeObject(w, h, frame)
		print ("dim after making it overflow is ({},{})".format(w,h))

		# resize the frame in steps_coarse pt steps
		while (scribus.textOverflows(frame) > 0):
			w += steps_coarse
			scribus.sizeObject(w, h, frame)

		# undo the latest steps_coarse pt step and fine adjust in steps_fine pt steps
		w -= steps_coarse
		scribus.sizeObject(w, h, frame)
		print ("dim after making undoing last overflow resolution is ({},{})".format(w,h))

		while (scribus.textOverflows(frame) > 0):
			w += steps_fine
			scribus.sizeObject(w, h, frame)
		print ("dim after making overflow resolution is ({},{})".format(w,h))
		

# run the script
main()