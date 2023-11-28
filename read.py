from PIL import Image

def read():
    file = input("Enter file name to read")
    img = Image.open(file)
    # img.show()

    if img.mode != 'RGBA':
        print("hlel")
        img = img.convert('RGBA')

    width, height = img.size
    i = 0
    j = 1

    p = abs(img.getpixel((0,0))[3] - 255)
    print(p)
    for c in range(p):
        p = chr(abs(img.getpixel((j,i))[3] - 255))
        print(p,end="")
        if(j<width): j+=1
        else: 
            i+=1
            j=0

