version = input().split(".")
version = list(map(int, version))

for n in range(len(version) - 1, -1, -1):
    if version[n] != 9:
        version[n] += 1
        break
    else:
        version[n] = 0

next_version = list(map(str, version))
print(".".join(next_version))