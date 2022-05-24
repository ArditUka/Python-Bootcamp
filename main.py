import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+."


string = lower + upper + numbers + symbols
length = int(input("Sa karaktere deshironi qe passwordi juaj ti posedoj: "))
password = "".join(random.sample(string, length))

print("Passwordi i gjeneruar:", password)