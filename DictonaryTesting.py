import ast

packet1 = dict(name="DataLogger",msg="I have successfully connected")

print('testing method one: ', packet1.get('msg'))

value = "{'name':'DataLogger','msg':'I have connected again!'}"
packet2 = dict(ast.literal_eval(value))

print('testing method two: ', packet2)


