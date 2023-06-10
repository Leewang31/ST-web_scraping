import re

pattern = re.compile("ca.e")


# . (ca.e) : 하나의 문자를 의미 > care, cafe, case
# ^ (^de) : 문자열의 시작 > desk, destination
# $ (se$) : 문자여릐 끝 > case, base

def print_match(m):
    if m:
        print(m)
    else:
        print("매치가 되지 않았습니다")


# m = pattern.match('careless')  # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)
lst = pattern.findall("care case cave cake")
print_match(lst)