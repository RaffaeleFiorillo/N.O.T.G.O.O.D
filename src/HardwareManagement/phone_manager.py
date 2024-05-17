from src.HardwareManagement.arduino_management import ArduinoManager


class PhoneManager:
	RING_TONES = ["A", "B", "C", "D"]
	
	def __init__(self):
		self.arduino_manager = ArduinoManager()  # object used to access the arduino functionalities
		self.is_connected = lambda: self.arduino_manager.connection_established
		self.handset_is_up = False  # The handset of the telephone is lifted from the base
		self.dialed_number = ""  # number the player has dialed. It can hold a max ammount of digits
	
	def ring(self, tone):
		if tone not in self.RING_TONES:
			print(f"*{tone}* is not a valid Tone!")
		elif not self.handset_is_up:
			self.arduino_manager.send_data_to_arduino(f"ring{tone}")
	
	def get_dialed_number(self):
		# obtain the values dialed on the phone as a list of strings representing ascii characters. Ex: ['53', '13']
		received_values = self.arduino_manager.read_data_from_arduino()
		if len(received_values) == 0:
			return
		# converter all values received from the arduino as ascii characters to a single string
		# the last two received characters are \r\n, therefore they are discarded
		value = "".join([chr(int(ascii_val)) for ascii_val in received_values[:-2]])
		
		if value == "up":
			print("Handset UP")
			self.handset_is_up = True
		elif value == "down":
			print("Handset DOWN")
			self.handset_is_up = False
			self.dialed_number = ""  # every time the handset is put down, the dialed number is reset to empty
		elif value.isdigit() and len(self.dialed_number) <= 4:
			self.dialed_number += value
			print(f"Dialed Number: {self.dialed_number}")
		else:
			print(value)
		