---
title: ["M2C6 Python Assignment"]
description: [Ejercicios control punto 6 del curso  FULL STACK]
author: [J. fernando Garrido]
ms.date: [ 03/28/2025]
---
# ¿Para qué usamos Clases en Python?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Una clase en Python es una plantilla o un plano para crear **objetos**. Define las propiedades (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella (**POO**, Programación Orientada a Objetos). Por convención, los nombres de clases deben usar *PascalCase*: mayúscula inicial en cada palabra y sin separadores. También deben tener nombres descriptivo claros de lo que representa la clase.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

### Características Principales de las clase:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Veamos las caracteísticas fundamentales de las clases sobre un ejemplo que controla los vehículos de un garaje (modelo, color, kilómetros), los kilometros realizados hoy, y los kiometros totales.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

1. ### <ins>**Abstracción**</ins>: 
   Las clases pueden ocultar detalles complejos, exponiendo solo lo esencial (interfaz), reduciendo la complejidad del código, facilitando el mantenimiento, y previniendo el acceso directo a datos críticos. (**Abstract Base Classes**) se importa al inicio del código (*from abc import ABC, abstractmethod*).Hace que el método no tenga una implementación en la clase principal (es solo una plantilla) y debe ser implementado obligatoriamente por todas las subclases que hereden de la clase principal.
  
        from abc import ABC, abstractmethod               
    ###### Obliga a las subclases a implementar los métodos marcados.
        
        class Vehiculo(ABC):                              
    ###### Hace que la clase sea abstracta (no se puede instanciar directamente).
    
2. ### <ins>**docstrings**</ins>: 
   Son cadenas de documentación que explican el propósito de módulos, clases, funciones o métodos. A diferencia de los comentarios, los docstrings son accesibles en tiempo de ejecución y se usan para generar documentación automática. 
   Van colocados entre triples comillas (`"""` o `'''`), y deben ser la primera declaración en el objeto que documentan.
  
        """    
            Clase abstracta que representa un vehículo genérico.
              Argumentos:
                color (str): Color del vehículo.        
                modelo (str): Modelo del vehículo.
                kilometraje (int): Kilometraje inicial (opcional, por defecto 0).
        """

3. ### <ins>**Encapsulación**</ins>: 
   Una clase puede agrupar datos (atributos) y comportamientos (métodos) en una sola entidad: 

        def __init__(self, color: str, modelo: str, kilometraje: int = 0): # Kilometraje inicial (opcional, por defecto 0).
          self.color = color                              
    ###### Atributo público (Acceso directo)
          self._modelo = modelo                           
    ###### Atributo protegido (convención: _nombre)
          self.__kilometraje = kilometraje                
    ###### Atributo privado (name mangling: _Clase__nombre)

    ##### Métodos privados con guiones bajos antes del nombre de la clase:
      ###### - Un guión bajo **`_`** **(Convención de <ins>"protegido"</ins>)**: Este atributo/método no debería usarse directamente, pero Python no lo bloquea. Convención para decir: *"No me uses fuera de la clase o sus subclases"*.
      ###### - Doble guión bajo **`__`** **(Name Mangling - <ins>"Privado real")</ins>**: Python altera el nombre del atributo/método para dificultar su acceso desde fuera.

          @abstractmethod
            def tipo_vehiculo(self) -> str: 
              pass             
    ###### Método abstracto que debe ser implementado por subclases.

    ##### Clases abstractas: 
      ###### - Fuerzan a las subclases a implementar ciertos métodos. Si no lo hacen, Python lanza un error.
      ###### - Pueden incluir métodos concretos (ya implementados) que las subclases heredan.
      ###### - Definen una estructura común para un grupo de clases relacionadas.
      ###### - Permiten tratar diferentes subclases de manera uniforme (polimorfismo)
      ###### - Mejoran la mantenibilidad.                                     
            
          @abstractmethod
            def conducir(self, km: int) -> str:    
              pass       
    ###### "Pass" es una palabra reservada de Python que significa "no hacer nada".Como el método es abstracto evita errores de sintaxis al dejar el bloque vacío. Las subclases deben reemplazar este pass con su propia implementación.
                       
            def obtener_kilometraje(self) -> int:         
              return self.__kilometraje
      ###### Utilizamos el método "Getter" para recoger el kilometraje privado. Este método permite acceder de forma controlada a atributos protegidos o privados de una clase.
            def actualizar_kilometraje(self, km: int) -> None:
              if km > 0:
                self.__kilometraje += km
      ###### Modifica el atributo privado __kilometraje de forma controlada. `-> None` Indica que no retorna valor (solo efecto secundario), y elcondicional asegura que solo se añadan valores positivos.

            def __str__(self) -> str:                     
      ###### Método especial que retorna objeto en formato de string.
              return f"{self.color} {self._modelo}"
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    

