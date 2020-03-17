"""
rat.py

Usage:  python rat.py L   ### L is maximum parent level


"""
import os
import sys
try: import matplotlib.pyplot as plt
except: plt = False

do_debug = 'DEBUG' in os.environ

class RAT(object):
  """
Class implementing one pass through algorithm loop of fb10002.txt

"""
  def __init__(self,parent_rat=None,up=False):
    """Initialize new RAT object"""

    if None is parent_rat:
      ### If there is no parent RAT, initialize to level 0
      self.level = 0
      self.d1,self.d2,self.d3,self.d4 = 0,1,1,1
    else:
      ### Else initialize to one level beyond parent ...
      self.level = parent_rat.level + 1
      self.d1,self.d2,self.d3,self.d4 = parent_rat.get_ds()

      ### ... and increment part I or part I parameters
      if up:
        self.d1 += self.d3
        self.d2 += self.d4
      else:
        self.d3 += self.d1
        self.d4 += self.d2

  def xratio(self):
   """Calculate RAT ratio"""
   return float(self.d1 + self.d3
        ) / float(self.d2 + self.d4)

  def get_ds(self):
    """Get parameters"""
    return self.d1,self.d2,self.d3,self.d4

  def make_children(self):
    """Create children of this parent RAT object"""
    return RAT(parent_rat=self,up=False),RAT(parent_rat=self,up=True)
### End of RAT class
########################################################################


if "__main__" == __name__ and sys.argv[1:]:

  ### Parse maximum level from sys.argv[1]
  max_level = int(sys.argv[1])

  ### Create FIFO queue of parent RAT objects; add level 0 RAT
  from Queue import Queue
  q = Queue()
  q.put(RAT())

  ### Loop while queue has parents
  while not q.empty():
    ### Pop RAT object; print its particulars if DEBUG or plotting disabled
    rat = q.get()
    if do_debug or not plt: print((rat.level,rat.xratio(),rat.get_ds(),))

    ### Make children RAT objects; iterate over them
    children = rat.make_children()
    for child in children:
      ### Plot parent-child lines, if plotting is enabled
      if plt: plt.plot([rat.level,child.level],[rat.xratio(),child.xratio()],'b-o')
      ### Add child to FIFO queue as future parent, if level allows
      if child.level <= max_level: q.put(child)

  ### Annotate plot, if plotting enabled
  if plt:
    plt.xlabel('Level')
    plt.ylabel('X ratio')
    plt.title('Coronavirus Puzzle; max parent level = {0}'.format(max_level))
    plt.show()
