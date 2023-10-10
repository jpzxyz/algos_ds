import time

start = time.time()

def print_it(n):
    # loop 1
    for i in range(n):
        print(i)
    # loop 2
    for i in range(n):
        print(i)
        for j in range(n):
            print(j)
            for h in range(n):
                print(h)

print_it(10)
end = time.time()
print(end - start)
