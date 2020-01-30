import pickle

#类和实例


class Record:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


R = pickle.dumps(Record)
print(R)
print(pickle.loads(R))

record = Record("贾敏强", "15801396646")
r = pickle.dumps(record)
print(r)
print(pickle.loads(r))
