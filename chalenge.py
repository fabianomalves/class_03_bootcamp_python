# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# variables
valid_name = False
valid_salary = False
valid_bonus = False

# loop to verify name
while not valid_name:
    try:
        name = str(input('Type your name: '))
        if len(name) == 0:
            raise ValueError('The name cannot be empty')
        elif any(char.isdigit() for char in name):
            raise ValueError('The name connot contains numbers')
        else:
            print('Valid name', name)
            valid_name = True
    except ValueError as e:
        print(e)
       
# loop to verify salary
try:
    salary = float(input('Type the salary value: '))
    if salary < 0:
        print('Type a positive value.')
    else:
        salary_valid = True
except ValueError:
    print('Invalid entry for salary. Type a number.')

# loop to verify bonus
try:
    bonus = float(input('Type the bonus value: '))
    if bonus < 0:
        print('Type a positive value.')
    else:
        bonus_valid = True
except ValueError:
    print('Invalid entry for bonus. Type a number.')

received_bonus = 1000 + salary * bonus_valid

print(f'{name}, your salary is R${salary:.2f} and your final bonus is R${received_bonus:.2f}')        