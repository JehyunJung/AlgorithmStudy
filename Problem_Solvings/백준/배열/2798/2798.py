from itertools import combinations

def solution():
    card_num,blackjack=map(int,input().split(' '))
    card_deck=list(map(int,input().split(' ')))
    card_sets=combinations(card_deck,3)
    current_sum=0
    for card_set in card_sets:
        sum=card_set[0]+card_set[1]+card_set[2]
        if sum > blackjack:
            continue
        elif abs(sum-blackjack) < abs(current_sum-blackjack):
            current_sum=sum

    print(current_sum)

if __name__ == "__main__":
    solution()