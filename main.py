# Write a python program to remove duplicates from Dictionary
db={

1:{
    "name":"James Gosling",
    "language":"JAVA"
  },
2:{
    "name":"Dennis Ritchie",
    "language":"C"
  },
3:{
    "name":"Bjarne Stroustrup",
    "language":"C++"
  },
4:{
    "name":"Guido van Rossum",
    "language":"python"
  },
5:{
    "name":"JAYAKRISHNAN",
    "language":"NotYET"
  },
6:{
    "name":"SIBI",
    "language":"Comming soon.."
  },
7:{
    "name":"Guido van Rossum",
    "language":"python"
  },
}

result = {}

for key,value in db.items():
    if value not in result.values():
        result[key] = value

print(result)