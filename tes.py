# def erosion(img_input, coldepth):
#   if coldepth != 24:
#     img_input = img_input.convert('RGB')

#   row = img_input.size[0]
#   col = img_input.size[1]

#   img_output = Image.new('RGB', (row, col))

#   img_bordered = Image.new('RGB', (row + 2, col + 2))
#   pixels = img_bordered.load()
#   pixels_input = img_input.load()

#   for i in range(row):
#     for j in range(col):
#       x = 1 + i
#       y = 1 + j
#       r1, g1, b1 = pixels_input[i, j]
#       if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
#         r, g, b = pixels[x, y]
#         pixels[x, y] = (r1, g1, b1)

#   pixels = img_output.load()

#   mask = [(0, 0)] * 9

#   for i in range(1, row + 1):
#     for j in range(1, col + 1):
#       mask[0] = img_bordered.getpixel((i - 1, j - 1))
#       mask[1] = img_bordered.getpixel((i - 1, j))
#       mask[2] = img_bordered.getpixel((i - 1, j + 1))
#       mask[3] = img_bordered.getpixel((i, j - 1))
#       mask[4] = img_bordered.getpixel((i, j))
#       mask[5] = img_bordered.getpixel((i, j + 1))
#       mask[6] = img_bordered.getpixel((i + 1, j - 1))
#       mask[7] = img_bordered.getpixel((i + 1, j))
#       mask[8] = img_bordered.getpixel((i + 1, j + 1))

#       if mask[4] == (255, 255, 255):  # Check if central pixel is white
#         # Check if all surrounding pixels are white
#         all_white = True
#         for p in mask:
#           if p != (255, 255, 255):
#             all_white = False
#             break
#         if not all_white:
#           img_output.putpixel((i - 1, j - 1), (0, 0, 0))
#         else:
#           img_output.putpixel((i - 1, j - 1), (255, 255, 255))
#       else:
#         img_output.putpixel((i - 1, j - 1), (0, 0, 0))

#   return img_output

# def dilation(img_input, coldepth):
#   if coldepth != 24:
#     img_input = img_input.convert('RGB')

#   row = img_input.size[0]
#   col = img_input.size[1]

#   img_output = Image.new('RGB', (row, col))

#   img_bordered = Image.new('RGB', (row + 2, col + 2))
#   pixels = img_bordered.load()
#   pixels_input = img_input.load()

#   for i in range(row):
#     for j in range(col):
#       x = 1 + i
#       y = 1 + j
#       r1, g1, b1 = pixels_input[i, j]
#       if x >= 0 and x < img_bordered.size[0] and y >= 0 and y < img_bordered.size[1]:
#         r, g, b = pixels[x, y]
#         pixels[x, y] = (r1, g1, b1)

#   pixels = img_output.load()

#   mask = [(0, 0)] * 9

#   for i in range(1, row + 1):
#     for j in range(1, col + 1):
#       mask[0] = img_bordered.getpixel((i - 1, j - 1))
#       mask[1] = img_bordered.getpixel((i - 1, j))
#       mask[2] = img_bordered.getpixel((i - 1, j + 1))
#       mask[3] = img_bordered.getpixel((i, j - 1))
#       mask[4] = img_bordered.getpixel((i, j))
#       mask[5] = img_bordered.getpixel((i, j + 1))
#       mask[6] = img_bordered.getpixel((i + 1, j - 1))
#       mask[7] = img_bordered.getpixel((i + 1, j))
#       mask[8] = img_bordered.getpixel((i + 1, j + 1))

#       if mask[4] == (0, 0, 0):  # Check if central pixel is black
#         # Check if all surrounding pixels are black
#         all_black = True
#         for p in mask:
#           if p != (0, 0, 0):
#             all_black = False
#             break
#         if not all_black:
#           img_output.putpixel((i - 1, j - 1), (255, 255, 255))
#         else:
#           img_output.putpixel((i - 1, j - 1), (0, 0, 0))
#       else:
#         img_output.putpixel((i - 1, j - 1), (255, 255, 255))

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
