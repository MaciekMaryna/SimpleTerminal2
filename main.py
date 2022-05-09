# from tkinter import *
from tkinter import Canvas
from time import sleep
import msvcrt
import serial.tools.list_ports
# import functools

my_run_flag = True

ports = serial.tools.list_ports.comports()


class SerialPort:
    def __init__(self, com, baud):
        self.my_serial = serial.Serial(com, baud, timeout=0)
        self.lastReadLine = ""

    def isSomethingToRecive(self):
        if self.my_serial.isOpen() and self.my_serial.in_waiting:
            return True
        else:
            return False

    def recive(self):
        self.lastReadLine = str(self.my_serial.readline().decode('utf'))
        return self.lastReadLine

    def transmit(self, char):
        buffer = bytearray(char)
        self.my_serial.write(buffer)

    def __del__(self):
        if self.my_serial.isOpen():
            self.my_serial.close()


def main():
    newCom = input("Podaj numer portu COM (ENTER=COM18): ")
    if "" == newCom:
        newCom = 'COM18'
    newBaud = input("Podaj prędkość transmisji (ENTER=115200): ")
    if "" == newBaud:
        newBaud = '115200'

    s = SerialPort(com=newCom.upper(), baud=int(newBaud))
    run = True
    char = ''
    sleep(0.1)
    while run:
        if s.isSomethingToRecive():
            print(s.recive().rstrip())
            sleep(0.1)

        if msvcrt.kbhit():
            char = msvcrt.getch().lower()
            if 'x' == char.decode('utf-8').lower():
                run = False
                break
            s.transmit(char)

main()
# # def section ########################################################################################################
# def init_com_port(index):
#     port_name = str(ports[index])
#     port_name_short = port_name.split(" ")[0]
#     serial_obj.port = port_name_short
#     serial_obj.baudrate = 115200
#     serial_obj.open()
#
#
# def write_serial_port(msg):
#     serial_obj.write(str(msg).encode())
#
#
# def open_port():
#     None
#
#
# def close_port():
#     if serial_obj.isOpen():
#         serial_obj.close()
#
#
# def enable_to_close():
#     global my_run_flag
#     my_run_flag = False
#     close_port()
#     my_window.quit()
#     my_window.destroy()
#
#
# def clear_revive_canvas():
#     print('Find out how to clear recived data canvas.')
#     recive_canvas.delete("all")
#     recive_canvas.xview_scroll(0)
#     recive_canvas.yview_scroll(0)
#
#
# def read_serial_port():
#     if serial_obj.isOpen() and serial_obj.in_waiting:
#         packet = serial_obj.readline()
#         if packet[0] == 13:
#             packet_string = packet[1:].decode('utf').rstrip("\n")
#         else:
#             packet_string = packet.decode('utf').rstrip("\n")
#         Label(recive_data_frame, text=packet_string, font=("Courier", 10), fg="white", bg="black").pack(anchor="w")


