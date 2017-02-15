import unittest
import audio
import time
import numpy as np


def simple_callback(in_data, frame_count, **kwargs):
	# print "size data:", len(in_data), "# frames:", frame_count
	left = in_data[:, 0]
	right = in_data[:, 1]
	data = np.column_stack((left, right))
	return data


class audioTest(unittest.TestCase):
	def setUp(self):
		self.audio = audio.Audio()

	def tearDown(self):
		self.audio.exit()
		del self.audio

	def test(self):
		self.audio.show_audio_devices()
		self.audio.choose_audio_device()
		self.audio.set_channels(2)
		self.audio.register_callback(simple_callback)
		self.audio.start()
		while self.audio.is_active():
			if raw_input("Press ENTER to exit\n") == '':
				self.audio.stop()
			time.sleep(0.1)


if __name__ == '__main__':
	unittest.main()
