import statistics

text = open(r'filename.txt').read()
data = []
with open(r'stuff.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        data.extend(rowdata)
mean = sum(data)/len(data)
std = statistics.stdev(data)
biggest = min(data)
smallest = max(data)
print(f"Statistics Summary")
print(f"mean: {mean}")
print(f"std: {std}")
print(f"min: {smallest}")
print(f"max: {biggest}")