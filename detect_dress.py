import Algorithmia
import urllib, cStringIO
from PIL import Image
import base64

#provide image path as an input 
img = Image.open('/Users/rashmisahu/Desktop/rashmi/internship/4.jpg')

#provide image path as an input 
#convert it into base 64 

image = base64.b64encode( open( "/Users/rashmisahu/Desktop/rashmi/internship/4.jpg", "rb").read())
input = {"image": 'data:image/jpg;base64,' + image.decode('ascii')}

client = Algorithmia.client('simb+HoZt1y2rsh4qvaHZ4pGbdy1')
algo = client.algo('algorithmiahq/DeepFashion/1.2.2')

#here c contains type of dress and its boundind box in a list of dictionaries
c=(algo.pipe(input).result)
#print c

b= c['articles']
print b

len1=len(b)

for i in range(0,len1):
	print b[i]['bounding_box']
	x=b[i]['bounding_box']
	img1=img.crop((x['x0'],x['y0'],x['x1'],x['y1']))
	img1.show()
	#break;



