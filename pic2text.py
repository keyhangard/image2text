from PIL import Image
from pytesseract import *


#read image
img = Image.open("your image path")

#image to str
Output = pytesseract.image_to_string(img)

#split numbers
#Output = Output.split(',')


# print (Output[0])
# print (Output[1])
print(Output)
