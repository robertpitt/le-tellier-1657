# Le Tellier to the Marquis de Castelnau, 12 May 1657

## Substantial partial decipherment — not a complete or manuscript-verified solution

Analysis date: 14 September 2026.

The ordered syllable assignments support a long, coherent French reading. The present result does **not** establish all the code entries or resolve all discrepancies in the published transcription. No person’s name has been inserted merely because it would fit the historical setting. No manuscript emendation has been silently applied.

This package preserves the input, the proposed key, every token-to-text alignment, and the remaining uncertainties. It is a reproducible working result, not a claim of publication priority or a finished scholarly edition.

## 1. Source and scope

The input is the 202-token transcription published by Satoshi Tomokiyo on Cryptiana on 20 October 2025. The post identifies a letter from Le Tellier to the Marquis de Castelnau dated 12 May 1657. Tomokiyo’s comment dated 7 December 2025 says that a photograph of the original was added and the transcription corrected. The displayed transcription checked during this attempt matches the supplied ciphertext file.

Source: https://cryptiana.blogspot.com/2025/10/an-undeciphered-letter-of-le-tellier-to.html

Related cipher survey, linked by the post: https://cryptiana.web.fc2.com/code/louisxiv0.htm

## 2. Readable reconstruction, with uncertainty retained

This is an **editorial reading of the encrypted passage**, not a literal transcription of the original French spelling. Punctuation, accents and word divisions are supplied. Bracketed material is unresolved or conjectural. In particular, `[donnera lieu ?]` and `[joindre ?]` are not exact outputs of the fixed key. The opening `71` and closing `72` are omitted from this reading for presentation only; their functions are not established, and both remain visible in the strict output.

> d’obliger, s’il est possible, les ennemis à ne point dégarnir Rocroi ni à faire monter les troupes que **[A : passage non résolu, se terminant par « Meuse »]**.
>
> Il faudra que vous régliez votre marche en sorte que vous donniez jalousie tant à Rocroi qu’aux places du Hainaut, et qu’en **[même ?]** temps que **[B : sujet non identifié]**, par la marche qu’il a ordre de faire, leur **[C : donnera lieu ?]** de craindre pour Rocroi, vous leur fassiez croire que la vôtre est pour l’y aller **[joindre ?] [D : fin non résolue]**.

The reading `même` comes from the single-occurrence hypothesis `"25 = MESME`; it is a persuasive contextual expansion, not an independently matched codebook entry.

### English rendering of the same partial reading

> …to oblige the enemy, if possible, not to strip Rocroi of its garrison or move up the troops that **[A: unresolved passage ending with “Meuse”]**.
>
> You must arrange your march so as to cause concern both for Rocroi and for the towns of Hainaut; and so that, at **[the same?]** time as **[B: unidentified subject]**, by the march he has orders to make, **[C: gives/will give them reason?]** to fear for Rocroi, you make them believe that your march is intended to go and **[join him there?] [D: unresolved ending]**.

This suggests a diversion or deception about the destination of Castelnau’s march. That is an interpretation of the partial reading, not independent historical corroboration. The name of the other marching party is not established.

## 3. Literal working output by token span

Upper case is used below for readability. Brackets represent unresolved source tokens, not plaintext. No missing letters have been supplied in these literal strings.

| Positions (1-based, inclusive) | Fixed-key output                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------------------- |
| 1                              | `[71: boundary or null hypothesis]`                                                             |
| 2–26                           | `DOBLIGERSILESPOSIBLELESENNEMISANEPOINT`                                                        |
| 27–52                          | `DEGARNIRROCROYNIAFAIREMONTERLESTROUPESQUE`                                                     |
| 53–69                          | `["48]A[~53]M[x-]LEESTRESEI[y-]RE[12]MEUSE`                                                     |
| 70–123                         | `ILFAUDRAQUEVOUSREGLIEZVOSTREMARCHEENSORTEQUEVOUSDONIEZJALOUSIETANTAROCROYQUAUXPLACESDUHAINAUT` |
| 124–133                        | `ETQUANMESMETEMPSQUE["40]`                                                                      |
| 134–161                        | `PARLAMARCHEQUILAORDREDEFAIRELEURDONE[2]MALIEU`                                                 |
| 162–194                        | `DECRAINDREPOURROCROYVOUSLEURFASIEZCROIREQUELAVOSTREESPOURLIALER`                               |
| 195–201                        | `JONNDRE[~42][~53]`                                                                             |
| 202                            | `[72: boundary or null hypothesis]`                                                             |

