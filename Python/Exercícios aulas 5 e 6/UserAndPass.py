#Faça um programa que leia um nome de usuário e a sua senha e não aceita a senha igual ao nome do usuario,
#mostrando mensagem de erro e pedindo novamente as informações

nome = input('Coloque seu nome: ')
senha = nota = input('Coloque sua senha: ')
cripto = len(senha)
if nome != senha:
    print('Você esta logado com o usuário {nome} e a senha criptografada é', '*' * cripto)
else:
    print(f'Não é permitido user e senha iguais')
