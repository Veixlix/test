def DamageCalculation(DR, lvl):
    prot= (4 * lvl)
    tot= 100 - ((100 - DR) * ((100 - prot) / 100))
    return tot

a= input("Type what kind of armor you are using")
h= int(input("Insert what level of protection your helmet has"))
c= int(input("Insert what level of protection your chestplate has"))
l= int(input("Insert what level of protection your leggings have"))
b= int(input("Insert what level of protection your boots have"))

if "diamond" in a:
    DamageRed= 80
elif "iron" in a:
    DamageRed= 60
else:
    DamageRed= 0
Bedrock1= [h]
if 4 in Bedrock1:
    h= 5
Bedrock2= [c]
if 4 in Bedrock2:
    c= 5
Bedrock3= [l]
if 4 in Bedrock3:
    l= 5
Bedrock4= [b]
if 4 in Bedrock4:
    b= 5
ProtectionLvL= h + c + l + b
print(DamageCalculation(DamageRed, ProtectionLvL))