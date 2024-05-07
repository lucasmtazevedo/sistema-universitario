import json

cadastro_estudante = list() 
estudantes = {'Codigo':'000', 'Nome':'Nome', 'CPF': '0000'}

cadastro_professores = list() 
professores = {'Codigo':'000', 'Nome':'Nome', 'CPF':'0000'}

cadastro_disciplinas = list()
disciplinas = {'Codigo':'000', 'Nome':'Nome'} 

cadastro_turmas = list() 
turmas = {'Codigoturma':'000','Codigoprofessor':'000', 'Codigodisciplina':'000'}

cadastro_matriculas = list() 
matriculas = {'Codigoturma':'000', 'Codigo':'000'}

def escrever_json(data, file_name):
    with open (file_name + '.json', 'w') as f :
        json.dump(data, f, indent=4)
        f.close()

def ler_json(file_name):
    data = []
    try:
        with open(file_name + '.json', 'r') as f :
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        escrever_json(data, file_name)
        return data

def limpar_tela():

        print('\n' * 5)
 
def menu_principal():
    op = 0 
    while op != 9 :
        print ('>>>>>> Bem-vindo ao Sistema PUC <<<<<')
        print ('>>>>> Menu Principal <<<<<')
        print ('1 - Gerenciar Estudantes.')
        print ('2 - Gerenciar Professores.')
        print ('3 - Gerenciar Disciplinas.')
        print ('4 - Gerenciar Turmas.')
        print ('5 - Gerenciar Matriculas.')
        print ("9 - Sair do Sistema.")
        op = int(input('Digite a opção desejada: '))
        limpar_tela()
        if op == 1:
            menu_estudantes()            
        elif op == 2 :
            menu_professores()
        elif op == 3 :
            menu_disciplina()
        elif op == 4 :
            menu_turma()
        elif op == 5 :
            menu_matricula()
        elif op == 9 :
            print ("Saindo do sistema...")
        else :
            print ("Opção inválida, Tente novamente")

def novo_registro_estudante():
    print ('>>>>> Cadastrar Novo Registro <<<<<')
    estudantes['Codigo']= int(input('Digite o código do estudante: '))
    estudantes['Nome'] = str(input('Digite o nome do estudante: '))
    estudantes['CPF'] = str(input('Digite o CPF do estudante: '))
    cadastro_estudante.append(estudantes.copy())
    print ('Estudante cadastrado na base de dados com sucesso!!!.')
    escrever_json(cadastro_estudante, 'estudante')

def lista_estudante():
    print ('>>>>> Lista de Estudantes <<<<<')
    print(cadastro_estudante)
    if cadastro_estudante == [] :
        print('Não há estudantes cadastrados!!!.')

def atualizacao_estudante():
    print ('>>>>> Atualização <<<<<')
    atualizar = int(input('Digite o Codigo do estudante: '))
    for item in cadastro_estudante:
        if item['Codigo'] == atualizar :
            cadastro_estudante.remove(item)
            estudantes['Codigo']= int(input('Digite o novo Código do Estudante: '))
            estudantes['Nome'] = str(input('Digite o novo Nome do Estudante: '))
            estudantes['CPF'] = str(input('Digite o novo CPF do estudante: '))
            cadastro_estudante.append(estudantes.copy())
            print ('Dados do estudante atualizado com sucesso!!')
            break

def excluir_estudante():
    print('>>>>> Excluir Estudante <<<<<')
    excluir = int(input('Digite o código do estudante que desejar excluir: '))
    for item in cadastro_estudante:
        if item['Codigo'] == excluir :
            cadastro_estudante.remove(item)
            print ('Estudante excluído da base de dados com sucesso!!!')

def menu_estudantes():
    estudante = 0
    while estudante != 9:
        print ('>>>>> Gerenciamento de Estudantes <<<<<')
        print ('1. Criar novo registro')  
        print ('2. Listar registros')
        print ('3. Atualizar um registro')
        print ('4. Excluir um registro')
        print('9. Voltar ao Menu Principal')
        estudante = int(input('Digite a opção desejada: '))
        limpar_tela()
        if estudante == 1:
            novo_registro_estudante()
        elif estudante == 2:
            lista_estudante()
        elif estudante == 3:
            atualizacao_estudante()
        elif estudante == 4:
            excluir_estudante()
        else:
            print('Opção Inválida, Tente novamente!!!.')

