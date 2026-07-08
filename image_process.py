import cv2
import numpy as np

def preprocess_img(img, target_size=(640,640)):
    h,w = img.shape[:2]
    scale = min(target_size[0]/w, target_size[1]/h)
    new_w, new_h = int(w*scale), int(h*scale)
    img_resize = cv2.resize(img, (new_w, new_h))
    pad_img = np.zeros((target_size[0], target_size[1],3), dtype=np.uint8)
    pad_img[:new_h, :new_w, :] = img_resize
    img_norm = pad_img / 255.0
    return img_norm, scale

def draw_detect_box(img, bbox, label, score):
    x1,y1,x2,y2 = map(int, bbox)
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    text = f"{label}:{score:.2f}"
    cv2.putText(img, text, (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    return img