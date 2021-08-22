from proto.addressbook_pb2 import Person

import argparse

def serialize(id = 1234, name = "Jhon", email = "jhon@example.com"):

    person = Person()
    person.id = id
    person.name = name
    person.email = email

    return person.SerializeToString()

def serialize_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="Person's id", type=int, default=1234)
    parser.add_argument("-n", "--name", help="Person's name", default="Jhon")
    parser.add_argument("-e", "--email", help="Person's email", default="jhon@example.com")

    return parser

if __name__ == "__main__":

    args = serialize_parser().parse_args()
    print(serialize(args.id, args.name, args.email))
