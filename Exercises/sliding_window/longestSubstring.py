import sys


def longestSubstr(str, k):
    INT_MAX = -sys.maxsize - 1
    max_str = ""
    for i in range(len(str)):
        current_str = ""
        current_characters = set()
        count = 0
        j = i
        #print("max_str: {}".format(max_str))
        for j in range(i, len(str)):
            # print("character: {},current_caracters: {}, current_str: {}".format(str[j],
            #                                                                    current_characters, current_str))
            if str[j] not in current_characters and len(current_characters) < k:
                current_characters.add(str[j])
                current_str += str[j]
            else:
                if str[j] in current_characters:
                    current_str += str[j]
                    if j == len(str) - 1:
                        #print("current str finalized")
                        if len(current_str) > INT_MAX:
                            INT_MAX = len(current_str)
                            max_str = current_str
                else:
                    #print("current str finalized")

                    if len(current_str) > INT_MAX:
                        INT_MAX = len(current_str)
                        max_str = current_str

    return max_str


print("longest: "+longestSubstr("abcbdbdbbdcdabd", 2))
print()
print("longest: "+longestSubstr("abcbdbdbbdcdabd", 3))
print()
print("longest: "+longestSubstr("abcbdbdbbdcdabd", 5))
