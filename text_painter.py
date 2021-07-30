from PIL import Image
def text_split(x,y=79):
    n1 = x
    n = int(y)
    return [n1[i:i+n] for i in range(0, len(n1), n)] 
img = Image.open(str(input()))
res=''
(size_x,size_y)=img.size
print(f'Размер изображения: {size_x}X{size_y}')
for i in range(int(size_y)):
	for n in range(int(size_x)):
		pix=img.getpixel((n,i))	
		if pix==(0,0,0):
			res=f"{res}1"
		else:
			res=f"{res}0"
result=text_split(res,int(size_x))
result='\n'.join(result).replace('0',' ').replace('1','█')
print(result)






