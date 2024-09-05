import cv2
import pyautogui as p
import numpy as np

rs = p.size() # capture the resolution

fn = input("Please Enter any file name and path: ")
fps = 60

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn, fourcc, fps, rs)

cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL) # name and type
cv2.resizeWindow("Live Recording", (600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording", f)
    if cv2.waitKey(60) == ord('q'):
        break
    
output.release()
cv2.destroyAllWindows()
