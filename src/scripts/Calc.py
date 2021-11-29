import math

class Calc: 
  def __init__(self, altura: float, comprimento: float, peso: float) -> None:
    self.__peso_especifico_concreto = 24000

    self.__altura = altura
    self.__comprimento = comprimento
    self.__peso_especifico = peso

    self.__area = self.__altura * self.__comprimento


  # Lei de Stevin
  # calcular a pressao em uma profundidade h
  def stevin_pressao(self) -> float:
    return self.__peso_especifico * self.__altura


  def stevin_pressao_prof(self, altura) -> float:
    return self.__peso_especifico * altura


  # calcular a ordenada (y) do centro de pressoes
  # numericamente igual ao centro de gravidade de um triangulo
  def cp_y(self) -> float:
    return 2*self.__altura/3 if self.__altura != 0 else 0.0

  
  # calcular a largura minima da barragem
  # depende do equilibrio entre o momento da forca do fluido e da forca peso da barragem
  def largura_minima(self, forca: float) -> float:
    return math.sqrt((2 * forca * self.cp_y()) / (self.__altura * self.__comprimento * self.__peso_especifico_concreto))


  # primeiro valor: intensidade da forca resultante
  # segundo valor: ordenada da forca (profundidade)
  # terceiro valor: largura da base da barragem
  def exec(self) -> float:
    forca_resultante = self.__peso_especifico * (self.__altura/2) * self.__area
    return forca_resultante, self.cp_y(), self.largura_minima(forca_resultante)