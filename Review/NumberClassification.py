from random import randint


def main():
    count = 0
    all__nums = ""
    even = ""
    odd = ""
    mixed = ""
    pairs = ""

    while count is not 26:
        num = randint(100, 999)
        all__nums += "%d " % num
        nums = [int(d) for d in str(num)]
        num__type = get__type(nums)
        if num__type is 1:
            even += "%d " % num
        elif num__type is 2:
            odd += "%d " % num
        elif num__type is 3:
            mixed += "%d " % num
        elif num__type is 4:
            pairs += "%d " % num

        count += 1

    print "The numbers... \n" + all__nums
    print "The even digit numbers... \n" + even
    print "The odd digit numbers... \n" + odd
    print "The mixed digit numbers... \n" + mixed
    print "The paired digit numbers... \n" + pairs


def get__type(nums):
    if (nums[0] % 2 is 0) and (nums[1] % 2 is 0) and (nums[2] % 2 is 0):
        return 1
    elif (nums[0] % 2 is not 0) and (nums[1] % 2 is not 0) and (nums[2] % 2 is not 0):
        return 2
    elif (nums[0] is not nums[1]) and (nums[1] is not nums[2]) and (nums[0] is not nums[2]):
        return 3
    elif (nums[0] is nums[1]) or (nums[1] is nums[2]) or (nums[0] is nums[2]):
        return 4


if __name__ == "__main__":
    main()
