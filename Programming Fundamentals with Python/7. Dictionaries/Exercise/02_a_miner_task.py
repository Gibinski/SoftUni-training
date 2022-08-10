key = input()
miner_task = {}
while key != "stop":
    value = int(input())
    if key not in miner_task:
        miner_task[key] = 0
    miner_task[key] += value
    key = input()

for key, value in miner_task.items():
    print(f"{key} -> {value}")
