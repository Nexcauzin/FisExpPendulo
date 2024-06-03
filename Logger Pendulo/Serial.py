import csv, os, serial

class Sensor:
    def __init__(self, nome, porta, baud, colunas):
        self.nome = nome
        self.porta = porta
        self.baud = baud
        self.colunas = colunas
        
    diretorio = "Logs"

    @classmethod
    def verifica_diretorio(cls):
        num = 1
        diretorio_atual = [cls.diretorio,num]
        while os.path.exists(f"{diretorio_atual[0]}{diretorio_atual[1]}"):
            num+=1
            diretorio_atual[1] = num
            
        nome_definitivo = str(f"{diretorio_atual[0]}{diretorio_atual[1]}")
        os.makedirs(nome_definitivo)
        return nome_definitivo

    def leituras(self, diretorio):
        with serial.Serial(self.porta, self.baud) as ser:
            with open(f'{diretorio}/{self.nome}.csv', mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.colunas)
                writer.writeheader()

                while True:
                    leitura = ser.readline().strip()
                    dados = leitura.split(b',')
                    dados_float = list(map(float, dados))

                    row_data = dict(zip(self.colunas, dados_float))
                    print(row_data)
                    writer.writerow(row_data)
                    csv_file.flush()
