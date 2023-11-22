import os
import pypff

def convertir_pst_a_texto(archivo_pst, carpeta_destino):
    # Abrir el archivo PST
    pst = pypff.file()
    pst.open(archivo_pst)

    # Obtener todas las carpetas del archivo PST
    carpetas = pst.get_root_folder().sub_folders

    # Recorrer cada carpeta y extraer los mensajes de correo
    for carpeta in carpetas:
        if carpeta.number_of_sub_folders > 0:
            # Crear una carpeta para almacenar los mensajes de correo
            carpeta_destino_hija = f"{carpeta_destino}/{carpeta.name}"
            os.makedirs(carpeta_destino_hija, exist_ok=True)
            # Recorrer los mensajes de correo en la carpeta actual
            for mensaje in carpeta.sub_messages:
                # Obtener el cuerpo del mensaje en formato texto
                texto = mensaje.get_plain_text_body()
                print(texto)
                # Guardar el cuerpo del mensaje en un archivo de texto
                nombre_archivo = f"{carpeta_destino_hija}/{mensaje.subject}.txt"
                with open(nombre_archivo, "w", encoding="utf-8") as archivo_txt:
                    archivo_txt.write(texto)

    # Cerrar el archivo PST
    pst.close()

# Nombre del archivo PST de entrada y carpeta de destino para los archivos de texto
#archivo_pst = "D:\\CORREO HOSTING-220404-PST\\Wed Jun 15 15 57 59 CLT 2022\\Exchange Offline Storage (.ost)\\aflores@icsa-metaproject.cl\\aflores@icsa-metaproject.cl0.pst"
#archivo_pst = "D:\\CORREO HOSTING-220404-PST\\Wed Jun 15 15 57 59 CLT 2022\\Exchange Offline Storage (.ost)\\agonzalez@icsa-metaproject.cl\\agonzalez@icsa-metaproject.cl0.pst"
archivo_pst = "C:\\temp\\CORREOTXT\\cgutierrez@icsa-metaproject.cl.pst"
carpeta_destino = "C:\\temp\\CORREOTXT"

# Convertir el archivo PST a texto
convertir_pst_a_texto(archivo_pst, carpeta_destino)

print("La conversion de PST a texto se ha completado")
