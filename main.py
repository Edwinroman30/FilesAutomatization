import os
import shutil

#Files Automatization with Python is a script that allow you organize your data or files by folders.
    #? PROCESOS:
        #OBTENER LA RUTA.
        #BUSCAR TODO EN LA RUTA DIRECTORIOS Y ARCHIVOS
        #FILTRAL SOLO LOS ARCHIVOS
        #CREAR CARPETAS CON EL NOMBRE DE CADA TIPO DE ARCHIVO CONTENIDO EN LA RUTA. / COMPROBAR SI ESTOS EXISTEN O NO.
        #MOVER CADA ARCHIVO A SU CARPETA CREADA CORRESPONDIENTE.

def organiceRoot(ruta):
    allData = os.listdir(ruta) #CON ESTO BUSCO TODOS LOS DIRECTORIOS Y ARCHIVO DE LA RUTA PASADA.

    for data in allData:
        rutatemporal = os.path.join(ruta,data) #AQUÍ LOS UNOS TODOS PARA QUE PAREZCA UN PATH REAL.
        
        #print(data)
        
        #!FILTRAL QUE SEAN ARCHIVOS (DOCUMENTOS, DATOS, etc...) Y FILTRARLOS.
        if os.path.isfile(rutatemporal):
            
            #CREAR UN DICCIONARIO PARA TRABAJAR MAS ORGANIZADO Y FORMARTO DE OBJETO.
                #? CON ESTO PUEDO SABER LA RUTA Y LA EXTENCION DEL ARCHIVO
            archivo = {'root': os.path.splitext(rutatemporal)[0], #RUTA
                       'exten': os.path.splitext(rutatemporal)[1]} #EXTENCION ARCHIVO

            #Vamos a crear carpetas con la extensiones.
            # el diccionario en su clave archivo['exten'] nos retorna en su forma base un STRING con el formato (Eje: .PNG .PDF .HTML), pero tiene el punto, y para parsear solo el nombre utilice str.PARTICION y acceder solo al nombre sin el punto:
            # El objetivo de extraer solo las siglas de extención sin el punto, es para crear carpetas con dichos nombre en UPPERCASE.
            
            #!COMPROBAR SI EXISTE UN DIRECTORIO CON ESE NOMBRE OSEA UNA CARPETA CON ESE NOMBRE.
            if (archivo['exten'].partition('.')[2].upper() in os.listdir(ruta)):
                pass
                #print('Ya existe un directorio con este nombre:')
            else:
                #! CREANDO CARPETAS (DE LO CONTRARIO, CREARLA)  
                os.mkdir(archivo['exten'].partition('.')[2].upper())
            
            #!MOVER ARCHIVOS A SUS RESPECTIVO DIRECTORIO
            arch_Pasar = os.path.basename(rutatemporal) #Con esto obtengo el nombre del archivo y sus extención.
            ruta_archivo = os.path.join(archivo['exten'].partition('.')[2].upper(),  os.path.basename(rutatemporal)) #Reubico el archivo en su carpeta TIPO correspondiente.
            
            shutil.move(arch_Pasar, ruta_archivo) #MOVER CADA ARCHIVO.
                    
#SOLO pasar la ruta donde estan los archivos.
ruta = os.path.join(os.getcwd()) #Ejemplo pongo esta ruta.
organiceRoot(ruta)

# BY Edwin Roman