numbers = int(input())
positives = []
negatives = []

for _ in range(numbers):
    number = int(input())
    if number > 0:
        positives.append(number)
    elif number < 0:
        negatives.append(number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")