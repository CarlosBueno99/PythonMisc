import sys


if sys.argv[2].lower()=="lower":
    print(sys.argv[1].lower())
elif sys.argv[2].lower()=="uppercase":
    print(sys.argv[1].upper())
elif sys.argv[2].lower()=="title":
    print(sys.argv[1].title())