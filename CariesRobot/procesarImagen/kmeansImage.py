import numpy as np
import cv2
import logging

class kmeans:
    def identificarCarie(self):
        img = cv2.imread('photo/final.jpg')
        Z = img.reshape((-1, 3))
        # convert to np.float32
        Z = np.float32(Z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))

        x,y = center.shape
        carie=0
        for i in range(x):
            for j in range(y):
                if(center[i,j]<90):
                    carie+=1
                    if(carie==3):
                        print "tiene caries"
                        break
        cv2.imshow('res2',res2)
        cv2.imshow('original', img)
        cv2.imwrite('../photo/final2.jpg',res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()