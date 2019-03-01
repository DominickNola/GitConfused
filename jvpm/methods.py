"""import stack.py"""
import stack
S = stack.Stack()
OPERANDS = [0]

class Methods():
    """class of methods called from the main, using method names retrieved from jvpm_dict.py"""
    def __init__(self):
        self.VARIABLES = []
    
    # def i2b():
    #     print('i2b')
    #     https://www.delftstack.com/howto/python/how-to-convert-int-to-bytes-in-python-2-and-python-3/
    #     temp_int = S.pop()
    #     byte = bytes([temp_int])
    #     S.push(byte)
    #     print("i2b converts " + str(temp_int) + " to a byte: " + str(byte))

    # def i2c():
    #     print('i2c')

    # def i2d():
    #     print('i2d')

    # def i2f():
    #     print('i2f')

    # def i2l():
    #     print('i2l')

    # def i2s():
    #     print('i2s')

    def iadd(self):
        """iadd: add two ints"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 + var2)
        print("> 60 = iadd: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nadded the two,"
              " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return var1 + var2

    # def method11():
    #     print('method11')

    def iand():
        """iand: performed bitwise AND on two integers"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 & var2)
        print("> iand: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nperformed bitwise"
              " AND and pushed the result (" + str(var2 & var1) + ") back to Stack")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return var1 & var2
        
    # def iastore():
    #     print('iastore')

    def iconst_m1():
        """iconst_m1: load the int value -1 onto the stack"""
        S.push(-1)
        print("iconst_m1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")
        return S.peek()

    def iconst_0(self):
        """iconst_0: load the int value 0 onto the stack"""
        S.push(0)
        print("iconst_0: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")
        return S.peek()

    def iconst_1(self):
        """iconst_1: load the int value 1 onto the stack"""
        S.push(1)
        print("> 04 = iconst_1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")
        return S.peek()

    # load the int value 2 onto the stack
    def iconst_2(self):
        """iconst_2: load the int value 2 onto the stack"""
        S.push(2)
        print("iconst_2: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")
        return S.peek()

    def iconst_3(self):
        """iconst_3: load the int value 3 onto the stack"""
        S.push(3)
        print("> 06 = iconst_3: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")
        return S.peek()

    def iconst_4(self):
        """iconst_4: load the int value 4 onto the stack"""
        S.push(4)
        print('"iconst_4: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')
        return S.peek()

    def iconst_5(self):
        """iconst_5: load the int value 5 onto the stack"""
        S.push(5)
        print('"iconst_5: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')
        return S.peek()

    def idiv(self):
        """idiv: divide two numbers"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 / var2)
        print("> idiv: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \ndivided the two,"
              " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return var1 / var2

    # def if_acmpeq():
    #     print('if_acmpeq')

    # def if_acmpene():
    #     print('if_acmpene')

    # def if_icmpeq():
    #     print('if_icmpeq')

    # def if_icmpge():
    #     print('if_icmpge')

    # def if_icmpgt():
    #     print('if_icmpgt')

    # def if_icmple():
    #     print('if_icmple')

    # def if_icmplt():
    #     print('if_icmplt')

    # def if_icmpne():
    #     print('if_icmpne')

    # def ifeq():
    #     print('ifeq')

    # def ifge():
    #     print('ifge')

    # def ifgt():
    #     print('ifgt')

    # def ifle():
    #     print('ifle')

    # def iflt():
    #     print('iflt')

    # def ifne():
    #     print('ifne')

    # def ifnonnull():
    #     print('ifnonnull')

    # def ifnull():
    #     print('ifnull')

    def iinc():
        """iinc: increment local variable #index by signed byte const"""
        print("iinc: not needed for this sprint")

    # def iload():
    #     print('iload')

    def iload_0(self):
        """iload: push variable[0] to the Stack"""
        pushing = OPERANDS[0]
        S.push(pushing)
        print('iload_0: Push OPERANDS[0] on the Stack for processing.')
        return S.peek()

    def iload_1(self):
        """iload: push variable[1] to the Stack"""
        pushing = OPERANDS[1]
        S.push(pushing)
        print('> 1b = iload_1: Push OPERANDS[1] on the Stack for processing.')
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return S.peek()

    def iload_2(self):
        """iload: push variable[2] to the Stack"""
        pushing2 = OPERANDS[2]
        S.push(pushing2)
        print('> 1c = iload_2: Push OPERANDS[2] on the Stack for processing.')
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return S.peek()

    def iload_3(self):
        """iload: push variable[3] to the Stack"""
        pushing3 = OPERANDS[3]
        S.push(pushing3)
        print('iload_3: Push OPERANDS[3] on the Stack for processing.')
        return S.peek()

    # def impdep1():
    #     print('impdep1')

    # def impdep2():
    #     print('impdep2')

    def imul(self):
        """imul: multiply two integers"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 * var2)
        print("> imul: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nmultiplied the two,"
              " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return 

    def ineg(selfself):
        """ineg: value minus zero"""
        var1 = S.pop()
        S.push(0 - var1)
        print('ineg: Popped ' + str(var1) + ' from Stack, ineg = ' + str(S.peek()) + ','
              ' and pushed back to Stack.')
        return 0 - var1

    # def instanceof():
    #     print('instanceof')

    # def invokedynamic():
    #     print('invokedynamic')

    # def invokeinterface():
    #     print('invokeinterface')

    # def invokespecial():
    #     print('invokespecial')

    # def invokestatic():
    #     print('invokestatic')

    # def invokevirtual():
    #     print('invokevirtual')

    def ior(self):
        """ior: performed bitwise OR on two integers"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 | var2)
        print("> ior: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nperformed bitwise"
              " OR and pushed the result (" + str(var2 | var1) + ") back to Stack")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return var1 | var2

    def irem():
        """logical in remainder"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 % var2)
        print("irem = " + str(S.peek()))
        return var1 % var2

    # def ireturn():
    #     print('ireturn')

    def ishl():
        """int logical shift left"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 << var2)
        print("> ishl: Popped (" +str(var1) + ") and (" + str(var2) + ") and shifted"
              + str(var1) + " left by " + str(var2) + " bit(s) and pushed the result"
              " back to Stack.")
        print("ishl = " + str(S.peek()))
        return var1 << var2


    def ishr():
        """description here"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 >> var2)
        print("ishr = " + str(S.peek()))
        return var1 >> var2

    # def istore():
    #     """istore: store int value into array[in]"""
    #     print('method57')

    def istore_0():
        """istore_0: store int value into OPERANDS[0]"""
        popped = S.pop()
        OPERANDS.pop(0) # remove the assigned 0 from the [0]position
        OPERANDS.insert(0, popped)
        print("istore_0: Popped " + str(popped) +
              " from Stack and stored in OPERANDS[0] in methods.py.")
        return OPERANDS[0]

    def istore_1(self):
        """istore_1: store int value into OPERANDS[1]"""
        popped = S.pop()
        OPERANDS.insert(1, popped)
        print("> 3c = istore_1: Popped " + str(popped) +
              " from Stack and stored in OPERANDS[1] in methods.py.")
        print("OPERANDS[] = " + str(OPERANDS))
        return OPERANDS[1]

    def istore_2(self):
        """istore_2: store int value into OPERANDS[2]"""
        popped = S.pop()
        OPERANDS.insert(2, popped)
        print("> 3d = istore_2: Popped " + str(popped) +
              " from Stack and stored in OPERANDS[2] in methods.py.")
        print("OPERANDS[] = " + str(OPERANDS))
        return OPERANDS[2]

    def istore_3(self):
        """istore_3: store int value into OPERANDS[3]"""
        popped = S.pop()
        OPERANDS.insert(3, popped)
        print("> 3e = istore_3: Popped " + str(popped) +
              " from Stack and stored in OPERANDS[3] in methods.py,")
        print("OPERANDS[] = " + str(OPERANDS))
        print(">>>>>>>>>>>>>>>>>>>>>>>> c = " + str(popped) + " <<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(">>>> Size of Stack is now " + str(S.size()) + ".")
        return OPERANDS[3]

    def isub():
        """isub: subtract two ints"""
        var2 = S.pop()
        var1 = S.pop()
        S.push(var1 - var2)
        print("> isub: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nsubtracted the two,"
              " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(S.peek()) + ".")
        return var1 - var2

    def iushr():
        """int logical shift right"""
        var2 = S.pop()
        var1 = S.pop()
        if var1 >= 0:
            S.push(var1 >> var2)
        else:
            S.push((var1 + 0x10000000) >> var2)
        print("iushr = " + str(S.peek()))
        return var1 >> var2

    def ixor(self):
        """int xor"""
        variable2 = S.pop()
        variable1 = S.pop()
        S.push(variable1 ^ variable2)
        print("82 = ixor: Popped 2 values from the Stack and stored in local variables,"
              "\nixor = " + str(S.peek()) + " and pushed back to Stack")
        return variable1 ^ variable2
