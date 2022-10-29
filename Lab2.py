import statistics

def display_main_menu():
    print("Enter any numbers seperated by commas (Eg. 6,57,32)")


def get_user_input():
    a = input()
    strings = list(a.split(","))
    floats = [float(x) for x in strings]
    return floats


def calc_average(floats):
    avg = sum(floats) / len(floats)
    return avg


def find_min_max(floats):
    min_temp = min(floats)
    max_temp = max(floats)
    min_max_temp = [min_temp, max_temp]
    return min_max_temp


def sort_temperature(floats):
    ascending_temp = sorted(floats)
    descending_temp = sorted(floats, reverse=True)
    return(ascending_temp)

def calc_median_temperature(floats):
    median_temp = statistics.median(floats)
    return median_temp


def main():
    display_main_menu()
    floats = get_user_input()
    print("Average = " + str(calc_average(floats)))
    print("Min/Max Temp = " + str(find_min_max(floats)))
    print("Sorted list (in ascending):" + str(sort_temperature(floats)))
    print("Median Temperature = " + str(calc_median_temperature(floats)))


if __name__ == "__main__":
    main()
