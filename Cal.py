from pythonds.basic.stack import Stack
 
import math
 
class cal:
    prec = dict()
    def __init__(self):
        self.s = "";
        self.prec["*"] = 3
        self.prec["/"] = 3
        self.prec["+"] = 2
        self.prec["-"] = 2
        self.prec["("] = 1
         
     
    def calculator(self, data):
        self.s = data
        opstack = Stack()
         
        splitdata = self.s.split()
        postfix = list()
        for i in splitdata:
            if i in "0123456789":
                postfix.append(i)
            elif i == '(':
                opstack.push(i)
            elif i == ')':
                topToken = opstack.pop()
                while topToken != '(':
                    postfix.append(topToken)
                    topToken = opstack.pop()
            else:
                while (not opstack.isEmpty()) and \
                    (self.prec[opstack.peek()] >= self.prec[i]):
                    postfix.append(opstack.pop())
                    print("here")
                opstack.push(i)
            
        while not opstack.isEmpty():
            postfix.append(opstack.pop())
        opstack = Stack()
        operandList = list()
        print (postfix)
        for token in postfix:
            if token in "123456789":
                opstack.push(token)
            elif token == "*":
                i = opstack.pop()
                j = opstack.pop()
                resultdata = float(i)* float(j)
                opstack.push(resultdata)
            elif token == "+":
                i = opstack.pop()
                j = opstack.pop()
                resultdata = float(i)+ float(j)
                opstack.push(resultdata)
            elif token == "-":
                i = opstack.pop()
                j = opstack.pop()
                resultdata = float(j) - float(i)
                opstack.push(resultdata)
            elif token == "/":
                i = opstack.pop()
                j = opstack.pop()
                resultdata = float(j)/ float(i)
                opstack.push(resultdata)
        return opstack.pop()
 
if __name__ == "__main__":
    a =cal()
    res = a.calculator("( 2 + 3 ) * 3 - ( 3 - 2 ) * ( 3 + 2 )")
    print(res)
         

