# **LAB  Trabajando con la función print()**

## Escenario

El comando **`print()`**, el cual es una de las directivas más sencillas de Python, simplemente imprime una línea de texto en la pantalla.

En tu primer laboratorio:

- Utiliza la función **`print()`** para imprimir la linea **`¡Hola, Mundo!`** en la pantalla. Usa comillas dobles alrededor de la cadena.
- Habiendo hecho eso, usa la función **`print()`** nuevamente, pero esta vez imprime tu nombre.
- Elimina las comillas dobles y ejecuta tu código. Mira la reacción de Python. ¿Qué tipo de error arroja?
    - El error que arroja al no introducir las comillas en el comando print() es: SyntaxError: invalid syntax. Perhaps you forgot a comma?
- Luego, elimina los paréntesis, vuelve a colocar las comillas dobles y ejecuta tu código nuevamente. ¿Qué tipo de error arroja esta vez?
    - Al quitar las paréntesis, con comillas sale lo siguiente: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
- Experimenta todo lo que puedas. Cambia las comillas dobles a comillas simples, usa múltiples funciones **`print()`** en la misma línea, y luego en diferentes líneas. Mira qué pasa.
    - Print con comillas simple: funciona correctamente
    - Multiples funciones de **`print()`** en la misma linea: En caso de no colocar una "," al finalizar un comando **`print()`** dara un error de: SyntaxError: invalid syntax. Did you mean 'in'?, Si se usa "," se ejecutara normalmente el comando
    - En diferentes lineas: funciona normalmente, no tira errores