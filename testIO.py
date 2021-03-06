import platform
import glob
import serial


class SerialPort(object):
    def __init__(self, name):
        self.name = name
        self.port = serial.Serial()
        self.device = []
        self.system = platform.system()

    def scan(self):
        ports = None
        if self.system.lower() == "linux":
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif self.system.lower() == "windows":
            ports = ['COM%s' % (i + 1) for i in range(256)]
        else:
            print ("Unknown os")

        # print "OS: " ,self.system
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.device.append(port)
            except (OSError, serial.SerialException):
                pass

    def list(self):
        for index in range(len(self.device)):
            print("number:", index, "   ", "device:", self.device[index])

    def input(self):
        self.name = self.device[int(raw_input("Input serial device number:"))]

    def config(self, b_rate, t_out):
        self.port = serial.Serial(self.name, b_rate, timeout=t_out)

    def send(self):
        self.port.write(str.encode('ATI\r'))

    def read(self):
        return self.port.readlines()
