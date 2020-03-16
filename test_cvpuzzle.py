import os
import sys
import struct
import pyfb1002
import btcfb1002
import traceback as tb

do_debug = 'DEBUG' in os.environ

try:
  ### Initial count of successes and failures
  successes,failures = 0,0
  ### 64-character Dreaded ASCII Graphics animation for one million successes
  s_progress = '/|\\-' * 16

  sys.stdout.write('Hit Control-C to end program and get results\n')

  ### Open uniform random byte stream
  with open('/dev/urandom','rb') as frand:

    ### Convert 64-char DAG animation into list so .pop() is available
    lt_progress = list(s_progress)

    ### Limit to 2G successful trials
    while successes < (1<<31):

      ### Get three random 16-bit unsigned integers:  numerator; denominator; N
      n,d,N = struct.unpack('@3H',frand.read(6))

      ### Skip some uninteresting cases
      if n==d: continue
      if N<10: continue

      ### Ensure numerator is less than denominator; calculate real ratio
      if n>d: n,d = d,n
      x = float(n) / d

      ### Ensure N is large
      while N < 10000: N += N

      ### Run both implementations of algorithm on ratio
      fbpair = pyfb1002.orig_fb1002(x,N)
      btcpair = btcfb1002.btc_fb1002(x,N)

      ### Tally success or failure
      if fbpair==btcpair: successes += 1
      else              : failures += 1

      ### Advance progress animation using Dreaded ASCII Graphics
      if not (successes%15625):
        if lt_progress: s = '{0}{1}'.format(lt_progress.pop(),chr(8))
        else          : s,lt_progress  = '.',list(s_progress)
        sys.stdout.write(s)
        sys.stdout.flush()

### Handle Control-C (KeyboardInterrupt)
except KeyboardInterrupt as e: pass
### Handle any other error
except: tb.print_exc()

### Output results
print(dict(successes=successes,failures=failures))
