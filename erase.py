#Filtering man out of image
#Chris Webb

from PIL import Image
import glob

#Opening all the image files
image_files = []

for image in glob.glob('/Users/webbontheweb/Documents/Work/Projects/Python-Multimedia-Multimadness/Erasing-Man/images/*.png'):
    image_files.append(Image.open(image))

#finding height and width
max_height = 0
max_width = 0

for i in range (len(image_files)):
    if max_height < image_files[i].height:
        max_height = image_files[i].height
    if max_width < image_files[i].width:
        max_width = image_files[i].width

newImage = Image.new('RGB', (max_width, max_height))

#Creating a list to store the pixels for this value across the images
pixelList = []

for x in range (max_width):
    for y in range (max_height):
        for i in range (len(image_files)):
            pixelList.append(image_files[i].getpixel((x,y)))

        pixelList.sort()

        #Setting the new pixel as the median of this list
        newPixel = pixelList[round(len(image_files)/2)]
        pixelList.clear()

        #Setting pixel in new image to median
        newImage.putpixel((x,y), newPixel)

print("done")
newImage.show()



        


    
