import smbus
from collections import namedtuple

def dataConversion(high, low):
	value = low + (high<<8)
	if value > 2**15:
		value -= 2**16
	return value

class ADXL345():
	def __init__(self):
		self._bus = smbus.SMBus(1)
		self._addr = 0x53
		self.measure(True)
		
	def ID(self):
		ID = self._bus.read_byte_data(self._addr, 0x00)
		return ID
		
	def getData(self):
		v = self._bus.read_i2c_block_data(self._addr, 0x32, 6)
		data = namedtuple("data", "x y z")
		data.x = dataConversion(v[1], v[0])
		data.y = dataConversion(v[3], v[2])
		data.z = dataConversion(v[5], v[4])
		return data
		
	def measure(self, state):
		POWER_CTL = self._bus.read_byte_data(self._addr, 0x2D)
		if state == True:
			POWER_CTL = POWER_CTL | 0x08
		else:
			POWER_CTL = POWER_CTL & ~0x08
		self._bus.write_byte_data(self._addr, 0x2D, POWER_CTL)
		