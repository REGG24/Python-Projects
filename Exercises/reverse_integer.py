class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        while x > 0:
            residuo = x % 10
            #print(f"residuo: {residuo}")
            x = x//10
            num = num*10+residuo
        return num

    def reverse_going_backwards(self, x: int) -> int:
        return int(str(x)[::-1])


x = Solution()
print(x.reverse(123456789))

print(x.reverse_going_backwards(123456789))
