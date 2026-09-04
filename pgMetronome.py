import math
import struct
import subprocess
import time
import wave
import pygame as pg
import pygame_widgets
import sys
from pygame_widgets import slider
from pygame_widgets.button import Button


BEEP_FILE = "/tmp/metronome_beep.wav"

def create_beep(filename, frequency=880, duration=0.08, volume=0.5):
    sample_rate = 44100
    sample_count = int(sample_rate * duration)

    with wave.open(filename, "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        for i in range(sample_count):
            sample = math.sin(2 * math.pi * frequency * i / sample_rate)
            value = int(sample * volume * 32767)
            wav.writeframes(struct.pack("<h", value))

def play_beep():
    subprocess.run(["aplay", "-q", BEEP_FILE])

def run_metronome(bpm):
    interval = 60.0 / bpm
    next_beat = time.monotonic()

    while True:
        play_beep()

        next_beat += interval
        delay = next_beat - time.monotonic()

        if delay > 0:
            time.sleep(delay)

        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_r:
                    return
create_beep(
    BEEP_FILE,
    frequency = 700,
    duration = 0.04,
    volume = 0.3
    )


pg.init()

size=width,height=400,400
screen=pg.display.set_mode(size)
pg.display.set_caption("METRONOME")

font=pg.font.Font(None,20)
bpmFont=pg.font.Font(None,140)

head_rect=pg.Rect(180,30,40,20)
headTxt=font.render("BPM",True,"black")
headRect=headTxt.get_rect(center=head_rect.center)

buttons = []

button_width = 20
button_height = 20
gap = 5

total_width = (button_width * 4) + (gap * 3)

start_x = (400 - total_width) // 2
y = (400 - button_height)//2

for i in range(4):
    x = start_x + i * (button_width + gap)

    button = Button(
        screen,
        x,
        y,
        button_width,
        button_height,
        text='',
        radius=10,
        onClick=lambda i=i: print(f"Button {i + 1} clicked")
    )

    buttons.append(button)

def run():
    bpmInt='0'
    running=True
    while running:
        screen.fill("lightgray")
        events=pg.event.get()
        for event in events:
            if event.type==pg.QUIT:
                    running=False
                    pg.quit()
                    sys.exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_q:
                    running=False
                    pg.quit()
                    sys.exit()
                if event.key==pg.K_BACKSPACE:
                    bpmInt=bpmInt[:-1]
                if event.unicode.isnumeric() and int(bpmInt)<30 and len(bpmInt)<4:
                    bpmInt+=event.unicode
                if event.key == pg.K_RETURN:
                    run_metronome(float(bpmInt))
                if event.key == pg.K_r:
                    run()


        bpmm=bpmInt[1:]
        bpmTxt=bpmFont.render(bpmm,True,"black")
        bpmRect=bpmTxt.get_rect(center=(width//2,105))

        pg.draw.rect(screen,"darkgray",head_rect)
        screen.blit(headTxt,headRect)
        screen.blit(bpmTxt,bpmRect)

        pygame_widgets.update(events)
        pg.display.flip()

run()
