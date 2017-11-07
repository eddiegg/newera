def mydeco(func):
    print('In my deco')
    def inner(*args,**kwargs):
        print('Inner do something before call func')
        result = func(*args,**kwargs)
        print('Inner done')
        return result
    return inner

@mydeco
def calcsum(arg):
    print(arg+'haha')

calcsum('eddie')