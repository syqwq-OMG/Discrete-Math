n,m=map(int, input().split())
mat=[]
for i in range(n):
    mat.append(list(input().split()))
    
print('\n')
print(
    r'\begin{pmatrix}'
)
for i in mat:
    print(
        ' & '.join(i)+r' \\'
    )
print(
    r'\end{pmatrix}'
)
