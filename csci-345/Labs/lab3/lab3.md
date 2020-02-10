# Lab 3

## Part 1 - Simple Cipher Attack

1. 1-20-20-1-3-11 1-20 4-1-23-14 23-9-20-8 4-18-15-14-5-19

   - **Type:** Letter-Numbers

   - **Message:** ATTACK AT DAWN WITH DRONES

2. y. Tshoem eE yteo obfe Pervoivdiednecnec eo,f oar ctohnes pailrla-csye eiinnvgo levyien go ft hGeo df,o usnedeenr sh eorfe tohne tUhnei tUeSd $S1t abtielsl ,a nhda st hbee eInl ltuamkienna tbi

   - **Type:** Railfence, or Rotate, depending on parameters

     - We tried different trategies for this one. We noticed that we could take one alternate the letters and end up with two halves of the whole message, but some words were still scrambled.

     - After some fiddling, and looking it up, we found both Railfence and Rotate work, with two columns, rotated left/shift of 2.
     
   - **Message:** The Eye of Providence, or the all-seeing eye of God, on the US bill, has been taken by some to be evidence of a conspiracy involving the founders of the United States and the Illuminati.

3. .--. .-.. . .-... . / .-.. . -/ -.... . / --.-..-. . -. / -.--. ---.--/ -.... .--/ .. / .--.. .-.. .-.. / -.-. .-.-. .-. -.--/ ---..--/ -.... . / --.. ... ... .. ----. / .--.-. -.-. ---.-. -.. ..-. --. / ----/ .... . .-. / .--.. ... .... .-.-.-/ .... . .-. / ..-. .-.. -.... ..-. ..-.-.. / ... . .-. ...-.--. ---..--/ -..-
   - **Type:** Morse Code

   - **Message:** PLEASE LET THE QUEEN KNOW THAT I WILL CARRY OUT THE MISSION ACCORDING TO HER WISH, HER FAITHFUL SERVANT, X

4. QW4gdW5pZGVudGlmaWVkIGZseWluZyBvYmplY3Qgb3IgVUZPLCBpcyBkZWZpb mVkIGFzIGEgcGV yY2VpdmVkIG9iamVjdCBpbiB0aGUgc2t5LCBub3QgaWRlbnRpZ mlhYmxlIGJ5IHN0YW5kYXJkIGNyaXRlcmlhLiBNb3N0IFVGT3MgYXJlIGxhdGV yI GlkZW50aWZpZWQgYXMgY29udmVudGlvbmFsIG9iamVjdHMgb3IgcGhlbm9tZW5 hLiBUaGUgdGVybSBpcyB3aWRlbHkgdXNlZCBmb3IgY2xhaW1lZCBvYnNlcnZhdGl vbnMgb2YgZXh0cmF0ZXJyZXN0cmlhbCBjcmFmdC4= 

   - **Type:** Base64

   - **Message:** An unidentified flying object or UFO, is defined as a perceived object in the sky, not identifiable by standard criteria. Most UFOs are later identified as conventional objects or phenomena. The term is widely used for claimed observations of extraterrestrial craft.

5. Tn'tnhteotrdn a kr iur&nbsp; evoero yact lseen n, ncciaraaeefmo urZcpre 0s e7 sh sh.ahpweernoee mhhy ttleftg

   - **Type:** Ubchi 14325. Took a lot of guessing.

     - We knew that it used this cipher because it had a Z in it, and found this cipher would put a Z in a speudo-random spot in the ciphered text.

     - The only other capital letter was T, at the beginning, so the first value would have to be 1.

     - One of the most common words in the english alphabet is "the" so we attempted to force the first word in the cipher to be "The". After that, we just got lucky, and 14325 happened to work.

     - The only "word" we could come up with that matches that pattern was "Profx"
     
   - **Message:** The oceans cover more than 70 percent of the earth's surface, yet their depths remain largely unknown.

## Part 2: AES, RSA practice

