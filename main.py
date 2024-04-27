#imports for managing files
import os
import shutil

#import for UI
import customtkinter

#button that gets the path
def getText():
    path = textbox.get('1.0', 'end-1c').strip() #Path of the folder you want to organise
    files = os.listdir(path) #getting all the files
    #making sure all files get sorted
    for file in files: 
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension): #moving files to correct folder if it exists
         shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else: #creating a new one if it doesn't
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

#UI suff

root = customtkinter.CTk()

textbox = customtkinter.CTkTextbox(root)
button = customtkinter.CTkButton(root, command=getText)
textbox.pack(pady=30, padx=20)
button.pack(pady=10, padx=20)

root.mainloop()