from pygame import time
import serial


class ArduinoManager:
	CONNECTION_WAITING_DELAY = 3000  # milliseconds
	
	def __init__(self):
		self.serial_port = self._get_connection()
		self.connection_established = True
		
	def _get_connection(self):
		try:
			serial_port = serial.Serial('COM4')  # open serial port
			print("Connecting to Arduino...")
			time.wait(self.CONNECTION_WAITING_DELAY)
		except serial.serialutil.SerialException:
			self.connection_established = False
			raise Exception(f"Arduino-Connection-Error: Port C4  could not be open.")
		
		return serial_port

	def send_data_to_arduino(self, string: str) -> None:
		self.serial_port.write(string.encode())
	
	# Reads all the lines of bytes contained in the buffer.
	def read_data_from_arduino(self) -> [str]:
		if self.serial_port.in_waiting == 0:  # True: there isn't any content in the buffer
			return []
		return [str(value) for value in self.serial_port.readline()]
