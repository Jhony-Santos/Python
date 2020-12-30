import hashlib
import re

menuCadastro=True
senhaValida=False


def verifica_senha(senhaEnv):
    #DEFINICOES
    #=======================
    global senhaValida
    cont=0
    minimo_numeros = 1
    minimo_maiusculo = 1
    minimo_minusculo = 1
    minimo_especial = 1
    caracteres = 6
    #=======================
    
    if len(senhaEnv or ()) != caracteres:
        print('Senha tem que ter '+str(caracteres)+' caracteres')
        cont=cont+1

    if len(re.findall(r"[A-Z]", senhaEnv)) < minimo_maiusculo:
        print('Senha tem que ter no mínimo '+str(minimo_maiusculo)+' letra(s) maiuscula(s)')
        cont=cont+1
        
    if len(re.findall(r"[a-z]", senhaEnv)) < minimo_minusculo:
        print('Senha tem que ter no mínimo '+str(minimo_minusculo)+' letra(s) minusculas(s)')
        cont=cont+1

    if len(re.findall(r"[0-9]", senhaEnv)) < minimo_numeros:
        print('Senha tem que ter no mínimo '+str(minimo_numeros)+' numero(s)')
        cont=cont+1
    if cont == 0:
        senhaValida=True
    else:
        senhaValida=False

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
        senhaValida=False
        while senhaValida==False:
            print("Digite um Login:")
            login = input()
            print("Digite uma senha:")
            print("A senha deve conter os seguinte caracteres 'a-z' & 'A-Z' & '0-9' e deve ter um total de 6 caracteres.")
            senha=input()
            senhaHash=hashlib.md5(senha.encode()).hexdigest()
            verifica_senha(senha)
            if senhaValida==False:
                print("Operação cancelada!!! Você cometeu erros no cadastro, tente novamente...\n\n")
                break
            else:            
                print("Conta Cadastrada com Sucesso!!! Aperte 'enter' para continuar...")
                input()

                

                arquivo = open("contas/"+login+".txt", "w")#criou o .txt em modo escrita
                arquivo = open("contas/"+login+".txt", "r")#criou o .txt em modo leitura
                conteudo=arquivo.readlines()#leu conteudo e escreveu na var 'conteudo'
                conteudo.append(login+"\n")
                conteudo.append(senhaHash)
                
                arquivo = open("contas/"+login+".txt", "w")#abriu para escrever
                arquivo.writelines(conteudo)#escreveu a var 'conteudo' no .txt
                arquivo.close()









input()
