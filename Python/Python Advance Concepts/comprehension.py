digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

values = [(x) for x in range(5) if x % 2 == 0]

dic = {x:y for x,y in zip(range(10), digits)}

print(dic)