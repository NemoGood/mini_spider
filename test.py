import argparse
#test
parser = argparse.ArgumentParser()
parser.add_argument('-c','--filename',help="the file of the conf")
args = parser.parse_args()
argfile = args.filename
print(argfile)