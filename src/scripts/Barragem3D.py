import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Barragem3D:
  def __init__(self, largura: float, comprimento: float, altura: float) -> None:
    self.__x = largura
    self.__y = comprimento
    self.__z = altura

    self.__vertices = np.array([
      [0,        0,        0       ],
      [0,        self.__y, 0       ],
      [self.__x, self.__y, 0       ],
      [self.__x, 0,        0       ],
      [0,        0,        self.__z],
      [0,        self.__y, self.__z],
      [self.__x, self.__y, self.__z],
      [self.__x, 0,        self.__z],
    ])

  def render(self) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.xlim(0, self.__x + 0.05 * self.__x)
    plt.ylim(0, self.__y + 0.05 * self.__y)

    plt.title('Modelo 3D da barragem')
    fig.canvas.set_window_title('Dimensionamento preliminar de barragens de concreto')
    ax.set_xlabel('Largura')
    ax.set_ylabel('Comprimento')
    ax.set_zlabel('Altura')
    
    Z = self.__vertices

    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    verts = [
      [ Z[0], Z[1], Z[2], Z[3] ],
      [ Z[4], Z[5], Z[6], Z[7] ],
      [ Z[0], Z[1], Z[5], Z[4] ],
      [ Z[2], Z[3], Z[7], Z[6] ],
      [ Z[1], Z[2], Z[6], Z[5] ],
      [ Z[4], Z[7], Z[3], Z[0] ],
    ]

    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='black', alpha=.20))
    plt.show()


# exemplo de uso
# Barragem3D(largura=10, comprimento=20, altura=30).render()