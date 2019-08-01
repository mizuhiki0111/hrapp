from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from .main import evaluate
from PIL import Image
import cv2
from .image_resize import return_resize_image
import uuid


def index(request):
    if request.method == 'GET':
        return render(request, 'myapp/index.html', {'form': PhotoForm(),})

    elif request.method == 'POST':
        #uploadfile = request.FILES.get("uploadfile")
        #uploadfile = Image.open(uploadfile)
        #form = PhotoForm(request.POST, request.FILES["uploadfile"])
        #if not form.is_valid():
    #        raise ValueError('invalid form')
        try:
            photo = Photo()
            photo.image = request.FILES.get("uploadfile")
            photo.save()
            input_photo = photo.return_photo()
            img = cv2.imread("./" + input_photo)
            height = img.shape[0]
            width = img.shape[1]
        except:
            return render(request, 'myapp/error.html')

        else:
            resized_img = return_resize_image(img,height,width)
            ustr = str(uuid.uuid4())
            resized_path = "media/resized/" + ustr + ".png"
            cv2.imwrite(resized_path, resized_img)
            result = evaluate(resized_path)


            params = {
            "input":"../" + resized_path,
            "result": "../media/result/" + result + ".png",
            }
            return render(request, 'myapp/result.html', params)


def about(request):
    return render(request,"myapp/about.html")
