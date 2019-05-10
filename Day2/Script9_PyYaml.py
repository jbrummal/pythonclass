#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

import yaml


# --Functions
def main():


    """This is the runtime code"""
    hitchiker = [{"name": "Zaphod Beeblebrok", "species": "Betelgeusian"},
                 {"name": "Arthur Dent", "species": "Human"}]
    print(hitchiker)

#    print(yaml.dump(hitchiker))

    with open('yamlout.yml', 'w') as outfile:
#       outfile.write(yaml.dump(hitchiker))
        yaml.dump(hitchiker,outfile)

    return


# --Run main
main()