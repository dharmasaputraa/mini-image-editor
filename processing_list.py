# github.com/dharmasaputraa

from PIL import Image, ImageOps
import math

def ImgNegative(img, coldepth):
  if coldepth!=24:
    img = img.convert('RGB')
  
  # solusi 1
  # img_output = ImageOps.invert(img_input)
  
  # solusi 2
  width, height = img.size
  img_output = Image.new('RGB', (width, height))
  
  for i in range(width):
    for j in range(height):
      r, g, b = img.getpixel((i, j))
      img_output.putpixel((i, j), (255 - r, 255 - g, 255 - b))
      
  return img_output

def ImgGrayscale(img_input,coldepth):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
        
  img_output = Image.new('L',(img_input.size[0],img_input.size[1]))
  pixel = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i, j))
      value = int((r + g + b) / 3)
      # value = int((r * 0.299) + (g * 0.587) + (b * 0.114))
      pixel[i, j] = value
  return img_output

def ImgThreshold(img_input,coldepth,thrVal):
  if coldepth!=24:
    img_input = img_input.convert('RGB')

  img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
  pixels = img_output.load()
  oldPixels = img_input.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      if oldPixels[i,j] < (thrVal, thrVal, thrVal):
        pixels[i,j] = (0, 0, 0)
      elif oldPixels[i,j] >= (thrVal, thrVal, thrVal):
        pixels[i,j] = (255, 255, 255)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def ImgPLusMinus(img_input,coldepth, constant):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i, j))
      # operasi penjumlahan di mulai
      red = r + constant
      green = g + constant
      blue = b + constant
      # Teknik Clipping agar range tidak lewat dari 255
      if(red > 255):
          red = 255
      if(green > 255):
          green = 255
      if(blue > 255):
          blue = 255
      if(red < 0):
            red = 0
      if(green < 0):
          green = 0
      if(blue < 0):
          blue = 0
      pixels[i,j] = (red,green,blue) #gambar telah di oprasikan

  return img_output 

def ImgDiv(img_input,coldepth,constant):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
        
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      # oprasi pembagian di mulai
      r, g, b = img_input.getpixel((i, j))
      red = r / constant
      green = g / constant
      blue = b / constant

      # Teknik Clipping agar range tidak kurang dari 0 atau lebih dari 255
      if(red > 255):
          red = 255
      if(green > 255):
          green = 255
      if(blue > 255):
          blue = 255
      if(red < 0):
          red = 0
      if(green < 0):
          green = 0
      if(blue < 0):
          blue = 0
      pixels[i,j] = (int(red),int(green),int(blue))
  
  return img_output

def ImgMulti(img_input,coldepth,constant):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
        
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      # oprasi perkalian di mulai
      r, g, b = img_input.getpixel((i, j))
      red = r * constant
      green = g * constant
      blue = b * constant

      # Teknik Clipping agar range tidak kurang dari 0 atau lebih dari 255
      if(red > 255):
          red = 255
      if(green > 255):
          green = 255
      if(blue > 255):
          blue = 255
      if(red < 0):
          red = 0
      if(green < 0):
          green = 0
      if(blue < 0):
          blue = 0
      pixels[i,j] = (int(red),int(green),int(blue))
  
  return img_output

def ImgLogaritma (img_input, coldepth, constant):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      # oprasi perkalian di mulai
      r, g, b = img_input.getpixel((i, j))
      red = constant * math.log(1 + r)
      green = constant * math.log(1 + g)
      blue = constant * math.log(1 + b)

      # Teknik Clipping agar range tidak kurang dari 0 atau lebih dari 255
      if(red > 255):
          red = 255
      if(green > 255):
          green = 255
      if(blue > 255):
          blue = 255
      if(red < 0):
          red = 0
      if(green < 0):
          green = 0
      if(blue < 0):
          blue = 0
          
      pixels[i,j] = (int(red), int(green), int(blue))
  
  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
        
        
  return img_output

def ImgGamma(img_input,coldepth,constant):
    
  if coldepth!=24:
    img_input = img_input.convert('RGB')
        
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      # oprasi Power Low Transform di mulai
      r, g, b = img_input.getpixel((i, j))
      red = constant * pow(r, math.gamma(1))
      green = constant * pow(g, math.gamma(1))
      blue = constant * pow(b, math.gamma(1))

      # Teknik Clipping agar range tidak kurang dari 0 atau lebih dari 255
      if(red > 255):
        red = 255
      if(green > 255):
        green = 255
      if(blue > 255):
        blue = 255
      if(red < 0):
        red = 0
      if(green < 0):
        green = 0
      if(blue < 0):
        blue = 0
                
      pixels[i,j] = (int(red),int(green),int(blue))
            
  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
        
  return img_output

# github.com/dharmasaputraa

def ImgFlipHorizontal(img_input,coldepth):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i,(img_output.size[1]-1)-j))
            
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    mg_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgFlipVertical(img_input,coldepth):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel(((img_output.size[0]-1)-i,j))
        
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgRotate(img_input,coldepth,deg,direction):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  
  img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
  
  print(str(img_input.size[1]) + " x " + str(img_input.size[0]))
  
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      if direction=="C":
        if deg == 90:
          r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
        if deg == 180:
          r, g, b = img_input.getpixel((img_input.size[1]-i-1,img_output.size[0]-j-1))
        if deg == 270:
          r, g, b = img_input.getpixel((img_input.size[1]-j-1,i))
      else:
        if deg == 90:
          r, g, b = img_input.getpixel((img_input.size[1]-j-1,i))
        if deg == 180:
          r, g, b = img_input.getpixel((img_input.size[1]-i-1,img_output.size[0]-j-1))
        if deg == 270:
          r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
      
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgFlipHorizontal(img_input,coldepth):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i,(img_output.size[1]-1)-j))
            
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgFlipVertical(img_input,coldepth):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel(((img_output.size[0]-1)-i,j))
            
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgFlipHorizontalAndVertical(img_input,coldepth):
  #solusi 1
  #img_output=img_input.rotate(deg)

  #solusi 2
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel(((img_output.size[0]-1)-i,(img_output.size[1]-1)-j))
            
      pixels[i,j] = (r, g, b)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def ImgTranslation(img_input, coldepth, xVal, yVal):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  direction = "xy"
  n = None
  if yVal == 0:
    direction = "x"
    n = xVal
  elif xVal == 0:
    direction = "y"
    n = yVal
    
  img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
  pixels = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      if direction == "y":
        if j <= n:
          r, g, b = (0, 0, 0)
        else:
          r, g, b = img_input.getpixel((i, j - n))
      elif direction == "x":
        if i <= n:
          r, g, b = (0, 0, 0)
        else:
          r, g, b = img_input.getpixel((i - n, j))
      elif direction == "xy":
        if j <= yVal or i <= xVal:
          r, g, b = (0, 0, 0)
        else:
          r, g, b = img_input.getpixel((i - xVal, j - yVal))
      pixels[i,j] = (r, g, b) 

  if coldepth ==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output 

