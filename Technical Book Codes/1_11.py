InputString = input("Enter string: ")

StringList = InputString.split()

wordfreq = [StringList.count(p) for p in StringList]

print(dict(zip(StringList, wordfreq)))
