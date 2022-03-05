
import cv2 , numpy as np
from init import Effects

Vfx = Effects()

def visualEffects (img_src : str , img_dst : str , effects : str) -> None :

    img = cv2.imread(img_src,1)
    arr = np.asarray(img)
    img = Vfx.Make(arr,effects)
    cv2.imshow("Cute Kitens", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
