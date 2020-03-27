import hashlib
def solution():
    string=input()
    cypher=hashlib.sha256(string.encode()).hexdigest()
    print(cypher)

if __name__ == "__main__":
    solution()