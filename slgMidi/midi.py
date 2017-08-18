#!/usr/bin/env python
from IPython import embed
import mido
from mido import Message
import time
from threading import Thread
from midi_consts import *

note_state = {}
# TO DO global BPM variable
BPM = 60


class Note(object):
	"""A note event.

	Parameters
	----------
	pitch : int
		Note pitch, as a MIDI note number C4 format
	duration : float
		Note duration float or QN format
	velocity : int
		Note midi velocity.

	"""

	def __init__(self, pitch, duration, velocity=85):
		if pitch == REST:
			self.pitch = -1
			self.duration = duration
			self.velocity = 0
		else:
			self.pitch = pitch
			self.duration = duration
			self.velocity = velocity

	def __repr__(self):
		return 'Note(pitch={}, duration={}, velocity={})'.format(
			self.pitch, self.duration, self.velocity)


class Rest(Note):
	# here rest is defined as a 0 velocity C3
	def __init__(self, dur):
		Note.__init__(self, -1, dur, 0)


class NoteList(object):
	def __init__(self, notes, dur, dyn=85):
		self.notes = notes
		self.dur = dur

		if type(dyn) is int:
			self.dyn = [dyn] * len(notes)
		else:
			self.dyn = dyn

		self.note_list = [Note(n[0], n[1], n[2]) for n in zip(self.notes, self.dur, self.dyn)]

	def __repr__(self):
		s = ''
		for note in self.note_list:
			s += str(note) + '\n'
		return s

	def get(self):
		return self.note_list


class Phrase(object):
	def __init__(self, note_list=[], instrument=PIANO, bpm=60, start=0):
		self.start = start
		self.data = note_list
		self.bpm = bpm
		self.beat_duration = 60. / bpm
		self.instrument = instrument


class Midi(object):
	def __init__(self):
		mido.set_backend('mido.backends.rtmidi')
		self.input = mido.open_input()
		self.output = mido.open_output()
		self.midi_cb = None

	def show_devices(self):
		print "MIDI IN: ", mido.get_input_names()
		print "MIDI OUT: ", mido.get_output_names()

	def set_input_port(self, port):
		try:
			port_name = mido.get_input_names()[port]
			self.input = mido.open_input(port_name)
			print "Input Port:", port_name
		except Exception as e:
			print "Exception: ", str(e)

	def set_output_port(self, port):
		try:
			port_name = mido.get_output_names()[port]
			self.output = mido.open_output(port_name, autoreset=True)
			print "Output Port:", port_name
		except Exception as e:
			print "Exception: ", str(e)

	def choose_devices(self):
		i = mido.get_input_names()[int(raw_input("Enter input index: "))]
		try:
			self.input = mido.open_input(str(i))
			print str(i)
		except IOError:
			print "I/O error. {0} already opened".format(i)

		o = mido.get_output_names()[int(raw_input("Enter output index: "))]
		try:
			self.ouput = mido.open_output(str(o))
			print o
		except IOError:
			print "I/O error. {0} already opened".format(o)

	def close_devices(self):
		self.input.close()
		self.output.close()

	def register_callback(self, callback):
		self.midi_cb = callback

	def run_callback(self):
		self.midi_cb()

	def instrument(self, instrument=PIANO, channel=0):
		message = Message('program_change', channel=channel, program=instrument)
		self.output.send(message)

	def panning(self, panning=64, channel=0):
		message = Message('control_change', channel=channel, control=10, value=panning)
		self.output.send(message)

	def modulation(self, value, channel=0):
		message = Message('control_change', channel=channel, control=1, value=value)

	def play_(self, notes, channel=0):
		# exepect list of notes. input [note] if just 1 note
		if not isinstance(notes, list):
			notes = [notes]

		for note in notes:
			on = Message('note_on', note=note.pitch, velocity=note.velocity, channel=channel)
			# pan_message = Message('note_on', note=note.p, velocity=note.dyn, channel=channel)
			self.output.send(on)
			time.sleep(note.duration)
			off = Message('note_off', note=note.pitch, channel=channel)
			self.output.send(off)

	def play(self, notes, channel=0):
		# TODO: give arguments to threaded function
		new_thread = Thread(target=self.play_, args=[notes, channel])
		new_thread.start()
		new_thread.join()

	def play_chord_(self, pitches, duration, velocity, channel=0):
		for note in pitches:
			on = Message('note_on', note=note, velocity=velocity, channel=channel)
			self.output.send(on)
		time.sleep(duration)
		for note in pitches:
			off = Message('note_off', note=note, channel=channel)
			self.output.send(off)

	def play_chord(self, pitches, velocity, duration, channel=0):
		new_thread = Thread(target=self.play_chord_, args=[pitches, velocity, duration, channel])
		new_thread.start()
		new_thread.join()
