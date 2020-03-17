"""
Usage:  make all ; python cvpuzzle.py

Pre-requisite:  pyfb1002.py, via command [make all]

"""
import pyfb1002

x = .11011
N = 10000
print('fb1002({0},{1}) => {2}'.format(x
                                     ,N
                                     ,pyfb1002.orig_fb1002(x,N)
                                     ))
