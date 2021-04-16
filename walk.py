import os

path="This PC\\Galaxy S9\\Phone\\Documents"
#print(list(os.walk(path)))
print("----------------------")

for root, directoriesList, filesList in os.walk(path):
    
    if len(directoriesList) == 0:
        print(root)
        for eachFile in filesList:
            print(os.path.join(root,eachFile))