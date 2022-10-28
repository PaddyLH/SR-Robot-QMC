
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
    piezo.buzz(0.3, note.C6)
    piezo.buzz(0.3, note.D6)
    piezo.buzz(0.3, note.E6)
    piezo.buzz(0.3, note.F6)
    piezo.buzz(0.3, note.G6)
    piezo.buzz(0.3, note.A7)
    piezo.buzz(0.3, note.B7)
    piezo.buzz(0.3, note.C7)

def shut_down():
    piezo.buzz(0.3, note.C7)
    piezo.buzz(0.3, note.B7)
    piezo.buzz(0.3, note.A7)
    piezo.buzz(0.3, note.G6)
    piezo.buzz(0.3, note.F6)
    piezo.buzz(0.3, note.E6)
    piezo.buzz(0.3, note.D6)
    piezo.buzz(0.3, note.C6)
