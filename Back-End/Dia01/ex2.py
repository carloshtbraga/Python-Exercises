entradaUsuario = input('Coloque uma letra e lhe diremos se é vogal ou não: ')
if( entradaUsuario == 'a' or entradaUsuario == 'e' or entradaUsuario == 'i' or entradaUsuario == 'o' or entradaUsuario =='u '):
    print(f'Você escolheu a letra {entradaUsuario} e ela é uma vogal! Parabéns')
else:
    print(f'Não é vogal! A letra {entradaUsuario} é uma consoante!')
