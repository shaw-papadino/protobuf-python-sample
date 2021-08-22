from proto.addressbook_pb2 import Person

import argparse


def deserialize(binary):
    person = Person()
    person.ParseFromString(binary)
    return person

if __name__ == "__main__":
    # TODO: 本当はargparseとかでdeserializeするbinaryを入力できるようにしたい
    binary = b'\n\x04Jhon\x10\xd2\t\x1a\x10jhon@example.com'
    print(deserialize(binary))
