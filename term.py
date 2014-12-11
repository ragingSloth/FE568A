import serial

class Singleton(type):
    _instances = {}
    COM = serial.Serial()
    def __call__(cls, tty, *args, **kwargs):
        if cls not in cls._instances:
            cls.COM.port = tty
            cls.COM.timeout = 1
            cls.COM.open()
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class fe568a:
    Fref = 50255057.456256
    __metaclass__ = Singleton
    def __init__(self):
        pass

    @staticmethod
    def set_freq_volatile(freq):
        frac = freq/fe568a.Fref
        val = hex(int(frac*(2**32-1)))[2:]
        if len(val) <= 8:
            val = '0' * (8 - len(val)) + val
        else:
            raise Exception('Frequency too high')
        fe568a.COM.write('F=' + val + '\r\n')


    @staticmethod
    def set_freq_nonvolatile(freq):
        fe568.COM.write('E\r\n')


    @staticmethod
    def get_info():
        fe568a.COM.write("S\r\n")
        x = fe568a.COM.readline()
        if x: return x
        else: raise Exception('could not read data')


if __name__ == '__main__':
    fe568a('/dev/ttyUSB0')
    print fe568a.get_info()
    fe568a.set_freq_volatile(10000000)
