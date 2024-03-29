"""
IR Control for Robosapien

Author: Matt Avallone
"""

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
from ir_codes import CODE_RSNoOp

CYCLE = 833
MAGNET_PIN = 13
SUCTION_PIN = 16

class Robosapien(object):

	def __init__(self, pin):
		self.pin = pin
		self.pi = pigpio.pi() # Connect to Pi.
		self.pi.set_mode(pin, pigpio.OUTPUT) # IR TX connected to this GPIO.
		self.pi.write(self.pin, 1)
		self.pi.wave_clear()
		
		self.wf_head = self.add_wave(8, 8)
		self.wf_hi = self.add_wave(4, 1)
		self.wf_lo = self.add_wave(1, 1)
		self.wf_tail = self.add_wave(8, 8)
		
		self.keep_alive = self.create_code(CODE_RSNoOp[0])


	def add_wave(self, hi, lo):
		self.pi.wave_add_generic([pigpio.pulse(1<<self.pin, 0, hi * CYCLE), pigpio.pulse(0, 1<<self.pin, lo * CYCLE)])
		return self.pi.wave_create()
	
	def create_code(self, code):
		data = code
		# print(data)
		wave = []
		wave.append(self.wf_head)

		for x in range(8):
			if (data & 128 != 0):
				wave.append(self.wf_hi)
				# print(1)
			else:
				wave.append(self.wf_lo)
				# print(0)
			data <<= 1

		wave.append(self.wf_tail)
		# print(wave)
		# print("end")
		return wave

	def send_wave(self, wave):
		#print wave
		self.pi.wave_chain(wave)
		while self.pi.wave_tx_busy():
			time.sleep(0.002)

		self.pi.write(self.pin, 1)
	
	def send_code(self, code):
		self.send_wave(self.create_code(code))
		time.sleep(0.5)

	def turn_on_magnet(self):
		self.pi.set_PWM_dutycycle(MAGNET_PIN, 255)

	def turn_off_magnet(self):
		self.pi.set_PWM_dutycycle(MAGNET_PIN, 0)

	def turn_on_suction(self):
		self.pi.set_PWM_dutycycle(SUCTION_PIN, 255)

	def turn_off_suction(self):
		self.pi.set_PWM_dutycycle(SUCTION_PIN, 0)

	def get_pwm_value(self, pin):
		return self.pi.get_PWM_dutycycle(pin)

	def clean_up(self):
		pi.wave_clear()
		pi.stop() # Disconnect from Pi.
	