FE568A
======

clean interface for FE568A atomic frequency reference

Usage
=====

    fe568a('/dev/tty/USB0')
    print fe568a.get_info()
    fe568a.set_freq_volatile(10**7)
    fe568a.set_freq_volatile_hex('2ABB5040')
    fe568a.set_freq_nonvolatile()
