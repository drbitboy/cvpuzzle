"""
btcfb1002.py

Alternate implementation of algorithm from [fb1002.txt], using Python 
- Method .btc_fb1002
- See test_cvpuzzle.py for usage
- Also Uses locally-scoped variables lcl_* for numerator and denominator
  that are updated on each pass through the while loop


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
DINT_TO_LREAL = DINT_TO_REAL = float
def btc_fb1002(x,N):

        ### Initialize integer parameters
        diVar1 = 0  ### Numerator part I
        diVar2 = 1  ### Denominator part I
        diVar3 = 1  ### Numerator part II
        diVar4 = 1  ### Denominator part II

        ### Continue loop while denominator parameters are less than N
        while diVar2 <= N and diVar4 <= N:

                    ### Calculate combined numerator and combined denominator
                    lcl_numer  = diVar1 + diVar3
                    lcl_denom  = diVar2 + diVar4

                    ### Calculate floating-point ratio
                    lrVar1 = DINT_TO_LREAL(lcl_numer) / DINT_TO_REAL(lcl_denom)

                    ### If ratio matches target [x] ...
                    if x == lrVar1:

                        ### Choose which numerator and denominator pair to use
                        if lcl_denom < N:
                            Numerator = lcl_numer
                            Denominator = lcl_denom
                        elif diVar4 > diVar2:
                            Numerator = diVar3
                            Denominator = diVar4
                        else:
                            Numerator = diVar1
                            Denominator = diVar2

                        ### Exit loop early as well as method
                        return Numerator,Denominator

                    ### Otherwise repeat loop after adjusting either ...
                    if x > lrVar1:
                        ### ... part I parameters to increase ratio, ...
                        diVar1 = lcl_numer
                        diVar2 = lcl_denom
                    else:
                        ### ... or part II parameters to decrease ratio
                        diVar3 = lcl_numer
                        diVar4 = lcl_denom

        ### On loop exit* use best parts for result
        ### * Exact ratio not found; diVar2 or diVar4 exceeded N
        if diVar2 > N:
            Numerator = diVar3
            Denominator = diVar4
        else:
            Numerator = diVar1
            Denominator = diVar2

        ### Exit method
        return Numerator,Denominator
