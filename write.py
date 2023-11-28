from PIL import Image


def write():

    file = input("Enter File name:  ")
    img = Image.open(file)

    msg = input("enter msg:  ")
  
    # img.show()

    if img.mode != 'RGBA':
        img = img.convert('RGBA')
  
    width, height = img.size
    i = 0;j = 1
  
    p = img.getpixel((0,0))

    alpha  = 255-len(msg)
    img.putpixel((0,0),(p[0],p[1],p[2],alpha))
   
   
    for c in msg:
        p = img.getpixel((j,i))
        img.putpixel((j,i),(p[0],p[1],p[2],255-ord(c)))
        if(j<width): j+=1
        else: 
            i+=1
            j=0
   
    # img.show()
    img.save("file2.png")


