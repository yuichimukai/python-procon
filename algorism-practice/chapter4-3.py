from collections import deque

n, q = map(int, input().split())
Queue = deque([])
for i in range(n):
    name, time = input().split()
    Queue.append([name, int(time)])

t = 0
while len(Queue) != 0:
    process = Queue.popleft()
    process[1] = process[1] - q
    if process[1] <= 0:
        t += q + process[1]
        print(process[0]+" "+str(t))
    else:
        t += q
        Queue.append(process)
