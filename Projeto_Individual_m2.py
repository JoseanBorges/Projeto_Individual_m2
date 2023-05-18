#Função para fazer a busca dos candidatos.
def busca_candidato():

candidatos = []
#Laço para adicionar/cadastrar candidato e adicionar notas.
while True:
    nome_candidato = input('Digite o nome do candidato: ')
    ent = int(input('Resultado da entrevista: '))
    tt = int(input('Resultado do Teste Teórico: '))
    tp = int(input('Resultado do Teste Prático: '))
    ss = int(input('Resultado das Soft Skills: '))

    candidatos.append([nome_candidato, ent, tt, tp, ss])
    #Outro laço para adicionar mais candidatos.
    while True:
        inserir_candidato = input('\nDeseja inserir outro candidato? (Digite "s/S" para "sim" ou "n/N" para sair): ')

        if inserir_candidato in 'Nn':
            break
        elif inserir_candidato in 'Ss':
            break
        else:
            print('Opção inválida, tente novamente.')
    
    if inserir_candidato in 'Nn':
        break

#Imprimindo os candidatos inseridos.
print('Candidatos inseridos')
for cand in candidatos:
    formato_cand = '{} - e{}_t{}_p{}_s{}'.format(cand[0], cand[1], cand[2], cand[3], cand[4])
    print(formato_cand)

#Coletando as notas mínimas.
print('\nDigite as notas mínimas: ')

#Mostrando os candidatos que atendem às notas.
print('\nCandidatos encontrados: ')
