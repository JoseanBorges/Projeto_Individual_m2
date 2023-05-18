print('\nOlá seja bem vindo à consulta de candidatos aprovados!')
#Função para fazer a busca dos candidatos.
def busca_candidato(candidatos, ver_ent, ver_tt, ver_tp, ver_ss):
    candidato_aprov = []
    for candidato in candidatos:
        nome_cand = candidato[0]
        nota_e_cand = int(candidato[1])
        nota_t_cand = int(candidato[2])
        nota_p_cand = int(candidato[3])
        nota_s_cand = int(candidato[4])

        if nota_e_cand >= ver_ent and nota_t_cand >= ver_tt and nota_p_cand >= ver_tp and nota_s_cand >= ver_ss:
            candidato_aprov.append([nome_cand, nota_e_cand, nota_t_cand, nota_p_cand, nota_s_cand])
    return candidato_aprov

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
ver_ent = int(input('Nota da Entrevista: '))
ver_tt = int(input('Nota do Teste Teórico: '))
ver_tp = int(input('Nota do Teste Prático: '))
ver_ss = int(input('Nota Soft Skills: '))

#Mostrando os candidatos que atendem às notas.
print('\nCandidatos encontrados: ')
candidato_aprov = busca_candidato(candidatos, ver_ent, ver_tt, ver_tp, ver_ss)
if len(candidato_aprov) == 0:
    print('Não foram encontrados candidatos dentro dos requisitos.')
else:
    for cand in candidato_aprov:
         formato_cand = '{} - e{}_t{}_p{}_s{}'.format(cand[0], cand[1], cand[2], cand[3], cand[4])
         print(formato_cand)

print('Agradecemos por fazer uso da nossa plataforma.')