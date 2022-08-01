from ast import Break
import os 
import shutil

extensionDocuments=r".pdf",r".docx",r".ppt",r".xlsx"

extensionImages=r".png",r".jpg",r".jfif",r".iso",r".psd",r".PNG"

extensionOther=r".exe",r".zip",r".mp4"



def CreateDirectories():

    while(True):
        if os.path.exists("Documentos")==True:
            print("entro documentos")
            pass
        else:
            os.mkdir("Documentos")
            continue
        
        if os.path.exists("Imagenes")==True:
            print("entro Imagenes")
            pass
        else:
            os.mkdir("Imagenes")
            continue
        
        if os.path.exists("Otros")==True:
            pass
        else:
            os.mkdir("Otros")
        break
    
    MoveFiles(extensionDocuments,"Documentos")
    MoveFiles(extensionImages,"Imagenes")
    MoveFiles(extensionOther,"Otros")
    

def MoveFiles(extensions, folderName):
    filter=[_ for _ in os.listdir() if _.endswith(extensions)]
    for i in filter:
        shutil.move(i,folderName)


CreateDirectories()