Pérez Camacho Nayeli Fernanda
Cohorte 21

AUTOMATIZACIÓN DE PRUEBAS DE LA APLICACIÓN WEB

En el siguiente proyecto, 
se ejecutan pruebas autoatizadas para 
la aplicación Urban Routes. 
Se agrega punto de partida y de destino, 
se selecciona un tipo de vehículo y se hacen 
solicitudes especifcas para así,
solicitar el mismo.


Tecnología usada en el código.
En la automatización de pruebas de software:
El código utiliza la biblioteca selenium para automatizar la interacción
con un navegador web (Chrome).
 Selenium es una herramienta ampliamente utilizada para
 probar aplicaciones web.
Las importaciones expected_conditions, WebDriverWait, Options, y Service 
son todas partes de la tecnología Selenium.

En programación se muestra en:
El código está escrito en Python, un lenguaje de programación de alto nivel.
La estructura del código, las importaciones, y el uso de clases y funciones
son todos conceptos fundamentales de la programación.

Para la navegación web:
El código interactúa con un navegador web, por ende, el uso de tecnologías web 
como HTML, CSS y JavaScript (a pesar de no verse directamente en este fragmento).

En los sistemas operativos:
Para que todo esto se ejecute, es necesario un sistema operativo que corra el 
navegador chrome, y python.

Control de versiones:
El código no lo muestra, sin embargo, se usa Git, una herramienta de control
de versiones.

Básicamente, el código utiliza tecnologías de automatización de pruebas, 
programación y navegación web para interactuar con una aplicación web.

Tecnicas aprendidas y aplicadas en el código
Automatización de pruebas de interfaz de usuario (UI):
La técnica central es la automatización de pruebas de UI utilizando Selenium.
Conlleva escribir código para simular las acciones de un usuario en un navegador
web como hacer clic en botones, ingresar texto y verificar la presencia de elementos.

Técnicas de espera explícita:
El código utiliza WebDriverWait y expected_conditions para implementar esperas explícitas.

Técnicas de localización de elementos:
El código utiliza localizadores (como XPath y selectores CSS) para identificar
elementos en la página web. 

Técnicas de manejo de logs:
La función retrieve_phone_code, hace uso de la lectura de los logs del 
navegador para obtener información que de otra forma no se podría obtener.

Técnicas de refactorización de código:
La creación de la clase UrbanRoutesPage, ayuda a la refactorización del código,
para que sea mas fácil de mantener y de leer.

Pasos para ejecutar las pruebas.
1) Reiniciar el servidor Urban Routes.
2) Copiar la URL
3) Pegar la URL en "data.py"
4) Ejecutar la pruebas DE "main.py"
5) Abrir la terminal
6) Ejecutar pytest -v para ver detalles de estado de pruebas

