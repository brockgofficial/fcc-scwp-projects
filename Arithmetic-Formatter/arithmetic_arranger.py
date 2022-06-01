###
# Function to define how to format the arithmetic
#
# - Args:
#   - problems: List of of strings of problems.
#   - displayResult: Boolean to display answer (optional).
#
# - Return:
#   - arranged_problems, either error message or the formatted output.
###
def arithmetic_arranger(problems, displayResult=False):
  #Function Constants
  BUFFER = 4

  #Check whether the list has over 5 problems
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
  else:
    #Initialise output layers as empty, first arithmetic as true
    #and error flag as false
    first_operands_layer = second_operands_layer = third_layer = answer_layer = ""
    first_arithmetic = True
    error_flag = False

    #Loop through each of the arithmetics in the list
    for arithmetic in problems:
      #Split arithmetic into operands and operators
      operand = arithmetic.split(" ")

      #Check for correct operators, only digits and digit length
      if operand[1] not in ["+", "-"]:
        arranged_problems = "Error: Operator must be '+' or '-'."
        error_flag = True
        break
      elif not operand[0].isdigit() or not operand[2].isdigit():
        arranged_problems = "Error: Numbers must only contain digits."
        error_flag = True
        break
      elif len(operand[0]) > 4 or len(operand[2]) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        error_flag = True
        break
      else:
        #Length of arithmetic for display output layout and spacing
        max_arithmetic_length = len(operand[0]) + 2 if len(operand[0]) > len(operand[2]) else len(operand[2]) + 2

        #Perform formatting (must do layer 1, layer 2, layer 3 and layer 4 (if True on second argument))
        first_operands_layer += "{buffer}{operand_one_spaces}{operand_one}".format(operand_one_spaces=(" " * (max_arithmetic_length - len(operand[0]))), operand_one=operand[0], buffer=(" " * 0 if first_arithmetic else " " * BUFFER))
        second_operands_layer += "{buffer}{operator}{operand_two_spaces}{operand_two}".format(operator=operand[1], operand_two_spaces=(" " * (max_arithmetic_length - len(operand[2]) -1)), operand_two=operand[2], buffer=(" " * 0 if first_arithmetic else " " * BUFFER))
        third_layer += "{buffer}{hyphens}".format(hyphens=("-" * max_arithmetic_length), buffer=(" " * 0 if first_arithmetic else " " * BUFFER))

        #Answer display
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
        answer = "{}".format(ops[operand[1]](int(operand[0]),int(operand[2])))
        answer_layer += "{buffer}{answer_spaces}{answer}".format(answer_spaces=(" " * (max_arithmetic_length - len(answer))), answer=answer, buffer=(" " * 0 if first_arithmetic else " " * BUFFER))

        #First arithmetic done, set to false for the following arithmetics
        if first_arithmetic:
          first_arithmetic = False
          
    if not error_flag:
      #Construct final answer (include answers if required)
      arranged_problems = "{}\n{}\n{}{}".format(first_operands_layer, second_operands_layer, third_layer, ("\n" + answer_layer if displayResult else ""))

  return arranged_problems