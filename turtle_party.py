strawberries =int(input('how many strawberries are there?'))
weekend=bool(input('is it weekend?'))
if weekend:
    if strawberries<39  :
        print('Not Fun !')
    else:
        print('fun!')
elif strawberries <39 and strawberries>61:
    print('not fun')
else:
    print(' fun')