4. ### <ins>**Herencia**</ins>: 
   Permite crear subclases que heredan atributos/métodos de una clase padre.
  
            class Coche(Vehiculo):     

      ######  Subclase que representa un coche. Heredada de Vehiculo.

              def __init__(self, color: str, modelo: str, carroceria: str, kilometraje: int=0):
                super().__init__(color, modelo, kilometraje)  
                self.carroceria = carroceria
      ###### "super()" está invocando el método *"\_\_init\_\_ "* de la clase padre (Vehiculo) para inicializar los atributos heredados (color, _modelo, __kilometraje) y evitar la duplicación de código.

              def tipo_vehiculo(self) -> str:              
                return f"Coche tipo {self.carroceria}"

      ###### Implementación del método abstracto. *"@abstractmethod"* 

              def conducir(self, km:int) -> str: 
                self.actualizar_kilometraje(km)
                f"He conducido {km} km., por lo que el {self._modelo} ya tiene {self.obtener_kilometraje()} km. totales"          
                """
                Simula la conducción del coche y actualiza el kilometraje.
                Argumentos:
                  km (int): Kilómetros recorridos.
                Retorno:
                  str: Mensaje descriptivo.
                """
      ###### Implementación del método abstracto. *"@abstractmethod"* 

            class Moto(Vehiculo):  
      ######  Subclase que representa una Moto Heredada de Vehiculo.
              def __init__(self, color: str, modelo: str, cilindrada: int, kilometraje: int = 0):
        
                super().__init__(color, modelo, kilometraje)
                self.cilindrada = cilindrada

              def tipo_vehiculo(self) -> str:
                return f"Moto de {self.cilindrada} cc."
    
              def conducir(self, km:int) -> str:
                  self.actualizar_kilometraje(km)
                  return f"He rodando {km} km. con la {self._modelo}, por lo que hoy ya tiene {self.obtener_kilometraje()} km."

    ##### Las subclases permiten extender o modificar el comportamiento de la clase padre sin reescribir todo el código. Son fundamentales en la herencia, uno de los pilares de la Programación Orientada a Objetos (POO).
      ###### - Heredan todo: Atributos y métodos de la clase padre.
      ###### - Pueden añadir nuevos métodos o atributos.
      ###### - Pueden modificar (sobrescribir) métodos existentes.
      ###### - Son relaciones "es-un": Ej: Coche es una subclase de la clase Vehiculo; Moto es otra subclase de la clase Vehiculo.
  
            class Garage:                                   
      ###### Clase que representa un garaje que almacena vehículos.
              def __init__(self, vehiculo: Vehiculo):      
                self.vehiculo = vehiculo
      ###### Parámetro vehiculo: Está tipado como Vehiculo y solo aceptará objetos que sean instancias de Vehiculo o sus subclases (Coche, Moto, etc.).
      ###### Asigna el vehículo recibido como atributo de instancia del garaje. Ahora el garage "contiene" ese vehículo.
              def mostrar_info(self) -> str:                
      ###### Muestra información del vehículo en el garaje (polimorfismo).*"str->"* Retorna la descripción del vehículo.
  
              return (
                      f"El garaje contiene: {self.vehiculo.tipo_vehiculo()}, "
                      f"modelo {self.vehiculo._modelo}, de color {self.vehiculo.color}, "
                      f" y con un Kilometraje de {self.vehiculo.obtener_kilometraje()} km."
                    )                   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

5. ### <ins>**Polimorfismo**</ins>: 
   Es un principio muy importante en la programación orientada a objetos (POO). Permite que objetos de diferentes clases respondan de manera distinta a un mismo método o función, simplificando el código y haciéndolo más flexible. Se trata de usar una misma "interfaz" para operar sobre diferentes tipos de datos.

  
            if __name__ == "__main__":            
      ###### *"\_\_name\_\_"* es una variable especial que Python asigna automáticamente, y su valor es *"\_\_main\_\_"*: Cuando ejecutas el archivo directamente (no se importa). La condición actúa como un "guardián", ejecutando el bloque si el archivo es el programa principal; si no ese código se ignora.
                                                     
                                                     

                mi_coche = Coche(color="rojo", modelo="Mercedes", carroceria="SUV", kilometraje=12000)
                mi_moto = Moto(color="azul", modelo="Honda CBR", cilindrada=500, kilometraje=8000)
    
                garaje_coche = Garage(mi_coche)
                garaje_moto = Garage(mi_moto)
  
                print(garaje_coche.mostrar_info())  
                print(garaje_moto.mostrar_info())   

                print(mi_coche.conducir(150))  
                print(mi_moto.conducir(80))    

    #### La salida esperada al ejecutar este código es:

         El garaje contiene: Coche tipo SUV, modelo Mercedes, de color rojo,  y con un Kilometraje de 12000 km.
         El garaje contiene: Moto de 500 cc., modelo Honda CBR, de color azul,  y con un Kilometraje de 8000 km.
         He conducido 150 km., por lo que el Mercedes ya tiene 12150 km. totales
         He rodando 80 km. con la Honda CBR, por lo que hoy ya tiene 8080 km.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
### Relación entre las clases/subclases

