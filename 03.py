codigo = int(input ("digite o codigo do primeiro produto : "))
nome = input("Digite o nome do primeiro produto : ")
quantidade = int(input ("digite a quantidade do primeiro produto : "))
precouni = float(input ("Digite o preço do primeiro produto: "))


codigo2 = int(input ("digite o codigo do segundo produto : "))
nome2 = input("Digite o nome do segundo produto : ")
quantidade2 = int(input ("digite a quantidade do segundo produto : "))
precouni2 = float(input ("Digite o preço do segundo produto: "))

total = (quantidade * precouni) + (quantidade2 * precouni2)
print("***********************************************")
print("*** Primeiro produto ***")
print("***********************************************")
print (f"      Codigo: {codigo}")
print (f"      Nome: {nome}")
print (f"      quantidade do produto: {quantidade}")
print (f"      preço unitario: R$ {precouni}")
print("***********************************************")

print("*** Segundo produto ***")
print("***********************************************")
print (f"      Codigo: {codigo2}")
print (f"      Nome: {nome2}")
print (f"      quantidade do produto: {quantidade2}")
print (f"      preço unitario: R$ {precouni2}")
print("***********************************************")
print (f"   valor total da nota R$ {total:.2f}   ")
print("***********************************************")
