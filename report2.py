import cv2
import matplotlib.pyplot as plt
import numpy as np

capture = cv2.VideoCapture(0)
count = 0
x = []
y = []

while(True):
	ret, frame = capture.read()
	print(frame.mean())
	count = count+1
	x.append(count)
	y.append(frame.mean())
	if count==500:
		break
plt.plot(x, y) 
plt.xlabel("x") 
plt.ylabel("y") 
plt.xlim(0, 500)
plt.ylim(90, 110)
plt.title("$average$")
plt.savefig("hoge.png")
plt.show()

capture.release()
cv2.destroyAllWindows()