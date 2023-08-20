def arithmetic_arranger(*problems):
  
  if len(problems[0])>5:
    return "Error: Too many problems."
  
  size = len(problems)
  is_results_active = 0
  
  if size == 2:
    is_results_active = 1
    
  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""

  amount_problems = len(problems[0])
  
  for problem in problems[0]:
    operation = problem.split(" ")
    first_operand = operation[0]
    operator = operation[1]
    second_operand = operation[2]

    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."
    if len(first_operand) > 4 or len(second_operand) > 4:
      return "Error: Numbers cannot be more than four digits."
    if not(first_operand.isnumeric() and second_operand.isnumeric()):
      return "Error: Numbers must only contain digits."

    char_size = len(first_operand)  
    if len(first_operand) < len(second_operand):
      char_size = len(second_operand)

    empty_space_1_length = char_size+2-len(first_operand)
    if problem == problems[0][amount_problems-1]:
      first_operand_line = " "*empty_space_1_length + first_operand + "\n"
    else:
      first_operand_line = " "*empty_space_1_length + first_operand + "    "

    first_line += first_operand_line

    empty_space_2_length = char_size+2-len(second_operand)-1
    if problem == problems[0][amount_problems-1]:
      second_operand_line = operator + " "*empty_space_2_length + second_operand + "\n"
    else:
      second_operand_line = operator + " "*empty_space_2_length + second_operand + "    "

    second_line += second_operand_line

    if problem == problems[0][amount_problems-1]:
      lines = "-"*(char_size+2)
    else :
      lines = "-"*(char_size+2) + "    "

    third_line += lines

    if is_results_active == 1:
      if problems[1] == True:
        if operator == "+":
         result = int(first_operand) + int(second_operand)
        if operator == "-":
         result = int(first_operand) - int(second_operand)
        result = str(result)
        empty_space_result_length = char_size+2-len(result)
    
        if problem == problems[0][amount_problems-1]:
          result_line = " "*empty_space_result_length + result
          third_line += "\n"
        else:
          result_line = " "*empty_space_result_length + result + "    "
      fourth_line += result_line
  
  arranged_problems = first_line + second_line + third_line + fourth_line
  
  return arranged_problems
