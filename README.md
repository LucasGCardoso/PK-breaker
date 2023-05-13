# PK-breaker
In cryptography, it is known that the basics of the [RSA system](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) requires a secret key (SK) and public key (PK), in order to perform the necessary cryptography steps, which involves the PK exchange between the two communicators, in order to cypher the message. The PK is basically a very big number that is also a multiplication of two prime numbers (P and Q), while the SK is composed by these two prime numbers P and Q, and some other information as well.

So, if we were to break a PK and discover the SK (the two prime numbers that factor the PK), we would need to factor this number and discover two primes that multiplied result in the PK. In the real world, it is only safe to share the PK with other people because of the mathematical complexity of this operation, since we use very big numbers (around 2048 bits or even more!) as mentioned before.

Despite that, it does not stop us from making a very dummy PK breaker algorithm, which consists in basically trying to factor the passed number, using some basic math and the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#:~:text=In%20mathematics%2C%20the%20Euclidean%20algorithm,them%20both%20without%20a%20remainder.).

This project was made just for fun and for learning purposes as well. Please feel free to test it out. Just remember using some very small numbers, since complexity will easily grow.