def novo_registro_professor():
    print ('>>>>> Cadastrar Novo Registro <<<<<')
    professores['Codigo'] = int(input('Digite o código do professor: '))
    professores['Nome'] = str(input('Digite o nome do professor: '))
    professores ['CPF'] = str(input('Digite o CPF do professor: '))
    cadastro_professores.append(professores.copy())
    print ('Professor cadastrado na base de dados com sucesso!!!')
    escrever_json(cadastro_professores, 'professores')

def lista_professor():
    print('>>>>> Lista de Professores <<<<<')
    print(cadastro_professores)
    if cadastro_professores == []:
        print ('Não há professores cadastrados!!!.')

def atualizacao_professor():
    print ('>>>>> Atualização <<<<<')
    atualizar = int(input('Digite o código do professor: '))
    for item in cadastro_professores:
        if item['Codigo'] == atualizar :
            cadastro_professores.remove(item)
            professores['Codigo'] = int(input('Digite o código do professor: '))
            professores['Nome'] = str(input('Digite o nome do professor: '))
            professores ['CPF'] = str(input('Digite o CPF do professor: '))
            cadastro_professores.append(professores.copy())
            print ('Dados do professor atualizados com sucesso!!!')
            break

def excluir_professor():
    print('>>>>> Excluir Professor <<<<<')
    excluir = int(input('Digite o código do professor que deseja excluir: '))
    for item in cadastro_professores:
        if item['Codigo'] == excluir :
            cadastro_professores.remove(item)
            print('Professor excluído da base de dados com sucesso!!!')

def menu_professores():
    professor = 0
    while professor != 9:
        print ('>>>>> Gerenciamento de Professores <<<<<')
        print ('1. Criar novo registro')  
        print ('2. Listar registros')
        print ('3. Atualizar um registro')
        print ('4. Excluir um registro')
        print('9. Voltar ao Menu Principal')
        professor = int(input('Digite a opção desejada: '))
        limpar_tela()
        if professor == 1:
            novo_registro_professor()
        elif professor == 2:
            lista_professor()
        elif professor == 3:
            atualizacao_professor()
        elif professor == 4:
            excluir_professor()
        else:
            print('Opção Inválida, Tente novamente!!!.')

def novo_registro_disciplina():
    print ('>>>>> Cadastrar Novo Registro <<<<<')
    disciplinas['Codigo'] = int(input('Digite o código da disciplina: '))
    disciplinas['Nome'] = str(input('Digite o nome da disciplina: '))
    cadastro_disciplinas.append(disciplinas.copy())
    print ('Disciplina cadastrada na base de dados com sucesso!!!')
    escrever_json(cadastro_disciplinas, 'disciplinas')

def lista_disciplina():
    print('>>>>> Lista de Disciplinas <<<<<')
    print(cadastro_disciplinas)
    if cadastro_disciplinas == []:
        print ('Não há disciplinas cadastrados!!!.')

def atualizacao_disciplina():
    print ('>>>>> Atualização <<<<<')
    atualizar = int(input('Digite o código da disciplina: '))
    for item in cadastro_disciplinas:
        if item['Codigo'] == atualizar :
            cadastro_disciplinas.remove(item)
            disciplinas['Codigo'] = int(input('Digite o código da disciplina: '))
            disciplinas['Nome'] = str(input('Digite o nome da disciplina: '))
            cadastro_disciplinas.append(disciplinas.copy())
            print ('Dados da disciplina atualizados com sucesso!!!')
            break

def excluir_disciplina():
    print('>>>>> Excluir Disciplina <<<<<')
    excluir = int(input('Digite o código da disciplina que deseja excluir: '))
    for item in cadastro_disciplinas:
        if item['Codigo'] == excluir :
            cadastro_disciplinas.remove(item)
            print('Disciplina excluída da base de dados com sucesso!!!')

def menu_disciplina():
    disciplina = 0
    while disciplina != 9:
        print ('>>>>> Gerenciamento de Disciplinas <<<<<')
        print ('1. Criar novo registro')  
        print ('2. Listar registros')
        print ('3. Atualizar um registro')
        print ('4. Excluir um registro')
        print('9. Voltar ao Menu Principal')
        disciplina = int(input('Digite a opção desejada: '))
        limpar_tela()
        if disciplina == 1:
            novo_registro_disciplina()
        elif disciplina == 2:
            lista_disciplina()
        elif disciplina == 3:
            atualizacao_disciplina()
        elif disciplina == 4:
            excluir_disciplina()
        else:
            print('Opção Inválida, Tente novamente!!!.')

