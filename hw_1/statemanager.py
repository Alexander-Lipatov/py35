import pickle

def load_old(data):
  '''
  data is dict with filename keys 
  '''
  for el in data.keys():
    with open(el+'.pickle', 'rb') as f:
      data[el].extend(pickle.load(f))

def save_old(el, data):
  name = el.__class__.__name__.lower()
  with open(name+'s.pickle', 'wb') as f:
    pickle.dump(data[name+'s'], f)



def load() -> dict:
  with open('state.bin', 'rb') as f:
    return pickle.load(f)
  
def save(data: dict) -> None:
  with open('state.bin', 'wb') as f:
    pickle.dump(data, f)
