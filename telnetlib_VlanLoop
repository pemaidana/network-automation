import getpass
import telnetlib

HOST = "IP DO HOST"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password + "\n")

tn.write(b"en\n")
tn.write(b"conf t\n")

# O parâmetro "for n" se refere na variável que estamos criando, essa variável trata-se de uma string.
# Depois setamos o valor do range no qual queremos criar as VLANs.

for n in range (2,20):
	tn.write("vlan" + str(n) + "\n")
  
  # Nessa linha é criado o nome da VLAN e associando ela à variável, com isso é alocado o mesmo número que foi alocado no comando acima
	tn.write("name vlan_" + str(n) + "\n") 

tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")

print(tn.read_all().decode('ascii'))
