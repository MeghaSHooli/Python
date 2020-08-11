
from datetime import datetime, timedelta
import sys

__author__ = 'mhooli'
__version__ = '1.0'


def text_parser(filepath, separator="="):
    """
     :text_parser:

    """
    return_dict = {}
    with open(filepath, "r") as f:
                for line in f:
                    if separator in line:
                        key, value = line.split(separator)
                        return_dict[key.strip()] = value.strip()
                    else:
                        pass
                f.close()
    return return_dict

text_parser_dictionary = text_parser("Read_maint")

happy = text_parser_dictionary['happy']
sad = text_parser_dictionary['sad']

print(happy)
print(sad)

#if line.startswith('#'):
#   continue
