



def hannuo(a,b,c,n):
    '''This is a method of recursion to implement a hannuota '''
    if n==1:
        move(a,c)
        return

    hannuo(a,c,b,n-1)
    move(a,c)
    hannuo(b,a,c,n-1)

    pass

def move(a,b):
    '''Move the wooden stick from a into b'''
    print(f"move {a} to {b}")

    pass
