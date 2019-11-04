""" first of all you need to know the path of the hosts file:
in MAC or LINUX => /etc/hosts
in windows => C:\Windows\System32\drivers\etc
"""

import time    # modulo utilizado para poner a dormir el bucle
from datetime import datetime as dt # modulo usado para obtener fechas 

# configuracion del host y los sitios web que se desea bloquear
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect ="127.0.0.1"
websites =["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    # condicional que verifica si le fecha y hora actual es mayo a las 8 am y menos a las 4pm 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16) :
        print("working hours... you have to be working... :()")
    else:
        print("Fun hours.. you can do whatever you want.. :D")
    print(1)
    time.sleep(5)