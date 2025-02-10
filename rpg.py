import random #import para randomizar números
from time import sleep #import para delay
delay = 1 #definição do tempo de delay para 1 segundos
delay2 = 2 #definição do tempo de delay para 2 segundos
delay3 = 3 #definição do tempo de delay para 3 segundos

#ESCOLHA DA CLASSE-------------------------------------------------------------------------------------------------------------------------------------------------------------
classe = 'undefined'#faz com que inicialmente seja indefinido a variável classe
confirmacaoClasse = 'undefined'#faz com que inicialmente seja indefinido a variável confirmacaoClasse
lowercase_classe = 'undefined' #faz com que inicialmente seja indefinido a variável lowercase_classe

while lowercase_classe != 'guerreiro' and lowercase_classe != 'mago' and lowercase_classe != 'ladino': 
    classe = input("escolha sua classe: Guerreiro, Mago ou Ladino: ")
    lowercase_classe = classe.lower() #faz com a entrada do usuário fique em minúsculo

#DEFINIR VALORES DE VIDA E MANA COM BASE NA CLASSE
if lowercase_classe == 'guerreiro':
    vidaMax = 250
    defesaFisica = 0.8 #20% de redução de dano
    defesaMagica = 0.8
elif lowercase_classe == 'mago':
    vidaMax = 100
    defesaFisica = 0.95 #5% de redução de dano
    defesaMagica = 0.95
elif lowercase_classe == 'ladino':
    vidaMax = 150
    defesaFisica = 0.9 #10% de redução de dano
    defesaMagica = 0.9

#MOSTRAR A CLASSE E OS VALORES  
print(f'Sua classe é {lowercase_classe} e sua vida é {vidaMax}')

sleep(delay)#delay

#ESCOLHA DA HABILIDADE DA CLASSE------------------------------------------------------------------------------------------------------------------------------------------------
habilidadeClasse = 'undefined'#faz com que inicialmente seja indefinido a variável habilidadeClasse
if lowercase_classe == 'guerreiro':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para fúria (aumento de dano em 50% por 3 rodadas), digite 2 para golpe desleal (30 de dano real) ou digite 3 para revigorância (recupera instantaneamente 40 de vida, ultrapassando o valor base): ")
elif lowercase_classe == 'mago':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para bola de fogo (100 de dano mágico), digite 2 para raio (20 de dano real e atordoa o inimigo) ou digite 3 para véu mágico (sofre 40% menos de dano por 3 rodadas): ")
elif lowercase_classe == 'ladino':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para roubo (roube 20 de vida do adversário), digite 2 para astúcia (por 3 rodadas você terá 1/3 de chance de desviar do ataque) ou digite 3 para ataque surpresa (50 de dano real): ")

sleep(delay)#delay    

#MOSTRAR AO USUÁRIO A HABILIDADE ESCOLHIDA
#GUERREIRO
if lowercase_classe == 'guerreiro' and habilidadeClasse == '1':
    habilidadeClasse = 'fúria'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif lowercase_classe == 'guerreiro' and habilidadeClasse == '2':
    habilidadeClasse = 'golpe desleal'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif lowercase_classe == 'guerreiro' and habilidadeClasse == '3':
    habilidadeClasse = 'revigorância'
    print(f'Sua habilidade é {habilidadeClasse}')
#MAGO
elif lowercase_classe == 'mago' and habilidadeClasse == '1':
    habilidadeClasse = 'bola de fogo'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif lowercase_classe == 'mago' and habilidadeClasse == '2':
    habilidadeClasse = 'raio'
    print(f'Sua habilidade é {habilidadeClasse}')
elif lowercase_classe == 'mago' and habilidadeClasse == '3':
    habilidadeClasse = 'véu mágico'
    print(f'Sua habilidade é {habilidadeClasse}')
#LADINO
elif lowercase_classe == 'ladino' and habilidadeClasse == '1':
    habilidadeClasse = 'roubo'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif lowercase_classe == 'ladino' and habilidadeClasse == '2':
    habilidadeClasse = 'astúcia'
    print(f'Sua habilidade é {habilidadeClasse}')
