"""
IR Codes for Robosapien

Author: Matt Avallone
"""

CODE_RSTurnRight       = (0x80, "Turn Right")
CODE_RSRightArmUp      = (0x81, "Right Arm Up")
CODE_RSRightArmOut     = (0x82, "Right Arm Out")
CODE_RSTiltBodyRight   = (0x83, "Tilt Body Right")
CODE_RSRightArmDown    = (0x84, "Right Arm Down")
CODE_RSRightArmIn      = (0x85, "Right Arm In")
CODE_RSWalkForward     = (0x86, "Walk Forward")
CODE_RSWalkBackward    = (0x87, "Walk Backward")
CODE_RSTurnLeft        = (0x88, "Turn Left")
CODE_RSLeftArmUp       = (0x89, "Left Arm Up")
CODE_RSLeftArmOut      = (0x8A, "Left Arm Out")
CODE_RSTiltBodyLeft    = (0x8B, "Tilt Body Left")
CODE_RSLeftArmDown     = (0x8C, "Left Arm Down")
CODE_RSLeftArmIn       = (0x8D, "Left Arm In")
CODE_RSStop            = (0x8E, "Stop")

CODE_RSRightTurnStop   = (0xA0, "Right Turn Stop")
CODE_RSRightHandThump  = (0xA1, "Right Hand Thump")
CODE_RSRightHandThrow  = (0xA2, "Right Hand Throw")
CODE_RSSleep           = (0xA3, "Sleep")
CODE_RSRightHandPickup = (0xA4, "Right Hand Pickup")
CODE_RSLeanBackward    = (0xA5, "Lean Backward")
CODE_RSForwardStep     = (0xA6, "Forward Step")
CODE_RSBackwardStep    = (0xA7, "Backward Step")
CODE_RSLeftTurnStep    = (0xA8, "Left Turn Step")
CODE_RSLeftHandThump   = (0xA9, "Left Hand Thump")
CODE_RSLeftHandThrow   = (0xAA, "Left Hand Throw")
CODE_RSListen          = (0xAB, "Listen")
CODE_RSLeftHandPickup  = (0xAC, "Left Hand Pick Up")
CODE_RSLeanForward     = (0xAD, "Lean Forward")
CODE_RSReset           = (0xAE, "Reset")

CODE_RSExecute         = (0xB0, "Execute")
CODE_RSWakeUp          = (0xB1, "Wake Up")

CODE_RSRightHandStrike3 = (0xC0, "Right Hand Strike 3")
CODE_RSRightHandSweep   = (0xC1, "Right Hand Sweep")
CODE_RSBurp             = (0xC2, "Burp")
CODE_RSRightHandStrike2 = (0xC3, "Right Hand Strike 2")
CODE_RSHigh5            = (0xC4, "High Five")
CODE_RSRightHandStrike1 = (0xC5, "Right Hand Strike 1")
CODE_RSBulldozer        = (0xC6, "Bulldozer")
CODE_RSOops             = (0xC7, "Oops")
CODE_RSLeftHandStrike3  = (0xC8, "Left Hand Strike 3")
CODE_RSRightHandSweep   = (0xC9, "Right Hand Sweep")
CODE_RSWhistle          = (0xCA, "Whistle")
CODE_RSLeftHandStrike2  = (0xCB, "Left Hand Strike 2")
CODE_RSTalkback         = (0xCC, "Talk Back")
CODE_RSLeftHandStrike1  = (0xCD, "Left Hand Strike 1")
CODE_RSRoar             = (0xCE, "Roar")

CODE_RSNoOp             = (0xEF, "No Op")


rs_codes = [
	CODE_RSTurnRight,
	CODE_RSRightArmUp,
	CODE_RSRightArmOut,
	CODE_RSTiltBodyRight,
	CODE_RSRightArmDown,
	CODE_RSRightArmIn,
	CODE_RSWalkForward,
	CODE_RSWalkBackward,
	CODE_RSTurnLeft,
	CODE_RSLeftArmUp,
	CODE_RSLeftArmOut,
	CODE_RSTiltBodyLeft,
	CODE_RSLeftArmDown,
	CODE_RSLeftArmIn,
	CODE_RSStop,
	CODE_RSRightTurnStop,
	CODE_RSRightHandThump,
	CODE_RSRightHandThrow,
	CODE_RSSleep,
	CODE_RSRightHandPickup,
	CODE_RSLeanBackward,
	CODE_RSForwardStep,
	CODE_RSBackwardStep,
	CODE_RSLeftTurnStep,
	CODE_RSLeftHandThump,
	CODE_RSLeftHandThrow,
	CODE_RSListen,
	CODE_RSLeftHandPickup,
	CODE_RSLeanForward,
	CODE_RSReset,
	CODE_RSExecute,
	CODE_RSWakeUp,
	CODE_RSRightHandStrike3,
	CODE_RSRightHandSweep,
	CODE_RSBurp,
	CODE_RSRightHandStrike2,
	CODE_RSHigh5,
	CODE_RSRightHandStrike1,
	CODE_RSBulldozer,
	CODE_RSOops,
	CODE_RSLeftHandStrike3,
	CODE_RSRightHandSweep,
	CODE_RSWhistle,
	CODE_RSLeftHandStrike2,
	CODE_RSTalkback,
	CODE_RSLeftHandStrike1,
	CODE_RSRoar,
	CODE_RSNoOp
]