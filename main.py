from serialize import serialize
from deserialize import deserialize

if __name__ == "__main__":
    binary = serialize()
    print(f"done serialize: {binary}\n")
    person = deserialize(binary)
    print(f"done deserialize:\n{deserialize(binary)}")

