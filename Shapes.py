# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

def main():
    pass

import math

class Circle (object):

    @property
    def radius(self):
        pass

    @radius.setter
    def radius (self, radius):
        self.__radius = radius

    @property
    def area(self):
        return self.__radius**2 *math.pi






if __name__ == '__main__':
    main()