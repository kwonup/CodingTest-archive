import sys

def check_relation(a, b):
    if b % a == 0:
        return "factor"
    if a % b == 0:
        return "multiple"
    return "neither"

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        print(check_relation(a, b))

if __name__ == "__main__":
    main()