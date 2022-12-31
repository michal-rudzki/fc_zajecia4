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
        summary(weight_per_package, all_packages)
    else:
        print("Za mało elementów, sprawdź listę elementów.")


if __name__ == "__main__":
    main()