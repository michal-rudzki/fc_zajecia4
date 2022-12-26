import sys

element_count = int(input("Ile elementów: "))
all_packages_waight = []
packages = []
packages_count = []

for element in range(element_count):
    print(f"Wagi elementów [{element+1}]:", end=" ")
    packages_waight = int(input())

if packages_waight >= 1 or packages_waight <= 10:
    all_packages_waight.append([packages_waight])

packages_count.append(len(all_packages_waight))

print(f"Ilość elementów: {packages_count[0]}")
for waight in packages_waight:
    print(waight)
    print(f"Wagi elementów: (waga1, waga2)")
print(f"PODSUMOWANIE:")
print(f"Wysłano <ilosc_paczek> (waga1+waga2)")
print(f"Wysłano: XXkg")
print(f"Suma pustych kilogramow: YYkg")
print(f"Najwięcej pustych kilogramów ma paczka <numer_paczki> (waga)")