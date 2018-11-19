#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('owl.jpg',0)
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'),plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'),plt.xticks([]),plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
