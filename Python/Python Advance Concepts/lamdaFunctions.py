from distutils.command.config import LANG_EXT


my_list = ["geeks", "geeg", "keegs", "practice", "aa"]

#is_number = lambda n: "is number" if n.isdigit() else "not a number"

#filter_number = lambda str: "".join([ch for ch in str if not ch.isdigit()])

#sum_of_digits = lambda n: sum([int(x) for x in str(n)])

#my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]

#div_by_three = lambda n:[int(i) for i in n if i % 13 == 0]

#OR

#div_by_three1 = list(filter(lambda x:  x % 13 == 0, my_list))

#paliandrom using lambda

#paliandrom = list(filter(lambda x: x == x[::-1], my_list))

def anagram(str):
    for j in my_list:
        ctr = 0
        str1 = []
        for i in range(len(str)):
            if str[i] in j:
                ctr += 1
            if ctr == len(j):
                print(j)


#anagram("eegsk")

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

intersection = list(filter(lambda x: x in arr2, arr1))

print(intersection)