

def generate(n):
    for i in range(1,11):
        yield n*i




if __name__ == '__main__':
    # for i in generate(4):
    #     print(i)
    x=generate(7)
    
    for i in x:
        print(i)



