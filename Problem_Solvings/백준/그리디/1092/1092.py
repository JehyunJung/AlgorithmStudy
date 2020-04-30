def solution():
    n_crains=int(input())
    crain_weight_limits=list(map(int,input().split(' ')))
    crain_weight_limits.sort(reverse=True)
    n_boxes=int(input())
    box_weights=list(map(int,input().split(' ')))
    box_weights.sort(reverse=True)
    checked=[False]*n_boxes

    crain_positions=[0]*n_crains
    count=0
    result=0

    if box_weights[0]>crain_weight_limits[0]:
        print(-1)
    else:
        while True:
            if count==n_boxes:
                break
            for i in range(n_crains):
                while crain_positions[i]<n_boxes:
                    if not checked[crain_positions[i]] and box_weights[crain_positions[i]]<=crain_weight_limits[i]:
                        checked[crain_positions[i]]=True
                        crain_positions[i]+=1
                        count+=1
                        break
                    crain_positions[i]+=1
            result+=1
        print(result)

if __name__ == "__main__":
    solution()