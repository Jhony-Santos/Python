import socket
import sys

IPSERVIDOR='127.0.0.1'
PORTASERVIDOR=9999

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((IPSERVIDOR,PORTASERVIDOR))
except:
    print('#erro de conexão')
    sys.exit()

while True:
    try:
        line=input()
        if not line:
            print('linha vazia encerra o programa')
            break
    except:
        print('o programa abortado com CTRL+C')
        break
    data=bytes(line,'utf-8')
    tam=s.send(data)

    print('enviei ',tam,'bytes')
    print(data)