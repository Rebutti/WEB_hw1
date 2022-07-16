import json
import pickle
from abc import abstractmethod, ABCMeta


class AbstractForFiles(metaclass=ABCMeta):
    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def read(self):
        pass


class ForJson(AbstractForFiles):
    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename

    def dump(self, data):
        with open(self.filename, "w") as write_file:
            json.dump(data, write_file)

    def read(self):
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)
        return data


class ForBin(AbstractForFiles):
    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename

    def dump(self, data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)

    def read(self):
        with open('data.pickle', 'rb') as f:
            data_new = pickle.load(f)
        return data_new


if __name__ == "__main__":
    data1 = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    c = ForJson('test.json')
    c.dump(data1)
    new_data = c.read()
    print(new_data)
    # -----------------------------------
    data2 = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
    }
    c = ForBin('test.bin')
    c.dump(data2)
    new_data = c.read()
    print(new_data)
