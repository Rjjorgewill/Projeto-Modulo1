opcao=(1)
def sinistro(): # Sub menu. Reportar sinistro
    while True:
        print("=" *44)
        print("        Dificulity Proteção Veicular")
        print("=" *44)
        print("1. Roubo ")
        print("2. Colisão ")
        print("3. Incêndio/Desastre natural ")
        print("4. Outros ")
        print("5. Voltar ")
        print("6. Sair ")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if (opcao ==1):
            roubo()  
        elif(opcao== 2):
            colisao()
        elif(opcao== 3):
            incendio()
        elif(opcao== 4):
            outros()
        elif(opcao== 5):
            break
        elif (opcao == 6):
            print("\n""Atendimento encerrado.""\n")
            exit()   
        else:
            ("\n""Opcão inválida, tente novamente.")    
def roubo(): # Sub menu. Roubo
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!""\n""Vá para a delegacia mais próxima para registrar o boletim de ocorrência e retorne para cadastrar o sinistro.")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def colisao(): # Sub menu. Colisão
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!""\n""Caso não haja vítimas, leve seu veículo para um lugar seguro e retorne depois de ter realizado o registro no órgão responsável, BRAT (Polícia Militar), DAT/BAT(Polícia federal). ")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def incendio(): # Sub menu. Incêndio/Destrastre natural
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def outros(): # Sub menu. Consultar outros
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue              
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.             
            (input("Reporte com detalhes o ocorrido: "))           
            print ("\n""Solicitação enviada. Entraremos em contato imediatamente! ")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break       
def planos(): # Sub menu. Consultar planos
    while True:
        print("=" *44)
        print("1. Plano Bronze")
        print("2. Plano Prata")
        print("3. Plano Ouro")
        print("4. Voltar")
        print("5. Sair ")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        print("=" *44)
        if(opcao ==1):
            print("\n""PLANO BRONZE: ""\n"" A partir de $44,90. ""\n""Proteção contra roubo e furto (100""%"" ""FIPE*"")"". ""\n""Cobertura nacional sem perfil de condutor. ""\n""Guincho 200 km (100km ida 100km volta).""\n""")           
        elif(opcao== 2):
            print ("\n""PLANO PRATA: ""\n"" A partir de $85,00. ""\n""" "Proteção contra roubo, furto, colisão e incêndio (100""%"" ""FIPE*"")."" ""\n""Assistência 24hs em todo Brasil (Guincho, táxi, hotel,chaveiro etc…). ""\n""Guincho 400 Km (200 Km de ida e 200 Km de volta.) ""\n""Cobertura nacional sem perfil de condutor. ""\n""Proteção contra terceiros de R$30 mil (danos materiais).""\n""")
        elif(opcao== 3):
            print("\n""PLANO OURO:""\n"" A partir de $105,00.""\n""Proteção contra roubo, furto, colisão e incêndio* (100""% ""FIPE*).""\n""Assistência 24hs em todo Brasil (Guincho, táxi, hotel,chaveiro etc…).""\n""Guincho 1000 Km (500 Km de ida e 500 Km de volta.)""\n""Cobertura nacional sem perfil de condutor.""\n""Proteção contra terceiros de R$30 mil (danos materiais).""\n""Cobertura para vidros (exceto teto solar), faróis, retrovisores, lanternas de 50""%"" do valor.""\n""Carro reserva de 10 dias.""\n""")
        elif(opcao== 4):
            break
        elif (opcao ==5):           
            print("\n""Atendimento encerrado.""\n")
            exit()       
        else: 
            print ("\n""Opcão inválida, tente novamente.")
            (planos)
def duvidas(): # Sub menu. Dúvidas
    while True:
        print("=" *44)
        print("1. Quem Somos?")
        print("2. Como Funciona?")
        print("3. Onde Estamos?")
        print("4. Voltar")
        print("5. Sair ")       
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        print("=" *44)
        if(opcao ==1):
            print("\n""A Dificulity Proteção Veícular é uma Associação de Proteção Veicular sem fins lucrativos.""\n""Nosso Objetivo é reunir pessoas comprometidas em proteger-se mutuamente dos eventuais prejuízos inesperados provenientes de sinistros em seus veículos.""\n""")
        elif(opcao== 2):
            print("\n""O Programa de associados da Dificulity Proteção Veicular, foi criado pela Diretoria Executiva e aprovado em Assembleia Geral""\n""com a finalidade de proporcionar aos seus associados a proteção e assistência de seus veículos,""\n""e também oferecer aos seus associados uma série de benefícios, cujo principal serviço é a Proteção Veicular, pelo sistema de rateio.""\n""Desta forma, todos os associados dividem, entre si, através de rateio, os prejuízos materiais causados aos veículos dos associados.""\n""")
        elif(opcao== 3):
            print("\n""A Dificulity Proteção Veicular é uma sociedade civil, pessoa jurídica de direito privado e sem fins lucrativos, ou político-partidário e religioso;""\n""de âmbito nacional e com registro no CNPJ sob o número 00.000.000/0000-00 com duração por prazo indeterminado, e ilimitado número de associados.""\n""Nossa sede está localizada em Nova Iguaçu- RJ, na Av. xxxxxxx, nº xxx, Centro.""\n""")
        elif(opcao== 4):
            break
        elif (opcao== 5):
            print("\n""Atendimento encerrado.""\n")
            exit()
        else:
            print ("\n""Opcão inválida, tente novamente.")
def cotacao(): # Sub menu. Consultar planos
    (input("Nome: "))
    (input("E-mail: "))
    (input("Telefone: "))
    (input("Cidade\Estado: "))
    (input("Veículo (Modelo e ano): "))
    print ("\n""Solicitação enviada. Entraremos em contato imediatamente! ")
def faleconosco(): # Sub menu. Fale Conosco
    (input("Digite sua mensagem: "))
    print("\n""Mensagem enviada. Aguarde atendimento! ")
while opcao !="6": #Menu Principal
    print("=" *44)
    print("        Dificulity Proteção Veicular")
    print("=" *44)
    print("1. Reportar sinistro")
    print("2. Consultar planos")
    print("3. Dúvidas")
    print("4. Realizar cotação")
    print("5. Fale Conosco")
    print("6. Sair ")
    try :
        opcao = int(input("\n""Opção: "))
    except:
        print ("\n""Opcão inválida, tente novamente.")
        continue
    if(opcao==1):
        sinistro()
    elif(opcao==2):
        planos()
    elif(opcao==3):
        duvidas()
    elif(opcao==4):
        cotacao()  
    elif(opcao==5):
        faleconosco()
    elif(opcao==6):
        print("\n""Atendimento encerrado.""\n")
        break
    else:
        print ("\n""Opcão inválida, tente novamente.")
