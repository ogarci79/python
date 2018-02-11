#!/usr/bin/env python

#import matplotlib.pyplot as plt
import cv2
import argparse
#import numpy as np
#from scipy import linalg 

def main():
    print "Hi"
    parser = argparse.ArgumentParser(description='Crop an image')
    parser.add_argument('-i','--image',help='Image to crop',required=True)
    parser.add_argument('-r','--rows',help='Rows to leave',required=False)
    parser.add_argument('-c','--columns',help='Columns to leave',required=False)
    args=vars(parser.parse_args())

    if args['rows'] :
        rows=args['rows']
    if args['columns'] :
        cols=args['columns']
    I=args['image']
    image=cv2.imread(I)
    cv2.imshow('Original',image)
    cv2.waitKey(0)
    I_row,I_col,I_channels = image.shape

    if rows > I_row :
        rows = I_row
    if cols > I_col :
        cols = I_col

    cropped = image[70:170,440:540]
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)

    cv2.imwrite("small.jpg",cropped)

if __name__ == "__main__":
    main()

