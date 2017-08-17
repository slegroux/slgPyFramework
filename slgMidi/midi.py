#!/usr/bin/env python
from IPython import embed
import mido
from mido import Message
import time
from threading import Thread
from midi_consts import *

note_state = {}

def bpm(self, b):
	self.beat = 60000 / b


class Note(object):
	def __init__(self, p, dur, dyn=85):
		if p == REST:
			self.p = 0
			self.dur = dur
			self.dyn = 0
		else:
			self.p = p
			self.dur = dur
			self.dyn = dyn

	def print_note(self):
		print (self.p, self.dur, self.dyn)


class Rest(Note):
	# here rest is defined as a 0 velocity C3
	def __init__(self, dur):
		Note.__init__(self, 60, dur, 0, 0)


class NoteList(object):
	def __init__(self, notes, dur, dyn=85):
		self.notes=  notes
		self.dur = dur

		if type(dyn) is int:
			self.dyn = [dyn] * len(notes)
		else:
			self.dyn = dyn

	def get(self):
		return [Note(n[0], n[1], n[2]) for n in zip(self.notes, self.dur, self.dyn)]


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

	def play_(self, notes, channel=0):
		# exepect list of notes. input [note] if just 1 note
		if not isinstance(notes, list):
			notes = [notes]

		for note in notes:
			on = Message('note_on', note=note.p, velocity=note.dyn, channel=channel)
			# pan_message = Message('note_on', note=note.p, velocity=note.dyn, channel=channel)
			self.output.send(on)
			time.sleep(note.dur)
			off = Message('note_off', note=note.p, channel=channel)
			self.output.send(off)

	def play(self, notes, channel=0):
		# TODO: give arguments to threaded function
		new_thread = Thread(target=self.play_, args=[notes, channel])
		new_thread.start()
		new_thread.join()

	def play_chord_(self, pitches, dur, velocity, channel=0):
		for note in pitches:
			on = Message('note_on', note=note, velocity=velocity, channel=channel)
			self.output.send(on)
		time.sleep(dur)
		for note in pitches:
			off = Message('note_off', note=note, channel=channel)
			self.output.send(off)

	def play_chord(self, pitches, velocity, dur, channel=0):
		new_thread = Thread(target=self.play_chord_, args=[pitches, velocity, dur, channel])
		new_thread.start()
		new_thread.join()
