import socket
import sys

HOST='127.0.0.1'
PORT=9999
#PORT=int(input('A porta do servidor: ')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
 s.bind((HOST,PORT))
except:
    print('# erro de bind')
    sys.exit()
s.listen(5)
while True:
    print('aguardando conexões em, ',PORT)
    conn, addr=s.accept()
    print('recebi uma conexão de ',addr)

    print('O cliente encerrou')
    conn.close()

   # while True:
    #    data=conn.recv(1024)
     #   print('recebi',len(data),' bytes')

      #  if not data:
       #     break
        #print(data)

        #print('a conexão foi encerrada')
        #conn.close()

    #print('O cliente encerrou')
    #conn.close()

    ## 25/03

#import socket
#import sys

#HOST='127.0.0.1'
#PORT=9999
#PORT=int(input('A porta do servidor: ')

#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#try:
#    s.bind((HOST,PORT))
#except:
 #   print('# erro de bind')
 #   sys.exit()
#s.listen(5)
#while True:
 #   print('aguardando conexões em, ',PORT)
  #  conn, addr=s.accept()
   # print('recebi uma conexão de ',addr)

    #while True:
     #   input('Digita qualquer coisa ai chara')
      #  print ('recebi ',len(data),' bytes')
       # if not data:
        #    break

        #print (data)

    #print('a conexão foi encerrada')
    #conn.close()



