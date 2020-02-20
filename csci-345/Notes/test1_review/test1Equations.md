## Information Entropy

E = Σ<sub>i=1</sub><sup>n</sup> P<sub>i</sub> * lob<sub>2</sub>(P<sub>i</sub>)

<br/>

---

## Diffie-Hellman key exchange
- Turing award winners, 2015
- intruduced the idea of a "common paint"
- *The "Common Paint" concept*


Assume *g*, *p* are known publicly
|Alice| |Bob|
|-|-|-|
|a, g, p | | b |
|A = g<sup>a</sup> `mod` p | ─<sup>1</sup>[ g, p, A ]─> | B = g<sup>b</sup> `mod` p
| | | |
| K = B<sup>a</sup> `mod` p | <─<sup>2</sup>[ B ]─ | K = A<sup>b</sup> `mod` p

K = A<sup>b</sup> mod p = (g<sup>a</sup> mod p )<sup>b</sup> mod p = g <sup>ab</sup> mod p = (g<sup>b</sup>

*Variable names*
- g ─ "generator" - prime number
- p ─ also a prime number
- A ─ Alice's message to Bob
- B - Bob's message to Alice

***Prime numbers make the best keys.***

<br/>

---

## RSA