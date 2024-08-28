n = int(input())
worker = {}

for _ in range(n):
    name, status = input().split()
    worker[name] = status
    if status == "leave":
        del worker[name]

w = sorted(worker.items(), reverse=True)
worker = dict(w)

for i in worker.keys():
    print(i)