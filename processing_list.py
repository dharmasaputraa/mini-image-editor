from PIL import Image, ImageOps
import math

def imageResize(img, width, height):
  widthRatio = width/img.size[0]
  heightRatio = height/img.size[1]
    
  newWidth = int(widthRatio*img.size[0])
  newHeight = int(heightRatio*img.size[1])
    
  newImage = img.resize((newWidth, newHeight))
  return newImage

# def ImgNegative(img_input,coldepth):
#   #solusi 1
#   #img_output = ImageOps.invert(img_input)

#   #solusi 2
#   if coldepth!=24:
#     img_input = img_input.convert('RGB')

#   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
#   pixels = img_output.load()
#   for i in range(img_output.size[0]):
#     for j in range(img_output.size[1]):
#       r, g, b = img_input.getpixel((i, j))
#       pixels[i,j] = (255-r, 255-g, 255-b)

#   if coldepth==1:
#     img_output = img_output.convert("1")
#   elif coldepth==8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")

#   return img_output 

def ImgNegative(img, coldepth):
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

# def ImgBlend(img_input, coldepth, img_input2, coldepth2, alpha1, alpha2):

#   # img_input = imageResize(300, 300, img_input)
#   # img_input2 = imageResize(300, 300, img_input2)
  
#   if coldepth!=24:
#     img_input = img_input.convert('RGB')
#   elif coldepth2!=24:
#     img_input2 = img_input2.convert('RGB')
      
#   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
#   pixels = img_output.load()
  
#   for i in range(img_output.size[0]):
#     for j in range(img_output.size[1]):
#       color1 = img_input.getpixel((i, j))
#       color2 = img_input2.getpixel((i, j))
#       r = int(color1[0]*alpha1) + int(color2[0]*alpha2)
#       g = int(color1[1]*alpha1) + int(color2[1]*alpha2)
#       b = int(color1[2]*alpha1) + int(color2[2]*alpha2)
#       pixels[i,j] =  (r, g, b)
  
#   if coldepth==1:
#     img_output = img_output.convert("1")
#   elif coldepth==8:
#     img_output = img_output.convert("L")
#   else:
#     img_output = img_output.convert("RGB")

#   return img_output 

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

# def uts_1(img_input, coldepth, img_input2, coldepth2):
#   if coldepth!=24:
#     img_input = img_input.convert('RGB')
#   elif coldepth2!=24:
#     img_input2 = img_input2.convert('RGB')
    
#   img_negatived = ImgNegative(img_input2, coldepth2)
    
#   center_x = img_negatived.size[0] // 2
#   center_y = img_negatived.size[1] // 2
  
#   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
#   pixels = img_output.load()
  
#   for i in range(img_output.size[0]):
#     for j in range(img_output.size[1]):
#       r, g, b = img_input.getpixel((i, j))
#       pixels[i, j] = (r, g, b)
  
#   for i in range(img_negatived.size[0]):
#     for j in range(img_negatived.size[1]):
#       x = center_x + i
#       y = center_y + j
#       r1, g1, b1 = img_negatived.getpixel((i, j))
#       if r1 != 0 and g1 != 0 and b1 != 0 and x >= 0 and x < img_output.size[0] and y >= 0 and y < img_output.size[1]:
#         r, g, b = pixels[x, y]
#         pixels[x, y] = (r1, g1, b1)
  
#   return img_output

def ImgBlend(img_input, coldepth, img_input2, coldepth2, alpha1, alpha2, posX, posY):

  # img_input = imageResize(300, 300, img_input)
  # img_input2 = imageResize(300, 300, img_input2)
  
  if coldepth!=24:
    img_input = img_input.convert('RGB')
  elif coldepth2!=24:
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