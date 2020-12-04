import re


_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_passport_invalid_p1(pd: dict):
    for key in _keys:
        if key not in pd.keys():
            return True


def check_passport_invalid_p2(pd: dict):
    for key in _keys:
        if key == 'byr':
            m = re.fullmatch(r'(\d{4})', pd[key])
            if not m or not 1920 <= int(m.group(1)) <= 2002:
                return True
        elif key == 'iyr':
            m = re.fullmatch(r'(\d{4})', pd[key])
            if not m or not 2010 <= int(m.group(1)) <= 2020:
                return True
        elif key == 'eyr':
            m = re.fullmatch(r'(\d{4})', pd[key])
            if not m or not 2020 <= int(m.group(1)) <= 2030:
                return True
        elif key == 'hgt':
            m = re.fullmatch(r'(\d{2})in|(\d{3})cm', pd[key])
            if not m:
                return True
            elif m.group(1) is not None and not 59 <= int(m.group(1)) <= 76:
                return True
            elif m.group(2) is not None and not 150 <= int(m.group(2)) <= 193:
                return True
        elif key == 'hcl':
            m = re.fullmatch(r'#([0-9a-f]{6})', pd[key])
            if not m:
                return True
        elif key == 'ecl':
            m = re.fullmatch(r'(\w{3})', pd[key])
            if not m or m.group(1) not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return True
        elif key == 'pid':
            m = re.fullmatch(r'(\d{9})', pd[key])
            if not m:
                return True


with open('input') as f:
    validated_p1 = 0
    validated_p2 = 0
    for p in f.read().split('\n\n'):
        pd = {}
        for e in re.split(r'\s+', p):
            pd[e.split(':')[0]] = e.split(':')[1]
        if not check_passport_invalid_p1(pd):
            validated_p1 += 1
            if not check_passport_invalid_p2(pd):
                validated_p2 += 1
    print('part 1:', validated_p1)
    print('part 2:', validated_p2)
