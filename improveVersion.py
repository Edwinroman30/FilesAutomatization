import os
import shutil

ruta_origen = '//home//edwin//Downloads//Directorio_Prueba'

#* Formato de archivos a aceptar.
imgExt = ['.png','.jpg','.jpeg','.gif']
vidExt = ['.mp4','.mov']
textExt = ['.txt','.md']

def crear_directorios():
 
    if not 'Imagenes' in os.listdir(ruta_origen):
        os.mkdir(os.path.join(ruta_origen,'Imagenes'))
    if not 'Videos' in os.listdir(ruta_origen):
        os.mkdir(os.path.join(ruta_origen,'Videos'))
    if not 'Textos' in os.listdir(ruta_origen):
        os.mkdir(os.path.join(ruta_origen,'Textos'))
    if not 'Otros' in os.listdir(ruta_origen):
        os.mkdir(os.path.join(ruta_origen,'Otros'))


def ordernador(archivo,extencion):

        print(archivo+extencion)
        
        for ext in imgExt:
            if(extencion == ext):
                ruta_arc = os.path.join(ruta_origen,'Imagenes')
                shutil.move(os.path.join(ruta_origen,archivo+extencion) , ruta_arc)
        
        for ext in vidExt:
            if(extencion == ext):
                ruta_arc = os.path.join(ruta_origen,'Videos')
                shutil.move(os.path.join(ruta_origen,archivo+extencion) , ruta_arc)
        
        for ext in textExt:
            if(extencion == ext):
                ruta_arc = os.path.join(ruta_origen,'Textos')
                shutil.move(os.path.join(ruta_origen,archivo+extencion) , ruta_arc)
        
        if ext != ' ' and os.path.isfile(os.path.join(ruta_origen,archivo+extencion)):
            ruta_arc = os.path.join(ruta_origen,'Otros')
            shutil.move(os.path.join(ruta_origen,archivo+extencion), ruta_arc)
              
        
def main():
    archivos = os.listdir(ruta_origen)
    crear_directorios()
    print(archivos)
    
    for archivo in archivos:
        arc, exten = os.path.splitext(archivo)
        ordernador(arc, exten)

#Ejecución del programa.
main()