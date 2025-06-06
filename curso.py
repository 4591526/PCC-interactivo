import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz

#st.title("Pensamiento Computacional")

st.sidebar.title("Pensamiento Computacional")
opciones = st.sidebar.selectbox("Selecciona la clase que deseas ver:",["Mi primer programa en Python", 
            "Variables", "Tipos de datos", "Operadores aritméticos", "Cadena de caracteres", "Listas", 
            "Expresiones booleanas", "Declaraciones condicionales", "Bucles", "Diccionarios", "Librerías", "Abrir archivos"] )

if opciones == "Mi primer programa en Python":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Mi primer programa en Python</h2>', unsafe_allow_html=True)
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")
    

    # Descripción general
    st.code("print('¡Hola Mundo!')", language='python')

    st.write("""
    <p style='text-align: justify;'>
    Al aprender a programar en Python, se acostumbra comenzar con un ejemplo sencillo como se indica antes. 
    Esta línea de código nos enseña cómo imprimir una cadena de caracteres (string) en el output (salida), además de 
    cómo ejecutar un código dentro de las celdas de un notebook (Google Colab o Jupyter) o 
    en un script de Python en VSCode que ejecutará su visualización en el terminal (output).
    </p>
    """, unsafe_allow_html=True)

    # Cargar la imagen desde una URL o archivo local
    image_csv = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAToAAAChCAMAAABgSoNaAAAA2FBMVEX///8krPIAhNAAbbAAdLYAhtEfn/AkrvMipvIAd7klsPMjqvIAgM8AjNQgovEAebr3+/0Aj9UAcLLW5/JyxPeT0/kAaa8AfM0hpPGZw97x9/uCtdYAZKsms/S61+nj8PYAX6qnyeB1rtIPjNrH3u03ib8AbsVgnck/kMNVm8mSwNwafbno8vjS5fG/2usAd8tqqNAAdLzC5forgrtOlcVZs+lMvvh3yvex3fg8nNIgj8leqta84vlDufWL0fhIodJtuuYtnNqbz+0uoNuEwOQmjtBstOEAWafbIBkiAAAQd0lEQVR4nO2dC2ObOBLHaUS6cRsbGTZKeAQChfIQpmyh2+51t9ukae/7f6OTxBuE7ez1Lm3Qf7NujEGIHzOjGRSDJAkJCQkJCQkJCQkJCQkJCQn9WIKOpqWP3YmfUtrdu79+f//Beex+/HzK/vhNXV1dX/8q4D1Q9r9kWUbqy+vr698FvIfILVaKoshoTdBdv/j9QnvsDv000jElt5LB9pqxu/79YvfYffopBE2FklNWao2usjwB76AMryJH0FUO28J7+9hd+8GV5kotYnU9dHTA+CTg7ZH2UenQUat7wVTD++v9n4/dwR9Wu3i1ashVVveiE4P3q7A8rvxy1Rld3+r68D7Bx+7mD6jsD0UZoRuSq+h9eux+/niy/8XSudUsuhrgX8JnR6pKiM7q5Bl0L67fP3ZXfzCNyO1B9+LXx+7rDyWYKENye9D9IqyuJ8OckCPogEB3UKm3GpFj1b+wuoNycg65PehErGukfZySI0bH0P0i0O3R7u8puAqdtWiHhalxYI1dJHPcdS+6RViddv/u89u98HxKjqd5h322BHR/3q6JPu+ZWrALPjhCrkLH0QLQwQ+36+12u371tz+3ilvM2BxBp1KHXSY6eMfIEb26/cB1Wqgrc+QoOrV8d/1siejg3bYmRwxve8+ZTCUlhLxi7DgvsrzKnQ8veOSePfER1rjvyFHDezdxWsNbMXLsR5bZGxLhqt9lGZuGdPGS57Avn7bVwbs+OMruiztcw/EqRquK16qBVr2sIps0wkf3xK1udztCN3ZaUnzJe5TTaVeC7tlUT93q/jwdk1uvtx87p93F+8jhhP15GB/dsyeOLlv3ta3/bZ3WL/eRo85KtUx0zrv1emByFcHtPTMnUkLsUdgY5zLRSf7t6Zqj7UcSxOwAqLPgFLMNiQtFJ739wmf3xXULBNQ5doHdTbMuFZ3k89mtb7FlEXRceGrcT//46F6ePXl00u4d3+7WJ8hCPHhqz1mpZqxuAejIWMG3u+0puEEAgCE8VS7c4d9ELBidlH7joiOGJxOnreCpLbloXKsRdFwtAZ1kfF7znXZ7zpy2x07xJlcIFo1Oku63M07LAl5rd+rYWakWjk6623LREaf9zergRRln06Wjk+5uT6nWp62qXwm7yvCArOTc70bAizMeuUUME5U+UHbrNfuh3NY1u8ZpVazz/9qQj+5sQejo7E5la+ue6TF2p8Rp1aban4ig47JbEDrp7bt166sDesRpVW92woyi42lJ6KDZGtx6FPa2X+e/SwIvrpaOzjCxdbJtmQ0sj9S07twcNw8dCXVXy0GXmqplWSejQNczvPuZrwwvHp3jkfwDWdZvM+xOqot4HM047GLQOSFN3dAedqfrV7ecWoKi2ywZnRaTxA3Udnc6w27GaZdtdbuSlVqN3c2zW3OclqDjsVsGOj8CoM8OzLI7Pf0ycdolW50dIFrcV+gYO3QyM1aQ/ydOu2B0bsHIMR1iR+ltvw0Li+Wi05WOHENXsTtnJsZlt74dlLNkhL3aXE20eeroYCKDhlqHDlko/jIb7k5Pb+97pQVNThirzaZ9WQA6w5TZtbihEFiZqfbufNZnT7cfu0t31OoaXPXLGTHDJ44O6uoUHEGH6TCafj4/mdWrzmkrdH0xI3z+tNHtCo7NARD5LAGB9/PoyGiR1FkKvHi+oX7KfjbN6+aJo7MtDjjVa7IPeH+6B972W7UeQVfTothagk8cXTY1OtS/jg7vt3ucdn3LZnlqdFctvwrhE0fnlBN2gT+oFu7W8+zOT7Z3sEZ3VQ+sm3aofeLoJL8YgpPzcX3/4eseuztZE+euY91mYHRP3uqIywZ9ckoyvar05x525+entzvpoqF11Yf35NE1pX/lrNxJL//2fEYE3fnlV/vubDBCXC0i1lGxC07MWcOZu/ftbufs7vL88vLN+e1Zl5J07BaAjl7mJKUXol8emZHz9/l5MzIM/ZWie/3qbBLsSG6yBHRSmmNFmZ2hZmt8nPPZFt2A3vOnn9fVglni7r9DrvFtL7qp0S0F3REihcUln13fYZ9vOvMT6BrNsKsdttOmfRHoGsG79ZTdZR/dpvf6XFhdT/Du64RdD93m+UgCXU8fvr6Z+uvIYQU6vuzbNzyrmxicQDeVT9ldsh/2j0B3vLQ/KK5z+sPAMYcV6I6S8+1yoFl0m4vH7uoPp/Tb+VHofhGPApjI+Nxn9+Y1H92ZuMspR8b9ycFYJ+7pzJeRrN/U5LhWt/n1rXjezoxoUdaGujE6Au7QLd0WrQ/E7rjoNu8FuAPKvr55M0V39l4T914/KP/rGN1GgDtS2u0bQq5Ft3kpwB0t548O3eaXT+KBTg9Q+vHy9evXlwTcs0+idniYjM/r81ebsxcXAtyDBd9evH9/J8AJCQkJCQkJCQkJCQkJCQkJCQn9E/0PJg/+j/MRjzn1YcfcWwv9N8pi9/BK30dmfMTfFEA/mxyik9F5E8P5b45dRyZnc6jpJpH7Tya0oA489ouRPmhrmNoJ3ameGUdvF6EjZo6cQp6cyxCYhmREvC8PHi0uul1Y33RCjh8+bw91xNA5sTr/RanpVlmIm/uDYN7Z5OoodFKMolFHsgJlkuQrVvSd0bkFwiE5/14pN/s0HgChRpcVVnn0FIWWy0AOPGp1MVbL74vOVdTRap4Vk64ZcTFzn9ajxEFHTknMdgWhU0cJJ/aObrFBl3r46JiXBQh7GqxuzQDto93oOHRpAYYtpqWlV7s6toM8TdEZuTX5LqdvhUe32KB7QMfIyRp8l+/7xjpiZKAYeI0r4/kbjR6tKbpsVUzucP2P0B0tLWL+8w90JDpbkQePw8gt7zukFVN0LidE/U/RQdMKZh/OuF9HojMC0O+SH4DKxnt+YTip02QEA3fpvzFSx+myIR66UbJENs4IOghZK7PtSrRdY85hYZqmDj8J8xVZ537Q9NYZj1GQLqStD9CR9idr1jIB7n2SoLLazG2eMJK6XlmWYbKjje6SXqqrmc2DbwzfzeM4Dt1mlzx00SAQQNtMchTQnMtNJUNPuk4Yut68gTs9LOM4dx2pQZd5bTuObcZlXIY6J1E0yHA3N347tkd6W+Zu37iMzKQLPdvoo9PI/suS7p8jTZG7WGqEN0nV5xJVS7XYAkFQqDcsbiQg6Ppjo7B6s/MUSy3ISlZZH9YUnY+HGaSRI3rrE3ozMcJUK5TuMDQlaE6bji2ZNCxbcebW6Mx/t08fiy2Ead8srE8oacWc0UG7tAAOogJYUWcIqQdoYxgBLy0bdNANLIXsH1glz/dhBMK2ARsr1TowrhzXKa1A11Jy8tnd+HW1lwbaal69iW6K3N05Oz2yynQGnZHfDIe7LEk8FOhJkriG5AS4hw7X6AwPrFjDbogKrw4s5o3b9NWKzEwjn+YrNEmTMyvgByyoKyjWMy31kxiBJgNzQgt7tuZkSYm8okYHEyDT/ftJgALe4OmqRWuOplXTaNC5Vr2NoRmz6IKwHjx9rCYz6CS/sMbP3+iGCT66RG2SS8NT5RG6DKOwMQ4dg2QMyCo5xyqxTLZ5gIqRqGp1Oknq1JxYJ1YAqBq2Aa57rJWWx3H/FKuNaWsRqk9pjY64ldlfN+Gia2/9TUa1CgavmrCJ8ecDuz+ALitA63PQQ0N0RoTC3rCkFkOPIqEunx4qbZwMi90hmCBgjbhWt70ToAqdE6jtCbGxzHFZmKOmRHFBY5c1ujQepgR8q+vko8pj+TVsrt4ESS/gHkBHjj7tLRyic1e96EjDwdDsDFKJTw+V9syKej0wAmYraSD3Nk9k5rBkTO8dbGjxQmcG6n6TDjT7a61umHodQqfh6uzxr5wYemCBsot4+9FpEegFR8JigC5EeX8PLhrWKkbOR5fGw+WeSpvxUdDbWgsYOqNU+zzB5GDpOoVaNZdh3HS2iXU2GpSMfIdt5bhKwTbjoyOGZyokHDe2tB+drfQDPQnZfXQwAIPixC/w4P0cOk0ZFjW2TFIzYl8DA6mSk1Tu9Yl4bMRJUEgcidgviRW2UatGl+YWNrsWZtE5tp7kIRnw96OjmQECTX20H52O+ncbg21ywtA5GAwGUK1UB7eeaY10pN3Avmg7ckoHoQHnCt1OVcykVa5g3oi9U7HPdo+6sFyjk5wcgajNQmfQZXmEVctSgugQOtKgqaI6G9qPLrnpl4RtNVGh22E8QJCGQ3TQ4xd5u9HACxm6fJhzVuhslaWdjSwuOiNip8gGXdHXopMMN7JQYdb5GhddUlg4NN1sp9n4IDrJMJuUYD8686afD4zQkXUG9ZcxQkeHA14PHoROMfvSeQUfTFAAyYm66Wy8Q0edMQZqVUZx0SWyTLJmWB01PoiO5hVViD+Ibt7qtANWJ/kA824eRdANOmbMo3NBAQfiHowmK660K5SugT46ann1tdmBw7qIodsVarvd7girI0dft/KgWDccJrQCDNDtohEph5wfzq7HsW6HlXQyplToNLXgjKljGSEZYgbXNobo2F3A6Xtb7qFLbhg6XS7b7ZpzvR9dMkFHEtWu0NkhNpi5cjTI3IbJSYAGhmLLo0qJlBMFJ4nViuFFZl0lRTnxun5gdKrkJMUK7xl6Y9ko0HKrh36MLi0tCsOnJ6k9mKpqM7uMh/ThGKubojMiq+smKf4oOj/o+6AzSok9EPZtoq0gW2kFCqdWQzo9GHlLQDtqD2zRxVVeF/MH6ZFI6PBw/yyN0Uk5Q0dSwHYxKSJZd70OHUkmj0EXgybWtYGnap7JiesDyXs4iL8O0ZFyuddBP5jO7Lkq4NSdNuondrYiU0pO0ctOYFwXYi4qOKncWIYH8CA2NOiayUsjvqHvYQ5Koz1CVDtsUTtWmgN1Dl3aBQNbUave+6BNMxO5qauI5daLbdxe2KC/q8PyPwdF689OaIWT8Q+aAIT9hAJWfexdriY1OxuKqLe0dmPKdfmfBqg7d5o9N62doWHZ0NSwee4QetAgdTJrzldATgdTqMW4VFjLJDTEDlmHLFLiYgYdNAOXtESUJrgxU42UjhAa9PQQj43pBUvysRIVtfuYSNXph9BwFTyKdVIaIWyzT+GuRJPn8DIgABVJtVdoaEll6rsABRlkrfoBqs+dUxJ3gfQgHE8NcX3RyVZQyCbUYOoWs/McTjAoi1t0IcJx4iYRaK6HknNSmLabYzWx63CjYxRVizy/Tk4Sa4IOARx7nhdiYgtpc2wWzr2AXR/NCoQ91zUjUuQ2F51IxgEi07XNAGBXH1/q3JWqGpD9JrGC+LechW4BgFKSvXp5oKpx1aUsAHKZkO1KGbQDESkH1FK39RyD0imterGrIJxXS8HsxDlM8LDmy1lIIDtX2LNu277BpJBV8h9OyNHWscQNZLpO4RI7qp7s6uLxpKfmBYpMJ+GVoLuk64QrsmHlVVm0IntSiSU7UXOGoV7vjKzi1h1M2qhmsK7Qj805i9DMQKnm/le4veDlmJj1RG4SfbYwx2xXdFnYZkpZpFR7iO09sXv0UZMBGhmt4Pp/mZK69Mqu01tHMmyyyDZ6i3jXTXZ0w2Rw/3C4S9q/QDEyPUnYNEN/SontjK3SLOx3he434U8ctHulF6ITPYPjQ6g63HXFYbtKpcH+Idv8wA1GhYSEhISEhISEfkb9B4OPb3SZVoTJAAAAAElFTkSuQmCC"  

    # Crear tres columnas, la del medio contendrá la imagen para centrarla
    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.empty()  # Columna vacía para la alineación

    with col2:
        st.image(image_csv,  width=300, use_container_width=True)

    with col3:
        st.empty()  # Columna vacía para la alineación

    # Descripción general
    st.write("""
    <p style='text-align: justify;'>
    Visual Studio Code (VS Code) es un editor de código fuente ligero y rápido, 
    ideal para quienes saben otros lenguajes de progración, incluyendo quienes recién están aprendiendo Python.
    Es fácil de usar y muy popular entre programadores. 
    </p>
    """, unsafe_allow_html=True)

    # Display text block
    content = st_monaco(
        value="# Escribimos nuestro primer programa en Python \nprint('¡Hola Mundo!')",
        height="100px",
        language="python",
        lineNumbers=True,
        minimap=False,
        theme="vs-dark",)
    if st.button("▶️"):
        if "print('¡Hola Mundo!')" in content:
            st.markdown(f"¡Hola Mundo!") 
        else:
            st.markdown(f"**SyntaxError:** Parece que escribiste algo incorrecto. Asegúrate de usar `print('¡Hola Mundo!')` en tu código.")

    st.divider() ## Separador

    image_colab = "data:image/png;base64,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"

    # Crear tres columnas, la del medio contendrá la imagen para centrarla
    col4, col5, col6 = st.columns([1, 1.5, 1])

    with col4:
        st.empty()  # Columna vacía para la alineación

    with col5:
        st.image(image_colab,  width=300, use_container_width=True)

    with col6:
        st.empty()  # Columna vacía para la alineación

    # Crear un diccionario con las características de Google Colab y Jupyter Notebook
    colab_vs_jupyter = {
        "Google Colab": {
            "Acceso": "Es accesible desde cualquier dispositivo con internet.",
            "Almacenamiento": "Se integra con Google Drive para guardar y cargar archivos a la nube.",
            "Recursos": "Proporciona GPU y TPU gratuitas (con ciertas limitaciones).",
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

    # Bloque de texto en un box
    st.markdown(
    """
    <div style="
        padding: 10px;
        background-color: #fefefb;
        font-weight: bold;
        font-size: 18px;">
        La función print()
    </div>
    """,
    unsafe_allow_html=True,
    )
            
    # Bloque de código con comentario explicativo
    codigo = """# Este programa imprime un mensaje en la pantalla
    print('¡Hola Mundo!')"""

    # Mostrar código en bloque con resaltado de sintaxis
    content_2 = st_monaco(
        value=codigo,
        height="120px",
        language="python",
        lineNumbers=True,
        minimap=False,
        theme="jupyter",)

    # Display both code blocks together
    if st.button("▶️", key="run_button"):
        if "print('¡Hola Mundo!')" in content_2:
            st.markdown(f"¡Hola Mundo!") 
        else:
            st.markdown(f"**SyntaxError:** Parece que escribiste algo incorrecto. Asegúrate de usar `print('¡Hola Mundo!')` en tu código.")

    # Encabezado
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">¿Qué está ocurriendo aquí?</h2>', unsafe_allow_html=True)

    # Contenido del texto
    st.write("""
    Usamos la función `print()` para imprimir el texto `'¡Hola Mundo!'` en la pantalla (output). 
    Es decir, la función `print()` muestra la cadena de caracteres (argumento) dentro de sus paréntesis en la pantalla.

    **Nota:** Una función es un bloque de código que realiza una tarea específica. 
    Las funciones toman entradas (llamadas argumentos, un término para referirse a los valores que introduces dentro de una función) 
    y devuelven salidas. 
             
    En este caso, la función `print()` toma el texto `'¡Hola Mundo!'` como entrada y devuelve el mismo texto como salida, 
    que se muestra en la pantalla.
             
    """, unsafe_allow_html=True)


if opciones == "Variables":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Variables en Python</h2>', unsafe_allow_html=True)
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")
    
    st.code("perro = 'guau' \nprint(perro)", language='python')

        # Create the family tree graph
    family_tree = graphviz.Digraph('family_tree')

        # Set global attributes
    family_tree.attr(rankdir='TB')  # Top-to-bottom alignment
    family_tree.attr('edge', color='gray')

        # Define nodes
    family_tree.node('Valor1', label='14', shape='circle', style='filled', color='orange')
    family_tree.node('Valor2', label='14', shape='circle', style='filled', color='orange')

    family_tree.node('Variable1', label='Variable\nX', shape='box', style='filled', color='yellow')
    family_tree.node('Variable2', label='X = 14', shape='box', style='filled', color='goldenrod')

        # Define edges
    family_tree.edge('Valor1', 'Valor2')
    family_tree.edge('Valor2', 'Variable1', label='     asignación', color='black')
    family_tree.edge('Variable1', 'Variable2', style='invis')

    # Descripción general
    st.write("""
        <h2 style='text-align: justify;'>
        Visual Studio Code (VS Code)
        </h2>
        """, unsafe_allow_html=True)
   
    # Display text block
    content_3 = st_monaco(
            value="# Creamos dos variables y le asignamos un valor a cada una\n perro = 'guau'\n X = 14 \n print(perro)\n print(X)",
            height="100px",
            language="python",
            lineNumbers=True,
            minimap=False,
            theme="vs-dark",)
    if st.button("▶️"):
            if "perro = 'guau'\n X = 14 \n print(perro)\n print(X)" in content_3:
                st.markdown("guau")
                st.markdown("14")
            else:
                st.markdown(f"**SyntaxError o NameError:** Parece que escribiste algo incorrecto. Asegúrate de usar `print()` e ingresar el nombre de la variable que deseas imprimir.")
        
    # Descripción general
    st.write("""
        <h2 style='text-align: justify;'>
        Google Colab
        </h2>
        """, unsafe_allow_html=True)
        # Bloque de texto en un box
    st.markdown(
        """
        <div style="
            padding: 10px;
            background-color: #fefefb;
            font-weight: bold;
            font-size: 18px;">
            Variables
        </div>
        """,
        unsafe_allow_html=True,
        )
        # Bloque de código con comentario explicativo
    codigo_2 = """# La función print() imprime el valor asignado a una variable 
    perro = 'guau'
    X = 14
    print(perro)
    print(X)"""

    # Mostrar código en bloque con resaltado de sintaxis
    content_4 = st_monaco(
            value=codigo_2,
            height="120px",
            language="python",
            lineNumbers=True,
            minimap=False,
            theme="jupyter",)

        # lista de palabras clave
    frases = ["perro = 'guau'", "X = 14", "print(perro)", "print(X)"]
        # Display both code blocks together
    if st.button("▶️", key="run_button"):
            if all(palabra in content_4 for palabra in frases):
                st.markdown("guau")
                st.markdown("14")
            else:
                st.markdown(f"**SyntaxError o NameError:** Parece que escribiste algo incorrecto. Recuerda que en los notebooks puedes mostrar el contenido de la variable con la función 'print()' o simplemente escribiendo el nombre de la variable.")

        # Encabezado
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">¿Qué está ocurriendo aquí?</h2>', unsafe_allow_html=True)

        # Display the graph in Streamlit
    st.write("En Python, una variable es un espacio que almacena un valor. Para asignar un valor a una variable, usamos el símbolo `=`. Por ejemplo, `X = 14` asigna el valor `14` a la variable `X`. "
        "Recuerda que el nombre de la variable puede ser cualquier palabra, pero no puede comenzar con un número. "
        "Además, no puede contener espacios ni caracteres especiales. "
        "Revisa las palabras reservadas de Python para asegurarte de que el nombre de tu variable no sea una palabra reservada: "
        "[Palabras reservadas en Python.](https://www.w3schools.com/python/python_ref_keywords.asp) "
        "Los valores pueden ser números, cadenas de texto, listas, etc.")
    
      # Center the graph using columns
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed
    with col1:
        st.empty()  # Empty column for alignment
    with col2:
        st.graphviz_chart(family_tree)  # Graph displayed in the center column
    with col3:
        st.empty()  # Empty column for alignment


if opciones == "Tipos de datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Tipos de datos en Python</h2>', unsafe_allow_html=True)
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")
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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")    

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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
    st.write("Por Luisa Gomez (luisa.gomez@pucp.edu.pe)")

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



    
    


   
   
   


