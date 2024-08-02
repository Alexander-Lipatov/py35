import pickle

def load(data: dict):
  with open('data.pickle', 'rb') as f:
    rf:dict = pickle.load(f)
    for key, val in rf.items():
      data[key]=val
 


def save(data):
  with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)