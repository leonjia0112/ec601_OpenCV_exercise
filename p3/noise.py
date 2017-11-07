import os
import sys
import cv2
import numpy as np

MEANS = [0, 50, 10, 20]
SIGMAS = [0, 20, 50, 100]
BLKS = [0.01, 0.03, 0.05, 0.4]
WHTS = [0.01, 0.03, 0.05, 0.4]
KERNAL = [3, 5, 7]

def main():
    if len(sys.argv) < 2:
        exit(1)
    image = cv2.imread(sys.argv[1])
    if ".png" in sys.argv[1]:
        ftype = ".png"
    else:
        ftype = ".jpg"
    for kernal in KERNAL:
        for mean in MEANS:
            for sigma in SIGMAS:        
                noise = image.copy()
                cv2.randn(noise, mean, sigma)
                GN_img = np.add(image, noise)
                GN_img_bf = cv2.blur(GN_img, (kernal, kernal))
                GN_img_gf = cv2.GaussianBlur(GN_img, (kernal, kernal), 1.5)
                GN_img_mf = cv2.medianBlur(GN_img, kernal)
                target = ("./Exercise3_Output/"+sys.argv[1].rstrip(ftype)+
                          "/Gaussian/K"+str(kernal)+"_M"+str(mean)+
                          "_S"+str(sigma)+"/"
                )
                if not os.path.exists(target):
                    os.makedirs(target)
                cv2.imwrite(target+"Noise"+ftype, GN_img)
                cv2.imwrite(target+"Box_Filter"+ftype, GN_img_bf)
                cv2.imwrite(target+"Gaussian_Filter"+ftype, GN_img_gf)
                cv2.imwrite(target+"Median_Filter"+ftype, GN_img_mf)
        for blks in BLKS:
            for whts in WHTS:
                SP_img = image.copy()
                for i in range(int(SP_img.shape[0]*SP_img.shape[1]*blks)):
                    rows = np.random.randint(0, SP_img.shape[0])
                    cols = np.random.randint(0, SP_img.shape[1])
                    SP_img[rows, cols] = 0
                for i in range(int(SP_img.shape[0]*SP_img.shape[1]*whts)):
                    rows = np.random.randint(0, SP_img.shape[0])
                    cols = np.random.randint(0, SP_img.shape[1])
                    SP_img[rows, cols] = 255
                SP_img_bf = cv2.blur(SP_img, (3,3))
                SP_img_gf = cv2.GaussianBlur(SP_img, (3,3), 1.5)
                SP_img_mf = cv2.medianBlur(SP_img, 3)
                target = ("./Exercise3_Output/"+sys.argv[1].rstrip(ftype)+
                          "/Salt_and_Pepper/K"+str(kernal)+"_B"+
                          str(int(100*blks))+"_W"+str(int(100*whts))+"/"
                )
                if not os.path.exists(target):
                    os.makedirs(target)
                cv2.imwrite(target+"Noise"+ftype, SP_img)
                cv2.imwrite(target+"Box_Filter"+ftype, SP_img_bf)
                cv2.imwrite(target+"Gaussian_Filter"+ftype, SP_img_gf)
                cv2.imwrite(target+"Median_Filter"+ftype, SP_img_mf)

if __name__ == "__main__":
    main()