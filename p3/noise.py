import numpy as np
import sys
import cv2

ftype = ".png"
path = 'result/'

kernels = [3, 5, 7]
means = [0, 50, 10, 20]
sigmas = [0, 20, 50, 100]
pa_values = [0.01, 0.03, 0.05, 0.4]
pb_values = [0.01, 0.03, 0.05, 0.4]



def main():
    if len(sys.argv) < 2:
        exit(1)
    image = cv2.imread(sys.argv[1])
    for kernal in kernels:
        for mean in means:
            for sigma in sigmas:  

                # add noise      
                noise = image.copy()
                cv2.randn(noise, mean, sigma)
                noise_image = np.add(image, noise)

                # generate images
                blur_image = cv2.blur(noise_image, (kernal, kernal))
                gaussian_image = cv2.GaussianBlur(noise_image, (kernal, kernal), 1.5)
                median_image = cv2.medianBlur(noise_image, kernal)

                # save images
                cv2.imwrite("{}Noise_s{}_m{}_k{}{}".format(path, sigma, mean, kernal, ftype), noise_image)
                cv2.imwrite("{}Box_Filter_s{}_m{}_k{}{}".format(path, sigma, mean, kernal, ftype), blur_image)
                cv2.imwrite("{}Gaussian_Filter_s{}_m{}_k{}{}".format(path, sigma, mean, kernal, ftype), gaussian_image)
                cv2.imwrite("{}Median_Filter_s{}_m{}_k{}{}".format(path, sigma, mean, kernal, ftype), median_image)
        for pa in pa_values:
            for pb in pb_values:

                # add noise
                noise = image.copy()
                for i in range(int(noise.shape[0]*noise.shape[1]*pa)):
                    noise[np.random.randint(0, noise.shape[0]), np.random.randint(0, noise.shape[1])] = 0
                for i in range(int(noise.shape[0]*noise.shape[1]*pb)):
                    noise[np.random.randint(0, noise.shape[0]), np.random.randint(0, noise.shape[1])] = 255

                # generate images
                blur_image = cv2.blur(noise, (kernal, kernal))
                gaussian_image = cv2.GaussianBlur(noise, (kernal, kernal), 1.5)
                median_image = cv2.medianBlur(noise, kernal)

                # save images
                cv2.imwrite("{}Noise_pa{}_pb{}_k{}{}".format(path, pa, pb, kernal, ftype), noise)
                cv2.imwrite("{}Box_Filter_pa{}_pb{}_k{}{}".format(path, pa, pb, kernal, ftype), blur_image)
                cv2.imwrite("{}Gaussian_Filter_pa{}_pb{}_k{}{}".format(path, pa, pb, kernal, ftype), gaussian_image)
                cv2.imwrite("{}Median_Filter_pa{}_pb{}_k{}{}".format(path, pa, pb, kernal, ftype), median_image)

if __name__ == "__main__":
    main()