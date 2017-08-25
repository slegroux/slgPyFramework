from midi import Midi, Note, Rest, NoteList, Phrase, Instrument
from midi_consts import *
import time

# beverly hills cop
ostinato1_pitch = [
	D6, G5, REST, B5, FS5, B4, REST, E5, A5, FS5, REST
]

ostinato1_rhythm = [
	EN, EN, EN, QN, EN, EN, EN, EN, EN, EN, EN
]

bass1_p = [
	A2, REST, A3, REST, A2, A3, REST, C3, REST, REST, C4,
	C3, REST, C4, REST, E2, E3, REST, E2, REST, E3, REST
]

bass1_r = [
	EN, EN, EN, EN, EN, EN, QN, EN, EN, EN, EN,
	EN, EN, EN, EN, EN, EN, QN, EN, EN, EN, EN
]

bass2_t = [
	(A2, EN), (REST, QN), (A3, EN), (A2, EN), (REST, EN), (A3, EN), (REST, EN), (C3, EN), (C4, EN), (REST, QN),
	(C3, EN), (REST, EN), (REST, EN), (C4, EN), (E2, EN), (REST, EN), (E3, EN), (REST, EN), (E2, EN), (E3, EN), (REST, QN)
]

chord1_t = [
	([G4, C5, E5], QN ), ([F4, B4, D5], QN), ([E4, B4], QN)
]

theme = Phrase()
theme.add_lists(ostinato1_pitch, ostinato1_rhythm, loop=1)
# theme.add_lists(pitches2, durations2)
theme.instrument = XYLOPHONE
theme.channel = 0
theme.bpm = 192

bass = Phrase()
bass.instrument = BASS
bass.channel = 1
bass.bpm = 192
bass.add_lists(bass1_p, bass1_r, loop=1)

bass2 = Phrase()
bass2.instrument = BASS
bass2.channel = 2
bass2.bpm = 192
bass2.add_tuples(bass2_t, loop=1)

rest = Phrase()
r = Rest(EN)
for i in range(12):
	rest.add_note(r)

device = Midi()
# device.sync = PARALLEL
device.play(theme)
# device.play(rest)
device.play(theme)
# device.play(bass)
# time.sleep(EN*12)
# device.play(theme)
# device.play(bass)
# device.play(bass2)
raw_input("\nPress enter to exit")