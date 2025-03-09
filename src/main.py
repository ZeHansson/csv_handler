def main():

    print("Hello World!")

def read_data(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def write_data(path, data):
    with open(path, "a") as f:
        f.write(data)
        f.close()