def novo_registro_turma():
    print ('>>>>> Cadastrar Novo Registro <<<<<')
    turmas['Codigoturma'] = int(input('Digite o código da turma: '))
    turmas['Codigoprofessor'] = int(input('Digite o código do professor: '))
    turmas['Codigodisciplina'] = int(input('Digite o código da disciplina: '))
    cadastro_turmas.append(turmas.copy())
    print ('Turma cadastrada na base de dados com sucesso!!!')
    escrever_json(cadastro_turmas, 'turmas')

def lista_turma():
    print('>>>>> Lista de Turmas <<<<<')
    print(cadastro_turmas)
    if cadastro_turmas == []:
        print ('Não há turmas cadastradas!!!.')

def atualizacao_turma():
    print ('>>>>> Atualização <<<<<')
    atualizar = int(input('Digite o código da turma: '))
    for item in cadastro_turmas:
        if item['Codigoturma'] == atualizar :
            cadastro_turmas.remove(item)
            turmas['Codigoturma'] = int(input('Digite o código da turma: '))
            turmas['Codigoprofessor'] = int(input('Digite o código do professor: '))
            turmas['Codigodisciplina'] = int(input('Digite o código da disciplina: '))
            cadastro_turmas.append(turmas.copy())
            print ('Dados da turma atualizados com sucesso!!!')
            break

def excluir_turma():
    print('>>>>> Excluir Turma <<<<<')
    excluir = int(input('Digite o código da turma que deseja excluir: '))
    for item in cadastro_turmas:
        if item['Codigoturma'] == excluir :
            cadastro_turmas.remove(item)
            print('Turma excluída da base de dados com sucesso!!!')

def menu_turma():
    turma = 0
    while turma != 9:
        print ('>>>>> Gerenciamento de Turmas <<<<<')
        print ('1. Criar novo registro')  
        print ('2. Listar registros')
        print ('3. Atualizar um registro')
        print ('4. Excluir um registro')
        print('9. Voltar ao Menu Principal')
        turma = int(input('Digite a opção desejada: '))
        limpar_tela()
        if turma == 1:
            novo_registro_turma()
        elif turma == 2:
            lista_turma()
        elif turma == 3:
            atualizacao_turma()
        elif turma == 4:
            excluir_turma()
        else:
            print('Opção Inválida, Tente novamente!!!.')

def novo_registro_matricula():
    print ('>>>>> Cadastrar Novo Registro <<<<<')
    matriculas['Codigoturma'] = int(input('Digite o código da turma: '))
    matriculas['Codigo'] = int(input('Digite o código do estudante: '))
    cadastro_matriculas.append(matriculas.copy())
    print ('Matrícula cadastrada na base de dados com sucesso!!!')
    escrever_json(cadastro_matriculas, 'matriculas')

def lista_matricula():
    print('>>>>> Lista de Matriculas <<<<<')
    print(cadastro_matriculas)
    if cadastro_matriculas == []:
        print ('Não há matrículas cadastradas!!!.')

def atualizacao_matricula():
    print ('>>>>> Atualização <<<<<')
    atualizar = int(input('Digite o código da matricula: '))
    for item in cadastro_matriculas:
        if item['Codigoturma'] == atualizar :
            cadastro_matriculas.remove(item)
            matriculas['Codigoturma'] = int(input('Digite o código da turma: '))
            matriculas['Codigo'] = int(input('Digite o código do estudante: '))
            cadastro_matriculas.append(matriculas.copy())
            print ('Dados da matrícula atualizados com sucesso!!!')
            break

def excluir_matricula():
    print('>>>>> Excluir Matrícula <<<<<')
    excluir = int(input('Digite o código da matrícula que deseja excluir: '))
    for item in cadastro_matriculas:
        if item['Codigoturma'] == excluir :
            cadastro_matriculas.remove(item)
            print('Matrícula excluída da base de dados com sucesso!!!')

def menu_matricula():
    matricula = 0
    while matricula != 9:
        print ('>>>>> Gerenciamento de Matrículas <<<<<')
        print ('1. Criar novo registro')  
        print ('2. Listar registros')
        print ('3. Atualizar um registro')
        print ('4. Excluir um registro')
        print('9. Voltar ao Menu Principal')
        matricula = int(input('Digite a opção desejada: '))
        limpar_tela()
        if matricula == 1:
            novo_registro_matricula()
        elif matricula == 2:
            lista_matricula()
        elif matricula == 3:
            atualizacao_matricula()
        elif matricula == 4:
            excluir_matricula()
        else:
            print('Opção Inválida, Tente novamente!!!.')

menu_principal()