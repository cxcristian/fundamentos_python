# Ejercicios de Operadores, Matematicos.

Basado en el los conceptos anteriormente trabajado el aprendiz debe resolver de forma manual los ejercicios y luego comprobarlos con python, basate en la solución del ejercicio 1 el cual tiene el formato para presentar la solución al instructor. Documenta la soluciones en un archvio [operadores.md](http://operadores.md) que debe estar en el repositorio del proyecto.

### Ejercicio 1

**Expresión:**

`5 + 3 * 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
5 + 3 * 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - Suma (`+`)
    - Multiplicación ()
    
    La multiplicación tiene mayor prioridad que la suma.
    
2. **Realizar la multiplicación primero:**
    - `3 * 2 = 6`
3. **Realizar la suma:**
    - `5 + 6 = 11`

**Resultado final:**

```python
11
```

---
---
### Ejercicio 2
**Expresión:**

`8 / 2 + 4 * 3`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
`8 / 2 + 4 * 3`
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - divicion, suma y multiplicación (`/`, `+`, `*`)
    
    La multiplicación y la divicion tienen mas prioridad que la suma
    
2. **Realizar la divicion primero:**
    - `8/2=4`
3. **Realizar la multiplicacion:**
    - `4*3=12`
4. **Realizar la suma:**
    - `4+12=16`

**Resultado final:**

```python
16.0
```
### Ejercicio 3

**Expresión:**

`(7 + 3) * 2 - 5`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
(7 + 3) * 2 - 5
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - mulitiplicacion, suma y resta (`*`, `+`, `-`)
    La multiplicacion tiene mayor prioridad sobre la suma y resta
    y a su vez los "()" siempre tienen mayor prioridad de resolverse
    
    
2. **resolver el parentesis:**
    - `7+3=10`
3. **multiplicar:**
    - `10*2=20`
4. **restar:**
    - `20-5=15`

**Resultado final:**

```python
15
```

### Ejercicio 4

**Expresión:**

`10 - 4 + 2 * 3`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
10 - 4 + 2 * 3
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - multiplicacion, suma y resta (`*`, `+`, `-`)
    
2. **primero resolvemos la multiplicaion:**
    - `2*3=6`
3. **suma y resta de izquierda a derecha asi que resolvemos la resta primero:**
    - `10-4=6`
4. **restamos:**
    - `6+6=12`

**Resultado final:**

```python
12
```

### Ejercicio 5

**Expresión:**

`(10 / 2) * (3 + 2) - 4`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
(10 / 2) * (3 + 2) - 4
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - Tenemos parentesis, multiplicacion, suma y resta (`()`, `*`, `+`, `-`)
    
2. **primero resolvemos los parentesis:**
    - `10/2=5`
    - `3+2=5`
3. **multiplicamos :**
    - `5*5=25`
4. **restamos:**
    - `25-4=21.0`

**Resultado final:**

```python
21.0
```

### Ejercicio 6

**Expresión:**

`2 + 3 * (4 - 1)`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
2 + 3 * (4 - 1)
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos parentesis, multiplicacion y suma (`()`, `*`, `+`)
    
2. **resolvemos las parentesis:**
    - `4-1=3`

3. **resolvemos la multiplicacion:**
    - `3*3=9`

4. **resolvemos la suma:**
    - `2+9=11`

**Resultado final:**

```python
11
```

### Ejercicio 7

**Expresión:**

`5 * 2 ** 3`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
5 * 2 ** 3
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos exponencial y multiplicacion (`**`, `*`)
2. **resolvemos el exponencial:**
    - `2**3=8`
3. **resolvemos la multiplicacion:**
    - `5*8=40`

**Resultado final:**

```python
40
```

### Ejercicio 8

**Expresión:**

`6 + 4 / 2 ** 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
6 + 4 / 2 ** 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos el exponencial, divicion y suma (`**`, `/`, `+`)
    
2. **resolvemos el exponencial:**
    - `2**2=4`
3. **resolvemos la divicion:**
    - `4/4=1.0`
4. **resolvemos la suma:**
    - `6+1.0=7.0`

**Resultado final:**

```python
7.0
```
### Ejercicio 9

**Expresión:**

`10 % 3 + 2 * 5`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
10 % 3 + 2 * 5
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos modulo, multiplicacion y suma (`%`, `*`, `+`)
    
2. **resolvemos el modulo:**
    - `10%3=1`
3. **resolvemos la multiplicacion:**
    - `2*5=10`
4. **resolvemos la suma:**
    - `1+10=11`

**Resultado final:**

```python
11
```

### Ejercicio 10

**Expresión:**

`(8 + 2) * 3 ** 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
(8 + 2) * 3 ** 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos las parentesis, exponencial, multiplicacion y suma (`()`, `**`, `*`, `+`)
    
2. **resolvemos primero las parentesis:**
    - `8+2=10`
3. **resolvemos la exponencial:**
    - `3**2=9`
4. **resolvemos la multiplicacion:**
    - `10*9=90`

**Resultado final:**

```python
90
```

### Ejercicio 11

**Expresión:**

`7 + 2 * (3 + 5) / 4`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
7 + 2 * (3 + 5) / 4
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - Tenemos parentesis, multiplicacion, divicion y suma (`()`, `*`, `/`, `+`)
    
    
2. **resolvemos las parentesis:**
    - `3+5=8`
3. **resolvemos la multiplicacion:**
    - `2*8=16`
4. **resolvemos la divicion:**
    - `16/4=4.0`
5. **resolvemos la suma**
    - `7+4.0=11.0`
**Resultado final:**

```python
11.0
```

### Ejercicio 12

**Expresión:**

`2 ** 3 * 4 / 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
2 ** 3 * 4 / 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos la exponencial, multiplicacion y divicion (`**`, `*`, `/`)
    
2. **resolvemos primero la exponencial:**
    - `2**3=8`
3. **resolvmeos la multiplicacion:**
    - `8*4=32`
4. **resolvemos la divicion:**
    - `32/2=16.0`

**Resultado final:**

```python
16
```

### Ejercicio 13

**Expresión:**

`9 - 6 + 3 ** 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
9 - 6 + 3 ** 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos la exponencial, resta y suma (`**`, `+`, `-`)
    
2. **resolvemos la exponencial:**
    - `3**2=9`
3. **resolvemos la resta:**
    - `9-6=3`
4. **resolvmeos la suma:**
    - `3+9=12`

**Resultado final:**

```python
12
```

### Ejercicio 14

**Expresión:**

`(7 - 2) * 5 + 3 ** 2`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
(7 - 2) * 5 + 3 ** 2
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - Tenemos la parentesis, exponencial, multiplicacion, suma y resta (`()`, `**`, `*`, `+`, `-`)
    
2. **resolvemos las parentesis:**
    - `7-2=5`
3. **resolvemos la exponencial:**
    - `3**2=9`
4. **resolvemos la multiplicacion:**
    - `5*5=25`
5. **resolvemos la suma:**
    - `25+9=34`
    
**Resultado final:**

```python
34
```

### Ejercicio 15

**Expresión:**

`4 * 2 ** 3 / 8 + 1`

- **Pregunta:** ¿Cuál es el resultado? ¿Por qué?

### Solucion y Explicacion

**Expresión:**

```python
4 * 2 ** 3 / 8 + 1
```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - tenemos la exponencial, multiplicacion, divicion y suma (`**`, `*`, `/`, `+`)
    
2. **resolvemos la exponencial:**
    - `2**3=8`
3. **resolvemos la multiplicacion:**
    - `4*8=32`
4. **resolvemos la divicion:**
    - `32/8=4.0`
    
5. **resolvemos la suma:**
    - `4.0+1=5.0`


**Resultado final:**

```python
5.0
```
---
---
## borrador para las soluciones

### Solucion y Explicacion

**Expresión:**

```python

```

**Paso a paso:**

1. **Identificar las operaciones y su prioridad:**
    - d
    
2. **:**
    - ``
3. **:**
    - ``
4. **:**
    - ``

**Resultado final:**

```python

```