### Editorial changes in the readable reconstruction

* `ES` is read as *est* in two syntactically clear contexts; the T is supplied, not output by the current key. The same ES value is kept at the third occurrence in the unresolved Meuse span.
* `POSIBLE`, `DONIEZ`, `FASIEZ` and `ALER` are read as *possible*, *donniez*, *fassiez* and *aller*. The extra consonants are editorial restorations. Their absence does not by itself prove an error in the transcription.
* `VOSTRE`, `QUAN`, `LI` and candidate `MESME` are modernized as *votre/vôtre*, *qu’en*, *l’y* and *même*. The underlying literal output remains available.
* `ROCROY` is rendered as modern *Rocroi*. The current value Y for bare `33` is not distinguishable from I using these name occurrences alone.
* `JONNDRE` is **not** silently corrected in the literal output. *Joindre* is a flagged reconstruction.
* `DONE[2]MALIEU` is **not** silently changed to *donnera lieu*. That is a flagged reconstruction requiring an explanation of the inconsistent symbols.

## 4. Why the central reading is persuasive

### 4.1 Ordered syllable families

The main numerical blocks admit a five-vowel organization. Examples attested in the supplied transcription include:

| Family       | Working values in observed tokens                                                        |
| ------------ | ---------------------------------------------------------------------------------------- |
| Bare numbers | `47=DE`, `49=DO`, `50=DU`, `51=FA`, `56=GA`, `57=GE`, `61=HA`, `62=HE`, `66=JA`, `69=JO` |
| Tilde L row  | `~2=LA`, `~3=LE`, `~4=LI`; the separate source form `5~=LO` fits *jalousie*              |
| Tilde M row  | `~7=MA`, `~8=ME`, `~9=MI`, `~10=MO`                                                      |
| Tilde N row  | `~12=NA`, `~13=NE`, `~14=NI`                                                             |
| Tilde P row  | `~17=PA`, `~18=PE`, `~20=PO`                                                             |
| Tilde QU row | `~22=QUA`, `~23=QUE`, `~24=QUI`                                                          |
| Tilde R row  | `~27=RA`, `~28=RE`, `~30=RO`                                                             |
| Tilde S row  | `~33=SE`, `~34=SI`, `~35=SO`                                                             |
| Tilde T row  | `~37=TA`, `~38=TE`                                                                       |

The associated five-column extrapolation is saved separately in `syllabary_hypothesis.json`. **Unobserved cells are predictions of the structure, not recovered entries in a surviving key.** The observed-only working key does not depend on treating those predictions as attested. No extrapolation beyond `~41` is used to assign `~42` or `~53`.

### 4.2 A fixed value resolves two separated passages

Positions 76–86:

```text
"33   ~28  z-  ~4  c  31   "32     ~7  3  l  62
VOUS  RE   G   LI  E  Z    VOSTRE  MA  R  C  HE
```

This gives *vous régliez vostre marche*.

Positions 175–185:

```text
"33   q=  "14  51  ~34  h  31  m  ~30  ap  ~28
VOUS  L   EUR  FA  SI   E  Z   C  RO   I   RE
```

This gives the literal `VOUSLEURFASIEZCROIRE`, read as *vous leur fassiez croire*.

The value `31=Z` works in both. Earlier trial assignments `31=A` and `"14=ET` were rejected; they are not retained in the result key.

### 4.3 A continuous core

Positions **70–123** comprise **54 ciphertext tokens** and produce **93 letters** with the same fixed key:

```text
ilfaudraquevousregliezvostremarcheensortequevousdoniezjalousietantarocroyquauxplacesduhainaut
```

There are no unknown-token gaps in this core. The raw key output retains `DONIEZ` and `VOSTRE`; modern spelling is a separate editorial layer.

