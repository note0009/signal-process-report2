# signal-process-report2
import cv2
import matplotlib.pyplot as plt
import numpy as np

capture = cv2.VideoCapture(0)
count = 0
x = []
y = []

while(True):
	ret, frame = capture.read()　//フレームに画像を代入する。
	print(frame.mean())
	count = count+1　
	x.append(count)　//xにcountの値を代入する。
	y.append(frame.mean())　//yに画像の輝度値の平均を代入する。
	if count==500:　//countが500になったらwhileを止める。
		break
plt.plot(x, y) //リストx,yをグラフにプロットする。
plt.xlabel("x") 
plt.ylabel("y") 
plt.xlim(0, 500)
plt.ylim(90, 110)
plt.title("$average$")
plt.savefig("hoge.png")
plt.show()

capture.release()
cv2.destroyAllWindows()
