from PySimpleGUI import PySimpleGUI as sg

class View:
    def __init__(self) -> None:
      self.__title_btn_calc = 'Calcular'
      self.__title_btn_plot = 'Visualizar graficamente'

      self.__key_in_altura = 'in_altura_barragem'
      self.__key_in_largura = 'in_largura_barragem'
      self.__key_in_peso_especifico = 'in_peso_especifico'

      sg.theme('Reddit')

      layout = [
        [sg.Text('Informe os valores de entrada.\n')],
        [
          sg.Text('Altura da barragem (h): '),
          sg.Input(key=self.__key_in_altura, pad=((39, 5), (0, 0)))
        ],
        [
          sg.Text('Largura da barragem (L): '),
          sg.Input(key=self.__key_in_largura, pad=((30, 5), (0, 0)))
        ],
        [
          sg.Text('Peso específico do fluído (γ): '),
          sg.Input(key=self.__key_in_peso_especifico)
        ],
        [sg.Button(self.__title_btn_calc, size=(80, 1), pad=((80, 80), (50, 0)))],
        [sg.Button(self.__title_btn_plot, size=(80, 1), pad=((80, 80), (15, 0)))],
      ]
      
      self.__window = sg.Window('Dimensionamento de barragens', layout, size=(400, 280))

    def run(self):
      while True:
        events, values = self.__window.read()

        if events == sg.WINDOW_CLOSED: 
          break

        if events == self.__title_btn_calc or events == self.__title_btn_plot:
          try:
            self.__value_altura = float(values[self.__key_in_altura])
            self.__value_largura = float(values[self.__key_in_largura])
            self.__value_peso_especifico = float(values[self.__key_in_peso_especifico])
          except ValueError:
            sg.popup_error('Apenas valores numéricos são aceitos.')
            continue