import robosapien
import argparse
import lcd

display = lcd.Lcd()

display.lcd_display_string("Robosapien", 1)
display.lcd_display_string("Hack", 2)



def main():
	# Initiate the parser
	parser = argparse.ArgumentParser()
	parser.add_argument('--gpio_pin', type=int, default=14, help='GPIO pin for IR transmitter')
	parser.add_argument('--command', required=True, help='IR commmand to send to Robosapien')
	args = parser.parse_args()

	pin = args.gpio_pin
	command = args.command

	rs = robosapien.Robosapien(pin)	#create Robo object for GPIO pin
	rs.send_code(int(command, 16))
	# rs.send_code(0xB1)	#Issue reset command
	# raw_input('Enter')
	# rs.send_code(0x81)	#Right arm up
	# rs.send_code(0x81)
	# rs.send_code(0x82)	#Right wrist out
	# rs.send_code(0x85)	#Right wrist in
	# rs.send_code(0x82)
	# rs.send_code(0x85)

	# raw_input('Enter')
	# rs.send_code(0x89)	#Left arm up
	# rs.send_code(0x89)
	# for i in range(0,2):
	# 	rs.send_code(0x8B)	#Tilt left
	# 	rs.send_code(0x83)	#Tilt right	
	# 	rs.send_code(0x83)
	# 	rs.send_code(0x8B)
	# rs.send_code(0x8C)	#Left arm down
	# rs.send_code(0x84)	#Right arm down
	# rs.send_code(0x8C)
	# rs.send_code(0x84)

	# raw_input('Enter')
	# rs.send_code(0xC4)	#Hi 5

	# raw_input('Enter')
	# rs.send_code(0xCE)	#Roar

if __name__ == '__main__':
	main()