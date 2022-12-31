from pack import all_elements_weight, check_list_of_elements, check_empty_package_weight, sum_of_empty_weight, summary

def main():
    all_weight_per_package = []
    all_packages = []
    tmp_packages = []
    weight_per_package = ""
    packages_count = 0
    PACKAGE_LIMIT = 20
    MIN = 1
    MAX = 10

    element_count = input("Ile elementów: ")
    packages_weight = input("Wagi elementów: ")
    all_weight_per_package = all_elements_weight(packages_weight)

    if check_list_of_elements(all_weight_per_package, element_count) == True:
        for weight in all_weight_per_package:
            if len(all_packages) == 0:
                all_packages = [[weight]]
            elif sum(all_packages[packages_count]) + weight <= PACKAGE_LIMIT:
                all_packages[packages_count].append(weight)
            elif sum(all_packages[packages_count]) + weight >= PACKAGE_LIMIT:
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
        print(f"Suma pustych kilogramow: {sum_of_empty_weight(all_packages)}kg")
        print(f"Najwięcej pustych kilogramów ma paczka {check_empty_package_weight(sum_of_empty_weight(all_packages, False))}")
    else:
        print("Sprawdź listę elementów.")

if __name__ == "__main__":
    main()