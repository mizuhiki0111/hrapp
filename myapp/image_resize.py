import cv2
def return_resize_image(img,height,width):
    if height > 400 or width >400:
        if height == width:
            print("高さと横幅は一緒です")
            h_resize = 400 / height
            w_resize = 400 / width
            img = cv2.resize(img , (int(width*w_resize), int(height*h_resize)))
            return img


        elif height > width:
            print("高さがオーバーしています")
            h_resize = 400 / height
            img = cv2.resize(img , (int(width*h_resize), int(height*h_resize)))
            return img


        elif width >height:
            print("横幅がオーバーしています")
            w_resize = 400 / width
            img = cv2.resize(img , (int(width*w_resize), int(height*w_resize)))
            return img

    else:
        return img
