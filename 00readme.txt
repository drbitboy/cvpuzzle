
### Usage

      Run algorithm:

        make
        python cvpuzzle.py 

      Plot algorithm progression:

        python rat.py L   ### L is number of parent levels

        e.g.

        python rat.py 4    ### See image below

      Verify alternate implementation in btcfb1002.py/.txt is equivalent to pyfb1002.py/fb1002.txt:

        python test_cvpuzzle.py  ### and after a while, hit Control-C ...
        ^C{'successes': 52611, 'failures': 0}

![](https://github.com/drbitboy/cvpuzzle/raw/master/cvpuzzle.png)

### Manifest

    fb1002.txt          Original puzzle algorithm as Structured Text (ST) code
    Makefile            Make file to call st2py.bash
    st2py.bash          BASH script that creates pyfb1002.py from fb1002.txt
    =>pyfb1002.py       - File created by Makefile/st2py.bash; not part of repo
    cvpuzzle.py         Run single case against pyfb1002.py
    rat.py              Script to plot algorithm progression
    cvpuzzle.png        Image of plot from rat.py
    btcfb1002.py        Alternate implementation of algorithm in Python
    btcfb1002.txt       Alternate implementation of algorithm in ST
    test_cvpuzzle.py    Script to run test cases comparing original vs. alternate implementations
    00readme.txt        This file
    README.md           Symlink to this file for Github
