#Dictionary is used to store data values in a key: value pairs 
electronics = {
    'year': 2019, 
    'mobile phones': 'nothing',
    'laptop': 'asus',
    'television': 'samsung',
    'float': 9.45
}
print(electronics)
print(len(electronics))
print(type(electronics))

#2
football_2 = dict (man = 'senwin', woman = 'aitana', kid = 'james')
print(football_2)

#3
football = {
    'club' :  'manchester untited',
    'player' : 'mikel arteta',
    'country' : 'portugal',
    'city' : ['lagos', 'abuja', 'port harcourt']
}
#print(football)

laliga = football['country']
print(laliga)

laliga = football.get('club')
print(laliga)

laliga = football.get('city')
print(laliga)

laliga = football.keys()
print(laliga)

laliga = football.values()
print(laliga)

football ['club'] = 'barcelona'
print(laliga)

laliga = football.items()
print(laliga)

#IF STATEMENT
if 'club' in football:
    print("'club' is better than international breaks")
    
football.update({'player' : 'lionel messi'})
print(football)

#FOR LOOP 
for bundesliga in football:
    print(bundesliga)
    
for bundesliga in football:
    print(football[bundesliga])

for bundesliga in football.values():
    print(bundesliga)

#Creating a dictionary that contains three dictionaries 
basketball = {
    'team' : {
        'clubs' : 'lakers',
        'year' : 2023
        },
    'player' : {
        'name' : 'lebron james',
        'position' : 'power forward'
    },
    'player_2' : {
        'name_2' : 'steph curry',
        'position_2' : 'point guard'
    },
}
print(basketball)