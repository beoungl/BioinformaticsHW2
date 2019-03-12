# BioinformaticsHW2
# BioinformaticsHW2

For the Happy -> Sad -> Happy -> Sad -> Happy -> Sad -> Happy, run the file named hw3.py.

Click edit to read through README.md more easily.

Handsimulation

Given, 

P(Sunny) = 2/3
P(Rainy) = 1/3
P(Sunny|Sunny) = 0.8
P(Rainy|Sunny) = 0.2
P(Sunny|Rainy) = 0.4
P(Rainy|Rainy) = 0.6
P(Happy|Sunny) = 0.8
P(Sad|Sunny) = 0.2
P(Happy|Rainy) = 0.4
P(Sad|Rainy) = 0.6

1) Hand-simulate, given Happy  -> Sad, which weather was most likely?

Calculate the possibility of

Sunny -> Sunny, Sunny -> Rainy, Rainy -> Sunny, Rainy -> Rainy

a) Sunny -> Sunny

Sunny(2/3) -> Sunny(0.8)
    |             |
Happy(0.8)    Sad(0.2)

= 0.0853

b) Sunny -> Rain

Sunny(2/3) -> Rainy(0.2)
    |             |
Happy(0.8)    Sad(0.6)

= 0.064

c) Rainy -> Sunny

Rainy(1/3) -> Sunny(0.4)
    |             |
Happy(0.4)    Sad(0.2)

= 0.011

d) Rainy -> Rainy

Rainy(1/3) -> Rainy(0.6)
    |             |
Happy(0.4)    Sad(0.6)

= 0.048

So the answer is Sunny -> Sunny

2) Given Happy -> Sad -> Happy, determine the most likely weather.

Using Viterbi algorithm, pick the maximum from the previous probability, 0.0853(Sunny -> Sunny). So possibilities are

Sunny -> Sunny -> Sunny, or Sunny -> Sunny -> Rainy

a) Sunny -> Sunny -> Sunny
Sunny(2/3) -> Sunny(0.8) -> Sunny(0.8)
    |             |             |
Happy(0.8)    Sad(0.2)      Happy(0.8)

= 0.0546

b) Sunny -> Sunny -> Rainy

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2)
    |             |             |
Happy(0.8)    Sad(0.2)      Happy(0.4)

= 0.00682

3) Given Happy -> Happy -> Sad -> Sad -> Sad -> Happy, determine the most liekly weather.

Start with Happy -> Happy

a)
Sunny -> Sunny

Sunny(2/3) -> Sunny(0.8)
    |             |
Happy(0.8)    Happy(0.8)

= 0.341

Sunny -> Rain

Sunny(2/3) -> Rainy(0.2)
    |             |
Happy(0.8)    Happy(0.4)

= 0.0427

Rainy -> Sunny

Rainy(1/3) -> Sunny(0.4)
    |             |
Happy(0.4)    Happy(0.8)

= 0.0427

Rainy -> Rainy

Rainy(1/3) -> Rainy(0.6)
    |             |
Happy(0.4)    Happy(0.4)

= 0.032

b) Use Sunny -> Sunny based on Viterbi algorithm

b1)
Sunny -> Sunny -> Sunny -> Sunny

Sunny(2/3) -> Sunny(0.8) -> Sunny(0.8) -> Sunny(0.8)
    |             |            |            |
Happy(0.8)    Happy(0.8)    Sad(0.2)      Sad(0.2)

= 0.0087

b2)
Sunny -> Sunny -> Rainy -> Rainy

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Rainy(0.6)
    |             |            |            |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.6)

= 0.0147

b3) Use Sunny -> Sunny -> Sunny -> Rainy

Sunny(2/3) -> Sunny(0.8) -> Sunny(0.8) -> Rainy(0.2)
    |             |            |            |
Happy(0.8)    Happy(0.8)    Sad(0.2)      Sad(0.6)

= 0.00655

b4) Use Sunny -> Sunny -> Rainy -> Sunny

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Sunny(0.4)
    |             |            |            |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.2)

= 0.00328

c) Start from Sunny -> Sunny -> Rainy -> Rainy

c1) Sunny -> Sunny -> Rainy -> Rainy -> Rainy - > Rainy

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Rainy(0.6) -> Rainy(0.6) -> Rainy(0.6)
    |             |            |            |              |              |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.6)      Sad(0.6)      Happy(0.4)

= 0.00127

c2) Sunny -> Sunny -> Rainy -> Rainy -> Rainy - > Sunny

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Rainy(0.6) -> Rainy(0.6) -> Sunny(0.4)
    |             |            |            |              |              |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.6)      Sad(0.6)      Happy(0.8)

= 0.00169

c3) Sunny -> Sunny -> Rainy -> Rainy -> Sunny - > Rainy

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Rainy(0.6) -> Sunny(0.4) -> Rainy(0.2)
    |             |            |            |              |              |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.6)      Sad(0.2)      Happy(0.4)

= 0.000094

c4) Sunny -> Sunny -> Rainy -> Rainy -> Sunny - > Sunny

Sunny(2/3) -> Sunny(0.8) -> Rainy(0.2) -> Rainy(0.6) -> Sunny(0.4) -> Rainy(0.2)
    |             |            |            |              |              |
Happy(0.8)    Happy(0.8)    Sad(0.6)      Sad(0.6)      Sad(0.2)      Happy(0.4)

= 0.000094

Based on this, the most likely weather is

Sunny -> Sunny -> Rainy -> Rainy -> Rainy -> Sunny with 0.0169 probability.
