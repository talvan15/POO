dicionario = {}
def cadastrarAluno():

        while True:
                caso = int(input('Cadastrar novo aluno? Digite 1 para SIM e 0 para NÃO '))

                if caso == 1:
                        nome = input('Nome: ')

                        notas = []
                          
                        notas = [int(input(f'nota {i + 1}: '))for i in range(3)]

                        dicionario[nome] = notas

                elif caso == 0:
                        break

                else:
                        print(f'Digite um numero válido: ')
                        caso = int(input(''))

        print(f'{dicionario}')

#calcular media
def calcularMedia(aluno):
        medias = {}
        for aluno, notas in dicionario.items():
                media = sum(notas) / len(notas)
                medias[aluno] = media

                print(f"{aluno}: {media:.2f}")
                if media >= 7:
                        print(f'\nAluno aprovado! \n')
                else:
                        print(f'\nAluno reprovado! \n')


# cadastrar aluno:
while True:
        print("Escolha uma opção")
        caso = int(input('1-para cadastrar aluno\n2-para calcular media do aluno\n3-para media da turma\n0-para encerrar o programa\n '))
        if caso == 1:
                cadastrarAluno()
        elif caso == 2:
                aluno = calcularMedia(input('Aluno: '))
        else:
                break
