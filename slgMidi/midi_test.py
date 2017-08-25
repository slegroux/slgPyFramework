#!/usr/bin/env python
import unittest
import sys
import midi, mido
from mido import Message
import numpy as np
import random
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

	def test_mido_msg(self):
		timeList = np.array([32,64,128,256,512,1024])/1000.
		file = mido.MidiFile()
		track = mido.MidiTrack()
		file.tracks.append(track)
		track.append(mido.Message('program_change', program=12, time=0))
		msgs = []
		for i in range(100):
			msgs.append(mido.Message('note_on', note=random.randrange(0,127), velocity=64, time=random.choice(timeList)))

		# for msg in msgs:
		# 	# time.sleep(0.5)
		# 	self.device.output.send(msg)
		# 	time.sleep(msg.time)

			# time.sleep(random.choice(timeList))
		note = Note(C3, 1., 120)
		channel = 0
		
		on = Message('note_on', note=60, velocity=note.velocity, channel=channel, time=0.)
		self.device.output.send(on)
			# time.sleep(note.duration * 60. / self.bpm)
		off = Message('note_off', note=note.pitch, channel=channel, time=1.0)
		self.device.output.send(off)

		on = Message('note_on', note=64, velocity=note.velocity, channel=channel, time=1.0)
		self.device.output.send(on)
			# time.sleep(note.duration * 60. / self.bpm)
		off = Message('note_off', note=note.pitch, channel=channel, time=1.5)
		self.device.output.send(off)

		raw_input("\nPress enter to exit")

	def test_note(self):
		print Note(EF3, QN, 100)
		print Rest(QN)
		print Note(REST, QN)

	def test_play_note(self):
		n1 = Note(C3, 1., 120)
		r = Rest(EN)
		n2 = Note(EF3, QN, 100)
		n3 = Note(G3, EN, 127)
		n4 = Note(BF3, QN, 127)
		self.device.sync = SEQUENTIAL
		self.device.play(n1)
		self.device.play([r])
		self.device.play([n2])
		self.device.play([n3, n4])
		raw_input("\nPress enter to exit")

	def test_play_chord(self):
		# TODO check chords
		self.device.play_note([60, 63, 70], EN, 80, 0)
		# self.device.play_chord([C3, EF3, G3], 1., 100, 0)
		# self.device.play_chord([G3, BF3, D3], HN, 100, 0)

	def test_note_list(self):
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
		print nl
		self.device.sync = SEQUENTIAL
		self.device.play(nl)
		raw_input("\nPress enter to exit")

	def test_phrase(self):
		p = Phrase()
		p.instrument = ORGAN
		p.bpm = 120
		p.channel = 1
		p.add_note(Note(A4, QN))
		p.add_note(Note(B4, EN))
		print p
		notes = [60, 62]
		dur = [QN, QN]
		vel = [30, 120]
		nl = NoteList(notes, dur)
		p.add_note_list(nl)
		print p
		p.add_lists(notes, dur, vel)
		print p
		notes = [(A4, QN), (C3, EN)]
		notes_2 = [(A4, QN, 10), (C3, EN, 30)]
		p.add_tuples(notes)
		print p
		p.add_tuples(notes_2)
		print p
		print p.list

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
		p.add_note_list(nl)
		notes_2 = [(A4, QN, 90), (C3, EN, 120)]
		p.add_tuples(notes_2)
		print p
		print p.list
		self.device.play(p)
		raw_input("\nPress enter to exit")

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
		raw_input("\nPress enter to exit")

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
