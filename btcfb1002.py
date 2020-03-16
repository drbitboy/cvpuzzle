"""
FUNCTION_BLOCK "fb1002"
{ S7_Optimized_Access = 'TRUE' }
VERSION : 0.1
   VAR_INPUT 
      x : LReal
      N : Int
   END_VAR

   VAR_OUTPUT 
      Numerator : DInt
      Denominator : DInt
   END_VAR

   VAR 
      diVar1 : DInt
      diVar2 : DInt
      diVar3 : DInt
      diVar4 : DInt
      lcl_numer : DInt
      lcl_denom : DInt
      lrVar1 : LReal
   END_VAR


BEGIN
"""
import os
import sys
DINT_TO_LREAL = DINT_TO_REAL = float
def btc_fb1002(x,N):
        diVar1 = 0
        diVar2 = 1
        diVar3 = 1
        diVar4 = 1
        while diVar2 <= N and diVar4 <= N:
                    lcl_numer  = diVar1 + diVar3
                    lcl_denom  = diVar2 + diVar4
                    lrVar1 = DINT_TO_LREAL(lcl_numer) / DINT_TO_REAL(lcl_denom)
                    if x == lrVar1:
                        if lcl_denom < N:
                            Numerator = lcl_numer
                            Denominator = lcl_denom
                            return Numerator,Denominator
                            
                        elif diVar4 > diVar2:
                            Numerator = diVar3
                            Denominator = diVar4
                            return Numerator,Denominator
                        else:
                            Numerator = diVar1
                            Denominator = diVar2
                            return Numerator,Denominator

                    elif x > lrVar1:
                        diVar1 = lcl_numer
                        diVar2 = lcl_denom
                    else:
                        diVar3 = lcl_numer
                        diVar4 = lcl_denom

        if diVar2 > N:
            Numerator = diVar3
            Denominator = diVar4
        else:
            Numerator = diVar1
            Denominator = diVar2

        return Numerator,Denominator
