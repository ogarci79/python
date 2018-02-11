#!/usr/bin/env python

import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture('../../background_subtraction/src/vtest.avi')
    fgbg = cv2.BackgroundSubtractorMOG2()

    while(1) :
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27 :
            break
    cp.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

