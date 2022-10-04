def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num  = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return reversed_num 
        if x < 0:
            ans = ans.replace('-', '')
            ans = '-' + ans
            ans = int(ans)
        if -2 ** 31 <= ans <= 2 ** 31 - 1:
            return ans
        else:
            return 0

print(reverse(123))