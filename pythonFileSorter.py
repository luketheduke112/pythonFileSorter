
#file sorter for python.
#created by Luke Fisher
import os
import shutil

#this program sorts files based on extension. Change the path variable to a specific directory which you want sort.


path = 'C:\\Users\\luked\\Downloads\\pytest'
list_ = os.listdir(path)

#function that takes in two parameters, a source and a target. This takes the same parameters as .move from the os utility in python.
def moveFile(extensionToAdd, destinationDir):
    if(ext == extensionToAdd):
        shutil.move(pathAdded+extensionToAdd, destinationDir) 
        print("moved a: " + extensionToAdd + " file")

#look through all files in the specific directory.
for file_ in list_:
    name,ext = os.path.splitext(file_)#split the file name and extension.
    pathAdded = path+"\\"+name #connect the directory to sort and the specific file within that directory.
    print(file_)#just for the sake of debugging making sure that the program sees all the files in the directory to sort.
    
    #follow this format for choosing what types of files to sort and then  
    #move file takes a file extension and then the target directory to move those files with the extension to.
    moveFile(".txt", 'E:\\pytestfolderfortxtfiles')  
    moveFile(".jpg", "C:\\Users\\luked\\Pictures")  
    moveFile(".png","C:\\Users\\luked\\Pictures")
    
