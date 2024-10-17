class Files():
    def save_to_file(filename, text):
        open(filename, 'w').write(text)

    def read_from_file(filename):
        print(open(filename).read())




# def save_to_file(filename, text):
#     open(filename, 'w').write(text)

# def read_from_file(filename):
#     print(open(filename).read())
