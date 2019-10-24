
#production = []
p0 = {
    'name':'DFL7161',
    'price':'200'
    }
#production.append(p0)

p1 = {
    'name':'Grinder wheel',
    'price':'50'
    }
#production.append(p1)
production = [p0, p1]
print('The price of the ' + production[0]['name'] + ' is '+ production[0]['price'])
print('The price of the ' + production[1]['name'] + ' is '+ production[1]['price'])
print('====================')
print(production)
