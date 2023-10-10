import time 

start = time.time()
count = 0
n = 10
for i in range(1, n):
    print(i)
    count += i
end = time.time()
print(end - start)
