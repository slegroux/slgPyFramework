from midi import Midi, Note, Rest, NoteList, Phrase, Instrument
from midi_consts import *

# beverly hills cop
pitches1 = [
	F4, REST, AF4, REST, F4, F4, BF4, F4, EF4, F4, REST, C5, REST
]

durations1 = [
	QN, QN, QN, EN, QN, EN, QN, QN, QN, QN, QN, QN, EN
]

pitches2 = [
	F4, F4, DF5, C5, AF4, F4, C5, F5, F4, EF4, EF4, C4, G4, F4
]

durations2 = [
	QN, EN, QN, QN, QN, QN, QN, QN, EN, QN, EN, QN, QN, DQN
]

theme = Phrase()
theme.add_lists(pitches1, durations1)
theme.add_lists(pitches2, durations2)
theme.instrument = SYNTH_BASS1
theme.bpm = 220

device = Midi()
device.play(theme)