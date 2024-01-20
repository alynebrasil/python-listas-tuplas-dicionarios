contatos = {'Daniele':'098-765-432','Cibele':'876-00-000','Laura':'871-827-123','Alyne':'123-456-789', 'Livia':'111-222-333', 'Gabriela':'321-654-987', 'Renata':'102-938-475', 'Gessyca':'567-489-389', 'Ana Maria':'102-030-040', 'Thayna':'900-800-700'}

nome_procurado = input('Digite o nome que deseja consultar na lista de contatos: ')

if nome_procurado in contatos:
    telefone = contatos[nome_procurado]
    print(f'O número de telefone de {nome_procurado} é {telefone}')
else:
    print(f'Desculpe, o contato {nome_procurado} não consta na lista de contatos.')