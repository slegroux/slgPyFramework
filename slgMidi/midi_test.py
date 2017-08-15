#!/usr/bin/env python
import unittest
import sys
import midi, mido
from midi import Midi, Note
import time
import random
import midi_consts
# import mido
sys.path.insert(0, '..')


class audioTest(unittest.TestCase):
	def setUp(self):
		self.midi_io = midi.Midi()

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
		self.midi_io.close_devices()
		del self.midi_io

	def test(self):
		self.midi_io.show_devices()
		self.midi_io.set_input_port(0)
		self.midi_io.set_output_port(0)
		# self.midi.choose_devices()

		# Play midi messages
		notes = [60, 62, 64, 67, 69, 72]
		dur = [1., 1., 1., 1., 1., 1.]
		vel = [100, 120, 90, 80, 70, 100]

		list_notes = [midi.Note(n[0], n[1], n[2]) for n in zip(notes, dur, vel)]
		# self.midi_io.play([random.choice(list_notes)], 0)
		# self.midi_io.play([random.choice(list_notes)], 1)
		# self.midi_io.play([random.choice(list_notes)], 2)
		self.midi_io.play_chord([60, 64, 70], 120, 2, 2)
		self.midi_io.play(list_notes, 1)
		self.midi_io.play(list_notes, 0)

		try:
			while True:
				# self.midi_io.play([random.choice(list_notes)])
				# self.midi_io.play([random.choice(list_notes)], 0)
				# self.midi_io.play([random.choice(list_notes)], 1)
				# self.midi_io.play([random.choice(list_notes)], 2)
				pass
		except KeyboardInterrupt:
			pass

		# Listen to midi input
		# self.midi.register_callback(self.midi_in_callback)
		# self.midi.run_callback()

		# while True:
		# 	if raw_input("Press ENTER to exit\n") == '':
		# 		break



if __name__ == '__main__':
	unittest.main()
