
import cv2

def read_image(path1,path2):
	read_img1 = cv2.imread(path1)
	read_img2 = cv2.imread(path2)
	return (read_img1,read_img2)

def convert_to_grayscale(pic1,pic2):
	gray_img1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2GRAY)
	gray_img2 = cv2.cvtColor(pic2,cv2.COLOR_BGR2GRAY)
	return (gray_img1,gray_img2)


def detector(image1,image2):
	
	detect = cv2.ORB_create()

	
	key_point1,descrip1 = detect.detectAndCompute(image1,None)
	key_point2,descrip2 = detect.detectAndCompute(image2,None)
	return (key_point1,descrip1,key_point2,descrip2)

def BF_FeatureMatcher(des1,des2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    no_of_matches = brute_force.match(des1,des2)
 

    no_of_matches = sorted(no_of_matches,key=lambda x:x.distance)
    return no_of_matches
 

def display_output(pic1,kpt1,pic2,kpt2,best_match):
 
    
    output_image = cv2.drawMatches(pic1,kpt1,pic2,kpt2,best_match,None,flags=2)
    cv2.imwrite('O:/BR/Output 3/output_image.jpg',output_image)
    cv2.imshow('Output image',output_image)


first_image_path = "Input/test0.jpg"
second_image_path = "Input/test1.jpg"
img1, img2 = read_image(first_image_path,second_image_path)

	
gray_pic1, gray_pic2 = convert_to_grayscale(img1,img2)
	
key_pt1,descrip1,key_pt2,descrip2 = detector(img1,img2)
	
cv2.imshow("Key points of Image 1",cv2.drawKeypoints(img1,key_pt1,None))
cv2.imshow("Key points of Image 2",cv2.drawKeypoints(img2,key_pt2,None))
out1 = cv2.drawKeypoints(img1,key_pt1,None)
out2 = cv2.drawKeypoints(img2,key_pt2,None)
cv2.imwrite('O:/BR/Output 2/out1.jpg',out1)
cv2.imwrite('O:/BR/Output 2/out2.jpg',out2)


print(f'Descriptors of Image 1 {descrip1}')
print(f'Descriptors of Image 2 {descrip2}')
print('------------------------------')


print(f'Shape of descriptor of first image {descrip1.shape}')
print(f'Shape of descriptor of second image {descrip2.shape}')

cv2.waitKey()
cv2.destroyAllWindows()
number_of_matches = BF_FeatureMatcher(descrip1,descrip2)
tot_feature_matches = len(number_of_matches)
 

print(f'Total Number of Features matches found are {tot_feature_matches}')
 

display_output(img1,key_pt1,img2,key_pt2,number_of_matches)
cv2.waitKey()
cv2.destroyAllWindows()