# ProyectoCIDEF
## Principales programas utilizados

![Alt text](/logo/python.PNG)
![Alt text](/logo/django.PNG)

## Pasos para ejecutar el programa
**Tener previamente instalado git**

➜ En la CMD, clonar el proyecto (es recomentable realizar el comando directamente en el disco C/):

	✓ git clone https://github.com/Junisses/ProyectoCIDEF.git

➜ Luego, ubicar en que carpeta se encuentra el archivo pip, este es un comando que utiliza python para poder instalar complementos, de la misma manera que se instala django.
  Generalmente este comando se encuentra en la carpeta "Script" de python, una vez ubicado instalar los siguientes complementos:
	
		✓ pip install pillow
		✓ pip install django-crispy-forms
		✓ pip install djangorestframework
		✓ pip install social-auth-app-django-crispy-forms
		✓ pip install django-progressive-web-app
		✓ pip install django-core
		✓ pip install django-admin-interface
		✓ pip install django-widgets
		✓ pip install django-is-core
		✓ pip install django.core
		✓ pip install django-widget-tweaks
	
➜ Cuando este todo instalado, dirigirse mediante la CMD a la carpeta donde se clono el proyecto, luego ingresar a la carpeta de "ProyectoCIDEF" y procedente ingresar a "RepuestosCIDEF".
  En esta carpeta se encuentra un archivo que permite la ejecucion del programa, si se quiere comprobar escribir "dir" y buscar archivo manage.py.
	  
  Dentro de la carpeta "RepuestosCIDEF", ejecutar lo siguiente:
	  
		✓ python manage.py runserver
		
➜ Finalmente, copiar la dirección http que entrega la CMD, y pegarla en un navegador.
  A continuación una imagen de demostración:
		
![Alt text](/logo/indicaciones.PNG)


Nota:
> Para entrar al administrador ingresar http://127.0.0.1:8000/admin, en la cual para poder ingresar se debe crear un usuario mediante la CMD con el siguiente comando "python manage.py createsuperuser", ingresar los datos que se solicitan, luego ir al admin e ingresar la cuenta.