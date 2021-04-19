def EvaluatePostfix(s):
    stack = []
    for i in range(0, len(s)):
        if (ord(s[i]) in range(48, 58)):
            stack.append(s[i])
        else:
            operator = s[i]
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            res = evaluate(operator, operand1, operand2)
            stack.append(res)

    return res


def evaluate(operator, operand1, operand2):
    if (operator == '+'):
        return operand1 + operand2
    elif (operator == '-'):
        return operand1 - operand2
    elif (operator == '*'):
        return operand1 * operand2
    elif (operator == '/'):
        return operand1 / operand2

    return

if __name__ == '__main__':

    s=input("Enter Postfix Operator::")
    print("Result is::",EvaluatePostfix(s))

