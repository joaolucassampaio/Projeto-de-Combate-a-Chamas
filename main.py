#!/usr/bin/python3
import gpiod
import time

# Configuração do GPIO
chip = gpiod.Chip('gpiochip4')  # Usando o gpiochip4 conforme sua configuração
line = chip.get_line(21)  # Usando o GPIO 21

# Configurando o GPIO como entrada e solicitando eventos
line.request(consumer='flame_sensor', type=gpiod.LINE_REQ_EV_BOTH_EDGES)

def handle_event(event):
    # Imprime a informação do evento diretamente
    print(f"Incêndio detectado!")

# Loop infinito
try:
    while True:
        # Aguarda por um evento
        if line.event_wait(sec=1):
            # Lê um único evento
            event = line.event_read()
            handle_event(event)
        else:
            print("Nenhum incêndio foi detectado!")
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário!")
finally:
    line.release()
