

all:
	./st2py.bash < fb1002.txt > pyfb1002.py

zip:
	$(RM) cvpuzzle.zip
	zip cvpuzzle.zip 00readme.txt fb1002.txt Makefile st2py.bash rat.py cvpuzzle.py btcfb1002.py btcfb1002.txt test_cvpuzzle.py
