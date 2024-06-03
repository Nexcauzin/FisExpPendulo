from Serial import Sensor

Sensor.diretorio = "Logs/Rep"
diretorio = Sensor.verifica_diretorio()

# Aqui que define os sensores vindos da Serial
Estacao = Sensor('Pendulo', 'COM10', 9600, ['cm'])

Estacao.leituras(diretorio)