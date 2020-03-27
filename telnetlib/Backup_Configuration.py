# Esse script serve para fazer backup de configuração nos devices.

import getpass
#import sys
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

#  
f = open ("myswitches")

#  
for line in f:
	print "Getting running-config " + (line)
	
  # line.strip() faz com que os espaçamentos em branco do lado esquerdo e direito dos caracteres são retirados. EX. ( A B C ) para (ABC)
  HOST = line.strip() # Ou pode inserir apenas o parâmetro "line".
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")
  
  # Esse comando serve para que a saída do comando seja executada por completo, sem pausa ou interrupções de CLI.
	tn.write("terminal length 0\n")
	tn.write("show run\n")
	tn.write("exit\n")
        
        # Esse parâmetro read_all se refere que, todos os dados vão ser lidos até a conexão ser fechada.
        readoutput = tn.read_all()
        
        # Criamos a variável e atribuímos ela ao parâmetro "open" (arquivo) e ao mesmo tempo inserimos um nome para esse arquivo. 
        saveoutput =  open("switch" + HOST, "w") # ao invés de "w", não insere nada.
        
        #Integramos a variável saveoutput junto com o parâmetro ".write". Esse parâmetro faz a escrita dentro do arquivo que foi
        #que foi alocado na variável saveoutput.
        
        #Dentro desse parâmetro de escrita, associamos ele à variável "readoutput" para escrever os dados que estão sendo lidos
        #pela variável "readoutput".        
        saveoutput.write(readoutput)
        
        # O parâmetro de execução abaixo está alocado "\n", esse comando inclui uma linha em branco abaixo da saída do comando IOS.
        saveoutput.write("\n")
	      saveoutput.close
        print tn.read_all()
