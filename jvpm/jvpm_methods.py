import stack
# These 63 methods will eventually Implement all the opcode commands.
# ONLY BUILD THE METHODS NOT COMMENTED OUT.
# pylint: disable = W0603, C0330
from stack import Stack

#S = stack.Stack()

# According to the JVPM documentation Zach posted to Slack,
# we need to use a local arrays'[] index values when using MATH for iload and istore.
# Therefore, I transitioned the VARIABLES_0-4 to the VARIABLES[] array.
#VARIABLES = [0]

# ****************************************************************************************
class OpCodeMethods():

    def __init__(self):
        self.stack = Stack()
        self.VARIABLES = [0]

    def iadd(self):
        """iadd: add two ints"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 + var2)
        print("> iadd: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nadded the two,"
          " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(self.stack.peek()) + ".")

    def iand(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 & var2)

    def iconst_m1(self):
        self.stack.push(-1)

    def iconst_0(self):
        self.stack.push(0)

    def iconst_1(self):
        """iconst_1: load the int value 1 onto the stack"""
        self.stack.push(1)
        print(self.stack.peek())
        print("iconst_1: Pushed " + str(self.stack.peek()) + " to Stack in jvpm_methods.py.")

    def iconst_2(self):
        self.stack.push(2)

    def iconst_3(self):
        """iconst_3: load the int value 3 onto the stack"""
        self.stack.push(3)
        print("iconst_3: Pushed " + str(self.stack.peek()) + " to Stack in jvpm_methods.py.")

    def iconst_4(self):
        self.stack.push(4)

    def iconst_5(self):
        self.stack.push(5)

    def idiv(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 / var2)
        print("> idiv: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \ndivided the two,"
          " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(self.stack.peek()) + ".")

    def iinc(self):
        print("iinc: not needed for this sprint")

    def iload_0(self):
        pushing = self.VARIABLES[0]
        self.stack.push(pushing)

    def iload_1(self):
        pushing = self.VARIABLES[1]
        self.stack.push(pushing)
        print('iload_1: Load VARIABLES[1] on the Stack for processing.')

    def iload_2(self):
        pushing2 = self.VARIABLES[2]
        self.stack.push(pushing2)
        print('iload_2: Load VARIABLES[2] on the Stack for processing.')

    def iload_3(self):
        pushing3 = self.VARIABLES[3]
        print('iload_3: Load VARIABLES[3] on the Stack for processing.')

    def imul(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 * var2)
        print("> imul: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nmultiplied the two,"
          " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(self.stack.peek()) + ".")

    def ineg(self):
        var1 = self.stack.pop()
        self.stack.push(0 - var1)

    def ior(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 | var2)

    def irem(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 % var2)

    def ishl(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 << var2)

    def ishr(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 >> var2)

    def istore_0(self):
        popped = self.stack.pop()
        #self.VARIABLES.pop(0) # remove the assigned 0 from the [0]position
        self.VARIABLES.insert(0, popped)
        print("ran istore_0")


    def istore_1(self):
        """istore_1: store int value into VARIABLES[1]"""
        popped = self.stack.pop()
        self.VARIABLES.insert(1, popped)
        print(self.VARIABLES)
        print("istore_1: Popped " + str(popped) +
              " from Stack and stored in VARIABLES[1] in jvpm_methods.py.")


    def istore_2(self):
        popped = self.stack.pop()
        self.VARIABLES.insert(2, popped)
        print(self.VARIABLES)
        print("istore_2: Popped " + str(popped) +
              " from Stack and stored in VARIABLES[2] in jvpm_methods.py.")

    def istore_3(self):
        popped = self.stack.pop()
        self.VARIABLES.insert(3, popped)
        print("istore_3: Popped " + str(popped) +
              " from Stack and stored in VARIABLES[3] in jvpm_methods.py,"
              "\n>>>>>>>>>>>>>>>>>>>>>>>> c = " + str(popped) + " <<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(">>>> Top of Stack is now " + str(self.stack.size()) + ".")

    def isub(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 - var2)
        print("> isub: Popped (" + str(var1) + ") and (" + str(var2) +
              ") from the Stack, assigned to local variables, \nsubtracted the two,"
              " and pushed result back to Stack.")
        print(">>>> Top of Stack is now " + str(self.stack.peek()) + ".")

    def iushr(self):
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        if var1 >= 0:
            self.stack.push(var1 >> var2)
        else:
            self.stack.push((var1 + 0x10000000) >> var2)

    def ixor(self):
        variable2 = self.stack.pop()
        variable1 = self.stack.pop()
        self.stack.push(variable1 ^ variable2)
        print("ran ixor")

            # Array of arguments from the main for istore and iload
    switcher = {

            "iadd": iadd,  # add two ints
            "iand": iand,  # perform a bitwise AND on two integers
            "iconst_m1": iconst_m1,  # load the int value -1 onto the stack
            "iconst_0": iconst_0,  # load the int value 0 onto the stack
            "iconst_1": iconst_1,  # load the int value 1 onto the stack
            "iconst_2": iconst_2,  # load the int value 2 onto the stack
            "iconst_3": iconst_3,  # load the int value 3 onto the stack
            "iconst_4": iconst_4,  # load the int value 4 onto the stack
            "iconst_5": iconst_5,  # load the int value 5 onto the stack
            "idiv": idiv,  # divide two integers
            "iinc": iinc,  # increment local variable #index by signed byte const
            "iload_0": iload_0,  # load an int value from local array variable[0]
            "iload_1": iload_1,  # load an int value from local array variable[1]
            "iload_2": iload_2,  # load an int value from local variable[2]
            "iload_3": iload_3,  # load an int value from local variable[3]
            "imul": imul,  # multiply two integers
            "ineg": ineg,  # negate int
            "ior": ior,  # bitwise int OR
            "irem": irem,  # logical in remainder
            "ishl": ishl,  # int shift left
            "ishr": ishr,  # int arithmetic shift right
            "istore": istore_3,  # store int value into variable #index
            "istore_0": istore_0,  # store int value into VARIABLE[0]
            "istore_1": istore_1,  # store int value into VARIABLE[1]
            "istore_2": istore_2,  # store int value into VARIABLE[2]
            "istore_3": istore_3,  # store int value into VARIABLE[3]
            "isub": isub,  # int subtract
            "iushr": iushr,  # int logical shift right
            "ixor": ixor  # xor
    }
    def token_dict(self, argument):
        # get function from spinner
        method = OpCodeMethods.switcher.get(argument, "invalid")
        # execute function
        return method(self)
