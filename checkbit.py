def check_bit(A,B):
    if A&(1<<B):
        return 1
    return 0
if __name__ == '__main__':
    A=int(input())
    B=int(input())
    print(check_bit(A,B))
"""
You are given two integers A and B.
Return 1 if B-th bit in A is set
Return 0 if B-th bit in A is unset
"""