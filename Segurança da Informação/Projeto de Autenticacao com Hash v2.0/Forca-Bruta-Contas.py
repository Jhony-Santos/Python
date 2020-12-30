
import time
import itertools, string
import hashlib
import sys
import signal
import threading

info = """
  Name            : Python Md5 Brute-force
  Created By      : Sefa Said Deniz
  Blog            : sefasaiddeniz.com
  Documentation   : https://github.com/sefasaid/python-md5-bruteforce/
  License         : Completely Free
  Thanks to       :  Agus Makmun (Summon Agus)-bloggersmart.net - python.web.id
"""
done = False
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global done
    done=True
    sys.exit(0)
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==True:
            break
            
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    


def _attack(chrs, inputt):
    print("[+] Start Time: ", time.strftime('%H:%M:%S'))
    start_time = time.time()
    t = threading.Thread(target=animate)
    t.start()
    total_pass_try=0
    for n in range(1, 31+1):
      characterstart_time = time.time()
      print("\n[!] I'm at ", n , "-character")
      
      for xs in itertools.product(chrs, repeat=n):
          saved = ''.join(xs)
          stringg = saved
          m = hashlib.md5()
          m.update(bytes(saved, encoding='utf-8'))
          total_pass_try +=1
          if m.hexdigest() == inputt:
              time.sleep(10)
              global done
              done = True

              print("\n[!] Encontrado! ", stringg)
              print("\n[-] Tempo para Termino: ", time.strftime('%H:%M:%S'))
              print("\n[-] Total de caracteres utilizados: ", total_pass_try)
              print("\n---Md5 foi descoberto em %s segundos ---" % (time.time() - start_time))
              sys.exit("Obrgado!!!")
        
      print("\n[!]",n,"-character finished in %s seconds ---" % (time.time() - characterstart_time))

def main():
    print(info)
    usrSelecionado = input(" Digite o nome do usuario que deseja \n")
    arquivo = open("contas/"+usrSelecionado+".txt", "r")
    primeiraLinha = arquivo.readline() #LE A PRIMEIRA LINHA E COLOCA NUMA VARIAVEL
    segundaLinha = arquivo.readline() # LE A SEGUNDA LINHA E COLOCA NUMA SEGUNDA VARIAVEL
    arquivo.close()

    inp_usr = segundaLinha
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    print(chrs)
    signal.signal(signal.SIGINT, signal_handler)
    return _attack( chrs,inp_usr )

if __name__ == "__main__":
    main()
   
   
   
