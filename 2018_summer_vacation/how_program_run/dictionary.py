elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['hydrogen'])
print('lithium' in elements)
elements['lithium'] = 3
elements['nitrogen'] = 8
print(elements['nitrogen'])
elements['nitrogen'] = 7
print(elements['nitrogen'])
print(elements)