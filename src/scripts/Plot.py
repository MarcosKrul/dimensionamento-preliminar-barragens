import matplotlib.pyplot as pyplot

class Plot:
  def __init__(self) -> None:
    pass


  def render(self, y_altura: float, x_pressao: float, x_fr: float, y_fr: float) -> None:
    fig, plt = pyplot.subplots()

    # plt.text(0,0,'teste') ADICIONAR O VETOR FORCA

    fig.canvas.set_window_title('Dimensionamento preliminar de barragens de concreto')
    plt.set_title('Perfil de pressões na relação Profundidade X Pressão')
    plt.grid(True)
    plt.set_ylabel('Profundidade (m)')
    plt.set_xlabel('Pressão (Pa)')
    plt.invert_yaxis()

    legenda_pressao, = plt.plot(
      [0, x_pressao], 
      [0, y_altura],
      marker='o',
      markersize=4,
      color='red',
      linestyle='--',
      label='Pressão'
    )
    
    legenda_altura, = plt.plot(
      [0, 0], 
      [0, y_altura],
      color='blue',
      label='Profundidade'
    )

    legenda_fr, = plt.plot(
      [0, x_fr],
      [y_fr, y_fr],
      color='black',
      label='Força resultante',
      linewidth=2
    )

    # plt.quiver(x_fr, y_fr, -x_fr, 0, color='black', units='xy', scale=1, width=0.1)

    plt.legend(handles=[legenda_altura, legenda_pressao, legenda_fr])
    pyplot.show()


Plot().render(y_altura=10, x_pressao=20, x_fr=12.5, y_fr=6.27)