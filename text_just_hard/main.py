import math

maxWidth = 16
words = ["This", "is", "an", "example", "of", "text", "justification."]
new_str = 0
arr = []
for i in range(len(words)+1):
    if len(" ".join(words[new_str:i])) > maxWidth:
        arr.append(words[new_str:i-1])
        new_str = i - 1
arr.append(words[new_str:])
print(arr)
farr = []
spaces = ""
for final in arr:
    diff = maxWidth - len(" ".join(final))
    if arr.index(final) == len(arr) - 1:
        for i in range(diff):
            final[-1] += " "
        farr.append(" ".join(final))
    elif len(final) == 1:
        for i in range(diff):
            spaces += " "
        final[0] = final[0] + spaces
        spaces = ""
        farr.append("".join(final))
    elif diff % (len(final) - 1) == 0:
        for i in range(int(diff/(len(final) - 1)+1)):
            spaces += " "
        farr.append(spaces.join(final))
        spaces = ""
    else:
        ix = 0
        for i in range(diff//(len(final) - 1)+1):
            spaces += " "
        for j in range(diff % (len(final) - 1)):
            final[ix] += " "
            ix+=1
        farr.append(spaces.join(final))
        spaces = ""
print(farr)