def saudacao(msg,nome):
    return f'{msg}, {nome}'

def executa(function, *args):
    return function(*args)

print(executa(saudacao,'Oieeeeee', 'Carlos'))

