import sys

all_weight_per_package = []
all_packages = []
tmp_packages = []
packages_count = 0

def all_elements_weight(weights):
    all_elements_weight = []
    tmp = weights.split(",")
    for t in tmp:
        if int(t) >= 1 or int(t) <= 10:
            all_elements_weight.append(int(t))
    return all_elements_weight

def check_list_of_elements(list_of_elements, number_of_elements):
    if int(len(list_of_elements)) == int(number_of_elements):
        return True
    else:
        return False

def summary():
    pass

element_count = input("Ile elementów: ")
packages_weight = input("Wagi elementów: ")
all_weight_per_package = all_elements_weight(packages_weight)

if check_list_of_elements(all_weight_per_package, element_count) == True:
    for weight in all_weight_per_package:
        if len(tmp_packages) == 0:
            tmp_packages.append(weight)
            all_packages = [tmp_packages]
        elif sum(tmp_packages) + weight <= 20:
            all_packages[packages_count].append(weight)
        elif sum(tmp_packages) + weight >= 20:
            packages_count += 1
            all_packages.append([weight])
    
    print(f"\nPODSUMOWANIE:")
    print(f"Wysłano {len(all_packages)} (waga1+waga2)")
    print(f"Wysłano: {sum(all_weight_per_package)}kg")
    print(f"Suma pustych kilogramow: YYkg")
    print(f"Najwięcej pustych kilogramów ma paczka <numer_paczki> (waga)")
else:
    print("Sprawdź listę elementów.")
