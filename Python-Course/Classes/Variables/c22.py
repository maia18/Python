""" CONSTANTE """
# "Variáveis" que não mudam
# Muitas condições no mesmo if (ruim)
#     <- Contagem de complexidade (ruim)

velocidade = 50  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_ultrapassada = velocidade > RADAR_1
ultrapassagem_ = (local_carro >= (LOCAL_1 - RADAR_RANGE)) and (local_carro <= (LOCAL_1 + RADAR_RANGE))
multa = ultrapassagem_ and velocidade_ultrapassada

if velocidade_ultrapassada:
    print("Velocidade acima do permitido") 
if multa:
    print("Carro multado") 