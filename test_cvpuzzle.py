import os
import sys
import struct
import pyfb1002
import btcfb1002
import traceback as tb

do_debug = 'DEBUG' in os.environ

try:
  successes,failures = 0,0
  with open('/dev/urandom','rb') as frand:
    while successes < (1<<32):
      n,d = struct.unpack('@HH',frand.read(4))
      if n>=d: continue
      x = float(n) / d
      fbpair = pyfb1002.orig_fb1002(x,10000)
      btcpair = btcfb1002.btc_fb1002(x,10000)
      if fbpair==btcpair: successes += 1
      else              : failures += 1
      

except:
  if do_debug: tb.print_exc()

print(dict(successes=successes,failures=failures))
