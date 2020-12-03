_sum = 2020


def part1(nums: list) -> int:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == _sum:
                print(nums[i] * nums[j])
                return


def part2(nums: list) -> int:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == _sum:
                    print(nums[i] * nums[j] * nums[k])
                    return


def main():
    with open('input') as f:
        nums = [int(n) for n in f]
    part1(nums)
    part2(nums)


if __name__ == '__main__':
    main()
