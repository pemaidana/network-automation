# Esse script serve para você executar as mesmas configurações para os switches que você queira configurar. 

...
Para analisarmos a lógica na qual são executados comandos para printar conteúdos de um arquivo (.txt), o código abaixo simula essa lógica.

for line in f:
  print(line)
f.close()
...

import getpass
import sys
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

# A variável abaixo faz a chamada do arquivo "myswitches", nesse arquivo deverá ser inserido uma lista de endereços IPs de gerência
# dos switches que você queira aplicar uma determinada configuração. Essa lista deverá ser descrita linha por linha, 1 IP por linha.

f = open ('myswitches')

# O parâmetro line interage com a variável "f", essa variável representa o arquivo que irá ser lido pelo parâmetro line.

for line in f: 
    
    # Ao declarar o line novamente, iremos fazer com que esse parâmetro printe a linha que ele está lendo. Baseado nisso iremos perceber
    #  em qual switch está sendo executado o script.
    
    print "Configuring Switch " + (line) 
    
    # O parâmetro "line" na frente da variável HOST indica o endereço IP linha por linha do arquivo, esse IP que está sendo lido pelo
    # parâmetro line é o IP do switch no qual irá ser executado os comandos tn.write.
    
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for n in range (2,26):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
