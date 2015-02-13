import smbus
from collections import namedtuple

class ADXL345():
	def __init__(self):
		self._bus = smbus.SMBus(1)
		self._addr = 0x53
		self.measure(True)
		
	def ID(self):
		ID = self._bus.read_byte_data(self._addr, 0x00)
		return ID
		
	def Y(self):
		Y = self._bus.read_i2c_block_data(self._addr, 0x34, 2)
		#print "0x%0.4X" % (Y[0] + (Y[1]<<8))
		return Y[0] + (Y[1]<<8)
		
	def getData(self):
		v = self._bus.read_i2c_block_data(self._addr, 0x32, 6)
		data = namedtuple("data", "x y z")
		data.x = v[0] + (v[1]<<8)
		data.y = v[2] + (v[3]<<8)
		data.z = v[4] + (v[5]<<8)
		return data
		
	def measure(self, state):
		POWER_CTL = self._bus.read_byte_data(self._addr, 0x2D)
		if state == True:
			POWER_CTL = POWER_CTL | 0x08
		else:
			POWER_CTL = POWER_CTL & ~0x08
		self._bus.write_byte_data(self._addr, 0x2D, POWER_CTL)
		