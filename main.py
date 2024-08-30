#!/usr/bin/python3
import gpiod

# Configuração do GPIO
chip = gpiod.Chip('gpiochip4')  # Usando o gpiochip4 conforme sua configuração
line = chip.get_line(21)  # Usando o GPIO 21 para o sensor de chama
relay_line = chip.get_line(20)  # Usando o GPIO 20 para controlar o relé

# Configurando o GPIO como entrada e solicitando eventos
line.request(consumer='flame_sensor', type=gpiod.LINE_REQ_EV_BOTH_EDGES)
relay_line.request(consumer='water_pump', type=gpiod.LINE_REQ_DIR_OUT)

def handle_event():
    while True:   
        # Aguarda por um evento
        if line.event_wait(sec=10):
            value = line.get_value()
            print(f"pinagem: {value}")
            
            if value == 0:
                print("Um incêndio foi detectado!")
                relay_line.set_value(1)  # Liga a bomba
            elif value == 1:
                print("Nenhum incêndio foi detectado!")
                relay_line.set_value(0)  # Desliga a bomba
        else:
            print("Aguardando verificação!")

# Loop infinito
try:
    handle_event()
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")
finally:
    line.release()
    relay_line.set_value(0)  # Garante que a bomba esteja desligada
    relay_line.release()
