import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Pensamiento Computacional",
    page_icon="💻",
    layout="wide"
)

#st.title("Pensamiento Computacional")

st.sidebar.title("Pensamiento Computacional")

with st.sidebar:
    opciones = option_menu("Temas de clase: ",["Introducción","Mi primer código en Python", 
            "Variables", "Tipos de datos", "Operadores aritméticos", "Cadena de caracteres", "Listas", 
            "Expresiones booleanas", "Declaraciones condicionales", "Bucles", "Diccionarios", "Librerías", "Abrir archivos"] , 
        icons=['0-circle','1-circle', '2-circle', '3-circle', 'calculator', 'alphabet', 'list', '7-circle', '8-circle', '9-circle', 'braces', 
               'collection', 'file-earmark-arrow-up'], menu_icon="filetype-py", default_index=1)

if opciones == "Introducción":
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué es programar? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Una forma sencilla de entender qué es programar es pensar en una receta de cocina. 
    Por ejemplo, para preparar pasta seguimos una secuencia de instrucciones: primero hervimos agua, luego agregamos la pasta,
    después esperamos aproximadamente diez minutos y finalmente colamos. 
    Esta secuencia ordenada de pasos para lograr un objetivo es lo que en programación se conoce como un algoritmo.
    
    Un algoritmo, por tanto, no es algo exclusivo de las computadoras, 
    sino una forma estructurada de resolver un problema mediante instrucciones claras y ordenadas.

    Programar implica desarrollar habilidades como:
    * Descomponer un problema grande en partes más pequeñas y manejables.
    * Establecer una secuencia lógica u ordenada de acciones.
    * Definir qué hacer según ciertas condiciones.
    * Identificar repeticiones o similitudes que permitan simplificar el problema.
    * Lograr que una tarea repetitiva pueda ejecutarse de forma automática.
    
    En este sentido, programar no solo consiste en escribir código, sino en aprender a pensar de manera estructurada para resolver problemas de forma 
    eficiente.
    """)

    st.write("")
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué NO es programar? ❌</h2>', unsafe_allow_html=True)
    st.write("""
    Existen muchas ideas equivocadas sobre lo que significa programar. 
    Programar no consiste en memorizar grandes cantidades de código ni en conocer fórmulas complejas. 
    Tampoco implica necesariamente ser bueno en matemáticas, ni saber muchos lenguajes de programación. 
    Del mismo modo, no es una actividad exclusiva de ingenieros ni requiere escribir instrucciones complicadas o incomprensibles.

    Más bien, programar es una habilidad que puede aprender cualquier persona interesada en resolver problemas de manera estructurada. 
    Se trata principalmente de organizar ideas, pensar con lógica y encontrar formas claras de dar instrucciones paso a paso para alcanzar un objetivo.
    """)

    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué es Python? 💻</h2>', unsafe_allow_html=True)
    st.write("""
    Python es un lenguaje de programación que permite convertir ideas en instrucciones que una computadora puede ejecutar. 
    Fue creado por Guido van Rossum y presentado en 1991. 
    Se trata de un lenguaje de programación de alto nivel, diseñado para ser sencillo, claro y fácil de leer.

    Python puede considerarse como un puente entre el lenguaje humano y el lenguaje de las máquinas, 
    ya que su sintaxis se parece mucho al lenguaje natural. 
    Gracias a esta característica, su aprendizaje suele ser más accesible en comparación con otros lenguajes de programación, 
    especialmente para estudiantes que no provienen de áreas técnicas.
    
    Entre sus principales características destacan:
    * su sintaxis clara que permite comprender el código con relativa facilidad,
    * muchas de sus instrucciones se parecen a expresiones del inglés cotidiano,
    * Python es una herramienta muy utilizada en el análisis de datos y la investigación académica,
    * permite analizar textos, estudiar patrones lingüísticos y procesar lenguaje natural,
    * facilita el análisis de grandes volúmenes de información y la automatización de procesos de análisis.
    
    En este sentido, Python no solo es una herramienta técnica, sino también un recurso que permite a investigadores
    desarrollar nuevas formas de analizar información y resolver problemas mediante el pensamiento computacional.
    """)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Botón que abre el popup
        if st.button("Ver más sobre Python"):
            
            @st.dialog("Python")
            def show_info():
                
                col4, col5, col6 = st.columns([1,2,1])
    
                with col5:
                    st.image("https://upload.wikimedia.org/wikipedia/commons/6/66/Guido_van_Rossum_OSCON_2006.jpg", width=250)
                             
                    st.markdown("""
                    <p style="text-align:center; font-size:14px;">
                    Guido van Rossum <br>
                    Creador de Python
                    </p>
                    """, unsafe_allow_html=True)
        
                st.markdown("""
                🔗 Página oficial de [Python](https://www.python.org/)
                """)
        
            show_info()

    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A"> Entornos de programación en Python ⌨</h2>', unsafe_allow_html=True)
    st.write("""
    Antes de escribir nuestro primer programa, es importante conocer algunos 
    entornos donde podemos escribir y ejecutar código Python. Cada uno tiene 
    ventajas según el tipo de trabajo que queramos realizar.
    """)

    # VS CODE
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E"> Visual Studio Code</h2>', unsafe_allow_html=True)

    st.write("""
    **Visual Studio Code (VS Code)** es un editor de código fuente gratuito y 
    multiplataforma desarrollado por Microsoft.
    """)
    st.markdown("""
    **Características principales:**
    - Es un programa ligero y rápido  
    - Permite instalar extensiones (Python, JavaScript, R, C++, etc.)  
    - Permite manejar carpetas y archivos fácilmente  
    - Integra una terminal  
    - Permite personalizar apariencia y atajos  
    - Integra GitHub para control de versiones  
    """)

    col7, col8, col9 = st.columns([1,2,1])
    with col8:
        # Botón que abre el popup
        if st.button("Ver más sobre VS Code"):
            
            @st.dialog("Visual Studio Code")
            def show_info():
                
                col10, col11, col12 = st.columns([1,2,1])
    
                with col11:
                    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9E5HZlsBUfIyQdZy53DBNd5c9aIxECWdFww&s", width=250)
        
                st.markdown("""
                🔗 Página oficial de [VS Code](https://code.visualstudio.com)
                """)
        
            show_info()

    st.write("")
    
    # COLAB Y JUPYTER
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Google Colab y Jupyter Notebook</h2>', unsafe_allow_html=True)
    
    st.write("""
    **Google Colaboratory (Colab)** y **Jupyter Notebook** son entornos 
    interactivos muy usados en ciencia de datos, investigación y educación.
    """)
    # Crear un diccionario con las características de Google Colab y Jupyter Notebook
    colab_vs_jupyter = {
        "Google Colaboratory (Colab)": {
            "Acceso": "Es accesible desde cualquier dispositivo con internet.",
            "Almacenamiento": "Se integra con Google Drive para guardar y cargar archivos a la nube.",
            "Recursos": "Proporciona GPU (tarjeta gráfica) y TPU (procesador) gratuitas con ciertas limitaciones.",
            "Instalación": "No requiere instalación, solo una cuenta de Google.",
            "Colaboración": "Permite compartir y editar notebooks en tiempo real.",
            "Restricciones": "Límites de tiempo de ejecución y desconexión automática."
        },
        "Jupyter Notebook": {
            "Acceso": "Se ejecuta en la computadora del usuario.",
            "Almacenamiento": "Los archivos se guardan en el sistema local.",
            "Recursos": "Depende del hardware del usuario.",
            "Instalación": "Requiere instalación con Anaconda o VSCode.",
            "Colaboración": "No tiene colaboración en tiempo real sin herramientas externas.",
            "Restricciones": "No tiene límite de tiempo de ejecución, depende del equipo."
        }
    }

    # Convertir a DataFrame
    df = pd.DataFrame(colab_vs_jupyter)

    # Mostrar en Streamlit
    st.dataframe(df)

    col13, col14, col15 = st.columns([1,2,1])
    with col14:
        # Botón que abre el popup
        if st.button("Ver más sobre Colab y Jupyter"):
            
            @st.dialog("Notebooks: Colab y Jupyter")
            def show_info():
                
                col16, col17, col18 = st.columns([1,2,1])
    
                with col17:
                    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvyuHWMd6UOi4d_oVuHTBZsGvS7kG6TFK2yQ&s", width=250)
                    st.image("https://images.seeklogo.com/logo-png/35/1/jupyter-logo-png_seeklogo-354673.png", width=250)
        
                st.markdown("""
                🔗 Dónde descargar [Colab](https://workspace.google.com/marketplace/app/colaboratory/1014160490159?hl=es)
                
                🔗 Página oficial de [Jupyter](https://jupyter.org)
                """)
            show_info()
            
    st.write("")
    
    # VIDEO
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Video: Google Colab y Jupyter Notebook</h2>', unsafe_allow_html=True)
    col19, col20, col21 = st.columns([1,1.5,1])
    with col20:
    # Insertar un video explicativo de los entornos: VSC y Jupyter
        st.video("https://www.youtube.com/watch?v=IVMNhciviwc")

elif opciones == "Mi primer código en Python":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Mi primer código en Python</h2>', unsafe_allow_html=True)
    
    st.divider() ## Separador
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">¿Dónde programamos?</h2>', unsafe_allow_html=True)
    st.write("""
    Podemos usar Python en:
    
    **Notebooks (Colab, Jupyter):**
    - El archivo completo se guarda como .ipynb
    - La estructura del archivo presenta dos tipos de celdas: texto y código
    - Ejecutamos por celdas de código
    - El resultado se observa debajo de la celda código
    
    **VS Code:**
    - Ejecutamos el archivo completo (.py)
    - La estructura del archivo solo presenta líneas de código donde se puede explicar el proceso a través del formato de comentarios (#)
    - El resultado se observa en la terminal
    """)
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Función print() ▶️</h2>', unsafe_allow_html=True)
    st.code("print('¡Hola Mundo!')", language='python')
    st.markdown(f"La función `print()` permite mostrar la información en la pantalla.")

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Función help() 🆘</h2>', unsafe_allow_html=True)
    st.code("help(print)", language="python")
    st.markdown(f"Esta función permite consultar en la documentación de Python.")

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">¿Cómo escribir comentarios? #️⃣</h2>', unsafe_allow_html=True)
    st.code("""# Este es un comentario
    print("Hola")
    """, language="python")

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Errores en Python ❌</h2>', unsafe_allow_html=True)
    st.code("print(Hola)", language="python")
    st.markdown(f"Esto genera un error porque faltan comillas.")

    ###

    # Encabezado
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">¿Qué está ocurriendo aquí?</h2>', unsafe_allow_html=True)

    # Contenido del texto
    st.write("""
    Usamos la función `print()` para imprimir el texto `'¡Hola Mundo!'` en la pantalla (output). 
    Es decir, la función `print()` muestra la cadena de caracteres (argumento) dentro de sus paréntesis (simples o dobles) en la pantalla.

    **Nota:** Una función es un bloque de código que realiza una tarea específica. 
    Las funciones reciben entradas (llamadas argumentos, es decir, los valores que se introducen dentro de una función) y generan salidas. 
             
    En este caso, la función `print()` toma el texto `'¡Hola Mundo!'` como entrada y devuelve el mismo texto como salida, 
    que se muestra en la pantalla.
             
    """, unsafe_allow_html=True)

    col22, col23, col24 = st.columns([1,2,1])

    with col23:
    
        if st.button("Resolver ejercicios"):
            
            @st.dialog("Ejercicios: Primer programa en Python")
            def show_info():
                
                st.header("Quiz rápido")
    
                p1 = st.radio(
                    "1. ¿Qué función permite mostrar texto en pantalla?",
                    ["input()", "print()", "help()", "show()"],
                    key="p1"
                )
    
                p2 = st.radio(
                    "2. ¿Cómo consultamos ayuda sobre una función?",
                    ["info()", "help()", "doc()", "manual()"],
                    key="p2"
                )
    
                p3 = st.radio(
                    "3. ¿Cómo se escribe un comentario?",
                    ["// comentario", "# comentario", "/* comentario */"],
                    key="p3"
                )
    
                p4 = st.radio(
                    "4. ¿Qué error hay aquí?\n\n print(Hola)",
                    ["SyntaxError", "NameError", "TypeError"],
                    key="p4"
                )
    
                st.divider()
    
                col25, col26, col27 = st.columns([1,2,1])
    
                with col26:
    
                    if st.button("Revisar respuestas"):
                        
                        puntaje = 0
    
                        if p1 == "print()":
                            puntaje += 1
    
                        if p2 == "help()":
                            puntaje += 1
    
                        if p3 == "# comentario":
                            puntaje += 1
    
                        if p4 == "NameError":
                            puntaje += 1
    
                        st.subheader(f"Puntaje: {puntaje}/4")
    
                        if puntaje == 4:
                            st.success("Excelente")
                            st.balloons()
    
                        elif puntaje >= 2:
                            st.info("Vas bien")
    
                        else:
                            st.warning("Revisa el material y vuelve a intentar")
    
            show_info()
            
if opciones == "Variables":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Variables en Python</h2>', unsafe_allow_html=True)
    
    # Insertar vido
    st.video("https://youtu.be/wDqPp41z90E")

    # Ejemplos de creación de variables
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Ejemplos de variables</h3>', unsafe_allow_html=True)

    codigo_13 = """
    # Sintaxis: nombre_variable = valor
    # nombre_variable es la etiqueta
    # = es la asignación
    # valor es cualquier tipo de dato de Python

    # Creamos una variable sin error de nombre
    perro = "guau"
    print(perro)

    # Error de nombre: antes de ejecutar el nombre de una posible variable 
    # debes crearla y asignarle un valor
    print(gato)

    # ¿Cuál sería el valor de la variable perro "guau" o "sonido de perro"?
    perro = "sonido del perro"
    print(perro) 
    # Las variables conservan el último valor asignado a la variable
    """
    st.code(codigo_13, language = 'python')

    # Display the graph in Streamlit
    st.write("""
        En Python, una variable es un espacio que almacena un valor. Para asignar un valor a una variable, usamos el símbolo `=`. 
        Por ejemplo, `numero = 14` asigna el valor `14` a la variable `numero`. Recuerda que el nombre de la variable puede ser cualquier palabra, pero no puede comenzar con un número. 
        Además, no puede contener espacios ni caracteres especiales. Revisa las palabras reservadas de Python para asegurarte de que el nombre de tu variable no sea una palabra reservada: 
        [Palabras reservadas en Python.](https://www.w3schools.com/python/python_ref_keywords.asp) 
        Los valores pueden ser cadena de caracteres, enteros, flotantes, booleanos, listas, etc.
        """, unsafe_allow_html=True)

if opciones == "Tipos de datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Tipos de datos en Python</h2>', unsafe_allow_html=True)

        # Crear el gráfico
    data_types_graph = graphviz.Digraph('data_types')

        # Configuración global
    data_types_graph.attr(rankdir='TB', fontsize='12')
    data_types_graph.attr('node', fontname="Arial", fontsize='12', shape='box', style='filled', fillcolor='lightgray')
    data_types_graph.attr('edge', color='gray')

        # Definir nodos con colores diferenciados
    data_types_graph.node('Texto', label='Texto', color='firebrick2')
    data_types_graph.node('Números', label='Números', color='purple')
    data_types_graph.node('Booleanos', label='Boolean\n(bool)\n booleanos', color='deeppink')

    data_types_graph.node('String', label='String \n(str)\n cadena de caracteres', color='crimson')
    data_types_graph.node('Int', label='Interger\n(int)\n número entero', color='blue')
    data_types_graph.node('Float', label='Float\n(float)\n número decimal', color='blue')

    data_types_graph.node('True', label='True', color='coral')
    data_types_graph.node('False', label='False', color='coral')

    data_types_graph.node('cadena1', label='"¡Hola Mundo!"', color='red')
    data_types_graph.node('cadena2', label='"2025"', color='red')
    data_types_graph.node('cadena3', label='"@gmail.com"', color='red')

    data_types_graph.node('entero', label='7', color='cyan')
    data_types_graph.node('decimal', label='3.14', color='darkolivegreen1')
        # Define edges
    data_types_graph.edge('Texto', 'String')
    data_types_graph.edge('Números', 'Int')
    data_types_graph.edge('Números', 'Float')
    data_types_graph.edge('Booleanos', 'True')
    data_types_graph.edge('Booleanos', 'False')

    data_types_graph.edge('String', 'cadena1')
    data_types_graph.edge('String', 'cadena2')
    data_types_graph.edge('String', 'cadena3')

    data_types_graph.edge('Int', 'entero')
    data_types_graph.edge('Float', 'decimal')

        # Mostrar en Streamlit
    st.graphviz_chart(data_types_graph)

# Breve explicación de los tipos de datos
    st.write("""
        - **String (str)**: Son cadenas de caracteres que contienen letras, números y símbolos. En una conversión solo los caracteres numéricos se convierten en integer o float.
        - **Integer (int)**: Son números enteros, como `7` o `-3`. Estos pueden convertirse a float, pero no al revés. 
        - **Float (float)**: Son números decimales, como `3.14` o `-0.5`. Estos pueden convertirse a int, pero se pierde la parte decimal.
        - **Boolean (bool)**: Valores de verdad, que pueden ser `True` o `False`. Estos son útiles para condiciones y comparaciones.
        """, unsafe_allow_html=True)
    # Ejemplos de cada tipo de dato con variables
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Ejemplos de tipos de datos</h3>', unsafe_allow_html=True)

    codigo_3 = """
        # Variables de diferentes tipos de datos
        curso = "Python"  # Cadena de caracteres (str)
        ciclo = 2025         # Número entero (int)
        crédito = 3.5         # Número decimal (float)

        # Imprimir los tipos de datos
        print("Tipo de dato de curso:", type(curso))
        print("Tipo de dato de ciclo:", type(ciclo))
        print("Tipo de dato de crédito:", type(crédito))
        """
        # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_3, language='python')


if opciones == "Operadores aritméticos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Operadores aritméticos en Python</h2>', unsafe_allow_html=True)

    # Breve explicación de los operadores en una tabla con Streamlit

        # Crear un diccionario con los operadores y su descripción
    operadores = {
            "Operador": ["+", "-", "*", "/", "//", "%", "**"],
            "Descripción": [
                "Suma",
                "Resta",
                "Multiplicación",
                "División",
                "División entera",
                "Módulo (resto de la división)",
                "Potencia"
            ]
        }
        
        # Convertir a DataFrame
    df_operadores = pd.DataFrame(operadores)
        
        # Mostrar en Streamlit
    st.dataframe(df_operadores)

    # Agregar ejemplos con variables
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Ejemplos con operadores aritméticos</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_4 = """
        # Variables de diferentes tipos
        nombre = "Liam"  # Variable de tipo str
        apellido = "Payne"  # Variable de tipo str

        edad = 25         # Variable de tipo int

        altura = 1.68     # Variable de tipo float

        # Operaciones con variables
        suma = edad + 5           # Suma
        multiplicacion = altura * 2  # Multiplicación
        nombre_completo = nombre + apellido  # Concatenación de strings

        # Imprimir resultados
        print("Suma:", suma)
        print("Multiplicación:", multiplicacion)
        print("Usuario:", nombre_completo)
        """

# Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_4, language='python')

    # Explicación del ejemplo
    st.write("""
        En este ejemplo:
        - `nombre` y `apellido` son variables del tipo **str** que almacenan una cadena de caracteres cada una.
        - `edad` es una variable de tipo **int** que almacena un número entero.
        - `altura` es una variable de tipo **float** que almacena un número decimal.
        - Se realizan operaciones aritméticas como suma y multiplicación con las variables `edad` y `altura`.
        - Se realiza una concatenación de cadenas con las variables `nombre` y `apellido`.
        """)

if opciones == "Cadena de caracteres":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Cadena de caracteres (str)</h2>', unsafe_allow_html=True)


    st.code("texto = 'El 22 de febrero se nos anunció que regresaríamos a Colombia.' \nprint(texto)", language='python')

    # Ejemplos de algunos métodos de cadenas de caracteres
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Ejemplos de métodos con cadenas de caracteres</h3>', unsafe_allow_html=True)
    codigo_5 = """
    # Definición de una cadena de caracteres
    texto = "El 22 de febrero se nos anunció que regresaríamos a Colombia."
    print("Texto original:", texto)   

    # Convertir a mayúsculas
    texto_mayusculas = texto.upper()
    print("Texto en mayúsculas:", texto_mayusculas)

    # Convertir a minúsculas
    texto_minusculas = texto.lower()
    print("Texto en minúsculas:", texto_minusculas)

    # Contar la cantidad de caracteres
    cantidad_caracteres = len(texto)
    print("Cantidad de caracteres:", cantidad_caracteres)

    # Contar la cantidad de veces que aparece una palabra
    cantidad_veces = texto.count("Colombia")
    print("Cantidad de veces que aparece 'Colombia':", cantidad_veces)

    # Reemplazar una palabra por otra
    cambio_texto = texto.replace("Colombia", "Perú")
    print("Texto después de reemplazar 'Colombia' por 'Perú':", cambio_texto)

    # Convertir a una lista de palabras
    lista_palabras = texto.split()
    print("Lista de palabras:", lista_palabras)

    # Verificar si empieza con un caractero o palabra específica
    empieza_con = texto.startswith("El")
    print("¿Empieza con 'El'?:", empieza_con)

    # Verificar si termina con un caractero o palabra específica
    termina_con = texto.endswith("Colombia.")
    print("¿Termina con 'Colombia.'?:", termina_con)
        """
        # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_5, language='python')
        

if opciones == "Listas":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Listas (list)</h2>', unsafe_allow_html=True)

    st.code("comunicaciones = ['comunicación audiovisual', 'periodismo', 'comunicación para el desarrollo', 'publicidad'] \nprint(comunicaciones)", language='python')
    # Breve explicación de las listas
    st.write("""
        Las listas son estructuras de datos que permiten almacenar múltiples elementos en una sola variable. 
        Se definen utilizando corchetes `[]` y los elementos se separan por comas. 
        Las listas pueden contener diferentes tipos de datos, como números, cadenas de texto y otras listas.
        """, unsafe_allow_html=True)
    
    # Ejemplo de lista en formato código
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Ejemplo de métodos con listas</h3>', unsafe_allow_html=True)
    
    codigo_6 = """
    # Definición de una lista
    frutas = ["manzana", "banana", "naranja", "uva"]

    # Acceder a elementos de la lista
    print("Primera fruta:", frutas[0])  # Accede al primer elemento
    print("Última fruta:", frutas[-1])  # Accede al último elemento

    # Modificar un elemento de la lista
    frutas[1] = "pera"
    print("Lista modificada:", frutas)

    # Acceder al indice de un elemento
    print("Índice de 'naranja':", frutas.index("naranja"))

    # Agregar un nuevo elemento a la lista
    frutas.append("mango")
    print("Lista después de agregar un elemento:", frutas)

    # Eliminar un elemento de la lista
    frutas.remove("naranja")
    print("Lista después de eliminar un elemento:", frutas)

    # Ordenar los elementos de una lista 
    numeros = [5, 2, 9, 1, 7]
    numeros.sort()
    print("Lista ordenada:", numeros)

    # Ordenar de manera inversa 
    numeros.sort(reverse=True)
    print("Lista ordenada de manera inversa:", numeros)

    # Crear una lista vacía
    lista_vacia = []
    print("Lista vacía:", lista_vacia)

    lista_vacia_2 = list()
    print("Lista vacía 2:", lista_vacia_2)

    # Contar la cantidad de elementos en una lista
    cantidad_elementos = len(frutas)
    print("Cantidad de elementos en la lista:", cantidad_elementos)

    """

   # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_6, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una lista llamada `frutas` que contiene cuatro elementos.
    - Se accede a elementos específicos de la lista utilizando índices.
    - Se modifica un elemento de la lista reemplazando `"banana"` por `"pera"`.
    - Se agrega un nuevo elemento `"mango"` al final de la lista utilizando el método `append()`.
    - Se elimina el elemento `"naranja"` de la lista utilizando el método `remove()`.
    """)


if opciones == "Expresiones booleanas":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Expresiones booleanas en Python</h2>', unsafe_allow_html=True)
            
    # Breve explicación de las expresiones booleanas
    st.write("""
        Las expresiones booleanas son expresiones que pueden ser verdaderas (`True`) o falsas (`False`). 
        Se utilizan en condiciones y comparaciones para tomar decisiones en el código. 
        En Python, las expresiones booleanas se evaluan con operadores comparativos, de pertenencia y lógicos.
        """, unsafe_allow_html=True)

    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Operadores comparativos</h3>', unsafe_allow_html=True)
    # Crear tablas de cada tipo de operadores
    operadores_comparativos = {
        "Operador": ["==", "!=", ">", "<", ">=", "<="],
        "Descripción": [
            "Igual a",
            "Distinto de",
            "Mayor que",
            "Menor que",
            "Mayor o igual que",
            "Menor o igual que"
        ],        
        "Ejemplo": [
                "5 == 5",
                "5 != 3",  
                "7 > 3",   
                "3 < 7",  
                "3 >= 5",  
                "3 <= 5"  
            ]
        }
    
    # Convertir a DataFrame
    df_operadores_comparativos = pd.DataFrame(operadores_comparativos)
    
    # Mostrar en Streamlit
    st.dataframe(df_operadores_comparativos)
    
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Operadores de pertenencia</h3>', unsafe_allow_html=True)
    # Crear tablas de cada tipo de operadores
    operadores_pertenencia = {
            "Operador": ["in", "not in"],
            "Descripción": [
                "Verifica si un elemento está presente en una lista o cadena",
                "Verifica si un elemento no está presente en una lista o cadena"
            ],        
            "Ejemplo": [
                    "'a' in 'manzana'",
                    "'b' not in 'manzana'"
            ]
        }
        
    # Convertir a DataFrame
    df_operadores_pertenencia = pd.DataFrame(operadores_pertenencia)
        
        # Mostrar en Streamlit
    st.dataframe(df_operadores_pertenencia)
        
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Operadores lógicos</h3>', unsafe_allow_html=True)
    # Crear tablas de cada tipo de operadores
    operadores_logicos = {
                "Operador": ["and", "or", "not"],
                "Descripción": [
                    "Devuelve True si ambas expresiones son verdaderas",
                    "Devuelve True si al menos una expresión es verdadera",
                    "Devuelve True si la expresión es falsa"
                ],        
                "Ejemplo": [
                    "(5 > 3) and (7 > 5)",
                    "(5 > 3) or (7 < 5)",
                    "not(5 > 3)"
                ]
        }
        
        # Convertir a DataFrame
    df_operadores_logicos = pd.DataFrame(operadores_logicos)
        
        # Mostrar en Streamlit
    st.dataframe(df_operadores_logicos)

if opciones == "Declaraciones condicionales":
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; ">Declaraciones condicionales: if-elif-else</h2>', unsafe_allow_html=True)

    # Breve explicación de las declaraciones condicionales
    st.write("""
            Las declaraciones condicionales permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.
            En Python, se utilizan las palabras clave `if`, `elif` y `else` para crear estas estructuras de control.
            """, unsafe_allow_html=True)
    
    st.markdown(f'<h3 style="font-size: 38px; text-align: center; ">Estructura básica</h3>', unsafe_allow_html=True)
    # Crear tablas de cada tipo de operadores
    estructura_basica = {
                "Palabra clave": ["if", "elif", "else"],
                "Descripción": [
                    "Evalúa una condición y ejecuta el bloque de código si es verdadera",
                    "Evalúa una condición alternativa si la anterior es falsa",
                    "Ejecuta el bloque de código si todas las condiciones anteriores son falsas"
                ],        
                "Ejemplo": [
                    "if x > 5:",
                    "elif x == 5:",
                    "else:"
                ]
        }
        
        # Convertir a DataFrame
    df_estructura_basica = pd.DataFrame(estructura_basica)
            
        # Mostrar en Streamlit     
    st.dataframe(df_estructura_basica)

    # Ejemplo de declaración condicional
    st.markdown(f'<h3 style="font-size: 38px; text-align: center; ">Ejemplo de declaración condicional</h3>', unsafe_allow_html=True)
        # Código de ejemplo
    codigo_7 = """
    # Definición de una variable
    edad = 18

    # Declaración condicional
    if edad < 18:
        print("Eres menor de edad.")
    elif edad == 18:
        print("Tienes 18 años.")
    else:
        print("Eres mayor de edad.")
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_7, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una variable llamada `edad`.
    - Se utiliza una declaración condicional para verificar si la edad es menor, igual o mayor a 18.
    - Dependiendo del resultado, se imprime un mensaje diferente.
    """)

if opciones == "Bucles":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Bucles for y while</h2>', unsafe_allow_html=True)

    # Breve explicación de los bucles
    st.write("""
            Los bucles permiten ejecutar un bloque de código varias veces. 
            En Python, los bucles más comunes son `for` y `while`. 
            El bucle `for` se utiliza para iterar sobre una secuencia (como una lista o una cadena), 
            mientras que el bucle `while` se ejecuta mientras una condición sea verdadera.
            """, unsafe_allow_html=True)
    
    # Una tabla con la estructura básica de los bucles
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Estructura básica</h3>', unsafe_allow_html=True)

    # Crear tablas de cada tipo de operadores
    estructura_bucle = {
                "Palabra clave": ["for", "while"],
                "Descripción": [
                    "Itera sobre una secuencia (lista, cadena, etc.)",
                    "Ejecuta el bloque de código mientras la condición sea verdadera"
                ],        
                "Ejemplo": [
                    "for i in range(5):",
                    "while i < 5:"
                ]
        }
        
        # Convertir a DataFrame
    df_estructura_bucle = pd.DataFrame(estructura_bucle)
    
    # Mostrar en Streamlit
    st.dataframe(df_estructura_bucle)

    # Ejemplo de bucle for
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de bucle for</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_8 = """
    # Definición de una lista
    frutas = ["manzana", "banana", "naranja"]

    # Bucle for
    for fruta in frutas:
        print("Fruta:", fruta)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_8, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una lista llamada `frutas`.
    - Se utiliza un bucle `for` para iterar sobre cada elemento de la lista.
    - En cada iteración, se imprime el nombre de la fruta.
    """)

    # Ejemplo de bucle while
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de bucle while</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_9 = """
    # Definición de una variable
    contador = 0

    # Bucle while
    while contador < 5:
        print("Contador:", contador)
        contador += 1  # Incrementa el contador en 1
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_9, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una variable llamada `contador`.
    - Se utiliza un bucle `while` para imprimir el valor del contador mientras sea menor que 5.
    - En cada iteración, se incrementa el contador en 1.
    """)

    # Funciones de control de bucles: break y continue
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Funciones de control de bucles</h3>', unsafe_allow_html=True)
    st.write("""
    Las funciones `break` y `continue` se utilizan para controlar el flujo de los bucles:
    - `break`: Termina el bucle inmediatamente.
    - `continue`: Salta a la siguiente iteración del bucle.
    """, unsafe_allow_html=True)

    # Ejemplo de uso de break y continue
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de uso de break y continue</h3>', unsafe_allow_html=True)
    # Código de ejemplo
    codigo_10 = """
    # Bucle for con break y continue
    for i in range(10):
        if i == 5:
            print("Se encontró el número 5, saliendo del bucle.")
            break  # Termina el bucle si i es igual a 5
        if i % 2 == 0:
            print("Número par:", i)
        else:
            print("Número impar:", i)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_10, language='python')
    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se utiliza un bucle `for` para iterar sobre los números del 0 al 9.
    - Si el número es igual a 5, se imprime un mensaje y se utiliza `break` para salir del bucle.
    - Si el número es par, se imprime un mensaje indicando que es par.
    - Si el número es impar, se imprime un mensaje indicando que es impar.
    """)

if opciones == "Diccionarios":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Diccionarios de Python</h2>', unsafe_allow_html=True) 

    # Breve explicación de los diccionarios
    st.write("""
    Los diccionarios son estructuras de datos que almacenan pares clave-valor.
    Se definen utilizando llaves `{}` y cada par se separa por comas.
    Los diccionarios son útiles para almacenar datos relacionados y acceder a ellos de manera eficiente.
    """, unsafe_allow_html=True)

    # Ejemplo de diccionario en formato código
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de diccionario</h3>', unsafe_allow_html=True)
    codigo_11 = """
    # Definición de un diccionario
    estudiante = {
        "nombre": "Liam",
        "apellido": "Payne",
        "edad": 25,
        "cursos": ["Python", "Java", "C++"]
    }
    # Acceder a valores del diccionario
    print("Nombre:", estudiante["nombre"])
    print("Apellido:", estudiante["apellido"])
    print("Edad:", estudiante["edad"])
    print("Cursos:", estudiante["cursos"])

    # Modificar un valor del diccionario
    estudiante["edad"] = 26
    print("Edad modificada:", estudiante["edad"])

    # Agregar un nuevo par clave-valor
    estudiante["universidad"] = "PUCP"
    print("Universidad:", estudiante["universidad"])

    # Verificar si una clave existe en el diccionario
    existe_nombre = "nombre" in estudiante
    print("¿Existe la clave 'nombre'?:", existe_nombre)

    # Obtener todas las claves del diccionario
    claves = estudiante.keys()
    print("Claves del diccionario:", claves)

    # Obtener todos los valores del diccionario
    valores = estudiante.values()
    print("Valores del diccionario:", valores)

    
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_11, language='python')
    
    

if opciones == "Librerías":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Librerías de Python</h2>', unsafe_allow_html=True)

    # Breve explicación de las funciones
    st.write(""" 
    Librerías son colecciones de funciones y métodos que permiten realizar tareas específicas sin necesidad de escribir el código desde cero.
    En Python, existen muchas librerías predefinidas que puedes importar y utilizar en tu código.
    Algunas de las librerías más comunes son `pandas`, `random`, entre otras.
    """, unsafe_allow_html=True)

    # La librería random
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Librería random</h3>', unsafe_allow_html=True)
    st.write("""
    La librería `random` se utiliza para generar números aleatorios y realizar selecciones aleatorias.
    Puedes usarla para crear juegos, simulaciones y más.
    """, unsafe_allow_html=True)

    # Código de ejemplo
    codigo_10 = """
    # Importar la librería random
    import random

    # Generar un número aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1, 10)
    print("Número aleatorio:", numero_aleatorio)

    # Elegir un elemento aleatorio de una lista
    lista = ["manzana", "banana", "naranja"]
    fruta_aleatoria = random.choice(lista)
    print("Fruta aleatoria:", fruta_aleatoria)

    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_10, language='python')


    # Uso de range()
    st.write("""
    La función `range()` se utiliza para generar una secuencia de números.
    Puedes especificar el inicio, el final y el paso de la secuencia.
    Por ejemplo, `range(1, 10, 2)` generará la secuencia `1, 3, 5, 7, 9`.
    """, unsafe_allow_html=True)

    # La librería nklt
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Librería nltk</h3>', unsafe_allow_html=True)
    st.write("""
    La librería `nltk` (Natural Language Toolkit) se utiliza para el procesamiento de lenguaje natural.
    Proporciona herramientas para trabajar con texto, como tokenización, análisis de sentimientos y más.
    """, unsafe_allow_html=True)

    ## Código de ejemplo
    codigo_11 = """
    # Importar la librería nltk
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stopwords_es = stopwords.words('spanish')

    texto = "Domingo 14 de junio de 1942
    EL VIERNES DESPERTE ya a las seis. Era comprensible, pues
    fue el día de mi cumpleaños. Pero no podía levantarme tan
    temprano y hube de apaciguar mi curiosidad hasta un cuarto para
    las siete. Entonces ya no soporté más y corrí hasta el comedor,
    donde nuestro pequeño gatito, Mohrchen, me saludó con efusivo
    cariño. Después de las siete fui al dormitorio de mis padres y,
    enseguida, con ellos al salón para encontrar y desenvolver mis
    regalos. A ti, mi diario, te vi en primer lugar, y sin duda fuiste mi
    mejor regalo. También me obsequiaron un ramo de rosas, un
    cactus y unas ramas de rosas silvestres. Fueron los primeros saludos
    del día, ya que más tarde habría bastante más. Papá y mamá me entregaron 
    numerosos regalos y mis amigos tampoco se quedaron
    atrás en materia de mimarme. Entre otras cosas me regalaron un
    libro titulado, «Cámara Oscura», un juego de mesa, muchas
    golosinas, un rompecabezas, un broche, las «Sagas y Leyendas de
    Holanda» de Joseph Cohen, otro libro encantador, «Las
    Vacaciones de Daisy en la Montaña» y algún dinero. Con éste me
    compré las leyendas mitológicas griegas y romanas. ¡Fantástico!
    Enseguida vino Lies y partimos juntas a la escuela. Comencé
    siguiendo el ritual holandés de obsequiar golosinas a mis maestros
    y compañeros de clase y luego nos pusimos a trabajar."

    texto_minusculas = texto.lower()
    texto_depurado = texto_minusculas.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("¿", "").replace("¡", "").replace("!", "").replace("?", "").replace("«", "").replace("»", "").replace("/n", "").replace("-", "").replace("_", "")
    lista_palabras = texto_depurado.split()

    lista_depurada = list()
    for palabra in lista_palabras:
        if palabra not in stopwords_es:
            lista_depurada.append(palabra)
    
    print(len(cantidad_palabras))
    print(len(lista_depurada))        
    """ 
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_11, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se importa la librería `nltk` y se descargan las stopwords en español.
    - Se define un texto en español.
    - Se convierte el texto a minúsculas y se eliminan los signos de puntuación.
    - Se genera una lista de palabras y se eliminan las stopwords.
    - Se imprime la cantidad de palabras originales y la cantidad de palabras depuradas.
    """)


if opciones == "Abrir archivos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Abrir archivos en Colab</h2>', unsafe_allow_html=True)

    # Breve explicación de cómo abrir archivos
    st.write("""
    En Google Colab, puedes abrir archivos de diferentes maneras.
    Puedes cargar archivos desde tu computadora e importar archivos desde Google Drive.
    """, unsafe_allow_html=True)

    # Ejemplo de cómo abrir archivos
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de cómo abrir archivos</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_12 = """
    # Importar la librería necesaria
    from google.colab import files
    # Importar archivos desde tu computadora
    uploaded = files.upload()
    # Mostrar el nombre del archivo subido
    with open("nombre_archivo.txt", "r") as file:
        texto = file.read()
    print(texto)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_12, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se importa la librería `files` de Google Colab.
    - Se utiliza la función `files.upload()` para cargar un archivo desde tu computadora.
    - Se abre el archivo y se lee su contenido.
    - Se imprime el contenido del archivo.
    """)

st.markdown(""" 
<hr style="margin-top:40px; margin-bottom:20px;"> 
<div style=" text-align:center; font-size:18px; color:#555; padding-bottom:20px; "> 
<p><b>Luisa Gomez</b></p> 
📩 luisa.gomez@pucp.edu.pe </br>
💻 GitHub <a href="https://github.com/4591526/" target="_blank" style="text-decoration:none; font-weight:600;"> 
4591526 </a> </div> """, unsafe_allow_html=True)

    
    


   
   
   







