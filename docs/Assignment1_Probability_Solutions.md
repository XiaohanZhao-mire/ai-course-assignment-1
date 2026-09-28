# Assignment 1 - Probability Solutions

All calculations use the values in Assignment1-1.pdf. Probabilities are exact
until the final rounding step. Entropy is measured in bits using log base 2.

## Question 1 - Independent events

Given P(A) = 0.4 and P(B) = 0.3, with A and B independent:

**(a) Intersection**

P(A ∩ B) = P(A)P(B) = 0.4 × 0.3 = **0.12**.

**(b) Union**

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
= 0.4 + 0.3 − 0.12 = **0.58**.

The intersection is subtracted because it is counted in both P(A) and P(B).

## Question 2 - Testing independence

Given P(A) = 0.5, P(B) = 0.4, and P(A | B) = 0.7.

For independence, P(A | B) must equal P(A) when P(B) > 0.
Here 0.7 ≠ 0.5, so **A and B are not independent**.

Equivalently, P(A ∩ B) = P(A | B)P(B) = 0.7 × 0.4 = 0.28,
whereas P(A)P(B) = 0.5 × 0.4 = 0.20. These differ.

## Question 3 - Bayes' rule

Given P(A) = 0.6, P(B | A) = 0.5, and P(B | Aᶜ) = 0.2.

P(Aᶜ) = 1 − 0.6 = 0.4.

By total probability:

P(B) = P(B | A)P(A) + P(B | Aᶜ)P(Aᶜ)
= 0.5 × 0.6 + 0.2 × 0.4 = 0.30 + 0.08 = 0.38.

By Bayes' rule:

P(A | B) = P(B | A)P(A) / P(B)
= 0.30 / 0.38 = 15/19 ≈ **0.78947 (78.95%)**.

## Question 4 - Disease given a positive test

Let D mean having the disease and + mean a positive test.

P(D) = 0.02; P(Dᶜ) = 0.98; P(+ | D) = 0.95.
The true negative rate is 0.90, so P(+ | Dᶜ) = 1 − 0.90 = 0.10.

P(+) = P(+ | D)P(D) + P(+ | Dᶜ)P(Dᶜ)
= 0.95 × 0.02 + 0.10 × 0.98 = 0.019 + 0.098 = 0.117.

P(D | +) = P(+ | D)P(D) / P(+)
= 0.019 / 0.117 = 19/117 ≈ **0.16239 (16.24%)**.

For example, among 10,000 people at these rates, 200 have the disease and
190 of them test positive. Of the 9,800 healthy people, 980 test positive.
Therefore, 190 / (190 + 980) = 16.24% of positive tests come from people with
the disease. The low prior prevalence explains this result.

## Question 5 - Expected value, variance, and sample mean

| x | P(X = x) | x P(X = x) | x² P(X = x) |
|---|---|---|---|
| 85 | 0.375 | 31.875 | 2709.375 |
| 90 | 0.375 | 33.750 | 3037.500 |
| 95 | 0.125 | 11.875 | 1128.125 |
| 100 | 0.125 | 12.500 | 1250.000 |
| Total | 1.000 | 90.000 | 8125.000 |

**(a)** E[X] = Σ x P(X = x)
= 31.875 + 33.750 + 11.875 + 12.500 = **90 points**.

**(b)** E[X²] = 8125.

Var(X) = E[X²] − (E[X])² = 8125 − 90² = 8125 − 8100
= **25 points²**.

**(c)** The sample is {85, 90, 85, 95, 90, 85, 100, 90}.

Sample mean = (85 + 90 + 85 + 95 + 90 + 85 + 100 + 90) / 8
= 720 / 8 = **90 points**.

The sample mean equals E[X] here because the observed frequencies are
3/8, 3/8, 1/8, and 1/8, exactly matching the given probabilities. A different
random sample need not have a mean exactly equal to E[X].

## Question 6 - Entropy

**(a)** For probabilities 0.4, 0.3, 0.2, and 0.1:

H(X) = −Σ p(x) log₂ p(x)
= −[0.4 log₂(0.4) + 0.3 log₂(0.3) + 0.2 log₂(0.2) + 0.1 log₂(0.1)]
= 0.528771 + 0.521090 + 0.464386 + 0.332193
≈ **1.84644 bits**.

**(b)** With four equally likely messages, each probability is 1/4:

H(X) = −4 × (1/4) × log₂(1/4) = −1 × (−2) = **2 bits**.

The uniform distribution has the maximum entropy for four possible messages.
