from collections import Counter
if __name__ == '__main__':
    countries = set()
    x = int(input())
    for i in range(0,x):
        countries.add(input())
    a = sum(Counter(countries).values())
    print(a)
