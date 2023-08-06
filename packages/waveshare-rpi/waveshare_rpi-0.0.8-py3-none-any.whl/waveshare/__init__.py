import serial
import pynmea2
import threading
import continuous_threading

ser = None
lock = threading.Lock()

gga = None
gsa = None
gsv = None
rmc = None


def get_gga():
    with lock:
        return gga


def get_gsa():
    with lock:
        return gsa


def get_gsv():
    with lock:
        return gsv


def get_rmc():
    with lock:
        return rmc


def read_data():
    line = ser.read_until("\n").decode()

    print(line + '\n')
    print('foo!\n')

    headers = {
        "$gngga": gga,
        "$gngsa": gsa,
        "$gngsv": gsv,
        "$gnrmc": rmc,
    }

    if line[:6] in headers.keys():
        with lock:
            headers[line[:6]] = pynmea2.parse(line)


thread = continuous_threading.ContinuousThread(read_data())


def start(device):
    global ser

    global gga
    global gsa
    global gsv
    global rmc

    ser = serial.Serial(device, 19200, timeout=1)
    ser.write(str.encode("AT+CGNSPWR=1\n"))  # turn on the power for GPS

    # TODO: figure out if/why this is needed
    ser.write(str.encode("AT+CGNSSEQ=\"RMC\"\n"))  # define the last NMEA sentence that parsed

    ser.write(str.encode("AT+CGNSTST=1\n"))  # start gps streaming to serial

    thread.start()


def stop():
    with lock:
        if ser is not None:
            ser.write(str.encode("AT+CGNSTST=0\n"))
        if thread is not None:
            thread.stop()
