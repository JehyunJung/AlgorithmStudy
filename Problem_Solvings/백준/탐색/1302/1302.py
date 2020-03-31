from collections import defaultdict
def solution():
    num=int(input())
    books=defaultdict(int)
    for _ in range(num):
        books[input()]+=1
    max_count=max(books.values())

    sub_books=[book for book,count in books.items() if count == max_count ]
    sub_books.sort()
    print(sub_books[0])

if __name__ == "__main__":
    solution()
