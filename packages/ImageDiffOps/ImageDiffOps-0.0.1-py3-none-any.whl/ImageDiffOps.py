#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.measure import compare_ssim
import cv2
import numpy as np


# In[2]:



class ImageDiffOps:
   
    
    def __init__(self,Image1Path,Image2Path):
        '''
        initialiaze path of Images
        '''
        self.Image1Path = Image1Path
        self.Image2Path = Image2Path
        
    def detectDiffROI(self):
            '''
            Method to extract disimilar parts between two images ( finds those parts of images which has been changed )

            Return: 

               diffImagePart: list of differnt part of image
               bounding_coordinate : list of coordinates [x,y,w,h] of each part of image
            '''
        
        
        #try:
            image1 = cv2.imread(self.Image1Path)
            image2 = cv2.imread(self.Image2Path)
            if image1 is None or image2 is None:
                raise OSError("Image not found,Ensure the path is correct...")
              # Convert images to grayscale
            image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

            # Compute SSIM(structural similarity index) between two images
            (score, diff) = compare_ssim(image1_gray, image2_gray, full=True)
            

            # The diff image contains the actual image differences between the two images
            # and is represented as a floating point data type in the range [0,1] 
            # so we must convert the array to 8-bit unsigned integers in the range
            # [0,255] before we can use it with OpenCV
            diff = (diff * 255).astype("uint8")

            # Threshold the difference image, followed by finding contours to
            # obtain the regions of the two input images that differ
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = contours[0] if len(contours) == 2 else contours[1]

            mask = np.zeros(image1.shape, dtype='uint8')
            filled_after = image2.copy()
            diffImagePart = list()
            bounding_coordinate = list()
            
            for c in contours:
               
                area = cv2.contourArea(c)
                if area > 40:
                    x,y,w,h = cv2.boundingRect(c)
                    bounding_coordinate.append([x,y,w,h])
                    imgob= image1[y:y+h, x:x+w]
                    diffImagePart.append(imgob)
                  
            return diffImagePart , bounding_coordinate
        
        #except:
            #return "Check given path of Images... "
        
        
    def SimilarityScore(self):
            '''
            Method to check the similarity between two Images

            Return: 

               score: its similarity score of two images.
            '''
            image1 = cv2.imread(self.Image1Path)
            image2 = cv2.imread(self.Image2Path)
            if image1 is None or image2 is None:
                raise OSError("Image not found,Ensure the path is correct...")
              # Convert images to grayscale
            image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

            # Compute SSIM(structural similarity index) between two images
            score = compare_ssim(image1_gray, image2_gray, full=False)
            return score

        
        


# In[ ]:




