from PIL import Image
import sys
import cv2 
import pytesseract

def create_name(nr):
 name='pixelss'
 name+=str(nr)
 return name


def binaryToDecimal(binary):
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal  


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


#pentru primul plan
def pixelss1(numar):
 x=''
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 x+=numar[0]
 x+='0000000'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))


def pixelss2(numar):
 x='0'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if(len(numar)>1):
  x+=numar[1]
 x+='000000'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))



def pixelss3(numar):
 x='00'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if(len(numar)>2):
  x+=numar[2]
 x+='00000'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))






def pixelss4(numar):
 x='000'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if (len(numar)>4):
  x+=numar[4]
 else:
  x+='0'
 x+='0000'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))




def pixelss5(numar):
 x='0000'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if(len(numar)>4):
  x+=numar[4]
 x+='000'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))





def pixelss6(numar):
 x='00000'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if(len(numar)>5):
  x+=numar[5]
 x+='00'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))




def pixelss7(numar):
 x='000000'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if (len(numar)>6):
  x+=numar[6]
 else:
  x+='0'
 x+='0'
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))



def pixelss8(numar):
 x='0000000'
 numar=bin(numar)
 numar=numar[2:]
 numar=str(numar)
 if (len(numar)>7):
  x+=numar[7]
 if(x == '00000000'):
  return 255-binaryToDecimal(int(x))
 else:
  return binaryToDecimal(int(x))







def main():
 r,g,b=0,0,0
 red,green,blue=0,0,0
 ok=0
 text=0
 poza=''
 out=' '
 for i in range(len(sys.argv)):
  if sys.argv[i] == "r":
   red=1
  if sys.argv[i] == "g":
   green=1
  if sys.argv[i] == "b":
   blue=1
  if sys.argv[i] == "--name":
   poza=sys.argv[i+1]
  if sys.argv[i] == "--text":
   text=1
  if sys.argv[i] == "--out":
   out=sys.argv[i+1]
 im = Image.open(poza)
 pixelMap = im.load()

 lst=[]
 name=''
 name=create_name(sys.argv[1])
 img = Image.new(im.mode, im.size)
 pix=img.load()
 pixelsNew = im.load()
 for i in range(img.size[1]):
     for j in range(img.size[0]):
       if red==1:
        r=globals()[name](pixelMap[j,i][0])
       if green==1:
        g=globals()[name](pixelMap[j,i][1])
       if blue==1:
        b=globals()[name](pixelMap[j,i][2])
        pix=(r,g,b)
        lst.append(pix)
 img.putdata(lst)
 if out =='':
  img.save('solve.bmp')
 else:
  img.save(out)
 if text==1:
  custom_config = r'--oem 3 --psm 6'
  string=pytesseract.image_to_string(img, config=custom_config)
  print string

if __name__ == "__main__":
    main()
        
