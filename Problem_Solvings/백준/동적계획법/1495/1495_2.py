def guitar(current_volume, current_index, target_volume):
    if current_index==len(volumes):
        target_volume.append(current_volume)
        return

    if current_volume + volumes[current_index]<=max_volume:
        guitar(current_volume+volumes[current_index],current_index+1,target_volume)
    if current_volume - volumes[current_index]>=0:
        guitar(current_volume-volumes[current_index],current_index+1,target_volume)
    else:
        return

def solution():
    global max_volume,volumes
    volume_num,start_volume,max_volume=list(map(int, input().split(' ')))
    volumes=list(map(int,input().split(' ')))
    target_volume=[]
    guitar(start_volume,0,target_volume)
    if target_volume:
        print(max(target_volume))
    else:
        print(-1)

if __name__=="__main__":
    solution()