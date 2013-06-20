import os
import pickle
def cache (x,f) :

    filename = "data/%s.pkl" % x

    if not os.path.exists("data"):
        os.makedirs("data")
    if (os.path.exists(filename)):
        pkl_file = open(filename, 'rb')
        data = pickle.load(pkl_file)
        return data
    else:
        output = open(filename, 'wb')
        data = f()
        pickle.dump(data, output)
        return data
