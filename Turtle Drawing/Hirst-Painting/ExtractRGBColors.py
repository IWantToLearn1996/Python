import cv2, colorgram
#Load an Image using 'imread'
img = cv2.imread("D:\Applications\Downloads\DotImage.jpg")
#Display
cv2.imshow("Dot Image", img)
cv2.waitKey(0)

rgb_colors = []
colors = colorgram.extract("D:\Applications\Downloads\DotImage.jpg", 100)
print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)