elif lowercase_classe == 'ladino' and habilidadeClasse == '3':
    habilidadeClasse = 'ataque surpresa'
    print(f'Sua habilidade é {habilidadeClasse}')

#ESCOLHA DO EQUIPAMENTO------------------------------------------------------------------------------------------------------------------------------------------------
equipamento = 'undefined'#faz com que inicialmente seja indefinido a variável habilidadeClasse
if lowercase_classe == 'guerreiro':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 para espada longa (40 de dano físico), digite 2 para espada e escudo (25 de dano físico e sofre 10% menos de dano): ")
elif lowercase_classe == 'mago':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 para cajado mágico (40 de dano mágico), digite 2 para adaga mágica (25 de dano mágico e 15 de dano físico): ")
elif lowercase_classe == 'ladino':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 rapieira (30 de dano físico e 1/4 de chance de duplicar o dano), digite 2 para bastão (20 de dano físico e 1/4 de chance de atordoar o inimigo por 1 turno): ")

sleep(delay)#delay 

#MOSTRAR AO USUÁRIO O EQUIPAMENTO ESCOLHIDO
#GUERREIRO
if lowercase_classe == 'guerreiro' and equipamento == '1':
    equipamento = 'espada longa'
    danoFisico = 40
    danoMagico = 0
    atordoamento = '0'
elif lowercase_classe == 'guerreiro' and equipamento == '2':
    equipamento = 'espada e escudo'
    danoFisico = 25
    danoMagico = 0
    defesaFisica = defesaFisica - 0.1
    defesaMagica = defesaMagica - 0.1
    atordoamento = '0'
#MAGO
elif lowercase_classe == 'mago' and equipamento == '1':
    equipamento = 'cajado mágico'
    danoFisico = 0
    danoMagico = 40
    atordoamento = '0'
elif lowercase_classe == 'mago' and equipamento == '2':
    equipamento = 'adaga mágica'
    danoFisico = 15
    danoMagico = 25
    atordoamento = '0'
#LADINO
elif lowercase_classe == 'ladino' and equipamento == '1':
    equipamento = 'rapieira'
    danoFisico = 30
    danoMagico = 0
    atordoamento = '0'
elif lowercase_classe == 'ladino' and equipamento == '2':
    equipamento = 'bastão'
    danoFisico = 25
    danoMagico = 0 
    atordoamento = '0'
print(f'Seu equipamento é {equipamento}')

sleep(delay2)#delay

#FALAR TODOS OS ATRIBUTOS------------------------------------------------------------------------------------------------------------------------------------------------
print(f'Sua classe é {lowercase_classe}, sua vida é {vidaMax}, sua habilidade é {habilidadeClasse}, e seu equipamento é {equipamento}')

sleep(delay2)#delay

#ESCOLHA ALEATÓRIA DO INIMIGO--------------------------------------------------------------------------------------------------------------------------------------------
inimigo = random.randint(4,4) #faz a variável inimigo ter um valor entre 1 a 4

#Goliath
if inimigo == 1:
    inimigo = 'Goliath'
    vidaInimigo = random.randint(400,800)
    danoFisicoInimigo = random.randint(10,15)
    danoMagicoInimigo = 0
    defesaFisicaInimigo = 0.9
    defesaMagicaInimigo = 0.9
    habilidadeInimigo = 'Enfurecido' #sofre 55% menos dano quando abaixo de 150 de vida
#Caçador de mago
if inimigo == 2:
    inimigo = 'Caçador de magos'
    vidaInimigo = random.randint(90,120)
    danoFisicoInimigo = random.randint(40,60)
    danoMagicoInimigo = 0
    defesaFisicaInimigo = 1.1
    defesaMagicaInimigo = 0.4
    habilidadeInimigo = 'Caçar magia' #o usuário não poderá mais utlizar habilidade até o fim do combate, usa no início do 1 turno do combate
