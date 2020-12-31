class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x >= 2**31-1 or x <= -2**31:  # if x is 0 or outside our bounds, then return 0
            return 0

        negative = False
        if x < 0:
            negative = True
            x *= -1

        num = 0
        while x > 0:
            residuo = x % 10
            #print(f"residuo: {residuo}")
            x = x//10
            num = num*10+residuo

        if negative:
            num *= -1

        if num >= 2**31-1 or num <= -2**31:  # check if reversed x is now outside bounds
            return 0

        return num

    def reverse_going_backwards(self, x: int) -> int:
        return int(str(x)[::-1])


x = Solution()
print(x.reverse(-123456789))

print(x.reverse_going_backwards(123456789))
