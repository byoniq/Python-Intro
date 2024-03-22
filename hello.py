# def askForName():
#     name = input("whats your name? ")
#     print(f'hello, {name}')

# askForName()


# #prompt is going to be a parameter - local variable - used in the scope of the function
# #scope is everything tabbed over / indented 

# def askForName(prompt):
#     name = input(prompt)
#     print(f'hello, {name}')

# #argument: this is the data passed into our function
# askForName("What's your name? ")


# # list comprehensions

# nums = [i for i in range(10)]
# squares = [i**2 for i in range(10)]

# print(nums)
# print(squares)

# #not pythonic way 
# nums = [0,1,2,3,4,5,6,7,8,9]

# #pythonic way 
# nums_2 = list(range(10))

# company_pay_structure = [

# ("Jim", 50_000), ("Jane", 65_000),

# ("Julieanne", 105_000), ("Jake", 110_000)

# ]

# hundred_k_club = [x for x,y in company_pay_structure if y >= 100_000]

# print(hundred_k_club)


#One Liners 
#Sum of all prime numbers less than 50.
print(sum(n for n in range(2, 50) if all(n % m != 0 for m in range(2, int(n**0.5) + 1))))

print(sum(x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))))

print(sum(filter(lambda x: all(x % y != 0 for y in range(2, int(x**0.5) + 1)), range(2, 50))))

print(sum(x for x in range(2, 50) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))))

#Reverse word order in a sentence.

sentence = input("Enter a sentence: ")

print(" ".join(sentence.split()[::-1]))
print(' '.join(reversed(sentence.split())))
#print(' '.join(input().split()[::-1]))
print(" ".join(sentence.split()[::-1]))

#Word frequency count in text.
text = "The sky above the port was the color of television, tuned to a dead channel.Its not like Im using, Case heard someone say, as he shouldered his way through the crowd around the door of the Chat. Its like my bodys developed this massive drug deficiency. It was a Sprawl voice and a Sprawl joke. The Chatsubo was a bar for professional expatriates; you could drink there for a week and never hear two words in Japanese. Ratz was tending bar, his prosthetic arm jerking monotonously as he filled a tray of glasses with draft Kirin. He saw Case and smiled, his teeth a webwork of East European steel and brown decay. Case found a place at the bar, between the unlikely tan on one of Lonny Zones whores and the crisp naval uniform of a tall African whose cheekbones were ridged with precise rows of tribal scars."

high_value_words = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

print(high_value_words)