# caesarHacker

In cryptography, a Caesar cipher (AKA shift cipher) is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
Deciphering (decryption) is not that hard. Since there are only a limited number of possible shifts (26 in English), they can each be tested in turn in a brute force attack. This is what this tool does. In addition, this smart tool can predict which of the 26 possible plain texts is the correct one. This is done simply by comparing the decrypted words with english words stored in 'words.txt' file. If the decrypted text seems to be valid english, there is big probability this is the right plain text. At the end, the predicted plain sentence, or word, will be displayed.

![capture](https://cloud.githubusercontent.com/assets/9033365/25820011/768b3f1e-3438-11e7-88e8-0cf13a31cc8d.PNG)
