import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--arg', type=str, dest="ArgArg", default=" ")
parser.add_argument('--task', type=str, dest="ArgTask", default=" ")
args = parser.parse_args()

def vowels(text):
    i = 0
    for letter in text:
        if letter in "aeiouyAEIOUY":
            i = i + 1
    return i


perfect_list = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289,
                324, 343, 361, 400, 441, 484, 512, 529, 576,
                625, 676, 729, 784, 841, 900, 961, 1000, 1024, 1089, 1156, 1225, 1296, 1331, 1369, 1444, 1521, 1600,
                2197, 2209, 2304, 2401, 2500, 2601, 2704,
                2744, 2809, 2916, 3025, 3125, 3136, 3249, 3364, 3375, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356,
                4489, 4624, 4761, 4900, 4913, 5041, 5184,
                5329, 5476, 5625, 5776, 5832, 5929, 6084, 6241, 6400]


def perfect(place):
    return perfect_list[place - 1]



def lazy(n):
    return int(((n-1)**2 + n+1)/2)


if args.ArgTask == "vowels":
    text = args.ArgArg
    print(vowels(text))
elif args.ArgTask == "perfect":
    place = int(args.ArgArg)
    print(perfect(place))
elif args.ArgTask == "lazy":
    num = int(args.ArgArg)
    print(lazy(num))
else:
    print("wrong input, try again please")