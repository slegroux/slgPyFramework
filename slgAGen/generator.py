import random
import math
import sys
sys.path.insert(0, '..')
from slgUtils import utils


class Noise(object):
	def __init__(self):
		self.name = "Noise"

	def __str__(self):
		return "noise generator"

	def tick(self):
		return(random.random() * 2 - 1)


class Sinusoid(object):
	def __init__(self, freq=440, amplitude=0.9, sr=44100):
		self.freq = freq
		self.amplitude = amplitude
		self.sr = sr
		self.phi = 0
		self.delta_phi = 2 * math.pi * self.freq / self.sr

	def __str__(self):
		return "sinusoidal generator"

	def set_freq(self, freq):
		self.freq = freq
		self.delta_phi = 2 * math.pi * self.freq / self.sr

	def set_amplitude(self, amplitude):
		self.amplitude = amplitude

	def tick(self):
		# out = math.sin(2*math.pi*self.index*self.freq/self.sr)
		# self.index += 1
		# phase formulation avoids clicks
		self.phi += self.delta_phi
		out = self.amplitude * math.sin(self.phi)
		return(out)

	def note_on(self, note, velocity):
		self.set_freq(utils.m2f(note + 12))
		self.set_amplitude(utils.m2a(velocity))

	def note_off(self):
		# self.set_amplitude(0)
		pass
