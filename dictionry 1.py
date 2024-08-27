dictionory = {"Bug":"Bug is also known as the error in the code" ,"function " :"Function is the piece of code that can be get used repatedtivly "}

print(dictionory.keys())
print(dictionory.values())
print(type(dictionory))

dictionory["loop"]="Code that get executed repetatively"
print(dictionory)
# clearing the doctionory
# dictionory ={}
# print(dictionory)
for i in dictionory.values():
    print(i)


hybe ={"bts":{"members":"jk,jin,v,jimin,rm.j-ope,suga"},
       "blackpink":{"member":"jiso,rose,jennie,lisa"}}
print(hybe)

print(hybe.values())


group_leader ={"hype":["rm","soobin","scoups"],"bts":["jk","v","jimin","suga","j-hope","rm","jin"]}
print(group_leader)