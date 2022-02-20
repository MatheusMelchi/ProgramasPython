import sys

km, l = input("Quilometros percorridos e Litragem gasta: ").split()

kml = float(km) / float(l)

if float(kml) < 8:
    print("Venda o Carro!")
elif 14 >= float(kml) >= 8:
    print("Economico!")
elif float(kml) > 12:
    print("Super Economico!")
