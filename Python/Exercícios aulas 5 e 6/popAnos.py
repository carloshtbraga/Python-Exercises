#Supondo que a população de um pais A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#E QUE A POPULAÇÃO b SEJA 200000 HABITANTES COM UMA Taxa de crescimento de 1,5%> faça um porograma que calcule o
#número de anos necessários para que a população da A passe ou fique igual ao

popA = int(input('Coloque a populaçãoA: '))
popB = int(input('Coloque a populaçãoB: '))
pct1 = int(input('Coloque o número da porcentagem de crescimento da pop A: '))
pct2 = int(input('Coloque o número da porcentagem de crescimento da pop A: '))
growthA = popA * (pct1 / 100)
growthB = popB * (pct2 / 100)
anos=0
while popA<=popB:   
    popA += growthA
    popB += growthB
    anos += 1
print(f'Levaram {anos} ano(s) ')
