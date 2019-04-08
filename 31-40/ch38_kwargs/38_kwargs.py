# We need (keywords, value) and variable length of agruments 
def person (name, **data):
    print (name)
    for i, j in data.items():
        print (i, j)

person ('peter', age=62, city='Sunnyvale', zip=94089)