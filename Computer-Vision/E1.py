import cv2
import numpy as np

### ~~~~~~~~~~~~~~~~~Read image~~~~~~~~~~~~~~~~~
img = cv2.imread('F:/Computer-Vision/golden.jpg')

### ~~~~~~~~~~~~~~~~~Increase brightness 30 units~~~~~~~~~~~~~~~~~
## Using matrix
img_increase_brightness1 = img + 30	
# cv2.imshow('1.1 Result Image Brighter 30 Units', img_increase_brightness1)
# cv2.imwrite('F:/Computer-Vision/E1_Results/1.1 Result Image righter 30 Units.jpg', img_increase_brightness1)

## Using for loop
def increase_brightness_using_for(img, value):
	img_increase_brightness2 = np.zeros_like(img) #init variable
	for i in range(img.shape[0]): #run through x dimention Ox
		for j in range(img.shape[1]): #run though y dimension Oy
			for k in range(img.shape[2]): #run through z dimention, for B G R
				img_increase_brightness2[i][j][k] = img[i][j][k] + value
	return img_increase_brightness2
img_increase_brightness2 = increase_brightness_using_for(img, 30)
# cv2.imshow('1.2 Result Image Brighter 30 Units using loop', img_increase_brightness2)
# cv2.imwrite('F:/Computer-Vision/E1_Results/1.2 Result Image Brighter 30 Units using loop.jpg', img_increase_brightness2)

# img[i][j][k] means: i = width along Ox; j = length along Oy; k = {0,1,2} on be half of Blue Green Red in order


### ~~~~~~~~~~~~~~~~~Force color red = 0~~~~~~~~~~~~~~~~~
## Using matrix
imgblue0 = img.copy()
imgblue0[:, :, 0] = 0
# cv2.imshow('2.1 Result Image Blue=0', imgblue0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.1 Result Image Blue=0.jpg', imgblue0)

imggreen0 = img.copy()
imggreen0[:, :, 1] = 0
# cv2.imshow('2.1 Result Image Green=0', imggreen0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.1 Result Image Green=0.jpg', imggreen0)

imgred0 = img.copy()
imgred0[:, :, 2] = 0
# cv2.imshow('2.1 Result Image Red=0', imgred0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.1 Result Image Red=0.jpg', imgred0)

## Using for loop 
def set_red_is_zero(img):
	imgredis0 = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				if k == 2: #red layer
					imgredis0[i][j][k] = 0
	return imgredis0
redis0 = set_red_is_zero(img)
# cv2.imshow('2.2 Result Image red is 0', redis0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.2 Result Image red is 0.jpg', redis0)

def set_blue_is_zero(img):
	imgblueis0 = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				if k == 0: #blue layer
					imgblueis0[i][j][k] = 0
	return imgblueis0
blueis0 = set_blue_is_zero(img)
# cv2.imshow('2.2 Result Image blue is 0', blueis0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.2 Result Image blue is 0.jpg', blueis0)

def set_green_is_zero(img):
	imggreenis0 = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				if k == 1: #green layer
					imggreenis0[i][j][k] = 0
	return imggreenis0
greenis0 = set_green_is_zero(img)
# cv2.imshow('2.2 Result Image green is 0', greenis0)
# cv2.imwrite('F:/Computer-Vision/E1_Results/2.2 Result Image green is 0.jpg', greenis0)

### ~~~~~~~~~~~~~~~~~Convert red to blue~~~~~~~~~~~~~~~~~
## Using matrix
imgrtb = img.copy()  #red to blue
imgrtb[:, :, 0] = imgrtb[:, :, 2] #assign red = blue
imgrtb[:, :, 2] = img[:, :, 0] #assign blue = red of temp because imgrtb was replaced already
# cv2.imshow('3.1 Result Image Red To Blue and reverse', imgrtb)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.1 Result Image Red To Blue and reverse.jpg', imgrtb)

imgrtg = img.copy() #red to green
imgrtg[:, :, 1] = imgrtg[:, :, 2]
imgrtg[:, :, 2] = img[:, :, 1]
# cv2.imshow('3.1 Result Image Red To Green and reverse', imgrtg)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.1 Result Image Red To Green and reverse.jpg', imgrtg)

imggtb = img.copy() #green to blue
imggtb[:, :, 1] = imggtb[:, :, 0]
imggtb[:, :, 0] = img[:, :, 1]
# cv2.imshow('3.1 Result Image Green To Blue and reverse', imggtb)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.1 Result Image Green To Blue and reverse.jpg', imggtb)


## test if blue and green exchange for each other in pixel 300x300
# def test_if_Blue_Green_exchange_in_a_pixel(img, x, y):
# 	print("Green of the pixel", img[y][x][1]) #img[y][x][z]
# 	print("Blue of the pixel", img[y][x][0])
# 	print("Green of the pixel after exchange", imggtb[y][x][1])
# 	print("Blue of the pixel after exchange", imggtb[y][x][0])
# test_if_Blue_Green_exchange_in_a_pixel(img, 300, 320)

