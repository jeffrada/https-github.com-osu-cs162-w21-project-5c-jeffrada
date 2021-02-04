# Author: Adam Jeffries
# Date: 2/3/2021
# Description: Reads a JSON file and writes data text to a file in CSV format.

import json

class SatData:

    def __init__(self):
        with open('sat.json', 'r') as infile:
            self.restored_list = json.load(infile)

    def save_as_csv(self, dbn_list):
        output_file = open('output.txt', 'w')
        output_file.write(self.restored_list["meta"]["view"]["columns"][8]["name"])
        output_file.write(",{}".format(self.restored_list["meta"]["view"]["columns"][9]["name"]))
        output_file.write(",{}".format(self.restored_list["meta"]["view"]["columns"][10]["name"]))
        output_file.write(",{}".format(self.restored_list["meta"]["view"]["columns"][11]["name"]))
        output_file.write(",{}".format(self.restored_list["meta"]["view"]["columns"][12]["name"]))
        output_file.write(",{}".format(self.restored_list["meta"]["view"]["columns"][13]["name"]))
        output_file.write("\n")
        for dbn in dbn_list:
            for item in self.restored_list["data"]:
                if dbn == item[8]:
                    print(item)
                    line_to_write = "{},{},{},{},{},{}\n".format(item[8], item[9], item[10], item[11], item[12], item[13])
                    output_file.write(line_to_write)
        output_file.close()