#Mago antigo
if inimigo == 3:
    inimigo = 'mago antigo'
    vidaInimigo = random.randint(45,75)
    danoFisicoInimigo = 0
    danoMagicoInimigo = random.randint(45,85)
    defesaFisicaInimigo = 0.5
    defesaMagicaInimigo = 1.1
    habilidadeInimigo = 'Marca da morte' #causa 15 de dano real no jogador no início do turno até o fim do combate, usa no início do 1 turno
#Guerreiro de pedra
if inimigo == 4:
    inimigo = 'guerreiro de pedra'
    vidaInimigo = random.randint(250,600)
    danoFisicoInimigo = random.randint(15,25)
    danoMagicoInimigo = 0
    defesaFisicaInimigo = 0.8
    defesaMagicaInimigo = 0.8
    habilidadeInimigo = 'Petrificar' #petrifica o jogador, que pulará o próximo turno do mesmo, tem 1/2 de chance de ser usado por turno, após ser utilizado, voltara a a funcionar em 5 turnos
print(f'Seu inimigo é {inimigo}, com vida de {vidaInimigo}, dano físico de {danoFisicoInimigo}, dano mágico de {danoMagicoInimigo}, e sua habilidade é {habilidadeInimigo}') #falar o inimigo e seus atributos

sleep(delay3)#delay

#BATALHA------------------------------------------------------------------------------------------------------------------------------------------------
turno = 1 #define o turno inicial como 1
acao = 'undefined' #define a variável acao como indefinido
usoHabilidade = 'undefined' #define a variável usoHabilidade como indefinido
chanceDeCritar = 0 #define a variável chanceDeCritar como indefinido
contadorHabilidade = 5 #define a variável contadorHabilidade como 5
contadorFuria = 5 #define a variável contadorFuria como 5
contadorVeu = 5 #define a variável contadorVeu como 5
contadorAstucia = 5 #define a variável contadorAstucia como 5
desvioAstucia = 0 #define a variável desvioAstucia como 0
contadorEnfurecido = 0 #define como 0 o contador contadorEnfurecido(habilidade do inimigo Goliath)
contadorCacarmagia = 0 #define como 0 o contador contadorCacarmagia(habilidade do inimigo caçador de mago)
contadorMarcadamorte = 0 #define como 0 o contador contadorMarcadamorte(habilidade do inimigo mago antigo)
contadorPetrificar = 5 #define como 5 o contador contadorPetrificar(habilidade do inimigo guerreiro de pedra)
petrificar = 0 #define a variável petrificar como 0

print("Começo da batalha!")

