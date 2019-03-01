# """import the unittest"""
# import unittest
"""Read bit stream."""
from bitstring import ConstBitStream
import jvpm_dict    # import external opcode dictionary
import jvpm_methods # import external method dictionary
from methods import Methods
method_call = Methods()

# pylint: disable = W0105, C0122, R0903

# **************************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("\nMagic: ", magic)
        return magic

    def get_minor(self):
        print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        print("Contant Pool Count: ", self.data[8] + self.data[9] - 1)
        return self.data[8] + self.data[9]

# **************************************************************************************************

class OpCodes():
    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods"""
    def __init__(self):
        # List of the test1.java(math) opcodes.
#         self.opcodes = ['04', '3c', '05', '3d', '1b', '1c', '60', '1c', '68', '1c', '6c', '1c',
#                         '64', '3e']
        self.opcodes = ['06', '3c', '04', '3d', '1b', '1c', '82', '3e']
#        self.opcodes = ['06', '3c', '1b', '74', '3e']

        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """

    def dict_search(self):
        """Search the jvpm.dict.py(dictionary) file for the bytecode/opcode translation and
        implement if found."""
	# Hex to Opcode from imported opcode dictionary - jvpm_dict,
        # implemented using imported method dictionary - jvpm_methods.
        print("\nBytecodes from the .class file: " + str(self.opcodes))
        index = 0
        while index < len(self.opcodes):
            opcall = jvpm_methods.opcode_methods(self.opcodes[index])
            #print("Bytecode " + self.opcodes[index] + ' = Opcode: ' + opcall)
            opcall
            index += 1
        print()
        
        # Call methods from Methods() class in methods.py
        print("\nBytecodes from .class file: " + str(self.opcodes))
        index = 0
        while index < len(self.opcodes):
            opcall = jvpm_dict.get_opcode(self.opcodes[index])
            print("Bytecode " + self.opcodes[index] + ' = Opcode: ' + opcall)
            jvpm_methods.opcode_methods(opcall)
            # Im able to call the method in Methods() class in methods.py using the opcade name
            method_call.iconst_3()
            # but when I try to call opcall it fails, even though opcall = iconst_1.
            # method_call.opcall()
            index += 1
        print()
        # return

# **************************************************************************************************

if '__main__' == __name__:

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    D = HeaderClass()
    D.get_magic()
    D.get_minor()
    D.get_major()
    D.get_const_pool_count()

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'
          '\n  imported method dictionary to implement the method:___')
    Z = OpCodes()
    Z.dict_search()

# **************************************************************************************************

# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm_opcodes.py
# We have a warning about an unclosed file but no errors.

# class UnittestHeader(unittest.TestCase):
#     """unittest to test method outputs"""
#     def setUp(self):
#         """instantiate an instance of HeaderClass"""
#         self.test = HeaderClass()

#     def test_magic(self):
#         """method to test the pull_magic output"""
#         self.test.pull_magic()
#         """the comparison"""
#         self.assertEqual(self.test.header_magic, 'cafebabe')
#         print('<<<< passed header_magic, ' + self.test.header_magic + ' = cafebabe >>>>\n')

#     def test_minor(self):
#         """method to test the pull_minor output"""
#         known_minor = 0
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         """the comparison"""
#         self.assertEqual(self.test.header_minor, 0)
#         print(f'<<<< passed header_minor, {self.test.header_minor} = {known_minor} >>>>\n')

#     def test_major(self):
#         """method to test the pull_major output"""
#         known_major = 54
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         self.test.pull_major()
#         """the comparison"""
#         self.assertEqual(self.test.header_major, 54)
#         print(f'<<<< passed header_major, {self.test.header_major} = {known_major} >>>>\n')

#     def test_pool_count(self):
#         """method to test the pull_const_pool_count output"""
#         known_pool_count = 14
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         self.test.pull_major()
#         self.test.pull_const_pool_count()
#         """the comparison"""
#         self.assertEqual(self.test.header_const_pool_count, 14)
#         print(f'< passed poolCount, {self.test.header_const_pool_count} = {known_pool_count} >\n')

# **************************************************************************************************
