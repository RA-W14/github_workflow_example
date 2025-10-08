from main import *

def test():
    assert add(3, 2) == 5
    assert subtract(3, 5) == -2

def main():
    test()

if __name__ == '__main__':
    main() 