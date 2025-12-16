# *args元组，结果是带（）；**kwargs字典，结果是键对值{}
def test(a,b,*args,c='hello', **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

test('jack', 'man', 8,9,10,height='89kg', weight='180cm',c='666')
