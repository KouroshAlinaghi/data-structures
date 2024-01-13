s = input()
n = len(s)

fq = []
for i in range(500):
    fq.append([])
    for j in range(1000):
        fq[i].append(0)

for i in range(len(s)):
    if i == 0:
        fq[ord(s[0])][0] = 1
    else:
        for c in range(500):
            fq[c][i] = fq[c][i-1]
        fq[ord(s[i])][i] += 1 

def check(x):
    if (x > n): return False
    for i in range(n - x + 1):
        flag = False
        for c in range(500):
            if i == 0:
                if fq[c][i + x - 1] > 1: 
                    flag = True
            else:
                if fq[c][i + x - 1] - fq[c][i - 1] > 1:
                    flag = True

        if not flag:
            return True

    return False

for i in reversed(range(100)):
    if check(i): # doesn't have any substring of size k with any duplicate characters
        print(i)
        break
