#Aplicación de Django Rest Framework para un Restaurante
Este proyecto es una aplicación Django Rest Framework que permite a un usuario gestionar información de un restaurante, como el nombre del restaurante, identificación del usuario, menú, fecha de pago y valor pagado.

#Requisitos
Para correr esta aplicación, deberá tener lo siguiente instalado en su sistema:

Python 3.x
Django 3.x
Django Rest Framework
Configuración
Clone este repositorio en su sistema local utilizando el siguiente comando:

bash
Copy code
git clone https://github.com/<username>/django-rest-framework-restaurant.git
Cree un entorno virtual y activelo:

bash
Copy code
python -m venv myenv
source myenv/bin/activate
Instale las dependencias requeridas en el archivo requirements.txt:

Copy code
pip install -r requirements.txt
Ejecución
Ejecute las siguientes instrucciones en su terminal para correr la aplicación:

Copy code
python manage.py migrate
python manage.py runserver
Uso
La aplicación incluye las siguientes rutas:

/restaurantes/: Devuelve una lista de todos los restaurantes registrados.
/restaurantes/<id>/: Devuelve información específica de un restaurante con el id proporcionado.
Además, también se pueden realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en los restaurantes.

Validaciones
La aplicación incluye las siguientes validaciones en los datos de entrada:

El nombre del restaurante debe ser una cadena de caracteres.
La identificación de usuario debe ser un número.
La fecha de pago no puede ser un día par según el decreto de administración.
El valor pagado debe estar entre 1 y 1000000.
El valor del menú no puede ser negativo.
Documentación
Para obtener más información sobre cómo utilizar esta aplicación, consulte la documentación en línea en [django-rest-framework-restaurant](https://github.com/<username>/django-rest-framework-restaur
