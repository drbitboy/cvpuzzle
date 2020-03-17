#!/bin/bash

### Script to convert Structured Text code fb1002.txt to
### equivalent Python code in pyfb1002.py

### Usage:
###
###   ./st2py.bash < fb1002.txt > pyfb1002.py
###
### OR
###
###   make all

tr -d '\r﻿' \
| sed \
  -e 's/\r$//' \
  -e '1i"""' \
  -e '/^BEGIN/a"""' \
  -e '/^BEGIN/aimport os' \
  -e '/^BEGIN/aimport sys' \
  -e '/^BEGIN/aDINT_TO_LREAL = DINT_TO_REAL = float' \
  -e '/^BEGIN/adef orig_fb1002(x,N):' \
  -e 's/^\t/        /' \
  -e 's/#\([a-zA-Z]\)/\1/g' \
  -e 's/:=/=/' \
  -e 's/;\( *\)$/\1/' \
  -e 's/ WHILE \(.*\) DO/ while \1:/' \
  -e 's/ NOT / not /' \
  -e 's/ AND / and /' \
  -e 's/ IF \(.*\) THEN/ if \1:/' \
  -e '/^ *if/s/ = / == /' \
  -e 's/ ELSIF \(.*\) THEN/ elif \1:/' \
  -e 's/\(^ * \)ELSE/\1else:/' \
  -e 's/^ *END_IF.*$//' \
  -e 's/^ *END_WHILE.*$//' \
  -e 's/RETURN/return Numerator,Denominator/' \
  -e 's/^END_FUNCTION_BLOCK/        return Numerator,Denominator/'