![Relaciones entre clases](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/Relaciones%20entre%20clases.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


#### Conceptos que participan en la creación de una clase:
|<span style="color:orange">Concepto</span>|<span style="color:orange">	Descripción</span>|<span style="color:orange">Ejemplo en el código</span>|
|--------|-------------|------------------------|
|Clase	 | Una plantilla para crear objetos|	class Garage:|
|Método	 | Una función asociada a una clase|	def open_door(self):|
|Instancia|	Un objeto creado a partir de una clase|	home = Garage()|
|Objeto	  |Sinónimo de instancia. Una entidad con atributos y métodos|	home|
|Atributo|	Una variable asociada a un objeto (puede ser de instancia o de clase)|	self.color = color (en __init__)|


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

---------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El método que se ejecuta automáticamente al crear una instancia de una clase (objeto) es la función especial ***"\_\_init\_\_"***.

Este método inicializa el objeto y le asigna valores iniciales a los atributos. Recibe parámetros que personalizan cada instancia, pero no retorna nada porqué Su propósito es configurar el objeto, no devolver valores.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Su sintaxis básica sigue la siguiente estructura:

        class MiClase:
            def __init__(self, parametro1, parametro2):
                self.atributo1 = parametro1  # Asigna valores a atributos
                self.atributo2 = paramametro2
###### Se crea una clase que englobará a todos los objetos creados a partir de ella.***"MiClase"***
###### Se define la función constructora ***"\_\_init\_\_"*** y se le asignan los parámetros que compartirán todos los objetos que se creen a traves de esta clase ***"(self,parametro1, parametro2)"***. 
###### El parámetro ***"self"*** es una convención (no una palabra reservada), siempre es el primer parámetro, y hace referencia a la instacia creada (objeto). Permite acceder a los atributos y métodos de la clase, y definen cómo se configura cada objeto (color, modelo, etc.).
###### ***"self.atributo"*** permite dotar de un atributo específico a cada objeto que se instancie, y que tendrá su propio nombre. Si solo se indicaría ***"atributo1 = parametro1"*** no se guardaría en ningún sitio.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Un ejemplo con la clase Vehículo:

        class Vehiculo:
            def __init__(self, color: str, modelo: str, kilometraje: int = 0):
                self.color = color            # Atributo público
                self._modelo = modelo        # Atributo protegido
                self.__kilometraje = kilometraje  # Atributo privado

###### Se crea la clase ***"Vehículo"*** que englobará a todos los vehículos que se creen a partir de ella.
###### Se define la función constructora ***"\_\_init\_\_"*** y se le asignan los parámetros que compartirán todos los objetos que se creen a traves de esta clase ***"color"*** que será una cadena (*"str"*), ***"modelo"*** que también será una cadena (*"str"*), y ***"kilometraje"*** que será un número entero con valor inicial de cero (*"int = 0"*))".
###### ***"self.color"*** es un atributo público que guardará la variable *"color"* en los objetos que se creen, con el valor que se asigne al crearlo.
###### ***"self._modelo"*** es un atributo protegido que se escribe con un guión bajo (por convención) para indicar que no se uses fuera de la clase o subclases".
###### ***"self.__kilometraje"*** es un atributo privado que se escribe con dos guiones bajos (por convención), al que Python "ofusca" el nombre para evitar acceso directo desde fuera, aunque sigue siendo accesible si se insiste.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No es obligatorio utilizar ***"\_\_init\_\_"*** en la construcción de una clase, pero sin él los objetos se crearían vacios y se perdería el control sobre la inicalización.
Un ejemplo simple puede ser:
   - ***`__init__`*** es un proceso de ensamblaje de un coche.
   - ***`self`*** es el chasis del coche
   - Los parámetros son las piezas (ruedas, asientos, motor...)

Cuando instanciamos un objeto, el método ***`__init__`*** las instala correctamente.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Las clases y subclases se inician con el método ***`__init__`*** para crear objetos con sus atributos propios. Las sucblaes que heredan los atributos y métodos de las clases **"padre"**, deben invocar al constructor a través del método ***`super().__init__(...):`***. Primero asigna los atributos del **"padre"**, antes de asignar los suyos exclusivos.

Ejemplo de uso de ***`__init__`*** con herencia y ***`super()`***:

        class Vehiculo:
            def __init__(self, color: str, modelo: str, kilometraje: int = 0):
                self.color = color
                self._modelo = modelo
                self.__kilometraje = kilometraje

        class Coche(Vehiculo):
            def __init__(self, color: str, modelo: str, carroceria: str, kilometraje: int = 0):
                super().__init__(color, modelo, kilometraje)  
                self.carroceria = carroceria 

###### Atributo exclusivo de Coche

        mi_coche = Coche(color="rojo", modelo="Toyota", carroceria="SUV")

###### ***`super().__init__(...):`*** invoca al constructor de la clase padre **vehículo**, y le asigna los atributos de ***"color"***, ***"_modelo"*** y ***"__kilometraje"*** antes de que **Coche** añada sus propios atributos
###### Luego se ejecuta el ***`__init__`*** del hijo, que añade sus atributos exclusivos ***"carroceria2***
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
### Diagrama de flujo
![Flowchart](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/flowchart.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Cuáles son los tres verbos de API?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Los verbos de **API** (también conocidos como métodos HTTP) son fundamentales en el diseño de **APIs RESTful** (**APIs** que permiten la comunicación entre sistemas). Definen el tipo de operación que se realizará sobre un recurso (usuarios, productos, pedidos, etc.) identificado por una URL (p.ejmplo,***"/users/123"*** ). Aunque las rutas sean idénticas, la aplicación **Flask** escuchará el verbo enviado y se realizará la operación.
Estas tres operaciones principales son: 

- **POST**: Se usa para enviar datos al servidor, generalmente para crear nuevos recursos o realizar acciones que impliquen modificaciones en el servidor.
- **GET**: Se usa para obtener información de un servidor. Es el verbo más común y solo debe recuperar datos, no modificar nada.
- **PUT**: Se utiliza para actualizar o reemplazar un recurso existente en el servidor con los nuevos datos proporcionados.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### <ins>verbo HTTP POST (crear)</ins>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
El verbo HTTP **POST** se utiliza principalmente para crear nuevos recursos en el servidor. A diferencia de **PUT** (que suele usarse para actualizar), **POST** está diseñado para operaciones que agregan datos nuevos a un sistema, especialmente cuando el *"ID"* o la ubicación del recurso no son conocidos de antemano.
**POST** no es idempotente. Cada vez que se ejecuta crea un nuevo recurso en el servidor.

> Se llama operación <ins>**idempotente**</ins> cuándo al ejecutarla una o varias veces produce el mismo resultado (como si se hiciera solo una vez), es decir que el efecto final es el mismo.

Los datos se envían en el cuerpo (body) de la solicitud (generalmente en JSON, XML o form-data).

Cuándo se crea un recurso, la respuesta suele incluir el ID del recurso creado y una confirmación. La confirmación es un código HTTP del estilo: 201 Created (respuesta exitosa), 400 Bad Request (datos inválidos), 409 Conflict (Recurso ya existe), 401 Unauthorized (Falta autenticación).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### <ins>verbo HTTP **GET** (listar)</ins>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Se utiliza para solicitar datos de un recurso específico (ej: un usuario, lista de productos, etc.) sin modificarlo. Es de solo lectura y no tiene efectos secundarios en el servidor. Es decir, que es seguro e **idempotente**.

Los datos en un **GET** se envían exclusivamente en la URL, nunca en el cuerpo (body) de la solicitud. Esto es un estándar clave del protocolo HTTP. Aunque herramientas como Postman pueden permitirlo técnicamente, se considera una mala práctica. Incluso muchos servidores ignoran el body en un **GET**.
Usar **GET** con un *"ID"* en la URL es la forma estándar para recuperar un recurso específico (un solo elemento, no una lista). El *"ID"* puede ser cualquier cadena alfanumérica.

Cuándo se solicita información, la respuesta suele incluir un código HTTP de confirmación del estilo: 200 OK (La solicitud fue exitosa), 404 Not Found (El recurso no existe.), 401 Unauthorized (Falta autenticación).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### <ins>verbo HTTP PUT (actualizar)</ins>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Se utiliza para actualizar por completo un recurso existente o, en algunos casos, crearlo si no existe. A diferencia de **PATCH** (que actualiza parcialmente), **PUT** reemplaza todo el recurso con los nuevos datos proporcionados.
Si lo ejecutamos múltiples veces produce el mismo resultado (Es idempotente).
Los datos en un **PUT** van en el cuerpo.

Cuándo se reemplaza un recurso, La respuesta suele incluir  un código HTTP de confirmación del estilo: 200 OK (Actualización exitosa), 404 Not Found (El recurso a actualizar no existe), 400 Bad Request (Datos inválidos).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### Ejemplo Práctico con Flask (Python)

    from flask import Flask, request, jsonify

    app = Flask(__name__)
    vehiculos = [{"id": 1, "tipo": "Coche", "color": "rojo"}]  # "Base de datos"
###### Se importan las clases necesarias de Flask, y se crea la aplicación Flask.
###### Base de datos temporal: Lista que simula una DB, con un vehículo de ejemplo.

###### GET (Listar)Listar todos los vehículos en el garaje.
    @app.route('/vehiculos', methods=['GET'])
    def get_vehiculos():
        return jsonify(vehiculos), 200

###### POST (Crear) Añadir un nuevo vehículo (Coche o Moto) al garaje.
    @app.route('/vehiculos', methods=['POST'])
    def crear_vehiculo():
        nuevo_vehiculo = request.json
        vehiculos.append(nuevo_vehiculo)
        return jsonify({"mensaje": "Vehículo creado"}), 201

###### PUT (Actualizar) Actualizar solo el kilometraje de un vehículo mediante su id
    @app.route('/vehiculos/<int:id>', methods=['PUT'])
    def actualizar_vehiculo(id):
        for v in vehiculos:
            if v['id'] == id:
                v.update(request.json)
                return jsonify(v), 200
        return jsonify({"error": "No encontrado"}), 404
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

    if __name__ == '__main__':
        app.run(debug=True)
###### Inicia el servidor en modo desarrollo

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
> Seguridad: Nunca se debe usar GET para enviar datos sensibles, mejor utilizarlo para datos públicos, y en todo caso los datos deben ir en la URL. En el caso de PUT y POST, los datos deben ir en el cuerpo y protegidos por una validación de datos (p. ejemplo, en Python con marshmallow). Con cualquiera de las tres operaciones utilizar HTTPS.
> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Existen otros verbos HTTP como DELETE (para eliminar un recurso), PATCH (para modificaciones parciales) y OPTIONS (para obtener información sobre las capacidades de un servidor), pero los tres mencionados son los más fundamentales para interactuar con las APIs.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Tabla de Verbos HTTP y su Uso (con nuestro ejemplo del Vehículos)

|<span style="color:orange">Verbo</span>|<span style="color:orange">Descripción</span>|<span style="color:orange">Ejemplo en API de Vehículos</span>|<span style="color:orange">Código HTTP devuelto</span>|<span style="color:orange">Significado códigos HTTP</span>|
------|------------|----------------------------------|------------|-----------------------|
|GET|	Obtener recursos|	GET /vehiculos (Listar todos)|	200 OK| La solicitud fue exitosa y la respuesta contiene los datos solicitados|
|GET|	Obtener un recurso específico|	GET /vehiculos/{id} (Detalles de un coche)|	200 OK / 404 Not Found|El recurso solicitado no se encuentra en el servidor|
|POST|	Crear un recurso|	POST /vehiculos (Añadir nuevo vehículo)|	201 Created|La solicitud fue exitosa y un nuevo recurso ha sido creado|
|PUT|	Reemplazar un recurso|	PUT /vehiculos/{id} (Actualizar todos los datos)|	200 OK|La solicitud fue exitosa y la respuesta contiene los datos solicitados|
|PATCH|	Actualizar parcialmente|	PATCH /vehiculos/{id} (Modificar solo el color)|	200 OK|La solicitud fue exitosa y la respuesta contiene los datos solicitados|
|DELETE|	Eliminar un recurso|	DELETE /vehiculos/{id} (Borrar un vehículo)|	204 No Content|La solicitud fue exitosa, pero no hay contenido para devolver (eliminación)|



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Es MongoDB una base de datos SQL o NoSQL?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MongoDB** es una base de datos <ins>**NoSQL**</ins> (no relacional) de tipo documental, diseñada para almacenar y gestionar datos flexibles y escalables. A diferencia de las bases de datos **SQL** tradicionales, **MongoDB** no usa tablas con filas y columnas, sino colecciones de documentos en formato JSON-like

- No requiere una estructura fija (como las tablas en SQL). Cada documento puede tener campos diferentes dentro de una misma colección.
- Distribuye datos en múltiples servidores para manejar grandes volúmenes. Ideal para aplicaciones con crecimiento rápido.
- Soporta consultas similares a SQL, pero con sintaxis JSON.
- Optimizado para operaciones de lectura/escritura rápidas. Usa índices para acelerar búsquedas.
- Permite transformar y analizar datos con pipelines (Recibe los documentos procesados en la etapa anterior **->** Aplica una operación: filtrado, cálculo, agrupación, etc. **->** Pasa el resultado a la siguiente etapa.)

Sus usos más comunes están en Aplicaciones web/móviles (cuando los datos cambian frecuentemente), Big Data y análisis en tiempo real, contenido gestionado por usuarios (ej: redes sociales, comentarios), catálogos de productos (ej: e-commerce con atributos variables).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Ejemplo en el proyecto de vehículos con MongoDB (usando Python con pymongo):

    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
###### Conexión a una instancia local de MongoDB
    db = client["garaje"]
        coleccion = db["vehiculos"]
###### Usa la base de datos llamada "garaje" (la crea si no existe).
###### Accede a la colección "vehiculos" (también se crea automáticamente si no existe).
    documento = {
        "tipo": "Coche",
        "color": "rojo",
        "modelo": "Toyota",
        "carroceria": "SUV",
        "kilometraje": 12000
    }   
    coleccion.insert_one(documento) 
###### Inserta un documento con esta estructura.
Resultado esperado:

    {
    "_id": ObjectId("5f8d3a7b2c1d1e2f3a4b5c6d"),  // ID autogenerado
    "tipo": "Coche",
    "color": "rojo",
    "modelo": "Toyota",
    "carroceria": "SUV",
    "kilometraje": 12000
###### La colección vehiculos tendrá un nuevo documento como este (MongoDB añade automáticamente un campo _id único):
En la consola de Python:

    print(coleccion.insert_one(documento))
###### El método insert_one() devuelve un objeto InsertOneResult que confirma la inserción, con una salida: 

    <pymongo.results.InsertOneResult object at 0x7f8c3a7b2c1d>
Para ver el ID del documento insertado:

    resultado = coleccion.insert_one(documento)
    print(resultado.inserted_id) 

    Ej: 5f8d3a7b2c1d1e2f3a4b5c6d  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

**MongoDB** es ideal si necesitamos almacenar vehículos con atributos variables (ej: diferentes campos para coches vs motos). Pero si necesitamos hacer consultas complejas con relaciones (ej: vehículos + dueños + talleres), una **SQL** podría ser mejor.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Qué es una API?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Una API (Application Programming Interface, o Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permite que diferentes sistemas o componentes de software se comuniquen entre sí. Actúa como un "intermediario" que facilita el intercambio de datos y funcionalidades sin necesidad de conocer los detalles internos del otro sistema.

Imaginemos una API como el menú de un restaurante:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

![Interacción con API](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/Interacción_API.png)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

1. El cliente. Es quien consume la API (frontend, móvil, otro servicio). Solo necesita saber qué puede pedir (endpoints) y cómo interpretar la respuesta (JSON, XML), sin preocuparse por la lógica interna.
    ###### El cliente mira el menú (API documentation) y pide un plato de "Pizza" (request)
    ###### Técnicamente, el cliente (frontend/app) envía una solicitud HTTP a la API. (GET https://api.restaurante.com/pizzas/1, para obtener la pizza con ID 1).
    
2. El menú (API). Representa la documentación de la API, donde se definen los endpoints (platos disponibles), los parámetros de entrada (ingredientes del pedido) y el formato de respuesta (cómo se sirve el plato). Como una app móvil que muestra datos de usuarios obtenidos de la API.
    ###### El camarero (API) recibe el pedido y lo lleva a la cocina (backend)
    ###### Técnicamente, la API valida el request (¿existe el endpoint? ¿tiene permisos el cliente?).
    ###### Deriva la solicitud a la cocina (backend) (servidor, bases de datos, etc.).

3. La cocina (backend). Es el servidor que procesa las solicitudes: valida datos, consulta la base de datos, aplica reglas de negocio y envía la respuesta. El cliente no interactúa directamente con la cocina, solo con la API.
    ###### La cocina (backend) procesa el pedido. El chef preparan la pizza con los ingredientes correctos.
    ###### Técnicamente, el backend ejecuta lógica: consulta la base de datos (SELECT * FROM pizzas WHERE id = 1), aplica reglas de negocio (ej: "Si no hay queso, rechazar pedido").    
    ###### Deriva la solicitud al backend (servidor, bases de datos, etc.).

4. La cocina devuelve el plato (response) a la API.
    ###### El chef entregan la pizza al camarero.
    ###### Técnicamente, el backend envía los datos en un formato específico (ej: JSON) a la capa de la API.
    ###### Ejemplo de respuesta:
        { "id": 1, "nombre": "Margarita", "precio": 10.99 }
5. La API entrega la respuesta al cliente.
    ###### El mesero lleva la pizza a la mesa del cliente.
    ###### Técnicamente, la API estructura la respuesta (código HTTP, headers, cuerpo), y envía un status code (ej: 200 OK si todo sale bien, 404 si no existe la pizza).

6. Cliente recibe y procesa la respuesta.
    ###### El cliente recibe su pizza y decide qué hacer (comerla, quejarse si está fría, etc.).
    ###### Técnicamente, el frontend muestra los datos (ej: renderiza la pizza en la UI), maneja errores (ej: muestra "Pizza no encontrada" si recibe 404).

#### Características de una API:
- ***Lenguaje-agnóstica***: Que puede ser consumida por clientes desarrollados en cualquier lenguaje de programación, sin importar qué tecnología se usó para construirla. Es como un idioma universal que cualquier sistema puede entender. (Python, JavaScript, etc.).Diferentes sistemas (móvil, web, IoT) pueden integrarse sin problemas.

- ***Protocolos comunes***: Utiliza estándares ampliamente adoptados en la industria para la comunicación entre sistemas, lo que garantiza interoperabilidad, compatibilidad y facilidad de integración. Estos protocolos son reglas y convenciones técnicas que definen cómo se transmiten y estructuran los datos entre el cliente y el servidor. Los más utilizados son: HTTP/HTTPS (para APIs RESTful y SOAP), WebSockets (comunicación en tiempo real), gRPC (alto rendimiento), GraphQL (flexibilidad en consultas)...

- ***Autenticación***: Es el proceso de verificar la identidad de un cliente (usuario, app o servicio) antes de permitirle acceso a recursos.  Los métodos más usados son: 
    -  API Keys: Es una clave única (string aleatorio) que identifica al cliente. Se suele usar en APIs públicas como servicios de clima, Google Maps.
    -  Tokens JWT (JSON Web Tokens): Un token firmado que contiene datos del usuario para autenticación en apps web/móviles (tras login con usuario/contraseña).
    - C. OAuth 2.0: Protocolo para autorización delegada (ej: "Iniciar sesión con Google").
    - Autenticación Básica (Basic Auth): Envía usuario y contraseña en cada request (codificado en Base64).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

# ¿Qué es Postman?
![postman](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/postman.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postman es una herramienta que permite probar APIs REST de forma sencilla, simulando peticiones HTTP como GET, POST, PUT, DELETE, entre otras. Se usa mucho en desarrollo y pruebas de APIs porque facilita la interacción con los endpoints sin necesidad de escribir código.

Qué se puede hacer con Postman:
- Enviar peticiones HTTP (GET, POST, PUT, DELETE, etc.) y ver las respuestas del servidor.
- Automatizar pruebas de API con scripts y colecciones
- Documentar y compartir colecciones de endpoints.
- Probar APIs en desarrollo sin necesidad de un frontend.
- Gestionar entornos (development, production, etc.).

 ¿Cómo usar Postman?
Una vez descargado Postman: https://www.postman.com/downloads/
1. Abrir Postman y crear una nueva solicitud (New Request).
2. Elegir el método HTTP (GET, POST, PUT, DELETE, etc.).
3. Ingresar la URL de la API (por ejemplo, http://127.0.0.1:5000/vehiculos).
4. Agregar cuerpo (Body) en JSON si la solicitud lo necesita (en métodos POST o PUT).
6. Hacer clic en "Send" 
7. Respuesta en Postman, indicando el Id del registro que hemos hecho.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![cmd_post](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/Postman_post.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Respuesta del servidor en cmd , con el código HTTP de confirmación 201.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

![cmd_post](https://github.com/Fern-69/M2C6-Python-Assignment/raw/main/cmd_post.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Qué es el polimorfismo?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Polimorfismo es uno de los cuatro pilares de la Programación Orientada a Objetos (POO) que permite que objetos de diferentes clases respondan al mismo método o función de manera específica a cada clase. Esto permite escribir código más flexible y reutilizable.
**"Una interfaz, múltiples formas"**: Diferentes objetos pueden compartir el mismo nombre de método, pero su implementación varía según la clase.

Veamos un ejemplo simple:

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

###### Define la clase base Vehiculo con un constructor que recibe marca, modelo y año. Todos los vehículos compartirán estos atributos.

    def arrancar(self):
        raise NotImplementedError

###### Método ***arrancar()*** es abstracto. Las subclases deben implementarlo (<ins>POLIMORFISMO</ins> obligatorio).

    def describir(self): 
        return f"{self.marca} {self.modelo}, del año {self.año}"

###### Método común para todos los vehículos. Retorna una descripción formateada.

class Coche(Vehiculo):
    def arrancar(self):
        return "¡Motor encendido!"

###### Implementa ***arrancar()*** con un comportamiento específico para coches.
###### <ins>POLIMORFISMO</ins>. Mismo método implementado en la clase **Vheiculo** (Padre), y definido particularmente por la clase **Coche** (Hijo)

>Mismo nombre de método: Tanto Vehiculo como Coche tienen un método llamado ***arrancar()***.
>Comportamiento específico: Coche redefine el método con su propia implementación (retorna "¡Motor encendido!").
>Relación con la "clase Padre":
    >- La clase Vehiculo obliga a sus subclases a implementar arrancar() (con NotImplementedError).
    >- Coche cumple con este "contrato" al proporcionar su versión del método.

    def abrir_maletero(self):
        return "¡Maletero abierto!"

###### Método exclusivo de la calase **Coche**.

class Moto(Vehiculo):
    def arrancar(self):
        return "¡Moto en marcha!"

###### Esto es <ins>POLIMORFISMO</ins>: misma interfaz (nombre del método), distinta implementación.

    def probar_luces(self):  # Corregido el nombre del método (de provar_luces a probar_luces)
        return "¡Luces probadas!"

###### Método exclusivo de la clase **Moto**.

class Garaje:

    def __init__(self):
        self.vehiculos = []

###### Constructor inicializa una lista vacía para almacenar vehículos.

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"OK... {vehiculo.describir()} añadido al garaje.")

###### Añade un vehículo a la lista y muestra un mensaje. Usa el método común ***describir()*** de la clase **Vehículo** (Padre).    

    def probar_vehiculos(self):
        print("\n---- Probando todos los vehículos ----")
        for vehiculo in self.vehiculos:
            print(f"\nProbando {vehiculo.describir()}:")
            print(vehiculo.arrancar())

###### Itera sobre todos los vehículos y llama a sus métodos polimórficos, ***describir()*** (común a todos) y ***arrancar()*** (cada vehículo responde diferente).

            if isinstance(vehiculo, Coche):
                print(vehiculo.abrir_maletero())
            elif isinstance(vehiculo, Moto):
                print(vehiculo.probar_luces())

###### verifica si un objeto es instancia de una clase. Retorna ***`True`*** si vehiculo es una instancia de la clase Coche, o retorna ***`False`*** en caso contrario.

mi_coche = Coche("Toyota", "Corolla", 2022)
mi_moto = Moto("Yamaha", "MT-07", 2023)

###### Instancias de la clase **Coche** y de la clase **Moto**. Cada una tiene su propia implementación de ***arrancar()***.

mi_garaje = Garaje()
mi_garaje.agregar_vehiculo(mi_coche)
mi_garaje.agregar_vehiculo(mi_moto)
mi_garaje.probar_vehiculos()

###### Crea un garaje: Añade los vehículos (usa polimorfismo en ***agregar_vehiculo()***) y prueba todos los vehículos (demuestra polimorfismo en ***probar_vehiculos()***).


### Tipos de polimorfismo:

1. <ins>Polimorfismo de Sobreescritura (Overriding)</ins>
Ocurre cuando una subclase redefine un método de su clase padre.

######
    class Vehiculo:
        def arrancar(self):
            return "¡En marcha!"

    class Coche(Vehiculo):
        def arrancar(self):  

###### Sobreescribe el método de la clase Padre

            return "¡Coche en marcha!"

    class Moto(Vehiculo):
        def arrancar(self):  
###### Sobreescribe el método de la clase Padre
            return "¡Moto en marcha!"

    vehiculos = [Coche(), Moto()]
    for vehiculo in vehiculos:
        print(vehiculo.arrancar())  
    
###### Salida esperada: ¡Coche en marcha!  ¡Moto en marcha!

2. <ins>Polimorfismo por Interfaces (Duck Typing)</ins>
Python usa >"Si camina como pato y suena como pato, es un pato">:
donde diferentes objetos comparten un método con el mismo nombre sin heredar de una clase común.
###### Clases totalmente independientes (sin herencia)
    class Perro:
        def hacer_ruido(self):
            return "¡Guau!"

    class Coche:
    def hacer_ruido(self):
        return "¡Brummm!"

###### Función que acepta <ins>CUALQUIER</ins> objeto con el método ***hacer_ruido()***
    def escuchar(objeto):
        print(objeto.hacer_ruido())

    escuchar(Perro())  # Salida: ¡Guau!
    escuchar(Coche())   # Salida: ¡Brummm!

3. <ins>Polimorfismo de Sobrecarga (Overloading)</ins>
Cuando el mismo método maneja distintos casos según los parámetros.
######
    class Calculadora:
        def suma(self, a, b, c=None): 
            if c is None:
                return a + b
            else:
                return a + b + c

calc = Calculadora()
print(calc.suma(2, 3))     
print(calc.suma(2, 3, 4))  
###### El método ***suma()*** tiene diferentes salidas según los parámetros que recibe.

4. <ins>Polimorfismo de Coerción</ins>
Cuando un tipo se convierte automáticamente para operar con otro:

###### El operador **`+`** funciona con números y cadenas 
    print(3 + 5)      
###### 8 (suma)
    print("3" + "5")  
###### "35" (concatenación)

5. <ins>Polimorfismo Paramétrico (Genéricos)</ins>
Funciones que trabajan con múltiples tipos sin especificarlos.

######
    def primer_elemento(lista):
        return lista[0]

    print(primer_elemento([1, 2, 3]))        # 1
    print(primer_elemento(["a", "b", "c"]))  # "a"
###### La misma función trabaja con listas de cualquier tipo.

6. <ins>Polimorfismo con Clases Abstractas</ins>
Sobre el ejemplo inicial, la clase abstracta ***Garaje*** tiene el método ***arrancar()*** (abstracto) para realizar acciones comunes que tanto un coche como una moto puedan realizar, pero cada uno tendrá su propia implementación.

    class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

###### Define la clase base **Vehiculo** con un constructor que recibe marca, modelo y año. Todos los vehículos compartirán estos atributos.

    def arrancar(self):
        raise NotImplementedError

###### Método ***arrancar()*** es abstracto. Las subclases deben implementarlo (<ins>POLIMORFISMO</ins> obligatorio).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
En resumen: El polimorfismo hace que el código sea flexible y escalable, permitiendo que objetos diversos respondan a una misma acción de formas distintas.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Qué es un método dunder?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Del inglés "double underscore", o "doble guión bajo", un método dunder en Python es un método especial que tiene nombres encerrados entre dobles guiones bajos (__metodo__). Estos métodos definen comportamientos específicos de una clase y son invocados automáticamente por Python en ciertas situaciones. También se les llama "métodos mágicos".

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Invocación Automática: Python los llama automáticamente en situaciones específicas, sin necesidad de invocarlos directamente.
Sobrecarga de Operadores: Permiten definir cómo responden los objetos a operadores como +, -, ==, etc.
Personalización de Comportamientos: Controlan acciones como representación de cadenas, gestión de contextos, Iteración...
Convención de Nombres: Siempre tienen doble guión bajo al inicio y al final (__método__).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

A diferencia de _método "protegido" (un guión bajo), y __método "privado" (doble guión bajo), los Dunder son públicos:

    class Ejemplo:
        def metodo_normal(self):    
            return "Hola"
   ###### Método estándar
        def __str__(self):          
            return "Soy un objeto"
   ###### Método Dunder
    obj = Ejemplo()
    print(obj.metodo_normal())
   ###### Llamada manual: ***"Hola"***
    print(obj)                  
   ###### Llamada automática a __str__: ***"Soy un objeto"***


Ejemplos de métodos dunder comunes:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

|Método|	Descripción|
|------|---------------|
|__init__|	Se ejecuta cuando se crea una nueva instancia de la clase (constructor)|
|__str__|	Define cómo se muestra el objeto cuando se usa print(objeto).|
|__repr__|	Similar a __str__, pero más detallado (útil para depuración).|
|__len__|	Define qué devuelve len(objeto).|
|__getitem__|	Permite acceder a elementos como si fuera una lista (obj[index]).|
|__setitem__1	Permite modificar elementos con obj[index] = valor.|
|__delitem__1	Permite eliminar elementos con del obj[index].|
|__add__1	Personaliza el operador + entre objetos.|
|__eq__1	Personaliza el operador ==.|
|__lt__1	Personaliza < (menor que)|

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

------------------------------------------------------------------------------------------------------------------------------
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


# ¿Qué es un decorador de python?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Los decoradores permiten modificar o extender el comportamiento de funciones o clases sin cambiar su código original. Actúan como "envoltorios" que añaden funcionalidad extra.
Reciben una función/clase como argumento, y devuelven una nueva función/clase modificada.
Su sintaxis es: ***@nombre_decorador***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Los decoradores se clasifican principalmente por su uso y estructura. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
|Tipo|	Descripción|	Ejemplo|
|----|-------------|-----------|
|Funciones|	Modifican funciones|	@decorador|
|Clases|	Afectan clases completas|	@añadir_metodo1
|Con argumentos|	Personalizables con parámetros|	@validar_rango(1, 10)1
|Anidados|	Múltiples decoradores en cascada|	@decorador1 @decorador2|
|Built-in|	Integrados en Python|	@property, @staticmethod|
|Registro|	Almacenan funciones en diccionarios|	@registrar("nombre")|
|Depuración|	Debugging y profiling|	@contar_llamadas|
|Autenticación|	Control de acceso|	@requiere_login|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

Ejemplos con los decoradores principales:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
### <ins>@staticmethod</ins>: Útil para métodos que no necesitan acceder a la instancia (self) ni a la clase.

    class Calculadora:
        @staticmethod
        def sumar(a, b):
            return a + b

    print(Calculadora.sumar(3, 5))  
   ###### Salida: 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

### <ins>@classmethod</ins>: Accede a la clase  en lugar de la instancia (self).

    class Pizza:
        def __init__(self, ingredientes):
            self.ingredientes = ingredientes

    @classmethod
        def margarita(cls):
            return cls(["queso", "tomate"])
###### Por convención, el primer parámetro de un **@classmethod** siempre se llama ***"cls"*** (abreviatura de class), y se refiere a la clase misma (Pizza en este caso), no a la instancia.
    @classmethod
        def hawaiana(cls):
            return cls(["queso", "piña", "jamón"])

    pizza1 = Pizza.margarita()
    print(pizza1.ingredientes)  

   ###### Output: ["queso", "tomate"]
###### Cuando llamas ***"cls(["queso", "tomate"])"***, estás invocando al constructor ***\_\_init\_\_*** de la clase.
###### Equivale a hacer **Pizza(["queso", "tomate"])**, pero es más flexible (funciona incluso con herencia).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

### <ins>@property</ins>: Define ***getters***, ***setters*** y ***deleters*** de atributos de forma elegante.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

    class Termostato:
    def __init__(self, temperatura):
        self._temperatura = temperatura  # Atributo "privado"

    @property
    def temperatura(self):
        print("Leyendo temperatura...")
        return self._temperatura
###### **@property** (getter): Permite leer ***\_temperatura*** como si fuera pública (termo.temperatura). Añade lógica adicional (ej: imprimir un mensaje al leer).
    @temperatura.setter
    def temperatura(self, valor):
        if not (0 <= valor <= 100):
            raise ValueError("La temperatura debe estar entre 0°C y 100°C")
        print(f"Cambiando temperatura a {valor}°C")
        self._temperatura = valor
###### **@temperatura.setter**: Valida que la nueva temperatura esté entre 0°C y 100°C. Si es válida, actualiza _temperatura; si no, lanza un error.
    termo = Termostato(25)
    print(termo.temperatura)  
###### Salida: Leyendo temperatura... \n 25
    termo.temperatura = 30    
###### Salida: Cambiando temperatura a 30°C
###### termo.temperatura = -5  # ❌ ValueError



































































Decorador en Python es una herramienta poderosa que permite modificar o extender el comportamiento de funciones o clases sin alterar su código original. Actúa como un "envoltorio" (wrapper) que añade funcionalidad adicional. Aquí te lo explico con ejemplos basados en tu proyecto:

Un decorador es una función que recibe otra función/clase como argumento y devuelve una versión modificada de ella.

🛠 Sintaxis básica:
python
Copy
@decorador  # ← Así se aplica
def funcion():
    pass
(Equivale a: funcion = decorador(funcion))

📌 Ejemplos prácticos:
1. Decorador para medir tiempo de ejecución:
python
Copy
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)  # Llama a la función original
        print(f"Tiempo: {time.time() - inicio:.2f}s")
        return resultado
    return wrapper

@medir_tiempo
def calcular_kilometraje(km):
    time.sleep(1)  # Simula procesamiento
    return km * 1.6  # Conversión a millas

print(calcular_kilometraje(100))  # Output: Tiempo: 1.00s \n 160.0
2. Decorador de validación (para tu API):
python
Copy
def validar_color(func):
    def wrapper(color, modelo):
        if color.lower() not in ["rojo", "azul", "verde"]:
            raise ValueError("Color no permitido")
        return func(color, modelo)
    return wrapper

@validar_color
def crear_coche(color, modelo):
    return {"color": color, "modelo": modelo}

crear_coche("rojo", "Toyota")  # ✅
crear_coche("rosa", "BMW")     # ❌ ValueError
💡 Decoradores nativos comunes:
Decorador	Función	Ejemplo en tu proyecto
@property	Define getters elegantes	@property def modelo(self): return self._modelo
@classmethod	Métodos de clase (no de instancia)	@classmethod def desde_dict(cls, data):
@staticmethod	Funciones estáticas (sin self/cls)	@staticmethod def validar_km(km):
@abstractmethod	Obliga a implementar métodos (ABC)	@abstractmethod def conducir(self):
🌟 Decorador de registro para tu Garage:
python
Copy
def loggear_vehiculo(func):
    def wrapper(*args, **kwargs):
        print(f"🚗 Registrando vehículo: {args[1:]}")
        return func(*args, **kwargs)
    return wrapper

class Garage:
    @loggear_vehiculo
    def agregar_vehiculo(self, tipo, color):
        pass

mi_garaje = Garage()
mi_garaje.agregar_vehiculo("Coche", "rojo")  # Output: 🚗 Registrando vehículo: ('Coche', 'rojo')
⚠️ Errores comunes:
Olvidar ejecutar el wrapper:

python
Copy
def decorador(func):
    def wrapper():
        print("Antes")  # ❌ Falta llamar a func()
    return wrapper  # No hace nada con la función original
No preservar metadatos:
Usa functools.wraps para mantener el nombre/docstring:

python
Copy
from functools import wraps
def decorador(func):
    @wraps(func)  # ✅ Preserva metadatos
    def wrapper():
        pass
    return wrapper
📚 ¿Por qué son útiles?
Reutilización: Aplicas la misma lógica a múltiples funciones (ej: validación, logs).

Legibilidad: Separas preocupaciones (la función principal no se ensucia con código adicional).

Mantenibilidad: Cambias el comportamiento en un solo lugar (el decorador).

🎨 Analogía:
Imagina un decorador como un filtro de Instagram para funciones:

La foto original (función base) no cambia.

El filtro (decorador) añade efectos (loggear, validar, medir tiempo).
