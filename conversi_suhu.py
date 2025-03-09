celcius_ke_fahrenheit = lambda C: int((9/5) * C + 32)
celcius_ke_reamur = lambda C: int(0.8 * C)

C = int(input("Masukkan suhu dalam Celcius: "))

print(f"Fahrenheit: {celcius_ke_fahrenheit(C)}")
print(f"Reamur: {celcius_ke_reamur(C)}")
