def solution():
    player1_left,player1_right,player2_left,player2_right=input().split(' ')

    player1_winning=False
    player2_winning=False

    if player1_left==player1_right:
        if player1_left=='S' and (player2_left=='R' or player2_right=='R'):
            player2_winning=True
        elif player1_left=='R' and (player2_left=='P' or player2_right=='P'):
            player2_winning=True
        elif player1_left=='P' and (player2_left=='S' or player2_right=='S'):
            player2_winning=True

    if player2_left==player2_right:
        if player2_left=='S' and (player1_left=='R' or player1_right=='R'):
            player1_winning=True
        elif player2_left=='R' and (player1_left=='P' or player1_right=='P'):
            player1_winning=True
        elif player2_left=='P' and (player1_left=='S' or player1_right=='S'):
            player1_winning=True

    if player1_winning==False and player2_winning==True:
        print("TK")
    elif player1_winning==True and player2_winning==False:
        print("MS")
    else:
        print("?")

if __name__=="__main__":
    solution()