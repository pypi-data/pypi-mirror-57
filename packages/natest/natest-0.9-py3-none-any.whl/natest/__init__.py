#!/usr/bin/env python3
'''NaTest Ticktmaster Test validator for python3 code'''
from termcolor import colored

class NaTest():
    '''read:   read the input
       result: compare HAVE with WANT'''

    @staticmethod
    def read(my_input):
        '''read an input example (i.e. ssh show command) and return
           a list of splitlines() that can be use along the code.
           The input can be can be a str() varibale as well as a file
           (ideally under ./fixtures folder).'''

        input_list = list()

        for line in my_input:
            input_list.append(line)

        return input_list


    @staticmethod
    def result(want, have):
        '''WANT: pass the file name (under ./fitures) containing the desired output.
                 The file is converted in a list splitted by lines.
           HAVE: pass the return of your code. This can be a list of splitted lines
                 or a string (that will converted in a list of splitted lines)
        '''

        want_list = list()
        have_list = list()

        for line in want:
            want_list.append(line)

        if isinstance(have, list):
            have_list = have
        else:
            for line in have:
                have_list.append(line)

        want_diff = [diff for diff in want_list if diff not in have_list]
        have_diff = [diff for diff in have_list if diff not in want_list]

        return_want = list()
        return_have = list()

        if want_diff:
            color_w = 'yellow'
            for line in want_diff:
                return_want.append('+ {}'.format(str(line)))
        else:
            color_w = 'green'

        if have_diff:
            color_h = 'red'
            for line in have_diff:
                return_have.append('- {}'.format(str(line)))
        else:
            color_h = 'green'


        return colored(return_want, color_w) + '\n' + colored(return_have, color_h)

# f20191216
