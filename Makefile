
### Default target [all]:  create Python implementation of algorithm
###                        from Structured Text source in [fb1002.txt]

all:
	./st2py.bash < fb1002.txt > pyfb1002.py

### Target [zip]:  move most files to ZIP; this is now obsolete because
###                this suite of programs in in a Github repository

zip:
	$(RM) cvpuzzle.zip
	zip cvpuzzle.zip 00readme.txt fb1002.txt Makefile st2py.bash rat.py cvpuzzle.py btcfb1002.py btcfb1002.txt test_cvpuzzle.py
