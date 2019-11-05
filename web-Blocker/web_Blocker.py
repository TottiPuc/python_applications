""" first of all you need to know the path of the hosts file:
in MAC or LINUX => /etc/hosts
in windows => C:\Windows\System32\drivers\etc
"""

import time    # modulo utilizado para poner a dormir el bucle
from datetime import datetime as dt # modulo usado para obtener fechas 

# configuracion del host y los sitios web que se desea bloquear
host_temp ="hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"
websites_list =["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    # condicional que verifica si le fecha y hora actual es mayo a las 8 am y menos a las 4pm 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,15) :
        with open(hosts_path,'r+') as file:
            print("archivo ha ser modificado...{}".format(file.name))
            content = file.read() # lectura del archivo host como un string
            for website in websites_list: # rerorrer la lista de websites a bloquear
                # si los archivos existen no se hace nada caso contrario se los agrega al documento hosts
                if website in content: 
                    pass
                else:
                    file.write("\n" + redirect + "\t" + website )
            print("working hours... you have to be working... :()")
    else:
        with open(hosts_path,'r+') as file:
            print("archivo ha ser modificado...{}".format(file.name))
            content = file.readlines() # lectura del archivo host como una lista 
            file.seek(0)
            for item in content:
                """
                averiguar si existe el website en cada una de las lineas del archivos leido como lista
                si no existe se crea un nuevo archivo hosts con esta linea si existe se omite la linea
                """
                if not any(website in item for website in websites_list):
                    file.write(item)
            file.truncate()
        print("Fun hours.. you can do whatever you want.. :D")
    time.sleep(5)