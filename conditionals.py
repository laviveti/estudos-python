nota = float(input('Informe a nota do aluno: '))

if nota >= 7:
  print('Aprovado')
if nota < 7.0 and nota >= 4.0:
  print('Tem direito à exame')
if nota < 4.0:
  print('Reprovado')