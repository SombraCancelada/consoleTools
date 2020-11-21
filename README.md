# consoleTools
Set of tools to make console programs more friendly


## **¿Que es?**

#### Es una herramienta para agregar colores y estilos al texto mostrado en pantalla por consola, para los programas de linea de comandos, haciéndolos mas amigables con el usuario.

#### Los colores disponibles para el fondo del texto son: 
- `40`: ![colorNegro!](negro.png)
- `41`: ![color Rojo!](rojo.png)
- `42`: ![color verde!](verde.png)
- `43`: ![color narnja!](naranja.png)
- `44`: ![color azul!](azul.png)
- `45`: ![color rosado](morado.png)
- `46`: ![color celeste](celeste.png)
- `47`: ![color beige](beige.png)
## **¿Como Funciona?**

#### Se puede importar el modulo *console_tools.py* e instanciar la clase *TextDecorator*:
`text_decorator = TextDecorator()`
### Luego se puede acceder a cada una de las funciones medainte `text_decorator.`*`nombre_funcion`*.

### Las funciones disponbles son:

- #### `tprint(`text, bg\_color=None, text\_color=None, blink=False, underline=False, bold=False, italic=False`)`
    - `text`: El texto para darle estilo.
    - `bg_color`: Color de fondo del texto ( numero entre 40 y 47 ).
    - `text_color`: Color del texto
    - `blink`: Booleano, establece si el texto parpadea.
    - `underline`: Booleano, establece si el texto está subrayado.
    - `bold`: Booleano, establece si el texto está en negritas.
    - `italic`: Booleano, establece si el texto es italic. 
