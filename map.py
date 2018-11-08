import sys

def map(val, a1, a2, b1, b2):
	aRange = float(a2-a1)
	bRange = float(b2-b1)
	newVal = float(float(float(val-a1) * bRange) / aRange) + b1
	return newVal

colors = ["very red","red","meh","green","very green"]

default = 50

if len(sys.argv) > 1:
	default = int(sys.argv[1])

index = int(map(default, 0, 100, 0, 5))

print(colors[index])