def ZoomIn(img_input, coldepth, scaleVal):
  if coldepth != 24:
    img_input.convert('RGB')
    
  row = img_input.size[0] * scaleVal
  col = img_input.size[1] * scaleVal
  img_output = Image.new('RGB', (row, col))
  pixel = img_output.load()

  for i in range(row-1):
    for j in range(col-1):
      r, g, b = img_input.getpixel((int(i/scaleVal), int(j/scaleVal)))  
      pixel[i, j] = (r, g, b)   

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
                
  return img_output      
    
def ZoomOut(img_input, coldepth, scaleVal):
  if coldepth != 24:
    img_input.convert('RGB')
    
  print(scaleVal)
  row = int(img_input.size[0]/scaleVal)
  col = int(img_input.size[1]/scaleVal)
  img_output = Image.new('RGB', (row, col))
  pixel = img_output.load()
  print(row)
  print(col)
  
  for i in range(row-1):
    for j in range(col-1):
      r, g, b = img_input.getpixel((int(i * scaleVal), int(j * scaleVal)))  
      pixel[i, j] = (r, g, b)      

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output   

def ImgBlend(img_input, coldepth, img_input2, coldepth2, alpha1, alpha2, posX, posY):
  
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  if coldepth2!=24:
    img_input2 = img_input2.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixels = img_output.load()
  
  # Perulangan untuk menumpuk image_input/image1 pada image_output/image baru
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i, j))
      pixels[i, j] = (r, g, b)
  
  # Perulangan untuk menumpuk image_negatif pada image_output/image baru
  for i in range(img_input2.size[0]):
    for j in range(img_input2.size[1]):
      x = posX + i
      y = posY + j
      r1, g1, b1 = img_input2.getpixel((i, j))
      if x >= 0 and x < img_output.size[0] and y >= 0 and y < img_output.size[1]:
        r, g, b = pixels[x, y]
        r1 = int(r*alpha1) + int(r1*alpha2)
        g1 = int(g*alpha1) + int(g1*alpha2)
        b1 =  + int(b*alpha1) + int(b1*alpha2)
        pixels[x, y] = (r1, g1, b1)
  
  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output 

# UTS
def merge_flipped_images(img_original, coldepth):
    
  img_vertical = ImgFlipVertical(img_original, coldepth)
  img_horizontal = ImgFlipHorizontal(img_original, coldepth)
  img_horizontal_vertical = ImgFlipHorizontalAndVertical(img_original, coldepth)

  img_output = Image.new("RGB", (img_original.size[0] * 2, img_original.size[1] * 2))
  img_output.paste(img_original, (0, 0))
  img_output.paste(img_vertical, (img_original.size[0], 0))
  img_output.paste(img_horizontal, (0, img_original.size[1]))
  img_output.paste(img_horizontal_vertical, (img_original.size[0], img_original.size[1]))

  return img_output

