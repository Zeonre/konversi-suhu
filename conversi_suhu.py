celcius_to_fahrenheit = lambda C: int((9/5) * C + 32)
celcius_to_reamur = lambda C: int(0.8 * C)

C = int(input("Masukkan suhu dalam Celcius: "))

print(f"Fahrenheit: {celcius_to_fahrenheit(C)}")
print(f"Reamur: {celcius_to_reamur(C)}")
