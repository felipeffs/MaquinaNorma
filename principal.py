def lerArquivo(nome, op):
    op.append('0')
    try:
        arquivo = open(nome, 'rt')
    except (FileExistsError, FileNotFoundError):
        print('\033[31mErro ao tentar ler o arquivo\033[m')
    else:
        c = arquivo.readlines()
        for i in range(0, len(c)):
            op.append(c[i][:].replace(':', '').replace('\n', '').split(' '))
            arquivo.close()


def ADD(reg):
    registradores[reg] += 1


def SUB(reg):
    registradores[reg] -= 1


def ZER(reg):
    if registradores[reg] == 0:
        return True
    return False


# Troque o nome do arquivo aqui
arq = 'soma.txt'

registradores = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
instrucao = {'ADD': ADD, 'SUB': SUB}
linhas = list()

lerArquivo(arq, linhas)

for key in registradores:
    registradores[key] = int(input(f'Valor de {key}: '))
print(f'({registradores["A"]}, {registradores["B"]}, {registradores["C"]}, {registradores["D"]}), M) Entrada de Dados')

pos = 1
while pos <= len(linhas) - 1:
    if linhas[pos][1] == 'ZER':
        print(f'({registradores["A"]}, {registradores["B"]}, {registradores["C"]}, {registradores["D"]}), {pos}) SE {linhas[pos][1]} ({linhas[pos][2]}) ENTAO VA_PARA {linhas[pos][3]} SENAO VA_PARA {linhas[pos][4]}')
        if not ZER(linhas[pos][2]):
            pos = int(linhas[pos][4])
        else:
            pos = int(linhas[pos][3])
    else:
        print(f'({registradores["A"]}, {registradores["B"]}, {registradores["C"]}, {registradores["D"]}), {pos}) FACA {linhas[pos][1]} ({linhas[pos][2]}) VA_PARA {linhas[pos][3]}')
        instrucao[linhas[pos][1]](linhas[pos][2])
        pos = int(linhas[pos][3])
print(f'({registradores["A"]}, {registradores["B"]}, {registradores["C"]}, {registradores["D"]})')
