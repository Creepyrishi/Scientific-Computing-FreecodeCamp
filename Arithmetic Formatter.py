Lf, Ls, Lval, ld = '','','',''
def arithmetic_arranger(problems, solve = False):
    global Lf, Ls, Lval, ld
    Lf, Ls, Lval, ld = '','','',''
    if len(problems) > 5:
      return "Error: Too many problems."
    for problem in problems:
      for i in problem:
        if not i in ['1','2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '+', '-']:
          return "Error: Numbers must only contain digits."
      F,O,S = problem.split(' ')
      if O not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
      if len(F) > 4 or len(S) > 4:
        return "Error: Numbers cannot be more than four digits."
      D = "--"
      length = max(len(F), len(S))
      if O ==  '+':
        Val = str(int(F)+int(S))
      if O ==  '-':
        Val = str(int(F)-int(S))
      for i in range(0, length):
        D += "-"

      if len(F)>len(S):
        F = "  " + F
        for i in range(0,(len(D)-len(S))):
          S = " " + S
      elif len(S)>len(F):
        S = "  " + S
        for i in range(0,(len(D)-len(F))):
          F = " " + F
      else:
          S = "  " + S
          F = "  " + F 
      for i in range(0,(len(D)-len(Val))):
          Val = " " + Val
      Sf = O + S[1:]
      if problem != problems[-1]:
        Lf = Lf + F + "    "
        Ls = Ls + Sf + "    "
        Lval = Lval+ Val + "    "
        ld= ld + D + "    "
      else:
        Lf = Lf + F 
        Ls = Ls + Sf
        Lval = Lval+ Val
        ld= ld + D
    if solve:   
          return f"{Lf}\n{Ls}\n{ld}\n{Lval}"
    if not solve:   
          return f"{Lf}\n{Ls}\n{ld}"

print(arithmetic_arranger(["32 * 698", "3801 - 2", "45 + 43", "123 + 49"]))