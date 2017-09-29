import datetime
import time
import cv2
import os


class Camara:
    def Cam(self):
        self.cap = cv2.VideoCapture(0)
        time.sleep(2)

        while 1:
            # Capture of image and convert to RGB -> HSV
            ret, self.imagen = self.cap.read()
            if ret:
                cv2.imshow('Camara', self.imagen)
                tecla = cv2.waitKey(5) & 0xFF
                if tecla == 27:
                    ts = datetime.datetime.now()
                    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                    p = os.path.sep.join(("photo", filename))
                    # save the file
                    cv2.imwrite(p, self.imagen.copy())
                    print("[INFO] saved {}".format(filename))
                    break
        cv2.destroyAllWindows()





















