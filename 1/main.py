def main():
    total = 2020
    with open('input') as f:
        nums = [int(n) for n in f]
        min_num = min(nums)
    for i in range(len(nums)):
        diff = total - nums[i]
        if diff < min_num:
            continue
        for j in range(i + 1, len(nums)):
            if nums[j] == diff:
                print(nums[i] * nums[j])
                break
            diff2 = diff - nums[j]
            if diff2 < min_num:
                continue
            for k in range(j + 1, len(nums)):
                if nums[k] == diff2:
                    print(nums[i] * nums[j] * nums[k])
                    break


if __name__ == '__main__':
    main()
