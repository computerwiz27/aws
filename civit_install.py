#!/usr/bin/python

import os
import sys

def download(file, destination=""):
    lines = file.readlines()
    for i, line in enumerate(lines):
        args = line.split(",")
        args[1] = args[1].replace(" ","")

        if len(args) > 3 or len(args) < 2:
            print("Line {} is not properly formated".format(i+1))
            continue
        
        path = destination + args[0] + ".safetensors"
        os.system("cd {}".format(destination))
        os.system('wget -bqO "{}" {} > /dev/null'.format(args[0], args[1]))

if len(sys.argv) != 2:
    print("Please provide stable diffusion path")
    exit()

loraf = open("lora.txt")
loraPath = sys.argv[1] + "/models/Lora"
download(loraf, loraPath)

checkpointsf = open("checkpoints.txt")
ckpntPath = sys.argv[1] + "/models/Stable-diffusion"
download(checkpointsf, ckpntPath)
