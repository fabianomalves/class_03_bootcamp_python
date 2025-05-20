# # Exercício 1: Verificação de Qualidade de Dados
# # Você está analisando um conjunto de dados de vendas e precisa garantir
# # que todos os registros tenham valores positivos para `quantidade` e `preço`.
# # Escreva um programa que verifique esses campos e imprima "Dados válidos"
# # se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantity = -1
# price = 20

# if quantity > 0 and price > 0:
#     print('Valid data')
# else:
#     print('Invalid data')


# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada
# leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperature = 27

if temperature < 18:
    print('Low temperature')
elif temperature >= 18 and temperature <= 26:
    print('Normal temperature')
else:
    print('High temperature')

# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.


# # Exercício 1: Verificação de Qualidade de Dados
# # Você está analisando um conjunto de dados de vendas e precisa garantir
# # que todos os registros tenham valores positivos para `quantidade` e `preço`.
# # Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# # forem positivos ou "Dados inválidos" caso contrário.
# quantity = 10
# price = 20
# if quantity > 0 and price > 0:
#     print('Valid Data')
# else:
#     print('Invalid Data')

# # Exercício 2: Classificação de Dados de Sensor
# # Imagine que você está trabalhando com dados de sensores IoT.
# # Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# # como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# # Temperatura < 18°C é 'Baixa'
# # Temperatura >= 18°C e <= 26°C é 'Normal'
# # Temperatura > 26°C é 'Alta'
# temperature = 27

# if temperature < 18:
#     print('Low temperature')
# elif temperature >= 18 and temperature <= 26:
#     print('Normal temperature')
# else:
#     print('High temperature')

# # Exercício 3: Filtragem de Logs por Severidade
# # Você está analisando logs de uma aplicação e precisa filtrar mensagens
# # com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# # como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# # escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

# # Exercício 4: Validação de Dados de Entrada
# # Antes de processar os dados de usuários em um sistema de recomendação,
# # você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# # fornecido um email válido. Escreva um programa que valide essas condições
# # e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# age = 18
# email = 'teste@example.com'

# if not 18 <= age <= 65:
#     print('Age out of range')
# elif '@' not in email or '.' not in email:
#     print('Invalid email address')
# else:
#     print('Valid user data')

# # Exercício 5: Detecção de Anomalias em Dados de Transações
# # Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# # transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# # a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# # Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transaction = {'valor': 10000, 'hora': 18}

# if transaction['valor'] > 10000 or transaction['hora'] < 9 or transaction['hora'] > 18:
#     print('Suspecious transaction')
# else:
#     print('Normal transaction')

# # Exercício 6. Contagem de Palavras em Textos
# # Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# text = 'a raposa marrom salta sobre o cachorro marrom e preguiçoso'
# words = text.split(' ')
# words_count = {}

# for word in words:
#     if word in words_count:
#         words_count[word] += 1
#     else:
#         words_count[word] = 1
# print(words_count)

# # Exercício 7. Normalização de Dados
# # Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# min_number = min(numbers)
# max_number = max(numbers)
# normalized_numbers = [( x - min_number) / (max_number - min_number) for x in numbers]

# print(normalized_numbers)

# # Exercício 8. Filtragem de Dados Faltantes
# # Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# users = [
#     {'name': 'Fabiano', 'email': 'teste@teste.com'},
#     {'name': 'Allison', 'email':''},
#     {'name': 'José', 'email': 'jose@teste.com'}
#     ]
# valid_users = [user for user in users if user['email']]
# print(valid_users)

# # Exercício 9. Extração de Subconjuntos de Dados
# # Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# numbers = range(1, 11)
# even = [x for x in numbers if x % 2 == 0]

# print(even)


# # Exercício 10. Agregação de Dados por Categoria
# # Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# sales = [
#     {'category': 'eletronics', 'value': 1200},
#     {'category': 'books', 'value': 200},
#     {'category': 'eletronics', 'value': 200}
#     ]
# sales_by_category = {}

# for sale in sales:
#     category = sale['category']
#     value = sale['value']
#     if category in sales_by_category:
#         sales_by_category[category] += value
#     else:
#         sales_by_category[category] = value
# print(sales_by_category)

# # Exercícios com WHILE

# # Exercício 11. Leitura de Dados até Flag
# # Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# data = []
# enter_data = ''
# while enter_data.lower() != 'exit':
#     enter_data = input('Type a value (or "exit" to end the program): ')
#     if enter_data.lower() != 'exit':
#         data.append(enter_data)
# print(data)

# # Exercício 12. Validação de Entrada
# # Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# number = int(input('Type a number between 1 and 10: '))

# while number < 1 or number > 10:
#     print(f'Number out of interval: {number}')
#     number = int(input('Type a number between 1 and 10: '))
# print(f'Valid number: {number}')

# # Exercício 13. Consumo de API Simulado
# # Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# current_page = 1
# total_pages = 5

# while current_page <= total_pages:
#     print(f'Processing page {current_page} from {total_pages}')
#     current_page += 1
# print('All pages processed')

# # Exercício 14. Tentativas de Conexão
# # Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# max_attempts = 5
# attempt = 1

# while attempt <= max_attempts:
#     print(f'Attenpt {attempt} from {max_attempts}')
#     if True:
#         print('Connection successfull.')
#     attempt += 1
# else:
#     print('Failed to connect after many attempts')

# # Exercício 15. Processamento de Dados com Condição de Parada
# # Processar itens de uma lista até encontrar um valor específico que indica a parada.
# itens = [1, 2, 3, 'stop', 4, 5]

# i = 0

# while i < len(itens):
#     if itens[i] == 'stop':
#         print('Stop found, ending processing.')
#         break
#     print(f'Processing item: {itens[i]}')
#     i += 1
