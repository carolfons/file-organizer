import os
import shutil

def organize_files(folder_path):
    #verify all the files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,filename)):
            file_extension = filename.split('.')[-1]
            new_folder = os.path.join(folder_path,file_extension.upper())

            #creates new folder if doesnt exists
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            #moves the file to the new folder
            shutil.move(os.path.join(folder_path,filename),os.path.join(new_folder,filename))

    print("Arquivos organizados com sucesso!")


if __name__ == "__main__":
    folder_to_organize = "./pasta-exemplo" #file path
    organize_files(folder_to_organize)