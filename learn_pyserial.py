import serial
import serial.tools.list_ports
import time

ser = serial.Serial()
Com_Dict = {}
for port in list(serial.tools.list_ports.comports()):
    print(port)
    Com_Dict["%s" % port[0]] = "%s" % port[1]
    # print(Com_Dict)
    print(port[0])
    print(port[1])

ser.port = "COM7"
ser.baudrate = 19200
ser.bytesize = 8
ser.stopbits = 1
ser.parity = "N"

def serial_Open():
    try:
        ser.open()
        print("打开串口")
    except:
        print("Port Error", "此串口不能被打开！")
        return None


def data_send():
    if ser.isOpen():
        # input_s = "SendTestData"
        # ser.write(input_s.encode('utf-8'))
        ser.write(bytes([1,2,3,4]))
    else:
        pass

def data_receive():
    time.sleep(1)
    try:
        num = ser.inWaiting()
    except:
        ser.close()
    if num > 0:
        data = ser.read(num)
        print(data)
    else:
        pass
serial_Open()
while(True):
    data_send()
    data_receive()
# print(list(serial.tools.list_ports.comports()))