s = "dvdf"

max_length = 1
res = ""
if len(s) == 0:
    max_length = 0
for i in range(len(s)):
    if s[i] in res:
        max_length = max(max_length, len(res))
        res = res[res.index(s[i])+1:] + s[i]
    else:
        res += s[i]
max_length = max(max_length, len(res))
print(res)
print(max_length)