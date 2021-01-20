"""
Given two strings a and b, both consisting only of lowercase English letters, your task is to calculate how many strings equal to a can be constructed using only letters from the string b? Each letter can be used only once and in one string only.

Example

For a = "abc" and b = "abccba", the output should be stringsConstruction(a, b) = 2.

We can construct 2 strings a = "abc" using only letters from the string b.

For a = "ab" and b = "abcbcb", the output should be stringsConstruction(a, b) = 1.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string a

String to construct, containing only lowercase English letters.

Guaranteed constraints:
1 ≤ a.length ≤ 105.

[input] string b

String containing needed letters, containing only lowercase English letters.

Guaranteed constraints:
1 ≤ b.length ≤ 105.

[output] integer

The number of strings a that can be constructed from the string b.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""


def containsAll(current, target):
    pila = list(target)
    #print("current: {}".format(current))
    for i in range(len(current)):
        #print("Pila: {}".format(pila))
        if pila:
            if current[i] in pila:
                #print("eliminar posicion: "+str(i))
                pila.remove(current[i])
    #print("Pila al final: {}".format(pila))
    if not pila:
        return True
    else:
        return False


def stringsConstruction(a, b):
    n = len(b)
    k = len(a)
    count = 0
    for i in range(n-k+1):
        current_str = ""
        for j in range(k):
            current_str = current_str + b[i+j]
        #print("current str: {}".format(current_str))
        #print("containsAll: {}".format(containsAll(current_str,a)))
        if containsAll(current_str, a):
            #print("---found: {}".format(current_str))
            count += 1

    return count


print(stringsConstruction("abc", "abccba"))
print(stringsConstruction("ab", "abcbcb"))
