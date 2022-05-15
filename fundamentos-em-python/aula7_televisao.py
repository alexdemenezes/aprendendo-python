class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    
    def power(self):
      if self.ligada:
          self.ligada = False
      else:
          self.ligada = True

    def aumenta_canal(self):
      if self.ligada:
          self.canal += 1

    def diminui_canal(self):
      if self.ligada:
          self.canal -= 1


televisao = Televisao() # instancia da classe
print(televisao.ligada) 
televisao.power()
print(televisao.ligada)