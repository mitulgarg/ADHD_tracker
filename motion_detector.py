# Python program to implement
# Webcam Motion Detector

import numpy as np
import matplotlib.pyplot as plt

# importing OpenCV, time and Pandas library
import cv2, time, pandas
import csv
# importing datetime class from datetime library
from datetime import datetime

from tkinter import * 
from tkinter import messagebox


def tkinter():
        root = Tk()
        root.geometry("300x200")
        w = Label(root, text ='', font = "80") 
        w.pack()
        messagebox.showinfo("Continue", "GET TO WORK! FOCUS!!")
        root.mainloop()
  



# Assigning our static_back to None
static_back = None

# List when any moving object appear
motion_list = [ None, None ]

# Time of movement
time = []
l2=[]
# Initializing DataFrame, one column is start
# time and other column is end time

#df = pandas.DataFrame(columns = ["Start", "End"])
d1=[]

# Capturing video
video = cv2.VideoCapture(0)

# Infinite while loop to treat stack of image as video
while True:
	# Reading frame(image) from video
	check, frame = video.read()

	# Initializing motion = 0(no motion)
	motion = 0

	# Converting color image to gray_scale image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Converting gray scale image to GaussianBlur
	# so that change can be found easily
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# In first iteration we assign the value
	# of static_back to our first frame
	if static_back is None:
		static_back = gray
		continue

	# Difference between static background
	# and current frame(which is GaussianBlur)
	diff_frame = cv2.absdiff(static_back, gray)

	# If change in between static background and
	# current frame is greater than 30 it will show white color(255)
	thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
	thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

	# Finding contour of moving object
	cnts,_ = cv2.findContours(thresh_frame.copy(),
					cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in cnts:
		if cv2.contourArea(contour) < 110000:
			continue
		l2.append(contour)
		motion = 1
		#tkinter()
		
		
		(x, y, w, h) = cv2.boundingRect(contour)
		# making green rectangle around the moving object
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

	# Appending status of motion
	motion_list.append(motion)

	motion_list = motion_list[-2:]

	# Appending Start time of motion
	if motion_list[-1] == 1 and motion_list[-2] == 0:
		time.append(datetime.now())
		print('BREATHE! CALM DOWN!')
                

	# Appending End time of motion
	elif motion_list[-1] == 0 and motion_list[-2] == 1:
		time.append(datetime.now())
                
	# Displaying image in gray_scale
	cv2.imshow("Gray Frame", gray)

	# Displaying the difference in currentframe to
	# the staticframe(very first_frame)
	cv2.imshow("Difference Frame", diff_frame)

	# Displaying the black and white image in which if
	# intensity difference greater than 30 it will appear white
	cv2.imshow("Threshold Frame", thresh_frame)

	# Displaying color frame with contour of motion of object
	cv2.imshow("Color Frame", frame)

	key = cv2.waitKey(1)
	# if q entered whole process will stop
	if key == ord('q'):
		# if something is movingthen it append the end time of movement
		if motion == 1:
			time.append(datetime.now())
	
		break

# Appending time of motion in DataFrame
"""for i in range(0, len(time), 2):
	df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)"""
print()
print(time)


# Creating a CSV file in which time of movements will be saved
print(d1)


f1=open('Time_ofmovements.csv','w')
# create the csv writer
writer = csv.writer(f1)

# write a row to the csv file
writer.writerow(time)

# close the file
f1.close()


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array(time)
z=len(x)
l=[]
for i in range(0,z):
        l.append(i)



plt.title("Analysis graph")
plt.xlabel('Time of Movements')
plt.ylabel('Number')
plt.scatter(x, l, color="red")




# add axes labels

plt.show()

'''
#second graph
plt.title("Movement threshold graph")
plt.plot(x, l2, color="red")

# add axes labels
plt.xlabel('Time of Movements')
plt.ylabel('Threshold')





'''

'''
for i in d1:
    s=str(i)
    f1.write(s)
    f1.write(" ")

f1.close()
'''
video.release()

# Destroying all the windows
cv2.destroyAllWindows()
