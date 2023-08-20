def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    return total / len(list_of_nums)

def mode(list_of_nums):
    max_count = (0, 0)
    for num in list_of_nums:
        occurences = list_of_nums.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]

def median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 != 0:
        middle_index = int((len(list_of_nums) - 1) / 2)
        return list_of_nums[middle_index]
    elif len(list_of_nums) % 2 == 0:
        middle_index_1 = int(len(list_of_nums) / 2)
        middle_index_2 = int(len(list_of_nums) / 2) - 1
        return mean([list_of_nums[middle_index_1], list_of_nums[middle_index_2]])

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]
    
    print("List:", input_list)
    print("Median:", median(input_list))
    print("Mode:", mode(input_list))
    print("Mean:", mean(input_list))

if __name__ == "__main__":
    main()