**Validation limit:** this is a reproducibility and cross-occurrence consistency check, not a prospectively held-out validation. The working key was developed using information from multiple parts of the letter. No synthetic round-trip or percentage score is presented as independent proof.

## 5. What remains unresolved

### A. The Meuse clause: positions 53–69

```text
"48 p ~53 J- x- ~3 "13 18 ~28 ~33 h- y- ~28 12 ~8 20 ~33
[?] A [?]  M [?] LE ES  T  RE  SE  I [?]  RE [?] ME U  SE
```

The unresolved values here are `"48`, `~53`, `x-`, `y-` and bare `12`. Several already assigned tokens also fail to form an unambiguous grammatical phrase in this span.

A contextual conjecture involving *assemble entre Sambre et Meuse* was considered. It is **not** a fixed-key decipherment of these tokens: it requires changes to otherwise assigned forms as well as new assignments. It is excluded from the accepted readable text and is not evidence that the source really contains *Sambre*.

### B. The subject at position 133

`"40` occurs once before *par la marche qu’il a ordre de faire*. A named commander is plausible, but a particular name has not been recovered. Turenne, La Ferté or any other historical candidate must not be inserted as a deciphered value without further evidence.

### C. The “donnera lieu” conjecture: positions 155–161

```text
49 ~13 2   ~7 ~4 h 20
DO NE [?] MA LI E U
```

The natural conjecture *donnera lieu* is not an exact result. In particular, `~7=MA` is supported by its two occurrences in *marche*, so it cannot silently become RA here. Nor has bare `2` been shown to be a null. One possible emendation would involve a missing digit in `~27`, but the manuscript image has not been inspected to test that possibility.

### D. The end: positions 195–202

```text
69 t t f ~28 ~42 ~53 72
JO N N D RE  [?] [?] [boundary/null?]
```

The likely verb *joindre* requires resolving the literal NN. The final `~42` and `~53` are not decoded. In particular `~53` also occurs at position 55; treating it as expendable only at the end would be an unsupported exception. The end token `72` remains a boundary/null hypothesis, not an established null.

The corresponding start token `71` is also left visible as an unproven boundary/null hypothesis.

### Exact unresolved inventory

| Source form | Positions |
| ----------- | --------- |
| `"48`       | 53        |
| `~53`       | 55, 201   |
| `x-`        | 57        |
| `y-`        | 64        |
| `12`        | 66        |
| `"40`       | 133       |
| `2`         | 157       |
| `~42`       | 200       |

That is eight unassigned token forms at nine occurrences, **in addition to** the two unproven boundary/null symbols and the contextual or conflicting assignments documented above. It must not be turned into a claim that some percentage of the original message has been independently verified.

## 6. Methods and rejected routes

Initial single-letter substitution and numerical-family searches produced French-looking fragments, including on shuffled controls. Those outputs were rejected as evidence of a decipherment. The useful breakthrough was the structured syllable-family interpretation, followed by manual constraint checking against repeated tokens and coherent French phrases.

The package’s decoder reproduces the current key application. It does not purport to rerun the entire exploratory search or automatically rediscover the key. Archived trial-search outputs are not included because they are not accepted solutions.

The best evidential next steps concern the specific uncertain source marks, a matching original key, or a parallel text. General historical plausibility alone cannot establish single-occurrence codewords. No email, archive request, or other third-party contact was made.

## 7. Reproduce the audit

Run in the extracted folder:

```sh
python decode.py
```

Python 3.9 or later is sufficient; only the standard library is used. The program checks the exact source hash and inventory, applies one fixed candidate expansion per form, preserves all unknowns, and writes:

* `audit/strict_decoding.txt`
* `audit/token_alignment.json`
* `audit/token_alignment.tsv`
* `audit/audit_summary.json`

It checks that the documented 54-token core is reproduced and that the unresolved inventory matches this report. These checks are a guard against transcription drift and silent key changes, **not** proof of historical correctness.

## Bottom line

There is strong evidence for the main syllabic structure and for substantial connected French plaintext. There is **not yet a complete verified decipherment**. The remaining uncertainty is localized and documented, but it includes historically meaningful code entries and genuine consistency problems; it cannot responsibly be hidden by polishing the prose.
