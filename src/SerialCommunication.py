import serial
from utils.utils import logger
import time
PORT = "/dev/ttyS1"
BAUD_RATE = 9600
serial_connection = serial.Serial(PORT, BAUD_RATE)


class MotorEnum:
    MOTOR_1 = "MOTOR_1"
    MOTOR_2 = "MOTOR_2"
    MOTOR_3 = "MOTOR_3"


def move_motor(motor: MotorEnum, position: int, speed):
    logger.debug("Moving motor " + motor + " to position " + str(position))
    command = "MOVE " + motor + " " + str(position)
    write_line(command)


def write_line(command: str):
    logger.debug("Writing command " + command)
    serial_connection.write(command.encode())

