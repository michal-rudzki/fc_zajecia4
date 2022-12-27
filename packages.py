import sys

all_weight_per_package = []
all_packages = []
tmp_packages = []
packages_count = 0

def all_elements_weight(weights):
    all_elements_weight = []
    tmp = weights.split(",")
    for t in tmp:
        all_elements_weight.append(int(t))
    return all_elements_weight

def summary():
    pass

element_count = input("Ile elementów: ")
packages_weight = input("Wagi elementów: ")
all_weight_per_package = all_elements_weight(packages_weight)
if len(all_weight_per_package) == element_count:
    for weight in all_weight_per_package:
        if len(tmp_packages) == 0:
            tmp_packages.append(weight)
            all_packages = [tmp_packages]
        elif sum(tmp_packages) + weight <= 20:
            all_packages[packages_count].append(weight)
        elif sum(tmp_packages) + weight >= 20:
            packages_count += 1
            all_packages.append([weight])
else:
    print("Za mała lista elementów.")

print(f"\nPODSUMOWANIE:")
print(f"Wysłano {len(all_packages)} (waga1+waga2)")
print(f"Wysłano: {sum(all_weight_per_package)}kg")
print(f"Suma pustych kilogramow: YYkg")
print(f"Najwięcej pustych kilogramów ma paczka <numer_paczki> (waga)")