import serial
import pynmea2
import threading

ser = None
lock = threading.Lock()
thread = None

gga = None
gsa = None
gsv = None
rmc = None


def get_gga():
    with lock:
        return gga


def set_gga(val):
    global gga
    with lock:
        gga = val


def get_gsa():
    with lock:
        return gsa

def set_gsa(val):
    global gsa
    with lock:
        gsa = val


def get_gsv():
    with lock:
        return gsv


def set_gsv(val):
    global gsv
    with lock:
        gsv = val


def get_rmc():
    with lock:
        return rmc

def set_rmc(val):
    global rmc
    with lock:
        rmc = val


def start(device):
    global ser
    global thread

    ser = serial.Serial(device, 19200, timeout=1)
    ser.write(str.encode("AT+CGNSPWR=1\n"))  # turn on the power for GPS

    # TODO: figure out if/why this is needed
    ser.write(str.encode("AT+CGNSSEQ=\"RMC\"\n"))  # define the last NMEA sentence that parsed

    ser.write(str.encode("AT+CGNSTST=1\n"))  # start gps streaming to serial

    def read_data():
        global gga
        global gsa
        global gsv
        global rmc

        while True:
            line = ser.read_until(str.encode("\n")).decode()

            headers = {
                "$GNGGA": set_gga,
                "$GPGSA": set_gsa,
                "$GPGSV": set_gsv,
                "$GNRMC": set_rmc,
            }

            if line[:6] in headers.keys():
                with lock:
                    headers[line[:6]](pynmea2.parse(line))

    thread = threading.Thread(target=read_data)
    thread.daemon = True
    thread.start()

def stop():
    with lock:
        if ser is not None:
            ser.write(str.encode("AT+CGNSTST=0\n"))
        if thread is not None:
            thread.stop()
