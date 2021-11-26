from matplotlib import patches
import matplotlib.pyplot as pyplot

class Plot:
  def __init__(self) -> None:
    pass


  def render(self, y_altura: float, x_pressao: float, x_fr: float, y_fr: float, base: float) -> None:
    fig, plt = pyplot.subplots()

    fig.canvas.set_window_title('Dimensionamento preliminar de barragens de concreto')
    plt.set_title('Perfil de pressões na relação Profundidade X Pressão')
    plt.grid(False)
    plt.set_ylabel('Profundidade (m)')
    plt.set_xlabel('Pressão (Pa)')
    plt.invert_yaxis()

    # reta perfil de pressoes
    legenda_pressao, = plt.plot(
      [0, x_pressao], 
      [0, y_altura],
      marker='o',
      markersize=4,
      color='blue',
      label='Pressão'
    )
    
    # reta profundidade/altura da barragem
    legenda_altura, = plt.plot(
      [0, 0], 
      [0, y_altura],
      marker='o',
      markersize=4,
      color='green',
      label='Profundidade'
    )

    # altura e base da barragem
    barragem = patches.Rectangle(
      (-base, 0),
      base,
      y_altura,
      linewidth=1,
      color='gray'
    )

    pyplot.gca().add_patch(barragem)

    # dimensao da base (base)
    legenda_base, = plt.plot(
      [-base, 0],
      [0, 0],
      color='red',
      linewidth=1,
      label='Base',
      marker='|',
      markersize=4,
    )

    # vetor forca resultante
    legenda_forca_resultante, = plt.plot(
      [0, x_fr],
      [y_fr, y_fr],
      color='black',
      linewidth=1,
      label='Vetor Força Resultante',
      marker='<',
      markersize=4,
      markevery=[0]
    )

    plt.legend(handles=[legenda_altura, legenda_pressao, legenda_forca_resultante, legenda_base])
    pyplot.show()


# exemplo de uso
# Plot().render(y_altura=10, x_pressao=20, x_fr=12.5, y_fr=6.27, base=4)