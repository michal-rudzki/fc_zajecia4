import sys

all_weight_per_package = []
all_packages = []
tmp_packages = []
weight_per_package = ""
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

def empty_package_weight(list_all_packages):
    pass

def sum_of_empty_weight(list_all_packages):
    pass

def summary():
    pass

element_count = input("Ile elementów: ")
packages_weight = input("Wagi elementów: ")
all_weight_per_package = all_elements_weight(packages_weight)

if check_list_of_elements(all_weight_per_package, element_count) == True:
    for weight in all_weight_per_package:
        if len(all_packages) == 0:
            all_packages = [[weight]]
        elif sum(all_packages[packages_count]) + weight <= 20:
            all_packages[packages_count].append(weight)
        elif sum(all_packages[packages_count]) + weight >= 20:
            packages_count += 1
            all_packages.append([weight])
    
    print(f"\nPODSUMOWANIE:")
    
    for package in range(len(all_packages)):
        if len(weight_per_package) != 0:
            weight_per_package += ", "
        tmp = ""
        index = 0
        for weight in all_packages[package]:
            tmp += str(weight)
            if index < len(all_packages[package])-1:
                tmp += "+"
                index += 1
            else:
                weight_per_package += tmp

    print(f"Wysłano {len(all_packages)} paczki ({weight_per_package})")
    print(f"Wysłano: {sum(all_weight_per_package)}kg")
    print(f"Suma pustych kilogramow: {(len(all_packages) * 20) - sum(all_weight_per_package)}kg")
    print(f"Najwięcej pustych kilogramów ma paczka <numer_paczki> (waga)")
else:
    print("Sprawdź listę elementów.")
