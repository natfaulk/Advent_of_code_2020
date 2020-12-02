import os

BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
INPUT_PATH = os.path.join(BASE_PATH, 'inputs')

def loadIn(_file):
  with open(os.path.join(INPUT_PATH, _file)) as f:
    data=f.readlines()
    return data