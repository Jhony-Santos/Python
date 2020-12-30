import hashlib

menuCadastro=True

while menuCadastro:
    print("Selecione uma opracao")
    print("1 = Logar Com Conta Existente")
    print("2 = Cadastrar Nova Conta")
    escolhaOperacao=int(input())
    if escolhaOperacao == 1:
        menuLogin=True
        while menuLogin:
            menuCadastro=False
            print("Digite um Login:")
            login = input()
            print("Digite uma senha:")
            senha=input()
            senhaHash=hashlib.md5(senha.encode()).hexdigest()            
            
            arquivo = open("contas/"+login+".txt", "r")
            primeiraLinha = arquivo.readline() #LE A PRIMEIRA LINHA E COLOCA NUMA VARIAVEL
            segundaLinha = arquivo.readline() # LE A SEGUNDA LINHA E COLOCA NUMA SEGUNDA VARIAVEL
            arquivo.close()
            if primeiraLinha == login or segundaLinha == senhaHash: #VERIFICA SE LOGIN == LOGIN E SENHA == SENHA+HASH
                print("Autenticado com sucesso!!!")
                menuLogin=False
            else:
                print("Login e/ou senha incorretos!!!")
                
        
    elif escolhaOperacao == 2:
        repet=True
        while repet:
            print("Digite um Login:")
            login = input()
            print("Digite uma senha:")
            senha=input()
            senhaHash=hashlib.md5(senha.encode()).hexdigest()
            if len(senha or ()) != 4:
                print('Senha deve ter 4 caracteres\n')
                break
            
            

            arquivo = open("contas/"+login+".txt", "w")#criou o .txt em modo escrita
            arquivo = open("contas/"+login+".txt", "r")#criou o .txt em modo leitura
            conteudo=arquivo.readlines()#leu conteudo e escreveu na var 'conteudo'
            conteudo.append(login+"\n")
            conteudo.append(senhaHash)
            
            arquivo = open("contas/"+login+".txt", "w")#abriu para escrever
            arquivo.writelines(conteudo)#escreveu a var 'conteudo' no .txt
            arquivo.close()









input()
