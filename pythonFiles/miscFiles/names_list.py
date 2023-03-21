from pathlib import Path

# name1 = input("Type a name: ")
# name2 = input("Type a name: ")

def findUser():
    File = Path('iPadAssets', 'nameAndPass.txt')
    FileRead = File.read_text

    findName = input('Choose a name: ')
    with open(File) as FileRead:
        for i, line in enumerate(FileRead):
            if findName in line:
                print('James found at: ' + str(i))
                findUser()
            else:
                print('Name not found!!')
                findUser()
findUser()
