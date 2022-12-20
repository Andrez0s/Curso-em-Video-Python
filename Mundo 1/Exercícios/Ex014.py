# C = 5 * ((F-32) / 9).
# A equação é °F = (°C x 1,8) + 32

celsius = float(input('Insira a temperatura em °C: '))
f = 9 * celsius / 5 + 32
print(f'A temperatura {celsius}°C em Fahreinheit é {f}°F')
