def solution():
    music_num,start_volume,max_volume=list(map(int, input().split(' ')))
    volumes=list(map(int,input().split(' ')))
    music_volumes=[[0]*(max_volume+1) for _ in range(music_num+1)]
    music_volumes[0][start_volume]=1

    for index in range(1,music_num+1):
        for volume in range(max_volume+1):
            if music_volumes[index-1][volume]==1:
                if volume+volumes[index-1]<=max_volume:
                    music_volumes[index][volume+volumes[index-1]]=1
                if volume-volumes[index-1]>=0:
                    music_volumes[index][volume-volumes[index-1]]=1

    target_volume=-1
    for volume in range(max_volume,-1,-1):
        if music_volumes[music_num][volume]==1:
            target_volume=volume
            break

    print(target_volume)
if __name__=="__main__":
    solution()
