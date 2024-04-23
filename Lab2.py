import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g 5, 67, 32)")

def get_user_input():
    numlist = input()
    numlist= numlist.split(",")
    for i in range (len(numlist)):
        numlist[i]= float(numlist[i])
    print(numlist)
    return numlist

def cal_average(numlist):
    total_sum = 0
    for i in range (len(numlist)):
        total_sum = total_sum + numlist[i]
    average = total_sum/ len(numlist)
    average = float(average)
    print("average = " + str(average))
    return average

def find_min_max(numlist):
    min_temp = numlist[0]
    max_temp = numlist[0]
    for i in range (len(numlist)):
        if numlist[i] < min_temp:
            min_temp = numlist[i]
        if numlist[i] > max_temp:
            max_temp = numlist[i]
    print("Min temperature= " + str(min_temp))
    print("Max temperature = " + str(max_temp))
    return min_temp, max_temp

def sort_temperature (numlist):
    numlist= sorted(numlist)
    return sorted(numlist)

def calc_median_temperature(numlist):
    median_temp = statistics.median(sorted(numlist))
    median_temp = str(median_temp)
    print("Median Temperature = " + median_temp)
    return median_temp


def main():
    display_main_menu()
    numlist= get_user_input()
    cal_average(numlist)
    find_min_max(numlist)
    sort_temperature(numlist)
    calc_median_temperature(numlist)

if __name__ == "__main__":
    main()