import sys
sys.path.insert(0, '..')
import unittest
import time
import generator
from slgAudio import audio


def sine_callback(in_data, frame_count):
	data = [0] * frame_count
	for i in range(frame_count):
		data[i] = 0.2 * sinus.tick()
	return data


def noise_callback(in_data, frame_count):
	data = [0] * frame_count
	for i in range(frame_count):
		data[i] = 0.05 * noise.tick()
	return data


class genTest(unittest.TestCase):
	def setUp(self):
		self.audio = audio.Audio()
		global noise, sinus
		noise = generator.Noise()
		sinus = generator.Sinusoid()

	def tearDown(self):
		self.audio.exit()
		del self.audio

	def test(self):
		self.audio.show_audio_devices()
		self.audio.set_channels(1)
		self.audio.register_callback(sine_callback)
		self.audio.register_callback(noise_callback)
		self.audio.start()
		while self.audio.is_active():
			if raw_input("Press ENTER to exit\n") == '':
				self.audio.stop()
			time.sleep(0.1)


if __name__ == '__main__':
	unittest.main()
