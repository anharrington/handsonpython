'''Program with intended error to demonstrate traceback from nested call'''

def invminus4(x):
    return 1.0/(x-4)

def main():
    print('ok call to invminus4 next:')
    print(invminus4(6))
    print('bad call to invminus4 next:')
    print(invminus4(4))
    print("Won't get to here!")

main()
