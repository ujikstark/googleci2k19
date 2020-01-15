from PIL import Image
import os, sys

os.chdir(os.path.expanduser("~"))

file_image = input("Image : ") #input user
print("You can type Quality from 1-100")
quality = int(input("Quality : "))

for i in os.listdir(file_image):
	pic = Image.open(os.path.join(file_image, i)) #open file


def new_file(dir1): #make a dir
    try:
        if not os.path.exists(dir1):
            os.makedirs(dir1)
    except OSError:
        print('Error: Creating Directory. ' +  dir1)

 
list_dir = os.listdir(file_image)
wanna_size = 400

def start():
	global pic
	for i in list_dir:
		if os.path.isfile(file_image+i):
			pic = Image.open(file_image+i)
			x, y = os.path.splitext(file_image + 'result/' + i)
			size = pic.size	
			ratio = float(wanna_size) / max(size)
			round_image= tuple([int(wanna_size) for a in size])
			pic = pic.resize(round_image, Image.ANTIALIAS)
			result = Image.new("RGB", (wanna_size, wanna_size))
			result.paste(pic, ((wanna_size - round_image[0]) // 2, (wanna_size - round_image[1]) // 2))	
			show = result.save(x + 'ujik.jpg', quality=quality)
			print("Success!!" , x + 'ujik.jpg')

new_file(file_image + '/result/')
start()
