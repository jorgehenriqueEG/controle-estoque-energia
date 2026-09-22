def calcular_autonomia(baterias, consumo):
    tempos = []
    for b in baterias:
        if b <= 0 or consumo <= 0:
            tempos.append(0)
        else:
            tempo = b / consumo
            tempos.append(round(tempo, 2))
    return tempos

baterias = [5000, 12000, 3000, 8000]
consumo = 150

resultados = calcular_autonomia(baterias, consumo)
print(f"Autonomia (horas): " + " | ".join(map(str, resultados)))
menor = min(resultados)
print(f"Menor autonomia: {menor} horas")