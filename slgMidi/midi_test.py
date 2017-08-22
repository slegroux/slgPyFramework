#!/usr/bin/env python
import unittest
import sys
import midi, mido
from midi import Midi, Note, Rest, NoteList, Phrase, Instrument
import time
import random
# check double import with midi.py
from midi_consts import *
import sys
# import mido
sys.path.insert(0, '..')


class Test(unittest.TestCase):
	def setUp(self):
		self.device = midi.Midi()

	def midi_in_callback(self):
		for msg in self.midi_io.input:
			if msg.type == 'note_on':
				if msg.velocity == 0:
					# note_state[msg.note] = 'off'
					print "note off", msg.note, msg.velocity
				else:
					# note_state[msg.note] = 'on'
					print "note_on", msg.note, msg.velocity
			elif msg.type == 'note_off':
				# note_state[msg.note] = 'off'
				print "note_off", msg.note, msg.velocity
			else:
				print "print other"
			# print note_state

	def tearDown(self):
		self.device.close_devices()
		del self.device

	def test_io(self):
		self.device.show_devices()
		self.device.set_input_port(0)
		self.device.set_output_port(0)
		# self.midi.choose_devices()

	def test_print_note(self):
		print Note(EF3, QN, 100)
		print Rest(QN)
		print Note(REST, QN)

	def test_play_note(self):
		n1 = Note(C3, 1., 120)
		r = Rest(EN)
		n2 = Note(EF3, QN, 100)
		n3 = Note(G3, EN, 127)
		n4 = Note(BF3, QN, 127)

		self.device.play(n1)
		self.device.play([r])
		self.device.play([n2])
		self.device.play([n3, n4])

	def test_play_chord(self):
		self.device.play_chord([60, 63, 70], EN, 80, 0)
		self.device.play_chord([C3, EF3, G3], 1., 100, 0)
		self.device.play_chord([G3, BF3, D3], HN, 100, 0)

	def test_print_note_list(self):
		notes = [60, 62, 64, 67, 69, 72]
		dur = [1., 0.25, 1., 0.5, 1., 1.]
		dyn = [100, 120, 90, 80, 70, 100]
		nl = NoteList(notes, dur, dyn)
		print nl
		notes = [60, 62]
		dur = [QN, QN]
		nl = NoteList(notes, dur)
		print nl


	def test_play_note_list(self):
		notes = [60, 62, 64, 67, 69, 72]
		dur = [1., 0.25, 1., 0.5, 1., 1.]
		dyn = [100, 120, 90, 80, 70, 100]
		nl = NoteList(notes, dur, dyn)
		seq = nl.get()
		self.device.play(seq)

		# notes = [60, 62]
		# dur = [QN, QN]
		# nl = NoteList(notes, dur)
		# self.device.play(nl.list)

	def test_phrase(self):
		p = Phrase()
		p.instrument = ORGAN
		p.bpm = 120
		p.channel = 1
		p.add_note(Note(A4, QN))
		p.add_note(Note(B4, EN))
		notes = [60, 62]
		dur = [QN, QN]
		nl = NoteList(notes, dur)
		p.add_note_list(nl)
		print p

	def test_play_phrase(self):
		p = Phrase(name='My phrase')
		p.instrument = PIANO
		p.bpm = 70
		p.channel = 0
		p.add_note(Note(A4, QN))
		p.add_note(Note(B4, QN))
		p.add_note(Note(C4, QN))
		notes = [67, 62]
		dur = [QN, QN]
		nl = NoteList(notes, dur)
		# print nl.list
		p.add_note_list(nl)
		# p.add_note_list(toto)
		# print p.list
		self.device.play(p)


	def test_instrument(self):
		harp = Instrument(HARP, 0, 0)
		self.device.instrument(PIANO, 0)
		self.device.instrument(VIBRAPHONE, 1)
		self.device.play(Note(A4, QN), 1)
		self.device.play(Note(A4, QN), 0)

	def test_pan(self):
		self.device.panning(0, 1)
		self.device.play(Note(A4, QN), 1)
		self.device.panning(127, 1)
		self.device.play(Note(A4, QN), 1)

	def test_modulation(self):
		self.device.instrument(ORGAN,2)
		self.device.modulation(0, 2)
		self.device.play(Note(A4, QN), 2)
		self.device.modulation(127, 2)
		self.device.play(Note(A4, QN), 2)

	def test_fur_elise(self):
		pitches1 = [E5, DS5, E5, DS5, E5, B4, D5, C5, A4, REST, C4, E4, A4, B4, REST, E4]
		durations1 = [SN, SN, SN, SN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN]
		pitches2 = [GS4, B4, C5, REST, E4]
		durations2 = [SN, SN, EN, SN, SN]
		pitches3 = [C5, B4, A4]
		durations3 = [SN, SN, EN]
		seq1 = NoteList(pitches1, durations1)
		seq2 = NoteList(pitches2, durations2)
		seq3 = NoteList(pitches3, durations3)
		# seq.get() gives a list of Notes objects
		self.device.play(seq1.get() + seq2.get() + seq1.get() + seq3.get())

	def test_scales(self):
		scale = PENTATONIC_SCALE
		root = C4
		notes = [root + note for note in scale]
		for note in notes:
			self.device.play(Note(note, EN))

	def test_play_midi(self):
		# Play midi messages
		notes = [60, 62, 64, 67, 69, 72]
		dur = [1., 0.25, 1., 0.5, 1., 1.]
		vel = [100, 120, 90, 80, 70, 100]

		list_notes = [midi.Note(n[0], n[1], n[2]) for n in zip(notes, dur, vel)]
		self.device.play([list_notes[0], list_notes[1]], 1)

		# self.midi_io.play(list_notes, 0)

		# try:
		# 	while True:
		# 		# self.midi_io.play([random.choice(list_notes)])
		# 		# self.midi_io.play([random.choice(list_notes)], 0)
		# 		# self.midi_io.play([random.choice(list_notes)], 1)
		# 		# self.midi_io.play([random.choice(list_notes)], 2)
		# 		pass
		# except KeyboardInterrupt:
		# 	pass

		# Listen to midi input
		# self.midi.register_callback(self.midi_in_callback)
		# self.midi.run_callback()

		# while True:
		# 	if raw_input("Press ENTER to exit\n") == '':
		# 		break



if __name__ == '__main__':
	unittest.main()
