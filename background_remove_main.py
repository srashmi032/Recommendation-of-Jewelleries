"""Script to call the background-removal API with an image.

USAGE: python test.py static/bird.jpg
"""
import firefly
import sys
import shutil
from PIL import Image
import Image
import base64
import json
import roro

# background_removal = firefly.Client("https://background-removal.rorocloud.io/")
background_removal = roro.Client("https://background-removal.rorocloud.io/")

def main():
    image_path = sys.argv[1]
    print "arg: ", str(sys.argv)
    # image_path = 'back.png'
    formati = image_path.split(".")[-1]

    print("calling the background removal API...")
    img=Image.open(image_path)
    # img.show()
    # img_file = request.session.get(image_path)
    # with open(img_file , "wb") as fh:
    #     fh.write(base64.decodebytes(img_data))
    # json.dumps(str(image_path)) 
    with open(image_path,'rb') as imageFile:
        st= base64.b64encode(imageFile.read())
        #print st

    
    new_image = background_removal.predict(image=open(image_path,'rb'), format=formati)
    #with open(new_image,'rb') as image_file:
        #= base64.b64encode(imageFile.read())
        #print st


    # img = Image.open(image_path , 'rb')
    # new_image = background_removal.predict(image_file= open(image_path, 'rb'))

    ## To open Image using PIL
    # from PIL import Image
    # img = Image.open(new_image)
    #fh = open("output.png" , "wb")
    #fh.write(st.decode('base64'))
    #fh.close()

    with open("output.png", "wb") as f:
         shutil.copyfileobj(im, f)
    print("saved the output image in output.jpg")

if __name__ == '__main__':
    main()
