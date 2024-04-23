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
    print("cal_average")
    total_sum = 0
    for i in range (len(numlist)):
        total_sum = total_sum + numlist[i]
    average = total_sum/ len(numlist)
    average = float(average)
    print("average = " + str(average))
    return average

def find_min_max(numlist):
    min = numlist[0]
    max = numlist[0]
    for i in range (len(numlist)):
        if numlist[i] < min:
            min = numlist[i]
        if numlist[i] > max:
            max = numlist[i]
    print("min = " + str(min))
    print("max = " + str(max))
    return min, max

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    numlist= get_user_input()
    cal_average(numlist)
    find_min_max(numlist)

if __name__ == "__main__":
    main()