<h1 align="center"> Proyecto Final - Web Universidad Central </h1>
<h2 align="center"> Proyecto WEB Django </h2>

<h3 align="left"> Descripción del proyecto </h3>
Este proyecto lo que busca es mostrar la oferta académica de una universidad asi como demás funcionalidades para el cliente, 
se pretende que la persona pueda acceder de manera sencilla a todo lo que ofrece la universidad, fácil manejo de la web y una 
amplia información de sus carreras y el cuerpo académico que dicta las clases. 

Se aclara que este proyecto está aún en desarrollo dado que además de las secciones a las que se puede acceder desde el panel principal
también se agregarán otras como "Noticias", "Admisiones", "Eventos", etc.

<h3 align="left"> :hammer:Funcionalidades del proyecto </h3>

`Funcionalidad 1`: En los formularios carreraForm2, postgradoForm y docenteForm se hizo la prueba de ingresar nuevos datos los cuales fueron agregados de manera exitosa. 
En el archivo forms.py se especificó en las tres clases (CarreraForm, PostgradoForm, DocenteForm) que uno de los datos no sea obligatorio y que permita agregar ese nuevo 
dato. Se probó y también funcionó correctamente. 

`Funcionalidad 2`: Respecto al formulario que permita buscar datos en la base de datos, se definió la opción de buscar carreras por su duracion y se 
establecido que cuando no se ingrese ningun dato se emita un mensaje. Ambas cosas funcionaron correctamente.

`Funcionalidad 3`: Cuandp se ingresa con un usuario registrado y se loguea se pueden ver los distintos enlaces en la barra superior de navegación. Si el usuario no está registrado sólo pueden ver información genérica de la web.

<h3 align="left"> Descripción de modelos </h3>
Se establecieron cuatro modelos, Carrera, Postgrado, Docente y Alumno los cuales contienen la información de la oferta educativa de la universidad y además el grupo de docentes que están en las diferentes carreras y postgrados.


<h3 align="left"> Autor </h3> 
Nicolás Garateguy

<h3 align="left"> Usuario </h3> 
Usuario administrador: nicolas //  Contraseña: nikorasu