def circular_negative(img_input, coldepth, whVal):
    
  if img_input.mode != 'RGB':
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB', img_input.size)
  pixels = img_output.load()

  # Define the center point of the image
  center_x = img_input.size[0] // 2
  center_y = img_input.size[1] // 2

  # radius = min(center_x, center_y) // 2
  if whVal == 0:
    radius = min(center_x, center_y) // 2
  else:
    radius = min(whVal, whVal)

  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      distance = ((i - center_x) ** 2 + (j - center_y) ** 2) ** 0.5

      if distance <= radius:
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def reverse_circular_negative(img_input, coldepth, whVal):
    
  if img_input.mode != 'RGB':
    img_input = img_input.convert('RGB')

  img_output = Image.new('RGB', img_input.size)
  pixels = img_output.load()
  
  center_x = img_input.size[0] // 2
  center_y = img_input.size[1] // 2

  # radius = min(center_x, center_y) // 2
  if whVal == 0:
    radius = min(center_x, center_y) // 2
  else:
    radius = min(whVal, whVal)
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      distance = ((i - center_x) ** 2 + (j - center_y) ** 2) ** 0.5

      if distance >= radius:
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def diamond_negative(img_input, coldepth, whVal):
  
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  if whVal == 0:
    width = img_input.size[0] // 2
    height = img_input.size[1] // 2

  img_output = Image.new('RGB', img_input.size)
  pixels = img_output.load()

  center_x = img_input.size[0] // 2
  center_y = img_input.size[1] // 2

  # width = img_input.size[0] // 2
  # height = img_input.size[1] // 2
  if whVal == 0:
    width = img_input.size[0] // 2
    height = img_input.size[1] // 2
  else:
    width = whVal // 2
    height = whVal // 2

  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      # Calculate distance from pixel to center
      x_diff = abs(i - center_x)
      y_diff = abs(j - center_y)

      if (x_diff / width) + (y_diff / height) <= 1:
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))
      

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def reverse_diamond_negative(img_input, coldepth, whVal):
    
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  img_output = Image.new('RGB', img_input.size)
  pixels = img_output.load()

  center_x = img_input.size[0] // 2
  center_y = img_input.size[1] // 2
  
  # width = img_input.size[0] // 2
  # height = img_input.size[1] // 2
  if whVal == 0:
    width = img_input.size[0] // 2
    height = img_input.size[1] // 2
  else:
    width = whVal // 2
    height = whVal // 2
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      # Calculate distance from pixel to center
      x_diff = abs(i - center_x)
      y_diff = abs(j - center_y)

      if (x_diff / width) + (y_diff / height) >= 1:
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))
      

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def x_simbol_negative(img_input, coldepth):
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
  pixels = img_output.load()

  center_x = img_output.size[0] // 2 # posisi x tengah berada pada 1/4 dari lebar gambar
  center_y = img_output.size[1] // 2 # posisi y tengah berada pada setengah tinggi gambar

  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      if (j >= center_y and i <= center_x + ((j - center_y) * (img_output.size[0] // 2) // center_y)
        and i >= center_x - ((j - center_y) * (img_output.size[0] // 2) // center_y)):
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      elif (j < center_y and i <= center_x + ((center_y - j) * (img_output.size[0] // 2) // center_y)
        and i >= center_x - ((center_y - j) * (img_output.size[0] // 2) // center_y)):
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def reverse_x_simbol_negative(img_input, coldepth):
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
  pixels = img_output.load()

  center_x = img_output.size[0] // 2 # posisi x tengah berada pada setengah dari lebar gambar
  center_y = img_output.size[1] // 2 # posisi y tengah berada pada setengah tinggi gambar

  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      if (i >= center_x and j <= center_y + ((i - center_x) * (img_output.size[1] // 2) // center_x)
        and j >= center_y - ((i - center_x) * (img_output.size[1] // 2) // center_x)):
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      elif (i < center_x and j <= center_y + ((center_x - i) * (img_output.size[1] // 2) // center_x)
        and j >= center_y - ((center_x - i) * (img_output.size[1] // 2) // center_x)):
        r, g, b = img_input.getpixel((i, j))
        pixels[i, j] = (255 - r, 255 - g, 255 - b)
      else:
        pixels[i, j] = img_input.getpixel((i, j))

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def uts_1(img_input, coldepth, img_input2, coldepth2, alpha1, alpha2):
  alpha1 = float(alpha1)
  alpha2 = float(alpha2)
        
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  elif coldepth2!=24:
    img_input2 = img_input2.convert('RGB')

  # Membuat image baru dengan size
  img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
  pixels = img_output.load()

  # Perulangan untuk menumpuk image_input/image1 pada image_output/image baru
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i, j))
      pixels[i, j] = (r, g, b)

  # Membuat image2 menjadi negatif
  img_negatived = ImgNegative(img_input2, coldepth2)

  # Mencari titik tengah pada image2 negatif
  center_x = (img_output.size[0] - img_negatived.size[0]) // 2 # posisi x tengah berada pada 1/4 dari lebar gambar
  center_y = (img_output.size[1] - img_negatived.size[1]) // 2 # posisi y tengah berada pada setengah tinggi gambar
  
  img_output = ImgBlend(img_output, coldepth, img_input2, img_negatived, alpha1, alpha2, center_x, center_y)

  return img_output

def bubble_sort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

# Non Linear Filter
def Max_Filter(img_input, coldepth):
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  row = int(img_input.size[0])
  col = int(img_input.size[1])
    
  img_output = Image.new('RGB', (row, col))
    
  # memberi border (alternatif)
  # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
  # github.com/dharmasaputraa
  # sulusi memberi border 2
  img_bordered = Image.new('RGB', (row + 2, col + 2))
  pixels = img_bordered.load()
  pixels_input = img_input.load()
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      x = 1 + i
      y = 1 + j
      r1, g1, b1 = pixels_input[i,j]
      if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
        r, g, b = pixels[x, y]
        pixels[x, y] = (r1, g1, b1)
  
  # img_bordered.show()
  
  pixels = img_output.load()
    
  mask = [(0,0)] * 9

  for i in range(1, row + 1):
    for j in range(1, col + 1):
      mask[0] = img_bordered.getpixel((i-1,j-1))
      mask[1] = img_bordered.getpixel((i-1,j))
      mask[2] = img_bordered.getpixel((i-1,j+1))
      mask[3] = img_bordered.getpixel((i,j-1))
      mask[4] = img_bordered.getpixel((i,j))
      mask[5] = img_bordered.getpixel((i,j+1))
      mask[6] = img_bordered.getpixel((i+1,j-1))
      mask[7] = img_bordered.getpixel((i+1,j))
      mask[8] = img_bordered.getpixel((i+1,j+1))
      # alternatif
      # mask.sort()
      
      array = bubble_sort(mask)

      img_output.putpixel((i - 1, j - 1),(mask[8]))
      
  return img_output

def Min_Filter(img_input, coldepth):
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  row = int(img_input.size[0])
  col = int(img_input.size[1])
    
  img_output = Image.new('RGB', (row, col))
    
  # memberi border (alternatif)
  # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
  # github.com/dharmasaputraa
  # sulusi memberi border 2
  img_bordered = Image.new('RGB', (row + 2, col + 2))
  pixels = img_bordered.load()
  pixels_input = img_input.load()
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      x = 1 + i
      y = 1 + j
      r1, g1, b1 = pixels_input[i,j]
      if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
        r, g, b = pixels[x, y]
        pixels[x, y] = (r1, g1, b1)
  
  # img_bordered.show()
  
  pixels = img_output.load()
    
  mask = [(0,0)] * 9

  for i in range(1, row + 1):
    for j in range(1, col + 1):
      mask[0] = img_bordered.getpixel((i-1,j-1))
      mask[1] = img_bordered.getpixel((i-1,j))
      mask[2] = img_bordered.getpixel((i-1,j+1))
      mask[3] = img_bordered.getpixel((i,j-1))
      mask[4] = img_bordered.getpixel((i,j))
      mask[5] = img_bordered.getpixel((i,j+1))
      mask[6] = img_bordered.getpixel((i+1,j-1))
      mask[7] = img_bordered.getpixel((i+1,j))
      mask[8] = img_bordered.getpixel((i+1,j+1))
      
      # alternatif
      # mask.sort()
      
      array = bubble_sort(mask)

      img_output.putpixel((i - 1, j - 1),(mask[0]))
      
  return img_output

def Median_Filter(img_input, coldepth):
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  
  row = int(img_input.size[0])
  col = int(img_input.size[1])
  
  img_output = Image.new('RGB', (row, col))
  
  # memberi padding (alternatif)
  # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
  # sulusi memberi border 2
  img_bordered = Image.new('RGB', (row + 2, col + 2))
  pixels = img_bordered.load()
  pixels_input = img_input.load()
  
  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      x = 1 + i
      y = 1 + j
      r1, g1, b1 = pixels_input[(i, j)]
      if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
        r, g, b = pixels[x, y]
        pixels[x, y] = (r1, g1, b1)
  
  print(row)
  print(col)
  
  print(img_bordered.size[0])
  print(img_bordered.size[1])
  
  mask = [(0,0)] * 9
  for i in range(1, row + 1):
    for j in range(1, col + 1):
      mask[0] = img_bordered.getpixel((i-1, j-1))
      mask[1] = img_bordered.getpixel((i-1, j))
      mask[2] = img_bordered.getpixel((i-1, j+1))
      mask[3] = img_bordered.getpixel((i, j-1))
      mask[4] = img_bordered.getpixel((i, j))
      mask[5] = img_bordered.getpixel((i, j+1))
      mask[6] = img_bordered.getpixel((i+1, j-1))
      mask[7] = img_bordered.getpixel((i+1, j))
      mask[8] = img_bordered.getpixel((i+1, j+1)) 
      
      # alternatif
      # mask.sort()
      
      array = bubble_sort(mask)

      img_output.putpixel((i - 1, j - 1),(mask[4]))
      
  return img_output

# Linar Filter
def Mean_Filter(img_input, coldepth):
  if coldepth != 24:
    img_input = img_input.convert('RGB')

  row = int(img_input.size[0])
  col = int(img_input.size[1])
    
  img_output = Image.new('RGB', (row, col))
    
  # memberi border (alternatif)
  # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
  # github.com/dharmasaputraa
  # sulusi memberi border 2
  img_bordered = Image.new('RGB', (row + 2, col + 2))
  pixels = img_bordered.load()
  pixels_input = img_input.load()
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      x = 1 + i
      y = 1 + j
      r1, g1, b1 = pixels_input[i,j]
      if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
        r, g, b = pixels[x, y]
        pixels[x, y] = (r1, g1, b1)
  
  # img_bordered.show()
  
  pixels = img_output.load()
    
  mask = [(0,0)] * 9

  for i in range(1, row + 1):
    for j in range(1, col + 1):
      red = 0
      green = 0
      blue = 0
      mask[0] = img_bordered.getpixel((i-1,j-1))
      mask[1] = img_bordered.getpixel((i-1,j))
      mask[2] = img_bordered.getpixel((i-1,j+1))
      mask[3] = img_bordered.getpixel((i,j-1))
      mask[4] = img_bordered.getpixel((i,j))
      mask[5] = img_bordered.getpixel((i,j+1))
      mask[6] = img_bordered.getpixel((i+1,j-1))
      mask[7] = img_bordered.getpixel((i+1,j))
      mask[8] = img_bordered.getpixel((i+1,j+1))
      
      for k in range(8):
        r, g, b = mask[k]
        red = red + r
        green = green + g
        blue = blue + b

      red = int(red * 1/9)
      green = int(green * 1/9)
      blue = int(blue * 1/9)

      pixels[i - 1,j - 1] = (red, green, blue)

  if coldepth==1:
    img_output = img_output.convert("1")
  elif coldepth==8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output  

def Robert_Edge(img_input, coldepth):
  img_input = img_input.convert('L')

  img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
  pixel = img_output.load()
  mask = [(0,0)] * 9
  mask2 = [(0,0)] * 9

  gX = [[1, 0], [0, -1]]
  gY = [[0, 1], [-1, 0]]

  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      valueX = 0
      valueY = 0
        
      # Gradient X
      valueX += img_input.getpixel((i, j)) * gX[0][0]
      valueX += img_input.getpixel((i+1, j+1)) * gX[1][1]
        
      # Gradient Y
      valueY += img_input.getpixel((i, j+1)) * gY[0][1]
      valueY += img_input.getpixel((i+1, j)) * gY[1][0]
        
      finalValue = abs(valueX) + abs(valueY)
        
      if finalValue > 255:
        finalValue = 255
        
      pixel[i, j] = finalValue
      
  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def Sobel_Edge(img_input, coldepth):
  img_input = img_input.convert('L')

  img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
  pixel = img_output.load()
  mask = [(0,0)] * 9
  mask2 = [(0,0)] * 9
  
  gX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
  gY = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
  
  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      valueX = 0
      valueY = 0
      finalValue = 0
        
      #for gradient X
      mask[0] = (img_input.getpixel((i-1, j-1)) * gX[0][0])
      mask[1] = (img_input.getpixel((i-1, j)) * gX[0][1])
      mask[2] = (img_input.getpixel((i-1, j+1)) * gX[0][2])
      mask[3] = (img_input.getpixel((i, j-1)) * gX[1][0])
      mask[4] = (img_input.getpixel((i, j)) * gX[1][1])
      mask[5] = (img_input.getpixel((i, j+1)) * gX[1][2])
      mask[6] = (img_input.getpixel((i+1, j-1)) * gX[2][0])
      mask[7] = (img_input.getpixel((i+1, j)) * gX[2][1])
      mask[8] = (img_input.getpixel((i+1, j+1)) * gX[2][2])
        
      #for gradient Y
      mask2[0] = (img_input.getpixel((i-1, j-1)) * gY[0][0])
      mask2[1] = (img_input.getpixel((i-1, j)) * gY[0][1])
      mask2[2] = (img_input.getpixel((i-1, j+1)) * gY[0][2])
      mask2[3] = (img_input.getpixel((i, j-1)) * gY[1][0])
      mask2[4] = (img_input.getpixel((i, j)) * gY[1][1])
      mask2[5] = (img_input.getpixel((i, j+1)) * gY[1][2])
      mask2[6] = (img_input.getpixel((i+1, j-1)) * gY[2][0])
      mask2[7] = (img_input.getpixel((i+1, j)) * gY[2][1])
      mask2[8] = (img_input.getpixel((i+1, j+1)) * gY[2][2])
                  
      for x in range(8):
        rgb = mask[x]
        valueX = valueX + rgb
          
      for y in range(8):
        rgb2 = mask2[y]
        valueY = valueY + rgb2
      finalValue = valueX + valueY

      if finalValue < 0: 
        finalValue = 0
      elif finalValue > 255:
        finalValue = 255
        
      pixel[i,j] = (finalValue)  

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def Prewitt_Edge(img_input, coldepth):
  img_input = img_input.convert('L')

  img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
  pixel = img_output.load()
  mask = [(0,0)] * 9
  mask2 = [(0,0)] * 9
  
  gX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
  gY = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
  
  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      valueX = 0
      valueY = 0
      finalValue = 0
        
      #for gradient X
      mask[0] = (img_input.getpixel((i-1, j-1)) * gX[0][0])
      mask[1] = (img_input.getpixel((i-1, j)) * gX[0][1])
      mask[2] = (img_input.getpixel((i-1, j+1)) * gX[0][2])
      mask[3] = (img_input.getpixel((i, j-1)) * gX[1][0])
      mask[4] = (img_input.getpixel((i, j)) * gX[1][1])
      mask[5] = (img_input.getpixel((i, j+1)) * gX[1][2])
      mask[6] = (img_input.getpixel((i+1, j-1)) * gX[2][0])
      mask[7] = (img_input.getpixel((i+1, j)) * gX[2][1])
      mask[8] = (img_input.getpixel((i+1, j+1)) * gX[2][2])
        
      #for gradient Y
      mask2[0] = (img_input.getpixel((i-1, j-1)) * gY[0][0])
      mask2[1] = (img_input.getpixel((i-1, j)) * gY[0][1])
      mask2[2] = (img_input.getpixel((i-1, j+1)) * gY[0][2])
      mask2[3] = (img_input.getpixel((i, j-1)) * gY[1][0])
      mask2[4] = (img_input.getpixel((i, j)) * gY[1][1])
      mask2[5] = (img_input.getpixel((i, j+1)) * gY[1][2])
      mask2[6] = (img_input.getpixel((i+1, j-1)) * gY[2][0])
      mask2[7] = (img_input.getpixel((i+1, j)) * gY[2][1])
      mask2[8] = (img_input.getpixel((i+1, j+1)) * gY[2][2])
                  
      for x in range(8):
        rgb = mask[x]
        valueX = valueX + rgb
          
      for y in range(8):
        rgb2 = mask2[y]
        valueY = valueY + rgb2
      finalValue = valueX + valueY

      if finalValue < 0: 
        finalValue = 0
      elif finalValue > 255:
        finalValue = 255
        
      pixel[i,j] = (finalValue)  

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def Laplacian_Edge(img_input, coldepth):
  img_input = img_input.convert('L')

  img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
  pixel = img_output.load()
  mask = [(0,0)] * 9
  mask2 = [(0,0)] * 9
  
  gX = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
  gY = [[-1, 2, -1], [2, -4, 2], [-1, 2, -1]]
  
  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      valueX = 0
      valueY = 0
      finalValue = 0
        
      #for gradient X
      mask[0] = (img_input.getpixel((i-1, j-1)) * gX[0][0])
      mask[1] = (img_input.getpixel((i-1, j)) * gX[0][1])
      mask[2] = (img_input.getpixel((i-1, j+1)) * gX[0][2])
      mask[3] = (img_input.getpixel((i, j-1)) * gX[1][0])
      mask[4] = (img_input.getpixel((i, j)) * gX[1][1])
      mask[5] = (img_input.getpixel((i, j+1)) * gX[1][2])
      mask[6] = (img_input.getpixel((i+1, j-1)) * gX[2][0])
      mask[7] = (img_input.getpixel((i+1, j)) * gX[2][1])
      mask[8] = (img_input.getpixel((i+1, j+1)) * gX[2][2])
        
      #for gradient Y
      mask2[0] = (img_input.getpixel((i-1, j-1)) * gY[0][0])
      mask2[1] = (img_input.getpixel((i-1, j)) * gY[0][1])
      mask2[2] = (img_input.getpixel((i-1, j+1)) * gY[0][2])
      mask2[3] = (img_input.getpixel((i, j-1)) * gY[1][0])
      mask2[4] = (img_input.getpixel((i, j)) * gY[1][1])
      mask2[5] = (img_input.getpixel((i, j+1)) * gY[1][2])
      mask2[6] = (img_input.getpixel((i+1, j-1)) * gY[2][0])
      mask2[7] = (img_input.getpixel((i+1, j)) * gY[2][1])
      mask2[8] = (img_input.getpixel((i+1, j+1)) * gY[2][2])
                  
      for x in range(8):
        rgb = mask[x]
        valueX = valueX + rgb
          
      for y in range(8):
        rgb2 = mask2[y]
        valueY = valueY + rgb2
      finalValue = valueX + valueY

      if finalValue < 0: 
        finalValue = 0
      elif finalValue > 255:
        finalValue = 255
        
      pixel[i,j] = (finalValue)  

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def Scharr_Edge(img_input, coldepth):
  img_input = img_input.convert('L')

  img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
  pixel = img_output.load()
  mask = [(0,0)] * 9
  mask2 = [(0,0)] * 9
  
  gX = [[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]]
  gY = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]
  
  for i in range(img_input.size[0] - 1):
    for j in range(img_input.size[1] - 1):
      valueX = 0
      valueY = 0
      finalValue = 0
        
      #for gradient X
      mask[0] = (img_input.getpixel((i-1, j-1)) * gX[0][0])
      mask[1] = (img_input.getpixel((i-1, j)) * gX[0][1])
      mask[2] = (img_input.getpixel((i-1, j+1)) * gX[0][2])
      mask[3] = (img_input.getpixel((i, j-1)) * gX[1][0])
      mask[4] = (img_input.getpixel((i, j)) * gX[1][1])
      mask[5] = (img_input.getpixel((i, j+1)) * gX[1][2])
      mask[6] = (img_input.getpixel((i+1, j-1)) * gX[2][0])
      mask[7] = (img_input.getpixel((i+1, j)) * gX[2][1])
      mask[8] = (img_input.getpixel((i+1, j+1)) * gX[2][2])
        
      #for gradient Y
      mask2[0] = (img_input.getpixel((i-1, j-1)) * gY[0][0])
      mask2[1] = (img_input.getpixel((i-1, j)) * gY[0][1])
      mask2[2] = (img_input.getpixel((i-1, j+1)) * gY[0][2])
      mask2[3] = (img_input.getpixel((i, j-1)) * gY[1][0])
      mask2[4] = (img_input.getpixel((i, j)) * gY[1][1])
      mask2[5] = (img_input.getpixel((i, j+1)) * gY[1][2])
      mask2[6] = (img_input.getpixel((i+1, j-1)) * gY[2][0])
      mask2[7] = (img_input.getpixel((i+1, j)) * gY[2][1])
      mask2[8] = (img_input.getpixel((i+1, j+1)) * gY[2][2])
                  
      for x in range(8):
        rgb = mask[x]
        valueX = valueX + rgb
          
      for y in range(8):
        rgb2 = mask2[y]
        valueY = valueY + rgb2
      finalValue = valueX + valueY

      if finalValue < 0: 
        finalValue = 0
      elif finalValue > 255:
        finalValue = 255
        
      pixel[i,j] = (finalValue)  

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")
    
  return img_output

def CompassOperator(img_input, coldepth):
    img_input = img_input.convert('L')

    img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
    pixel = img_output.load()

    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']  # Directions: North, Northeast, East, Southeast, South, Southwest, West, Northwest
    masks = {
        'N': [[-1, -1, -1], [2, 2, 2], [-1, -1, -1]],
        'NE': [[-1, -1, 2], [-1, 2, -1], [2, -1, -1]],
        'E': [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]],
        'SE': [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]],
        'S': [[-1, -1, -1], [2, 2, 2], [-1, -1, -1]],
        'SW': [[-1, -1, 2], [-1, 2, -1], [2, -1, -1]],
        'W': [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]],
        'NW': [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
    }

    for direction in directions:
        mask = masks[direction]

        for i in range(img_input.size[0] - 2):
            for j in range(img_input.size[1] - 2):
                value = 0

                for x in range(3):
                    for y in range(3):
                        value += img_input.getpixel((i + x, j + y)) * mask[x][y]

                value = abs(value)

                if value > 255:
                    value = 255

                pixel[i, j] = value

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def Gaussian(img_input, coldepth, sigma=1):
  if coldepth != 24:
    img_input = img_input.convert('RGB')
    
  row = int(img_input.size[0])
  col = int(img_input.size[1])
    
  img_output = Image.new('RGB', (row, col))
    
  # memberi border (alternatif)
  # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
  # sulusi memberi border 2
  img_bordered = Image.new('RGB', (row + 2, col + 2))
  pixels = img_bordered.load()
  
  for i in range(img_input.size[0]):
    for j in range(img_input.size[1]):
      x = 1 + i
      y = 1 + j
      r1, g1, b1 = img_input.getpixel((i, j))
      if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
        r, g, b = pixels[x, y]
        pixels[x, y] = (r1, g1, b1)
  
  pixels = img_output.load()

  mask = [(0,0)] * 9
  weights = [0.0] * 9
  total_weight = 0.0

  # Membuat mask dan bobot berdasarkan nilai sigma
  for i in range(3):
    for j in range(3):
      x = i - 1
      y = j - 1
      weight = math.exp(-(x**2 + y**2)/(2*sigma**2)) / (2 * 3.14159 * sigma**2)
      total_weight += weight
      weights[i*3+j] = weight

  # Normalisasi bobot
  for i in range(9):
    weights[i] /= total_weight

  for i in range(1, row + 1):
    for j in range(1, col + 1):
      red = 0
      green = 0
      blue = 0

      # mengambil nilai piksel dari mask
      mask[0] = img_bordered.getpixel((i-1,j-1))
      mask[1] = img_bordered.getpixel((i-1,j))
      mask[2] = img_bordered.getpixel((i-1,j+1))
      mask[3] = img_bordered.getpixel((i,j-1))
      mask[4] = img_bordered.getpixel((i,j))
      mask[5] = img_bordered.getpixel((i,j+1))
      mask[6] = img_bordered.getpixel((i+1,j-1))
      mask[7] = img_bordered.getpixel((i+1,j))
      mask[8] = img_bordered.getpixel((i+1,j+1))

      # mengalikan nilai piksel dengan bobot
      for k in range(9):
        r, g, b = mask[k]
        red += r * weights[k]
        green += g * weights[k]
        blue += b * weights[k]

      red = int(red)
      green = int(green)
      blue = int(blue)

      pixels[i - 1,j - 1] = (red, green, blue)

  if coldepth == 1:
    img_output = img_output.convert("1")
  elif coldepth == 8:
    img_output = img_output.convert("L")
  else:
    img_output = img_output.convert("RGB")

  return img_output

def hsv(img_input,coldepth):
  # return img_input.convert("HSV")
  if coldepth!=24:
    img_input = img_input.convert('RGB')
    
  img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
  pixel = img_output.load()
  for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
      r, g, b = img_input.getpixel((i, j))
      r, g, b = r / 255.0, g / 255.0, b / 255.0
            
      cmax = max(r, g, b)
      cmin = min(r, g, b)
      diff = cmax-cmin
            
      if cmax == cmin:
        h = 0
      elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
      elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
      elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
      if cmax == 0:
        s = 0
      else:
        s = (diff / cmax) * 100
        v = cmax * 100

      pixel[i,j] = (int(h),int(s),int(v))
        
  return img_output

# github.com/dharmasaputraa

# def Morphology(img_input, coldepth, mode):
#   # if coldepth != 24:
#   # img_input.convert('L')

#   row = int(img_input.size[0])
#   col = int(img_input.size[1])
#   img_output = Image.new('L', (row, col))
#   print(row)
#   print(col)
#   mask = [(0,0)] * 9
#   singlePixel = [(0,0)] * 9
#   for i in range(row-1):
#     for j in range(col-1):
#       mask[0] = img_input.getpixel((i-1, j-1))
#       mask[1] = img_input.getpixel((i-1, j))
#       mask[2] = img_input.getpixel((i-1, j+1))
#       mask[3] = img_input.getpixel((i, j-1))
#       mask[4] = img_input.getpixel((i, j))
#       mask[5] = img_input.getpixel((i, j+1))
#       mask[6] = img_input.getpixel((i+1, j-1))
#       mask[7] = img_input.getpixel((i+1, j))
#       mask[8] = img_input.getpixel((i+1, j+1)) 
#       # print(mask[0][0])
            
#       for k in range(9):
#         singlePixel[k] = mask[k][0]
#         # print(singlePixel[k])
            
#     if mode == "erosion":
#       img_output.putpixel((i, j),(min(singlePixel)))
#     elif mode == "dilation":
#       img_output.putpixel((i, j),(max(singlePixel)))
      
#   if coldepth==1:
#     img_output = img_output.convert("1")
#   elif coldepth==8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")
    
#   return img_output  

# def Morphology2(img_input, coldepth, mode):
#   img_input.convert('L')

#   if mode == "opening": 
#     img_morphology1 = Morphology(img_input, coldepth, "erosion")
#     # img_morphology1.show()
#   elif "bottom_hat": 
#     img_morphology1 = Morphology(img_input, coldepth, "dilation")
#     # img_morphology1.show()
    
#   row = int(img_input.size[0])
#   col = int(img_input.size[1])
#   img_output = Image.new('L', (row, col))
#   print(row)
#   print(col)
#   mask = [(0,0)] * 9
#   mask_pure = [(0,0)] * 9
#   singlePixel = [(0,0)] * 9
#   for i in range(row-1):
#     for j in range(col-1):
#       mask[0] = img_morphology1.getpixel((i-1, j-1))
#       mask[1] = img_morphology1.getpixel((i-1, j))
#       mask[2] = img_morphology1.getpixel((i-1, j+1))
#       mask[3] = img_morphology1.getpixel((i, j-1))
#       mask[4] = img_morphology1.getpixel((i, j))
#       mask[5] = img_morphology1.getpixel((i, j+1))
#       mask[6] = img_morphology1.getpixel((i+1, j-1))
#       mask[7] = img_morphology1.getpixel((i+1, j))
#       mask[8] = img_morphology1.getpixel((i+1, j+1)) 

#       for k in range(9):
#         singlePixel[k] = mask[k][0]
#         # print(singlePixel[k])
#       if mode == "opening":
#         img_output.putpixel((i, j),(max(singlePixel)))
#       elif mode == "closing":
#         img_output.putpixel((i, j),(min(singlePixel)))
            
#   if coldepth==1:
#     img_output = img_output.convert("1")
#   elif coldepth==8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")
    
#   return img_output          

# def Morphology3(img_input, coldepth, mode):
#   img_input.convert('L')

#   if mode == "top_hat": 
#     img_morphology1 = Morphology2(img_input, coldepth, "opening")
#     # img_morphology1.show()
#   elif mode == "bottom_hat": 
#     img_morphology1 = Morphology2(img_input, coldepth, "closing")
#     # img_morphology1.show()
    
#   row = int(img_input.size[0])
#   col = int(img_input.size[1])
#   img_output = Image.new('L', (row, col))
#   print(row)
#   print(col)
#   mask = [(0,0)] * 9
#   mask_pure = [(0,0)] * 9
#   singlePixel = [(0,0)] * 9
#   for i in range(row-1):
#     for j in range(col-1):
#       mask_pure[0] = img_input.getpixel((i-1, j-1))
#       mask_pure[1] = img_input.getpixel((i-1, j))
#       mask_pure[2] = img_input.getpixel((i-1, j+1))
#       mask_pure[3] = img_input.getpixel((i, j-1))
#       mask_pure[4] = img_input.getpixel((i, j))
#       mask_pure[5] = img_input.getpixel((i, j+1))
#       mask_pure[6] = img_input.getpixel((i+1, j-1))
#       mask_pure[7] = img_input.getpixel((i+1, j))
#       mask_pure[8] = img_input.getpixel((i+1, j+1)) 
            
            
#       mask[0] = img_morphology1.getpixel((i-1, j-1))
#       mask[1] = img_morphology1.getpixel((i-1, j))
#       mask[2] = img_morphology1.getpixel((i-1, j+1))
#       mask[3] = img_morphology1.getpixel((i, j-1))
#       mask[4] = img_morphology1.getpixel((i, j))
#       mask[5] = img_morphology1.getpixel((i, j+1))
#       mask[6] = img_morphology1.getpixel((i+1, j-1))
#       mask[7] = img_morphology1.getpixel((i+1, j))
#       mask[8] = img_morphology1.getpixel((i+1, j+1)) 

#       for k in range(9):
#         singlePixel[k] = mask[k][0]
#         # print(singlePixel[k])
        
#       if mode == "top_hat":
#         for t in range(8):
#           img_output.putpixel((i, j),(mask_pure[t][0] - singlePixel[t]))
#       elif mode == "bottom_hat":
#         for t in range(8):
#           img_output.putpixel((i, j),(singlePixel[t] - mask_pure[t][0]))
            
#   if coldepth==1:
#     img_output = img_output.convert("1")
#   elif coldepth==8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")
                
#   return img_output  

# def Edge_Detaction(img_input, coldepth, type):
#   img_input = img_input.convert('L')

#   img_output = Image.new('L', (img_input.size[0], img_input.size[1]))
#   pixel = img_output.load()
#   mask = [(0,0)] * 9
#   mask2 = [(0,0)] * 9
  
#   if type == "robert":
#     gX = [[1, 0], [0, -1]]
#     gY = [[0, 1], [-1, 0]]

#     for i in range(img_input.size[0] - 1):
#       for j in range(img_input.size[1] - 1):
#         valueX = 0
#         valueY = 0
        
#         # Gradient X
#         valueX += img_input.getpixel((i, j)) * gX[0][0]
#         valueX += img_input.getpixel((i+1, j+1)) * gX[1][1]
        
#         # Gradient Y
#         valueY += img_input.getpixel((i, j+1)) * gY[0][1]
#         valueY += img_input.getpixel((i+1, j)) * gY[1][0]
        
#         finalValue = abs(valueX) + abs(valueY)
        
#         if finalValue > 255:
#           finalValue = 255
        
#         pixel[i, j] = finalValue

#   else:
#     if type == "sobel":
#       gX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
#       gY = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
#     elif type == "prewitt":
#       gX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
#       gY = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
#     elif type == "laplacian":
#       gX = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
#       gY = [[-1, 2, -1], [2, -4, 2], [-1, 2, -1]]
#     elif type == "scharr": 
#       gX = [[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]]
#       gY = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]

#     for i in range(img_input.size[0] - 1):
#       for j in range(img_input.size[1] - 1):
#         valueX = 0
#         valueY = 0
#         finalValue = 0
        
#         #for gradient X
#         mask[0] = (img_input.getpixel((i-1, j-1)) * gX[0][0])
#         mask[1] = (img_input.getpixel((i-1, j)) * gX[0][1])
#         mask[2] = (img_input.getpixel((i-1, j+1)) * gX[0][2])
#         mask[3] = (img_input.getpixel((i, j-1)) * gX[1][0])
#         mask[4] = (img_input.getpixel((i, j)) * gX[1][1])
#         mask[5] = (img_input.getpixel((i, j+1)) * gX[1][2])
#         mask[6] = (img_input.getpixel((i+1, j-1)) * gX[2][0])
#         mask[7] = (img_input.getpixel((i+1, j)) * gX[2][1])
#         mask[8] = (img_input.getpixel((i+1, j+1)) * gX[2][2])
        
#         #for gradient Y
#         mask2[0] = (img_input.getpixel((i-1, j-1)) * gY[0][0])
#         mask2[1] = (img_input.getpixel((i-1, j)) * gY[0][1])
#         mask2[2] = (img_input.getpixel((i-1, j+1)) * gY[0][2])
#         mask2[3] = (img_input.getpixel((i, j-1)) * gY[1][0])
#         mask2[4] = (img_input.getpixel((i, j)) * gY[1][1])
#         mask2[5] = (img_input.getpixel((i, j+1)) * gY[1][2])
#         mask2[6] = (img_input.getpixel((i+1, j-1)) * gY[2][0])
#         mask2[7] = (img_input.getpixel((i+1, j)) * gY[2][1])
#         mask2[8] = (img_input.getpixel((i+1, j+1)) * gY[2][2])
                  
#         for x in range(8):
#           rgb = mask[x]
#           valueX = valueX + rgb
          
#         for y in range(8):
#           rgb2 = mask2[y]
#           valueY = valueY + rgb2
#         finalValue = valueX + valueY

#         if finalValue < 0: 
#           finalValue = 0
#         elif finalValue > 255:
#           finalValue = 255
        
#         pixel[i,j] = (finalValue)  

#   if coldepth == 1:
#     img_output = img_output.convert("1")
#   elif coldepth == 8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")
    
#   return img_output

# def LowPassFilter(img_input, coldepth, type, sigma=1):
#   if coldepth!=24:
#     img_input = img_input.convert('RGB')
  
#   row = int(img_input.size[0])
#   col = int(img_input.size[1])
  
#   img_output = Image.new('RGB', (row, col))
  
#   # memberi border (alternatif)
#   # img_bordered = ImageOps.expand(img_input, border=1, fill="Black")
  
#   # sulusi memberi border 2
#   img_bordered = Image.new('RGB', (row + 2, col + 2))
#   pixels = img_bordered.load()
#   pixels_input = img_input.load()
  
#   for i in range(img_input.size[0] - 1):
#     for j in range(img_input.size[1] - 1):
#       x = 1 + i
#       y = 1 + j
#       r1, g1, b1 = pixels_input[(i, j)]
#       if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
#         r, g, b = pixels[x, y]
#         pixels[x, y] = (r1, g1, b1)
  
#   if type == 'Mean' or type == 'Median':
#     mask = [(0,0)] * 9
#     for i in range(1, row + 1):
#       for j in range(1, col + 1):
#         red = 0
#         green = 0
#         blue = 0
#         mask[0] = img_bordered.getpixel((i-1, j-1))
#         mask[1] = img_bordered.getpixel((i-1, j))
#         mask[2] = img_bordered.getpixel((i-1, j+1))
#         mask[3] = img_bordered.getpixel((i, j-1))
#         mask[4] = img_bordered.getpixel((i, j))
#         mask[5] = img_bordered.getpixel((i, j+1))
#         mask[6] = img_bordered.getpixel((i+1, j-1))
#         mask[7] = img_bordered.getpixel((i+1, j))
#         mask[8] = img_bordered.getpixel((i+1, j+1)) 
        
#         if type == 'Median':
#           # alternatif
#           # mask.sort()
          
#           array = bubble_sort(mask)
#           img_output.putpixel((i - 1, j - 1),(mask[4]))
          
#         elif type == 'Mean':
#           pixels = img_output.load()
          
#           for k in range(8):
#             r, g, b = mask[k]
#             red = red + r
#             green = green + g
#             blue = blue + b
            
#           red = int(red * 1/9)
#           green = int(green * 1/9)
#           blue = int(blue * 1/9)
          
#           pixels[i - 1,j - 1] = (red, green, blue)
          
#   elif type == 'Gaussian':
#     pixels = img_output.load()
    
#     mask = [(0,0)] * 9
#     weights = [0.0] * 9
#     total_weight = 0.0
    
#     # Membuat mask dan bobot berdasarkan nilai sigma
#     for i in range(3):
#       for j in range(3):
#         x = i - 1
#         y = j - 1
#         weight = math.exp(-(x**2 + y**2)/(2*sigma**2)) / (2 * 3.14159 * sigma**2)
#         total_weight += weight
#         weights[i*3+j] = weight
        
#     # Normalisasi bobot
#     for i in range(9):
#       weights[i] /= total_weight
      
#     for i in range(1, row + 1):
#       for j in range(1, col + 1):
#         red = 0
#         green = 0
#         blue = 0
        
#         # mengambil nilai piksel dari mask
#         mask[0] = img_bordered.getpixel((i-1,j-1))
#         mask[1] = img_bordered.getpixel((i-1,j))
#         mask[2] = img_bordered.getpixel((i-1,j+1))
#         mask[3] = img_bordered.getpixel((i,j-1))
#         mask[4] = img_bordered.getpixel((i,j))
#         mask[5] = img_bordered.getpixel((i,j+1))
#         mask[6] = img_bordered.getpixel((i+1,j-1))
#         mask[7] = img_bordered.getpixel((i+1,j))
#         mask[8] = img_bordered.getpixel((i+1,j+1))
        
#         # mengalikan nilai piksel dengan bobot
#         for k in range(9):
#           r, g, b = mask[k]
#           red += r * weights[k]
#           green += g * weights[k]
#           blue += b * weights[k]
          
#         red = int(red)
#         green = int(green)
#         blue = int(blue)
        
#         pixels[i - 1,j - 1] = (red, green, blue)
        
#   if coldepth == 1:
#     img_output = img_output.convert("1")
#   elif coldepth == 8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")
    
#   return img_output
