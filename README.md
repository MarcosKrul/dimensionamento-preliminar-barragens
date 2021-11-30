# Dimensionamento preliminar para barragens de concreto

## Sobre

Engenharia de Computação, UEPG - 6º período

Projeto realizado para a disciplina de Fenômenos de Transporte

Marcos Renan Krul - [Renato Cristiano Ruppel](https://github.com/HERuppel) - [Thiago Pankievicz](https://github.com/YounGTeX)

## Restrições

* Hidrostática
* Barragens de perfil retângular
* Profundidade e altura da barragem coincidentes

## Instalação

* Clonar o projeto

```
    mkdir dimensionamento-preliminar-barragens
    cd dimensionamento-preliminar-barragens
    git clone https://github.com/MarcosKrul/dimensionamento-preliminar-barragens.git .
```

* Criacão e ativação do ambiente virtual

Windows

```
    python -m venv venv
    cmd: .\venv\Scripts\activate.bat
    PowerShell: .\venv\Scripts\activate.ps1
```

Linux

```
    python3 -m venv venv
    source venv/bin/activate
```

* Instalação das bibliotecas necessárias

```
    pip install -r requirements.txt
```

* Execução

```
    cd src
    python index.py
```

## Resultados

* Interface principal

![Interface principal](https://github.com/MarcosKrul/dimensionamento-preliminar-barragens/blob/master/tmp/images/interface-principal.png)

* Resultado interface principal

![Resultado interface principal](https://github.com/MarcosKrul/dimensionamento-preliminar-barragens/blob/master/tmp/images/resultado-interface-principal.png)

* Perfil retangular de pressões

![Quicksort e ordenação digital para 5 dígitos](https://github.com/MarcosKrul/dimensionamento-preliminar-barragens/blob/master/tmp/images/perfil-pressoes.png)

* Modelo 3D da barragem

![Quicksort e ordenação digital para 10 dígitos](https://github.com/MarcosKrul/dimensionamento-preliminar-barragens/blob/master/tmp/images/modelo-3d.png)
