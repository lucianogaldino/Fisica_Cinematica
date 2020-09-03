import cinret
from time import sleep
print('='*20)
print('------CINECALC------')
print('='*20)
print('ORIENTAÇÕES:\n'
      '1) Utilizar os valores com unidades de medidas no SI.\n'
      '2) Colocar a sigla que representa a qual tipo de movimento que você deseja calcular.\n'
      '3) Colocar ponto ao invés de vírgula para representar as casas decimais dos algarismos')
print()
opcao = str(input('Indique a que se refere o seu cálculo: '
                    'Velocidade Média[vm], Aceleração Média [am],\n Movimento Retilíneo Uniforme[mru],'
                    'Movimento Retilíneo Uniformemente Variado[mruv]: ')).strip().upper()[0:4]

#CÁLCULO DA VELOCIDADE MÉDIA
if opcao == 'VM':
    cinret.velmed(str(input(f'Digite a velocidade média em m/s: ')).strip(),
           str(input(f'Digite a variação da posição em m: ')).strip(),
           str(input(f'Digite a variação do tempo em s: ')).strip())

#CÁLCULO DA ACELERAÇÃO MÉDIA
elif opcao == 'AM':
    cinret.acelmed(str(input(f'Digite a aceleração média em m/s2: ')).strip(),
            str(input(f'Digite a variação da velocidade em m/s: ')).strip(),
            str(input(f'Digite a variação do tempo em s: ')).strip())

#CÁLCULO DO MOVIMENTO RETILÍNEO UNIFORME
elif opcao == 'MRU':
    cinret.mru(str(input(f'Digite a posição final em m: ')).strip(),
        str(input(f'Digite a posição inicial em m: ')).strip(),
        str(input(f'Digite a velocidade em m/s: ')).strip(),
        str(input(f'Digite a varição do tempo em s: ')))

#CÁLCULO DO MOVIMENTO RETÍLINEO UNIFORMEMENTE VARIADO
elif opcao == 'MRUV':
    cinret.mruv(str(input(f'Digite a posição final em m: ')).strip(),
         str(input(f'Digite a posição inicial em m: ')).strip(),
         str(input(f'Digite o deslocamento em m: ')).strip(),
         str(input(f'Digite a velocidade final em m/s: ')).strip(),
         str(input(f'Digite a velocidade inicial em m/s: ')).strip(),
         str(input(f'Digite a aceleração em m/s2: ')).strip(),
         str(input(f'Digite a variação do tempo em s: ')).strip())
else:
    print('Opção inválida, tente novamente!')
    sleep(1)