cont = dict(input().split() for _ in range(int(input())))
while True:
    try:
        k = input()
        if k in cont.keys():
            print(f'{k}={cont[k]}')
        else:
            print('Not found')
    except EOFError:
        break
