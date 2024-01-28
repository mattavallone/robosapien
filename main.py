"""
Robosapien Project Main

Author: Matt Avallone
"""

import robosapien
import argparse
import lcd
import ir_codes
import time

def display_default():
	display.lcd_clear()
	display.lcd_display_string("Robosapien", 1)
	display.lcd_display_string("Hack", 2)
	time.sleep(1)

def display_command(command):
	display.lcd_clear()
	rs_commands = ir_codes.rs_codes
	for rscm in rs_commands:
		if int(command, 0) == rscm[0]:
			if len(rscm[1]) > 16:
				ws_count = rscm[1].count(' ')
				if ws_count == 1:
					line1, line2 = rscm[1].split(' ')
				elif ws_count == 2:
					line1, line2 = rscm[1].split(' ', 1)
				else:
					w1, w2, line2 = rscm[1].split(' ', 2)
					line1 = w1 + ' ' + w2

				display.lcd_display_string(line1, 1)
				display.lcd_display_string(line2, 2)

			else:
				display.lcd_display_string(rscm[1], 1)

def wakeup_robosapien(rs):
	# Power on Robosapien HW
	display.lcd_clear()
	display.lcd_display_string("Waking Up...", 1)

	rs.send_code(ir_codes.CODE_RSWakeUp[0])

	time.sleep(10)

def run(rs):
	while True:
		try:
			command = input("Enter IR command: ").strip()

			# Display command name
			display_command(command)

			# Turn on end effector
			if int(command, 0) == ir_codes.CODE_RSRightHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOnMagnet[0]:
				rs.turn_on_magnet()

			if int(command, 0) == ir_codes.CODE_RSLeftHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOnSuction[0]:
				rs.turn_on_suction()

			# Execute input command
			rs.send_code(int(command, 16))

			if int(command, 0) == ir_codes.CODE_RSTurnOffMagnet[0]:
				rs.turn_off_magnet()

			if int(command, 0) == ir_codes.CODE_RSTurnOffSuction[0]:
				rs.turn_off_suction()

		except Exception as e:
			print("Error - " + str(e))

def run_once(rs, command, wakeup):
	if wakeup:
		wakeup_robosapien(rs)

	# Display command name
	display_command(command)

	# Turn on end effector
	if int(command, 0) == ir_codes.CODE_RSRightHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOnMagnet[0]:
		rs.turn_on_magnet()

	if int(command, 0) == ir_codes.CODE_RSLeftHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOnSuction[0]:
		rs.turn_on_suction()

	# Execute input command
	rs.send_code(int(command, 16))

	time.sleep(5)

	display_default()

	# Turn off end effector after waiting 5 seconds
	if int(command, 0) == ir_codes.CODE_RSRightHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOffMagnet[0]:
		rs.turn_off_magnet()

	if int(command, 0) == ir_codes.CODE_RSLeftHandPickup[0] or int(command, 0) == ir_codes.CODE_RSTurnOffSuction[0]:
		rs.turn_off_suction()

if __name__ == '__main__':
	# Setup LCD Display
	display = lcd.Lcd()

	# Initiate the parser
	parser = argparse.ArgumentParser()
	parser.add_argument('--gpio_pin', type=int, default=14, help='GPIO pin for IR transmitter')
	parser.add_argument('--command', help='IR commmand to send to Robosapien')
	parser.add_argument('--wakeup', type=bool, default=False, help='Flag to initiate wakeup before executing command')
	args = parser.parse_args()

	pin = args.gpio_pin
	command = args.command
	wakeup = args.wakeup

	display_default()

	# Create Robosapien object for GPIO pin
	rs = robosapien.Robosapien(pin)

	# Run once
	# run_once(rs, command, wakeup)

	# Run forever
	run(rs)