## test if red and green exchange for each other in pixel 300x300
# def test_if_Red_Green_exchange_in_a_pixel(img, x, y):
# 	print("Green of the pixel", img[y][x][1]) #img[y][x][z]
# 	print("Red of the pixel", img[y][x][2])
# 	print("Green of the pixel after exchange", imgrtg[y][x][1])
# 	print("Red of the pixel after exchange", imgrtg[y][x][2])
# test_if_Red_Green_exchange_in_a_pixel(img, 300, 320)

## Using for loop
def convert_red_to_blue_and_reverse(img):
	redtoblue = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			redtoblue[i, j, 2] = img[i, j, 0]
			redtoblue[i, j, 0] = img[i, j, 2]
	return redtoblue
redtoblue = convert_red_to_blue_and_reverse(img)
# cv2.imshow('3.2 Result Image Red To Blue and reverse', redtoblue)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.2 Result Image Red To Blue and reverse.jpg', redtoblue)

def convert_red_to_green_and_reverse(img):
	redtogreen = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			redtogreen[i, j, 2] = img[i, j, 1]
			redtogreen[i, j, 1] = img[i, j, 2]   
	return redtogreen
redtogreen = convert_red_to_green_and_reverse(img)
# cv2.imshow('3.2 Result Image Red To Green and reverse', redtogreen)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.2 Result Image Red To Green and reverse.jpg', redtogreen)

def convert_green_to_blue_and_reverse(img):
	greentoblue = img.copy()
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			greentoblue[i, j, 1] = img[i, j, 0]
			greentoblue[i, j, 0] = img[i, j, 1]
	return greentoblue
greentoblue = convert_green_to_blue_and_reverse(img)
# cv2.imshow('3.2 Result Image Green To Blue and reverse', greentoblue)
# cv2.imwrite('F:/Computer-Vision/E1_Results/3.2 Result Image Green To Blue and reverse.jpg', greentoblue)


### ~~~~~~~~~~~~~~~~~Flip image vertically along Ox~~~~~~~~~~~~~~~~~
## Using function
horizontal_img = img.copy()
horizontal_img = cv2.flip(img, 0)
# cv2.imshow('4.1 Result Image Flipped Horizontally 1', horizontal_img)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.1 Result Image Flipped Horizontally 1.jpg', horizontal_img)

vertical_img = img.copy()
vertical_img = cv2.flip(img, 1)
# cv2.imshow('4.1 Result Image Flipped Vertically 1', vertical_img)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.1 Result Image Flipped Vertically 1.jpg', vertical_img)

## Using matrix
def flip_image_vertically(img):
	imgvertical = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
	for i in range(img.shape[0]):
		imgvertical[i, :] = img[img.shape[0] - i - 1, :] #x is still, change y
	return imgvertical
# np.zeros_like(img) means make a zero matrix with the size of img
# np.zeros([a,b,c], np.uint8) means make a zero matrix with size a x b x c with datatype int8
imgverticallyflipped = flip_image_vertically(img)
# cv2.imshow('4.2 Result Image Flipped Vertically', imgverticallyflipped)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.2 Result Image Flipped Vertically.jpg', imgverticallyflipped)


### ~~~~~~~~~~~~~~~~~Flip image horizontally along Oy~~~~~~~~~~~~~~~~~
def flip_image_horizontally(img):
	imgherizontal = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
	for j in range(img.shape[1]):
		imgherizontal[:, j] = img[:, img.shape[1] - j - 1] #y is still, change x
	return imgherizontal
imghorizontallyflipped = flip_image_horizontally(img)
# cv2.imshow('4.2 Result Image Flipped horizontally', imghorizontallyflipped)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.2 Result Image Flipped horizontally.jpg', imghorizontallyflipped)

#NOTE img.shape[y][x][z] means y length, x width and z depth

##Using for loop
def flip_image_vertically_with_for(img):
	imgflipedvertically = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				imgflipedvertically[i, j, k] = img[img.shape[0] - i - 1, j, k]
	return imgflipedvertically
imgflipedvertically = flip_image_vertically_with_for(img)
# cv2.imshow('4.2 Result Image Flipped vertically with for loop', imgflipedvertically)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.2 Result Image Flipped vertically with for loop.jpg', imgflipedvertically)


def flip_image_horizontally_with_for(img):
	imgflipedhorizontally = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				imgflipedhorizontally[i, j, k] = img[i, img.shape[1] - j - 1, k]
	return imgflipedhorizontally
imgflipedhorizontally = flip_image_horizontally_with_for(img)
# cv2.imshow('4.2 Result Image Flipped horizontally with for loop', imgflipedhorizontally)
# cv2.imwrite('F:/Computer-Vision/E1_Results/4.2 Result Image Flipped horizontally with for loop.jpg', imgflipedhorizontally)


cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

### ~~~~~~~~~~~~~~~~~Write image~~~~~~~~~~~~~~~~~