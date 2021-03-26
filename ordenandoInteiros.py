while True:
    vetor = [];
    
    print("\n\nDigite o primeiro número: ");
    a = int(input())
    print("Digite o segundo número: ");
    b = int(input())
    print("Digite o terceiro número: ");
    c = int(input())




    if ((a < b) and (a < c)): # SE O PRIMEIRO FOR MENOR QUE OS DOIS ...

        if (b < c): # SE O SEGUNDO FOR MENOR QUE O TERCEIRO
            vetor.append(a)
            vetor.append(b)
            vetor.append(c)
             
        else: # SE O SEGUNDO FOR MAIOR QUE O TERCEIRO
            vetor.append(a)
            vetor.append(c)
            vetor.append(b)
            

    elif ((a > b) and (a < c)): # SE O PRIMEIRO FOR MAIOR QUE O SEGUNDO E MENOR QUE O TERCEIRO (2,1,3)
        vetor.append(b)
        vetor.append(a)
        vetor.append(c)

    elif ((a > b) and (a > c)):
        if (b > c):
            vetor.append(c)
            vetor.append(b)
            vetor.append(a)
            
        else:
            vetor.append(b)
            vetor.append(c)
            vetor.append(a)

    elif ((a < b) and (a > c)):
        vetor.append(c)
        vetor.append(a)
        vetor.append(b)
        

    a = vetor[0]
    b = vetor[1]
    c = vetor[2]


    
    print("\n[",a,b,c,"]");





