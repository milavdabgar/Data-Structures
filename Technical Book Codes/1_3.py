myStr = input("Enter Your String: ")
all_freq = {}

for i in myStr:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(str(all_freq))
