def ispar( x):
    stack = []
    isbal = True
    ope = ['(', '[', '{']
    for i in range(0, len(x)):
        if (x[i] in ope):
            stack.append(x[i])
        elif (x[i] == ')' and len(stack) != 0):
            if (stack.pop() == '('):
                isbal = True
            else:
                isbal = False
                return isbal
        elif (x[i] == ']' and len(stack) != 0):
            if (stack.pop() == '['):
                isbal = True
            else:
                return False
        elif (x[i] == '}' and len(stack) != 0):
            if (stack.pop() == '{'):
                isbal = True
            else:
                return False
        elif (len(stack) == 0):
            return False

    if (len(stack) != 0):
        return False

    return isbal



s=input("Enter String:")
res=ispar(s)
if(res==True):
    print("Balanced")
else:
    print("Unbalanced")