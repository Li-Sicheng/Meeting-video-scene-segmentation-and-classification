import cv2

cap = cv2.VideoCapture("D:/Demo-1.mp4")
h = 256
w = 256
size = (h, w)
pix_sum = h * w
sensi_blur = 50
sensi_diff = 0.23
time_unit = 10

ret, frame_1 = cap.read()
frame_1_gray = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
frame_1_gray = cv2.GaussianBlur(frame_1_gray, (21, 21), 0)
frame_1_gray = cv2.resize(frame_1_gray, size)

cv2.imshow('video', frame_1)

avg_first = 0
i = 0
if cap.isOpened():
    while True:
        ret, frame_2 = cap.read()
        frame_2_gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
        frame_2_gray = cv2.GaussianBlur(frame_2_gray, (21, 21), 0)
        frame_2_gray = cv2.resize(frame_2_gray, size)

        frame_diff = cv2.absdiff(frame_1_gray, frame_2_gray)

        frame_diff_thres = cv2.threshold(frame_diff, sensi_blur, 255, cv2.THRESH_BINARY)[1]

        if ret == True:
            pix_diff = 0
            for y in range(h):
                for x in range(w):
                    if frame_diff_thres[x, y] != 0.0:
                        pix_diff = pix_diff + 1
            avg = (pix_diff * 1.00) / (pix_sum * 1.00)
            print "pix_diff:"
            print pix_diff
            print avg
            if (i % 10 == 0):
                cv2.imshow('follow',frame_2)
                if avg > sensi_diff:
                    cv2.imshow('video', frame_2)
        else:
            break

        i = i + 1
        frame_1_gray = frame_2_gray

        if cv2.waitKey(20)==27:
            break
cv2.destroyAllWindows()