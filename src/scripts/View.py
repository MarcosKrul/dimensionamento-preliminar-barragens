from PySimpleGUI import PySimpleGUI as sg
from scripts.Calc import Calc
from scripts.Plot import Plot
from scripts.Barragem3D import Barragem3D

class View:
    def __init__(self) -> None:
      self.__fr = 0.0
      self.__fr_y = 0.0
      self.__largura_barragem = 0.0

      self.__title_btn_calc = 'Calcular'
      self.__title_btn_plot = 'Visualizar graficamente'
      self.__title_btn_view_base = 'Visualizar base'

      self.__key_in_altura = 'in_altura_barragem'
      self.__key_in_comprimento = 'in_comprimento_barragem'
      self.__key_in_peso_especifico = 'in_peso_especifico'

      self.__key_out_fr = 'out_fr'
      self.__key_out_fr_y = 'out_fr_y'
      self.__key_out_largura_base = 'out_largura_base'

      sg.theme('Reddit')

      layout = [
        [sg.Text('Informe os valores de entrada:\n')],
        [
          sg.Text('Altura da barragem (h): '),
          sg.Input(key=self.__key_in_altura, pad=((48, 5), (0, 0)))
        ],
        [
          sg.Text('Comprimento da barragem (L): '),
          sg.Input(key=self.__key_in_comprimento)
        ],
        [
          sg.Text('Peso específico do fluído (γ): '),
          sg.Input(key=self.__key_in_peso_especifico, pad=((14, 5), (0, 0)))
        ],
        [sg.Text('', key=self.__key_out_fr, font='Arial 12 bold', pad=((0, 0), (20, 0)))],
        [sg.Text('', key=self.__key_out_fr_y, font='Arial 12 bold', pad=((0, 0), (5, 0)))],
        [sg.Text('', key=self.__key_out_largura_base, font='Arial 12 bold', pad=((0, 0), (5, 0)))],
        [sg.Button(self.__title_btn_calc, size=(80, 1), pad=((80, 80), (25, 0)))],
        [sg.Button(self.__title_btn_plot, size=(80, 1), pad=((80, 80), (15, 0)))],
        [sg.Button(self.__title_btn_view_base, size=(80, 1), pad=((80, 80), (15, 0)))],
      ]
      
      self.__window = sg.Window('Dimensionamento de barragens', layout, size=(400, 380))


    def update(self, showPlot: bool = False):
      calc = Calc(
        altura=self.__value_altura, 
        comprimento=self.__value_comprimento, 
        peso=self.__value_peso_especifico
      )

      self.__fr, self.__fr_y, self.__largura_barragem = calc.exec()

      self.__window[self.__key_out_fr].update(f'Intensidade da força: {self.__fr:.2f} N')
      self.__window[self.__key_out_fr_y].update(f'Ordenada (γ) da força resultante: {self.__fr_y:.2f} m')
      self.__window[self.__key_out_largura_base].update(f'Largura da base da barragem: {self.__largura_barragem:.4f} m')

      if showPlot:
        Plot().render(
          y_altura=self.__value_altura, 
          x_pressao=calc.stevin_pressao(), 
          x_fr=calc.stevin_pressao_prof(self.__fr_y), 
          y_fr=self.__fr_y,
          base=self.__largura_barragem
        )


    def run(self):
      while True:
        events, values = self.__window.read()

        if events == sg.WINDOW_CLOSED: 
          break

        if events == self.__title_btn_calc or events == self.__title_btn_plot or events == self.__title_btn_view_base:
          try:
            self.__value_altura = float(values[self.__key_in_altura])
            self.__value_comprimento = float(values[self.__key_in_comprimento])
            self.__value_peso_especifico = float(values[self.__key_in_peso_especifico])

            self.update(events == self.__title_btn_plot)

            if events == self.__title_btn_view_base:
              Barragem3D(largura=self.__largura_barragem, comprimento=self.__value_comprimento, altura=self.__value_altura).render()

          except ValueError:
            sg.popup_error('Apenas valores numéricos são aceitos.')
            continue