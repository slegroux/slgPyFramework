import pyaudio
import settings
# from IPython import embed
import numpy as np


class Audio(object):
	def __init__(self):
		self.p = pyaudio.PyAudio()
		# show_audio_devices(p)
		self.external_cb = None
		self.stream = None
		self.input_device = 0
		self.output_device = 1
		self.number_of_channels = settings.CHANNELS
		self.sampling_rate = settings.SAMPLING_RATE
		self.format = settings.FORMAT
		# self.external_cb = self.default_callback
		self.chunk = settings.CHUNK

	def register_callback(self, external_callback):
		self.external_cb = external_callback

	def set_channels(self, channels):
		self.number_of_channels = channels

	def start(self):
		self.stream = self.p.open(
			format=self.format,
			channels=self.number_of_channels,
			rate=self.sampling_rate,
			frames_per_buffer=self.chunk,
			input=True,
			output=True,
			stream_callback=self.audio_callback,
			input_device_index=self.input_device,
			output_device_index=self.output_device
		)
		self.stream.start_stream()

	def stop(self):
		self.stream.stop_stream()

	def exit(self):
		self.stream.close()
		self.p.terminate()

	def is_active(self):
		return self.stream.is_active()

	def show_audio_devices(self):
		info = self.p.get_host_api_info_by_index(0)
		numdevices = info.get('deviceCount')
		for i in range(0, numdevices):
			if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
				print "Input Device id ", i, " - ", self.p.get_device_info_by_host_api_device_index(0, i).get('name')
		print "-------"
		for i in range(0, numdevices):
			if self.p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
				print "Output Device id ", i, " - ", self.p.get_device_info_by_host_api_device_index(0, i).get('name')

	def choose_audio_device(self):
		self.input_device = int(raw_input("Please enter an input: "))
		self.output_device = int(raw_input("Please enter an output: "))

	def default_callback(in_data, frame_count):
		return (in_data)

	def audio_callback(self, in_data, frame_count, time_info, status): #, user_data=None):
		if status:
			print("Playback Error: %i" % status)

		in_data = np.fromstring(in_data, dtype=np.float32)
		in_data = np.reshape(in_data,(frame_count, self.number_of_channels))
		# data = np.array(frame_count * [0.0])
		# def external_cb(in_data, frame_count):
		#     for i in range(frame_count):
		#         data[i] = in_data[i] * self.gain
		#     return data

		data = np.array(self.external_cb(in_data, frame_count))
		# interleaved means L0, R0, L1, R1...
		data = data.flatten()
		data = data.astype(np.float32).tostring()
		return (data, pyaudio.paContinue)
