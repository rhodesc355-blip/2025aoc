# Main Code
# ---------------------------------------------
with open('input.txt', 'r') as file:
    nums = [line.rstrip() for line in file]

dial = 50
ans = 0

#print(nums)
for i in nums:
    d = i[0]
    r = int(i[1:])
    
    if d=='R':
        for _ in range(r):
            dial += 1
            if dial%100 == 0:
                ans += 1
    if d=='L':
        for _ in range(r):
            dial -= 1
            if dial%100 == 0:
                ans += 1

print(ans)
