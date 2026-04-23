# 1. Puntaje total
puntos_nivel1 = float(input("Puntos nivel 1: "))
puntos_nivel2 = float(input("Puntos nivel 2: "))
puntos_nivel3 = float(input("Puntos nivel 3: "))
puntaje_total = puntos_nivel1 + puntos_nivel2 + puntos_nivel3
print("Puntaje total:", puntaje_total)


# 2. Tiempo total en segundos
horas = float(input("Horas: "))
minutos = float(input("Minutos: "))
segundos = float(input("Segundos: "))
tiempo_total_seg = (horas * 3600) + (minutos * 60) + segundos
print("Tiempo total en segundos:", tiempo_total_seg)


# 3. Daño total
danio1 = float(input("Daño ataque 1: "))
danio2 = float(input("Daño ataque 2: "))
danio3 = float(input("Daño ataque 3: "))
danio_total = danio1 + danio2 + danio3
print("Daño total:", danio_total)


# 4. Experiencia total
xp1 = float(input("Experiencia misión 1: "))
xp2 = float(input("Experiencia misión 2: "))
xp3 = float(input("Experiencia misión 3: "))
experiencia_total = xp1 + xp2 + xp3
print("Experiencia total:", experiencia_total)


# 5. Porcentaje de vida restante
vida_maxima = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Porcentaje de vida restante:", porcentaje_vida, "%")


# 6. Oro total
oro1 = float(input("Oro misión 1: "))
oro2 = float(input("Oro misión 2: "))
oro3 = float(input("Oro misión 3: "))
oro_total = oro1 + oro2 + oro3
print("Oro total:", oro_total)


# 7. Velocidad promedio
distancia = float(input("Distancia recorrida: "))
tiempo = float(input("Tiempo tomado: "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio:", velocidad_promedio)


# 8. Costo total de mejoras
costo1 = float(input("Costo mejora 1: "))
costo2 = float(input("Costo mejora 2: "))
costo3 = float(input("Costo mejora 3: "))
costo_total_mejoras = costo1 + costo2 + costo3
print("Costo total de mejoras:", costo_total_mejoras)

# 9. Tiempo restante en las misiones
tiempo_total_mision = float(input("Tiempo total misión: "))
tiempo_transcurrido = float(input("Tiempo transcurrido: "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante:", tiempo_restante)
# 10. Nivel promedio
nivel1 = float(input("Nivel jugador 1: "))
nivel2 = float(input("Nivel jugador 2: "))
nivel3 = float(input("Nivel jugador 3: "))
nivel_promedio = (nivel1 + nivel2 + nivel3) / 3
print("Nivel promedio:", nivel_promedio)


# 11. Daño crítico
danio_base = float(input("Daño base: "))
multiplicador_critico = float(input("Multiplicador crítico: "))
danio_critico = danio_base * multiplicador_critico
print("Daño crítico:", danio_critico)


# 12. Tiempo en horas y minutos
minutos_totales = float(input("Minutos totales: "))
horas_convertidas = minutos_totales // 60
minutos_restantes = minutos_totales % 60
print("Horas:", horas_convertidas)
print("Minutos:", minutos_restantes)


# 13. Porcentaje de misiones completadas
misiones_totales = float(input("Misiones totales: "))
misiones_completadas = float(input("Misiones completadas: "))
porcentaje_misiones = (misiones_completadas / misiones_totales) * 100
print("Porcentaje completado:", porcentaje_misiones, "%")


# 14. Costo total de objetos
objeto1 = float(input("Costo objeto 1: "))
objeto2 = float(input("Costo objeto 2: "))
objeto3 = float(input("Costo objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print("Costo total:", costo_total_objetos)


# 15. Tiempo promedio de partidas
partida1 = float(input("Tiempo partida 1: "))
partida2 = float(input("Tiempo partida 2: "))
partida3 = float(input("Tiempo partida 3: "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio:", tiempo_promedio)


# 16. Porcentaje de enemigos derrotados
enemigos_totales = float(input("Enemigos totales: "))
enemigos_derrotados = float(input("Enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / enemigos_totales) * 100
print("Porcentaje derrotado:", porcentaje_enemigos, "%")