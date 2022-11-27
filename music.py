
from random import *
import constants

piezo = constants.power_board.piezo
note = constants.Note

def tune1():
    piezo.buzz(0.25, note.D6)
    piezo.buzz(0.25, note.D7)
    piezo.buzz(0.25, note.D6)
    piezo.buzz(0.25, note.D7)
    piezo.buzz(0.25, note.D6)
    piezo.buzz(0.25, note.D7)
    piezo.buzz(0.25, note.D6)
    piezo.buzz(0.25, note.D7)

def wake_up():
    piezo.buzz(0.25, note.G6, blocking = True)
    piezo.buzz(0.25, note.E6, blocking = True)
    piezo.buzz(0.25, note.C6, blocking = True)
    piezo.buzz(0.25, note.A6, blocking = True)

def rand_note(dur):
    n = randint(1,10)
    if (n == 1): piezo.buzz(dur, note.A6, blocking = True)
    if (n == 2): piezo.buzz(dur, note.B6, blocking = True)
    if (n == 3): piezo.buzz(dur, note.C6, blocking = True)
    if (n == 4): piezo.buzz(dur, note.D6, blocking = True)
    if (n == 5): piezo.buzz(dur, note.E6, blocking = True)
    if (n == 6): piezo.buzz(dur, note.F6, blocking = True)
    if (n == 7): piezo.buzz(dur, note.G6, blocking = True)
    if (n == 8): piezo.buzz(dur, note.A7, blocking = True)
    if (n == 9): piezo.buzz(dur, note.B7, blocking = True)
    if (n == 10): piezo.buzz(dur, note.C7, blocking = True)

def shut_down():
    piezo.buzz(0.3, note.C7)
    piezo.buzz(0.3, note.B7)
    piezo.buzz(0.3, note.A7)
    piezo.buzz(0.3, note.G6)
    piezo.buzz(0.3, note.F6)
    piezo.buzz(0.3, note.E6)
    piezo.buzz(0.3, note.D6)
    piezo.buzz(0.3, note.C6)

def tune():
    for i in range(16):
        rand_note(0.15)
