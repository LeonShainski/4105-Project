import os
from PIL import Image
import glob

directoryGood="4105-Project\dataset"
#directoryBad="4105-Project\images"


#Ensuring images are not corrupt before processing them
def checkImages(directory):
    arrErrors=[] 
    #Getting all folders in directory
    for filename in os.listdir(directory):
        #Getting all files in folder
        for file in os.listdir(directory+'\\'+filename):
            try:
                img = Image.open(directory+'\\'+filename+'\\'+file) #Attempting to open the file
                img.verify() #Verifying that the file is not corrupt
                img.close() 
            except:
                arrErrors.append(file) #Adding any corrpt files to a list
                print("Error with "+file)
    return arrErrors
                

arrErrors=checkImages(directoryGood)
if (len(arrErrors)==0):
    print("All images in order")
else:
    print("The following files had been found to be corrupt and/or unuseable: ",arrErrors) #Printing all files that were corrupt

