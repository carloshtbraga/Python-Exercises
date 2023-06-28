names = ["José", "Lucas", "Nádia",
         "Fernanda", "Cairo", "Joana", "CarlosComeCu"]
biggestName = ""
for name in names:
    if len(name) > len(biggestName):
        biggestName = name
print(biggestName)
