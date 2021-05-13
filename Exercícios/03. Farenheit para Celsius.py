# Enunciado
print("3. Fahrenheit para Celsius")
# Entrada de dados
tempFahrenheit = float(input('Insira a temperatura em °F: '))
# Execução
tempCelsius = float((tempFahrenheit - 32) / 1.8)
# Retorno ao usuário
print("A temperatura de ~{:.0f}°F equivale a ~{:.0f}°C.".format(tempFahrenheit, tempCelsius))
