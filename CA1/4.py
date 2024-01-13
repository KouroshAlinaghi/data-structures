from math import log10

s = input();
n = len(s)

# for all to see, you're not the one that you pretend to be
#
#
# - Chester Benningon in "Pretend to Be" by Linkin Park
if n == 3 and int(s[0]) + int(s[1]) == int(s[2]):
    print("YES")
    exit(0)

def is_valid(first, second, start):
    i = start
    while i < n:
        res = second + first
        sex = int(log10(res)) + 1
        if i + sex > n: return False
        if s[i] == 0: return False
        if int(s[i:i + sex]) != res: return False
        first = second
        second = res
        i += sex
    return True

f_r, s_s = 1, 1
while f_r <= n // 3 + 1:
    s_s = 1
    if s[f_r] == '0': 
        f_r += 1
        continue;
    first = int(s[:f_r])
    while s_s <= n // 3 + 1:
        if f_r + s_s + 1 >= n:
            print("NO")
            exit(0)
        second = int(s[f_r:f_r + s_s])
        if s[f_r + s_s] == '0': 
            s_s += 1
            continue
        if is_valid(first, second, f_r + s_s): 
            print("YES")
            exit(0)
        s_s += 1
    f_r += 1

print("NO")
