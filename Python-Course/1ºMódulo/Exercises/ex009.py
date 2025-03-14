""" Calculadora com while """
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operação = input('Digite uma operação (+-/*): ')
    
    nums_validação = None
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        nums_validação = True
    except:
        nums_validação = None
    
    if nums_validação is None:
        print('Um ou ambos os números são inválidos!')
        continue
    
    op_validação = '+-/*'
    
    if operação not in op_validação:
        print('Operação inválida!')
        continue 
    if len(operação) > 1:
        print('Digite apenas uma operação!')
        continue
    
    if operação == '+':
        resultado = num1 + num2
    elif operação == '-':
        resultado = num1 - num2
    elif operação == '*':
        resultado = num1 * num2
    elif operação == '/':
        resultado = num1 / num2
        
    print(f'{num1} {operação} {num2} = {resultado}')
    
    saída = input('Deseja sair? [s]im ou [n]ão: ').lower().endswith('s')
    if saída:
        break