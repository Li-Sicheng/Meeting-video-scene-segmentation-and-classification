import cv2

h =300
w = 200
size = (h, w)
pix_sum = h * w    #60000

frame_1 = cv2.imread("D:\\QQ½ØÍ¼1.png")

frame_1_gray = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
frame_1_gray = cv2.GaussianBlur(frame_1_gray, (21, 21), 0)

frame_2 = cv2.imread("D:\\QQ½ØÍ¼2.png")

frame_2_gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
frame_2_gray = cv2.GaussianBlur(frame_2_gray, (21, 21), 0)


frame_1_gray = cv2.resize(frame_1_gray, size)
frame_2_gray = cv2.resize(frame_2_gray, size)

frame_diff = cv2.absdiff(frame_1_gray, frame_2_gray)

frame_diff_thres = cv2.threshold(frame_diff, 50, 255, cv2.THRESH_BINARY)[1]


pix_diff = 0
for y in range(h):
    for x in range(w):
        if frame_diff_thres[x, y] != 0.0:
            pix_diff = pix_diff + 1

print pix_diff

avg = (pix_diff * 1.00) / (pix_sum * 1.00)
print avg
print pix_sum
if avg > 0.11:
    print "Moving!"
else:
    print "No."

cv2.imshow("Image", frame_diff_thres) 

cv2.waitKey (0)
cv2.destroyAllWindows()