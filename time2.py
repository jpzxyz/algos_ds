import time

start = time.time()
count = 0
for i in range(1, 10):
    print(i)
    count += i
end = time.time()
print(end - start)
