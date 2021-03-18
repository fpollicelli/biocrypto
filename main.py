import fingerprint_feature_extractor as ext
import fingerprint_enhancer as enh
import cv2
from random import randint

def T_generator(img):
    X = []
    Y = []
    R = []
    T = []
    enhanced_img = enh.enhance_Fingerprint(img)
    features_terminations, features_bifurcations = ext.extract_minutiae_features(enhanced_img, showResult=False)
    for termination in features_terminations:
        X.append(termination.locX)
        Y.append(termination.locY)
    for bifurcation in features_bifurcations:
        X.append(bifurcation.locX)
        Y.append(bifurcation.locY)
    n = len(Y)

    for i in range(0, 64):
        R.append(randint(0, 2 * (n-1)))
    for r in R:
        if r < n:
            T.append((X[r] % 256)-128)
        else:
            T.append((Y[r-n] % 256)-128)
    return T

if __name__ == '__main__':
    img_folder = 'C:\\Users\\Routi\\Desktop\\'
    img_1 = cv2.imread(img_folder+'002_4_5.png', 0)
    img_2 = cv2.imread(img_folder+'002_4_5.png', 0)

    T_1 = T_generator(img_1)
    T_2 = T_generator(img_2)
    TC = T_1 + T_2
    key = []
    for t in TC:
        if t >= 0:
            key.append(1)
        else:
            key.append(0)
    print(key)


