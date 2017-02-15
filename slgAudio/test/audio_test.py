import unittest
import sys
sys.path.insert(0, '..')
import audio
import time


def simple_callback(in_data, frame_count):
	return (in_data)


class audioTest(unittest.TestCase):
	def setUp(self):
		self.audio = audio.Audio()

	def tearDown(self):
		self.audio.exit()
		del self.audio

	def test(self):
		self.audio.show_audio_devices()
		self.audio.choose_audio_device()
		self.audio.register_callback(simple_callback)
		self.audio.start()
		while self.audio.is_active():
			if raw_input()=='':
				self.audio.stop()
			time.sleep(0.1)


if __name__ == '__main__':
	unittest.main()
