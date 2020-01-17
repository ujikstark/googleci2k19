from PIL import Image
import os, sys
from termcolor import colored

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
new_file(file_image + '/result/')

def start():
	global pic
	for i in list_dir:
		if os.path.isfile(file_image+i):
			#open file
			pic = Image.open(file_image+i)
			x, y = os.path.splitext(file_image + 'result/' + i)

			
			size = pic.size
			#set the pixel and save				
			if size[0] > size[1]:
				print(colored("Horizontal","blue"))
				wei_ave = (wanna_size / float(size[0]))
				hei_size = int((float(pic.size[1]) * float(wei_ave)))
				ratio = float(wanna_size) / max(size)
				round_image= tuple([int(wanna_size) for a in size])
					
				pic = pic.resize((wanna_size, hei_size), Image.ANTIALIAS)
				result = Image.new("RGB", (wanna_size, hei_size))
				result.paste(pic, ((wanna_size - round_image[0]) // 2, (wanna_size - round_image[1]) // 2))	
				show = result.save(x + 'ujik.jpg', quality=quality)
				print(colored(f"Success!! {x+'ujik.jpg'}","green"))
			else:
				print(colored("Vertical","blue"))
				hei_ave = (wanna_size / float(size[1]))
				wei_size = int((float(pic.size[0]) * float(hei_ave)))
				ratio = float(wanna_size) / max(size)
				
				round_image= tuple([int(wanna_size) for a in size])
				pic = pic.resize((wei_size, wanna_size), Image.ANTIALIAS)
				result = Image.new("RGB", (wei_size, wanna_size))
				
				result.paste(pic, ((wanna_size - round_image[0]) // 2, (wanna_size - round_image[1]) // 2))	
				show = result.save(x + 'ujik.jpg', quality=quality)
				print(colored(f"Success!! {x+'ujik.jpg'}","green"))

if __name__ == "__main__":
	start()

