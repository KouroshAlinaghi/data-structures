t = int(input())

def minutes(s, base):
        x = 12 if s[base+6] == "P" else 0
        return ((int(s[base:base+2]) % 12) + x) * 60 + int(s[base+3:base+5])

for i in range(t):
        fucking_stupid_string_for_fucking_stupid_output_because_python_is_fucking_stupid = ""
        t_l = []
        s = minutes(input(), 0)
        n = int(input())
        for j in range(n):
                khar = input()
                l = minutes(khar, 0)
                r = minutes(khar, 9)
                if s >= l and s <= r:
                        fucking_stupid_string_for_fucking_stupid_output_because_python_is_fucking_stupid += "1"
                else:
                        fucking_stupid_string_for_fucking_stupid_output_because_python_is_fucking_stupid += "0"

        print(fucking_stupid_string_for_fucking_stupid_output_because_python_is_fucking_stupid)