while vidaInimigo >= 0 and vidaMax >= 0:
    bloqueio = '0'#define o bloqueio como 0
    desvio = '0'#define o desvio como 0

    #habilidade Goliath
    if inimigo == 'Goliath' and vidaInimigo <= 150:
        defesaFisicaInimigo = 0.35
        defesaMagicaInimigo = 0.35
        if contadorEnfurecido == 0:
            print("Goliath ficou enfurecido!!!")
            contadorEnfurecido = 1

    #habilidade caçador de mago
    if inimigo == 'Caçador de magos' and contadorCacarmagia == 0:
        contadorHabilidade = 0
        print("Caçador de magos usou caçar magia!!!")
        contadorCacarmagia = 1

    #habilidade mago antigo
    if inimigo == 'mago antigo':
        vidaMax = vidaMax - 15
        if contadorMarcadamorte == 0:
            print("Mago antigo usou Marca da morte e lhe causou 15 de dano!!!")
            contadorMarcadamorte = 1
        else:
            print("Marca da morte te causou 15 de dano!!!")

    #habilidade guerreiro de pedra
    if inimigo == 'guerreiro de pedra' and contadorPetrificar >= 5: 
        petrificar = random.randint(1,2)
        if petrificar == 2:
            print ("Você foi petrificado!!!")
            contadorPetrificar = 0


    if contadorHabilidade >= 5:
        while usoHabilidade != '1' and usoHabilidade != '2':
            usoHabilidade = input(f'Quer usar sua habilidade {habilidadeClasse} 1 para sim 2 para não: ')

        #GUERREIRO
        if lowercase_classe == 'guerreiro' and habilidadeClasse == 'fúria' and usoHabilidade == "1": #fúria funcional
            contadorFuria = 0
            if contadorFuria <= 4: #contador da fúria
                danoExtraFisico = danoFisico * 1.5
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'guerreiro' and habilidadeClasse == 'golpe desleal' and usoHabilidade == "1": #golpe desleal funcional
            vidaInimigo = vidaInimigo - 30
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'guerreiro' and habilidadeClasse == 'revigorância' and usoHabilidade == "1": #revigorância funcional
            vidaMax = vidaMax + 40
            print(f'Você usou sua habilidade {habilidadeClasse}!')


        #MAGO
        elif lowercase_classe == 'mago' and habilidadeClasse == 'bola de fogo' and usoHabilidade == "1": #bola de fogo funcional
            vidaInimigo = vidaInimigo - (100 * defesaMagicaInimigo)
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'mago' and habilidadeClasse == 'raio' and usoHabilidade == "1": #raio funcional
            vidaInimigo = vidaInimigo - 20
            atordoamento = '1'
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'mago' and habilidadeClasse == 'véu mágico' and usoHabilidade == "1": #véu mágico funcional
            contadorVeu = 0
            if contadorVeu <= 4: #contador do véu mágico
                defesaFisica = defesaFisica * 1.40
                defesaMagica = defesaMagica * 1.40
            print(f'Você usou sua habilidade {habilidadeClasse}!')


        #LADINO
        elif lowercase_classe == 'ladino' and habilidadeClasse == 'roubo' and usoHabilidade == "1": #roubo funcional
            vidaInimigo = vidaInimigo - 20
            vidaMax = vidaMax + 20
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'ladino' and habilidadeClasse == 'astúcia' and usoHabilidade == "1": #astúcia funcional
            contadorAstucia = 0
            print(f'Você usou sua habilidade {habilidadeClasse}!')
        elif lowercase_classe == 'ladino' and habilidadeClasse == 'ataque surpresa': #ataque surpresa funcional
            vidaInimigo = vidaInimigo - 50
            print(f'Você usou sua habilidade {habilidadeClasse}!')


        if usoHabilidade == '1':
            contadorHabilidade = 0 #define o contadorHabilidade como 0

    #CONTADOR DA FÚRIA
    if contadorFuria < 4:
        contadorFuria = contadorFuria + 1
        if contadorFuria < 4:
            print(f'Faltam {3 - contadorFuria} rodadas para acabar a habilidade fúria')
        else:
            print('Você não está mais enfurecido!')

    #CONTADOR DO VÉU MÁGICO
    if contadorVeu < 4:
        contadorVeu = contadorVeu + 1
        if contadorVeu < 4:
            print(f'Faltam {3 - contadorVeu} rodadas para acabar a habilidade véu mágico')
        else:
            print('Você não está mais com o véu mágico ativo!')
            defesaFisica = defesaFisica / 1.4
            defesaMagica = defesaMagica / 1.4

    #CONTADOR DA ASTÚCIA
    if contadorAstucia < 4:
        contadorAstucia = contadorAstucia + 1
        if contadorAstucia < 4:
            print(f'Faltam {3 - contadorAstucia} rodadas para acabar a habilidade Astúcia')
            desvioAstucia = random.randint(1,3)
        else:
            print('Você não está mais com a habilidade Astúcia ativa!!')

    #CHANCE DE ATORDOAR EQUIPAMENTO BASTÃO LADINO
    if equipamento == 'bastão':
        chanceAtordoar = random.randint(1,4)
        if chanceAtordoar == 1: #if para verificar se o ataque vai atordoar 
            atordoamento = '1'
            print("ATORDOAMENTO!!!!!!!!")
        else:
            atordoamento = '0'

    #CHANCE DE CRITAR EQUIPAMENTO RAPIEIRA LADINO
    if equipamento == 'rapieira':
        chanceDeCritar = random.randint(1,4)
        if chanceDeCritar == 1: #if para verificar se o ataque foi crítico
            danoFisico = 90
            danoMagico = 0 
            print("CRÍTICO!!!!!!!!")
        else:
            danoFisico = 30
            danoMagico = 0 

    #ESCOLHA DAS AÇÕES + VERIFICA SE O JOGADOR NÃO ESTÁ PETRIFICADO
    while acao != '1' and acao != '2' and acao != '3' and petrificar != 2: 
        acao = input("Escolha sua ação: 1 para bloqueio 2 para ataque rápido 3 para ataque carregado): ")

    #DESVIO (HABILIDADE ASTUCIA DO LADINO)
    if contadorAstucia < 4:
        if desvioAstucia == 1:
            desvio = '1'
            print("VOCÊ DESVIOU DO ATAQUE!!!!!!!")
        else:
            print("DESVIO FALHOU")
    #BLOQUEIO
    if acao == '1':
        chanceBloqueio = random.randint(1,3)
        if chanceBloqueio == 1:
            bloqueio = '1'
            print("VOCÊ BLOQUEOU O ATAQUE!!!!!!!")
        else:
            print("BLOQUEIO FALHOU")
    #ATAQUE RÁPIDO
    elif acao == '2':
        if contadorFuria < 4:#verifica se a fúria está ativa
            vidaInimigo = (vidaInimigo - (danoExtraFisico * defesaFisicaInimigo)) - danoMagico * defesaMagicaInimigo
            print("ATAQUE RÁPIDO ENFURECIDO!!!!")
        else:
            vidaInimigo = (vidaInimigo - (danoFisico * defesaFisicaInimigo)) - danoMagico * defesaMagicaInimigo
            print("ATAQUE RÁPIDO!!!!") 
    #ATAQUE CARREGADO
    elif acao == '3':
        chanceAcertoCarregado = random.randint(1,3)
        if chanceAcertoCarregado == 1:
            if contadorFuria < 4:#verifica se a fúria está ativa
                vidaInimigo = (vidaInimigo - (danoExtraFisico * defesaFisicaInimigo)) - danoMagico * defesaMagicaInimigo
                print("ATAQUE CARREGADO ENFURECIDO!!!!")
            else:
                vidaInimigo = (vidaInimigo - ((danoFisico * 2) * defesaFisicaInimigo)) - (danoMagico * 2) * defesaMagicaInimigo
                print("ATAQUE CARREGADO ACERTOU!!!!")
        else:
            print("ATAQUE CARREGADO FALHOU!!!!")

    if chanceDeCritar == 1: #if para falar ao usuário de rapieira se critou ou não
            print("CRÍTICO!!!!!!!!")

    print(f'Vida atualmente do inimigo é {vidaInimigo:,.1f}') #falar ao usuário vida atual do inimigo

    if atordoamento == '0' and bloqueio != '1' and desvio !='1':
        vidaMax = (vidaMax - (danoFisicoInimigo * defesaFisica)) - danoMagicoInimigo * defesaMagica
        print(f'Sua vida atualmente é {vidaMax:,.1f}') #falar ao usuário sua vida atual

    sleep(delay2)#delay

    #contador de turno
    print(f'Fim do {turno} turno! -------------------------------------------------------')
    turno = turno + 1
    acao = 'undefined' #define a variável acao como indefinido
    atordoamento = '0'
    usoHabilidade = '3' #define usoHabilidade como 3
    desvioAstucia = 0 #define desvioAstucia como 0
    petrificar = 1

    if contadorHabilidade < 5 and inimigo != 'Caçador de magos':
        contadorHabilidade = contadorHabilidade + 1 #aumento o contador da habilidade em 1
        print(f'Faltam {5 - contadorHabilidade} turnos para usar sua habilidade')

    if contadorPetrificar < 5:
        contadorPetrificar = contadorPetrificar + 1
    
if vidaMax > vidaInimigo:
    print("Você ganhou!")
else:
    print("Você perdeu!")