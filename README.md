# Aplicación de Django Rest Framework para un Restaurante

Este proyecto es una aplicación Django Rest Framework que permite a un usuario gestionar información de un restaurante, 
como el nombre del restaurante, identificación del usuario, menú, fecha de pago y valor pagado.

# Requisitos

Para correr esta aplicación, deberá tener lo siguiente instalado en su sistema:

•	Python 3.x
•	Django 3.x
•	Django Rest Framework

# Configuración

Clone este repositorio en su sistema local utilizando el siguiente comando:
git clone https://github.com/<username>/django-rest-framework-restaurant.git

Cree un entorno virtual y activelo:

python -m venv myenv
source myenv/bin/activate

Instale las dependencias requeridas en el archivo requirements.txt:
  
pip install -r requirements.txt

# Ejecución
  
Para poder ejecutar la aplicacion es necesario crear una database llamada "base de datos"
Luego Ejecute las siguientes instrucciones en su terminal para correr la aplicación:

python manage.py migrate
python manage.py runserver

# Validaciones

La aplicación incluye las siguientes validaciones en los datos de entrada:

El nombre del restaurante debe ser una cadena de caracteres.

La identificación de usuario debe ser un número.

La fecha de pago no puede ser un día par según el decreto de administración.

El valor pagado debe estar entre 1 y 1000000.

El valor del menú no puede ser negativo.
  
