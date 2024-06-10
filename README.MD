Lo q tienes q hacer para halar el proyecto.


1 - instalar python

2 -  crear el entorno virtual.

> py -m venv venv

3 - Acceder al entorno

> .\venv\Scripts\activate

4 - Instalar las dependencias

> pip install -r requeriments.txt

5 - inicializar la base de datos.

> cd virtual_store
> py manage.py makemigrations
> py manage.py migrate

6 - crear un super usuario

> py manage.py createsuperuser

7 run

>py manage.py runserver