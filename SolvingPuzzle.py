from PIL import Image, ImageDraw
import math

theBits = []
oneArr = []
imgArr = []

def binToDec(*arr):
    catStr = ''
    arr = arr[0]
#    print(arr)
    for i in arr:
        catStr += str(i)
    
#    print(catStr)
    return int(catStr,2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def leftRotate(arr, mv, n):
    for i in range(gcd(mv,n)):
        temp = arr[i]
        j = i
        while 1:
            nxt = j + mv
            if nxt >= n:
                nxt = nxt - n
            if nxt == i:
                break
            arr[j] = arr[nxt]
            j = nxt
        arr[j] = temp 

def getFrameBits():
    for idx in range(0, 35):
        filename = "/home/csc15s/Documents/output-%02d.png" % idx
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        width, height = img.size
        midx = width / 2
        midy = height / 2
        
        imgArr = []
    
        for num in range(8):
            check = None
            if idx >= 9 and idx < 21:
                degree = num * 45 + 44
            elif idx >= 20:
                degree = num * 45 + 10
            else:
                degree = num * 45 + 24
            radian = math.radians(degree)
            x = midx + 300.1562 * math.sin(radian)
            y = midy + 300.1562 * math.cos(radian)
            
            for i in range(int(x-46), int(x+50)):
                for j in range(int(y-51), int(y+52)):
                    pixVal = img.getpixel((i,j))
                    if (check == None and pixVal == (0,0,255)):
                        imgArr.append(1)
                        check = True
      
            draw.rectangle((x-46, y-51, x+50, y+52), fill=(0, 0, 0))
     
            if check == None:
                imgArr.append(0)
    
        img.save("newframes-%d.png" % idx)              
                      
        theBits.append(imgArr)
#        print(imgArr)
        imgArr.reverse()
#        print(imgArr)
        if idx <= 20:
            leftRotate(imgArr, 3, 8)
        else:
            leftRotate(imgArr, 2, 8)

        print(imgArr)
        for elmt in imgArr:
            oneArr.append(elmt)

# code to extract frames and reset RGB colors in 35 frames
def extractColor():
    img_file = Image.open("redacted-puzzle.gif")

    string = 'frame'
    for idx in range(35):
	    img_file.seek(idx)
	    img_file.save('%s-%d.png' % (string, idx), 'PNG')

    for frame in range(0, img_file.n_frames):
        img_file.seek(frame)
        img_file.putpalette([255, 0, 0, 0, 255, 0, 0, 0, 255])
        new_img = img_file.convert('RGB')
        new_img.save("frame-%d.png" % frame)

extractColor() 
flag_alphabet = "+-=ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}" #32 chars
getFrameBits()
#print(theBits)

msg = ''
for num in range(0, len(oneArr), 5):
    arrFive = []

    for idx in range(5, 0, -1):
        arrFive.append(oneArr[num - idx])
#    print(arrFive)

    index = binToDec(arrFive)
    msg += flag_alphabet[index]

lastChar = msg[0]
msg = msg[1:] + lastChar
print(msg)    

