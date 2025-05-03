""" pip - instalando e desinstalando pacotes e bibliotecas """
# Instalar última versão: pip install nome_pacote
# Instalar versão precisa (tem outras formas também não mencionadas):
# pip install nome_pacote==0.0.0
# Desinstalar pacote: pip uninstall nome_pacote
# Congelar (ver pacotes): pip freeze

''' Criando e usando um requirements.txt '''
# pip freeze > requirements.txt

''' Instalando tudo do requirements.txt '''
# pip install -r requirements.txt