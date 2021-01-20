"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string sequence

A bracket sequence, consisting of the characters (, ), [, ], {, and }.

Guaranteed constraints:
0 ≤ sequence.length ≤ 106.

[output] boolean

true if sequence is a valid bracket sequence and false otherwise.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""


def validBracketSequence(sequence):
    if not sequence:
        return True

    pila = []
    for i in range(len(sequence)):
        # print(sequence[i])
        if not pila or (sequence[i] == '(' or sequence[i] == '[' or sequence[i] == '{'):
            pila.append(sequence[i])
        else:
            if sequence[i] == ')':
                if pila[-1] == '(':
                    pila.pop()
                else:
                    return False
            elif sequence[i] == ']':
                if pila[-1] == '[':
                    pila.pop()
                else:
                    return False
            elif sequence[i] == '}':
                if pila[-1] == '{':
                    pila.pop()
                else:
                    return False

    if not pila:
        return True
    else:
        return False


print(validBracketSequence("{}()[]"))
print(validBracketSequence("([)]"))
print(validBracketSequence("()"))
print(validBracketSequence("([])"))
