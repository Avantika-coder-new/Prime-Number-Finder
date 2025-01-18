{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def check_prime_or_composite(number):\
    if number <= 1:\
        return f"\{number\} is neither prime nor composite."\
    elif number == 2:\
        return f"\{number\} is a prime number."\
    \
    for i in range(2, int(number ** 0.5) + 1):\
        if number % i == 0:\
            return f"\{number\} is a composite number."\
    return f"\{number\} is a prime number."\
\
# Input from the user\
num = int(input("Enter a number: "))\
result = check_prime_or_composite(num)\
print(result)\
}