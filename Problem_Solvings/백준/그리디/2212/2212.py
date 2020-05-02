import sys
def solution():
    n_sensors=int(input())
    n_antennas=int(input())

    if n_antennas>=n_sensors:
        print(0)
        sys.exit()

    sensors=list(map(int,input().split(' ')))
    sensors.sort()
    distances=[]

    for i in range(1,n_sensors):
        distances.append(sensors[i]-sensors[i-1])

    distances.sort(reverse=True)

    for i in range(n_antennas-1):
        distances[i]=0
    print(sum(distances))

if __name__ == "__main__":
    solution()