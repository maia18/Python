'''
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
'''
from datetime import datetime

data_str_data = '2025/03/30 17:29:32'
data_str_data = '30/03/2025'
data_str_fmt  = '%d/%m/%Y'

data = datetime(2025, 3, 30, 17, 29, 32)              # datetime(ano, mês, dia, horas, minutos, segundos)
print(data)
data = datetime.strptime(data_str_data, data_str_fmt) # datetime.strptime('DATA', 'FORMATO')
print(data)