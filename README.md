# Projeto de Combate ao Incêndio
## Instalação da biblioteca gpiod pelo shell do Linux
```
sudo apt-get install -y gpiod
```
## Instalação da biblioteca gpiod pelo gerenciador de pacotes do python
```
pip install gpiod
```
## Verificação da instalação da biblioteca gpiod
```
gpiodetect
```
## Verificação da porta ligada ao pino 21 (flame sensor)
```
gpioinfo
```
## Executar programa no terminal
```
sudo python3 main.py
```
<br>

> [!CAUTION]
> O interpretador do python deve estar no diretório /usr/bin/python3
