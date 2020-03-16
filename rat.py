import os
import sys
try: import matplotlib.pyplot as plt
except: plt = False

do_debug = 'DEBUG' in os.environ

class RAT(object):
  def __init__(self,parent_rat=None,up=False):
    if None is parent_rat:
      self.level = 0
      self.d1,self.d2,self.d3,self.d4 = 0,1,1,1
    else:
      self.level = parent_rat.level + 1
      self.d1,self.d2,self.d3,self.d4 = parent_rat.get_ds()

      if up:
        self.d1 += self.d3
        self.d2 += self.d4
      else:
        self.d3 += self.d1
        self.d4 += self.d2

  def xratio(self): return float(self.d1 + self.d3
                       ) / float(self.d2 + self.d4)

  def get_ds(self): return self.d1,self.d2,self.d3,self.d4

  def make_children(self):
    return RAT(parent_rat=self,up=False),RAT(parent_rat=self,up=True)


if "__main__" == __name__ and sys.argv[1:]:
  max_level = int(sys.argv[1])

  from Queue import Queue
  q = Queue()
  q.put(RAT())
  while not q.empty():
    rat = q.get()
    if do_debug or not plt: print((rat.level,rat.xratio(),rat.get_ds(),))
    children = rat.make_children()
    for child in children:
      if plt: plt.plot([rat.level,child.level],[rat.xratio(),child.xratio()],'b-o')
      if child.level <= max_level: q.put(child)

  if plt:
    plt.xlabel('Level')
    plt.ylabel('X ratio')
    plt.title('Coronavirus Puzzle; max parent level = {0}'.format(max_level))
    plt.show()
