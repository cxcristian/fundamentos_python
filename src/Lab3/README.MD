# **LAB  Dando formato a la salida**

## Escenario

Te recomendamos encarecidamente que **juegues con el código** que hemos escrito para y realiza algunos (quizás incluso destructivos) cambios. Siéntete libre de modificar cualquier parte del código, pero hay una condición - aprende de tus errores y saca tus propias conclusiones.

Intenta:

- minimizar el número de invocaciones de la función **`print()`** insertando **`\n`** en las cadenas;
    - resultado: la flecha se alarga, dejando espacions debajo de cada print.
- hacer que la flecha sea el doble de grande (pero mantener las proporciones)
    - Para hacer que la flecha sea el doble de grande, se duplico los espacios y caracteres *2
- duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: **`"string" * 2`** producirá **`"stringstring"`** (pronto contaremos más al respecto)
    - Se uso el conocimiento del *2 para crear dos flechas una al lado de la otra además de darle un espacio extra a la derecha de la flecha par evitar que esten pegadas
- elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
    - Al eliminar las comillas de un print python nos dice lo siguiente:  File "c:\Users\Sena\Documents\3114227\python\clase1\fundamentos_python\src\Lab3\formatoSalida.py", line 34
    print(  *****)
              ^^
    SyntaxError: invalid syntax.
    Python nos señala la linea exacta en la cual se cometió un error de sintaxis.
- haz lo mismo con algunos de los paréntesis;
    - Al quitar los parentesis sale el siguiente error:   File "c:\Users\Sena\Documents\3114227\python\clase1\fundamentos_python\src\Lab3\formatoSalida.py", line 42
    print"  *   *"#aqui quitamos las parentesis para generar a drede un error y capturarlo
    ^^^^^^^^^^^^^^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
    En este caso nos señala la primera linea que python encontro con problemas de sintaxis
- cambia cualquiera de las palabras **`print`** por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, **`Print`**) - qué sucede ahora?
    - al poner una mayuscula inicial en print sale lo siguiente:  File "c:\Users\Sena\Documents\3114227\python\clase1\fundamentos_python\src\Lab3\formatoSalida.py", line 47, in <module>
    Print("error a proposito")
    ^^^^^
    NameError: name 'Print' is not defined. Did you mean: 'print'?
    python lo reconoce cono un name error, ya que esa no es la sintaxis del comando print o funcion print.
- reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.
    - Al usar apostrofes pasa esto: File "c:\Users\Sena\Documents\3114227\python\clase1\fundamentos_python\src\Lab3\formatoSalida.py", line 50
    print(¨apostrofes¨)
          ^
    SyntaxError: invalid character '¨' (U+00A8)
    los apostrofes son un caracter invalido.
```python

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

```