#trazer a data atual
from datetime import date, time, datetime, timedelta # importando a funcao date da biblioteca datetime

# data_atual = date.today() 
# print(data_atual) # resultado: 2022-05-18

# # editar formato de retorno 
# data_atual_str = data_atual.strftime('%d/%m/%y') # %d = dia, %m = mes, %y = ano
# print(data_atual_str) 

def trabalhando_com_date():
    data_atual = date.today() 
    print(data_atual) # resultado: 2022-05-18
    # editar formato de retorno 
    data_atual_str = data_atual.strftime('%d/%m/%y') # %d = dia, %m = mes, %y = ano
    print(data_atual_str) 


def trabalhando_com_time():
    horario = time(hours=15, minute=18, second=30)
    print(horario) # resultado:  15:18:30
    


def trabalhando_com_datetime():
    data_atual = datetime.now()
    #converter para alterar formato e tirar os milisegundos
    date_time_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(date_time_str)
    #pegar valores individualmente
    print(data_atual.year)
    print(data_atual.day)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.month)
    # forma de trazer o dia traduzido
    tupla = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday])
    # criar uma data
    data_criada = datetime(2022, 6, 20, 15, 30, 20)
    print(data_criada)
    # convertendo type string para date
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(type(data_convertida)) # resultado : datetime.datetime
    #subtracao e soma de data
    #subtracao de um ano
    nova_data = data_convertida - timedelta(days=365, hours=2) # tirar menos um ano com dias, tirei duas tambem


if __name__ == "__main__":
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()