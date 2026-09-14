# Follow-up: checking the remaining text

14 September 2026. **One transcription problem is resolved with strong image
support; the ending has a stronger conjectural reading. The letter remains
partially deciphered.** All positions below refer to the original 202-token input.

## Source inspected

The [manuscript photograph](https://cryptiana.web.fc2.com/code/LeTellier1657.jpg)
linked from [Cryptiana’s cipher survey](https://cryptiana.web.fc2.com/code/louisxiv0.htm#SEC6)
was retrieved and visually inspected, including enlarged portions of the difficult
passages. The image credits Alexandre Pillon. This is inspection of a published
photograph, not examination of the physical letter or an independent scholarly
verification. No archival shelfmark or original codebook has been established.

The surveyed JPEG is 1128 × 1513 pixels; SHA-256:

```text
db45b2197d145ba9e13539e746c494675e9481effae247ceb8674fce5527434f
```

The photograph remains at its source and is not redistributed in this repository.

## C: “donnera lieu” — supported transcription correction

In the third cipher line from the bottom, immediately after `49 ~13`, the image
shows **27 with one bar above the number**. The published transcription split it
into `2 ~7` at positions 157–158. Compare the same barred number in *faudra*
(position 74) and *craindre* (164).

```text
Published:  49  ~13  2    ~7  ~4  h  20
Key:        DO  NE   [?]  MA  LI  E  U

Reviewed:   49  ~13  ~27  ~4  h  20
Key:        DO  NE   RA   LI  E  U
```

This gives literal **DONERALIEU**, readable as **donnera lieu**. The second N is
an editorial spelling restoration, as in the existing *donniez* reconstruction.
The wider passage is:

> …leur donnera lieu de craindre pour Rocroi…

This correction uses an already established `~27=RA`; it needs no new key value,
no null for `2`, and no exception to `~7=MA`. Applying this correction alone gives
201 tokens and 94 distinct forms. It removes bare `2` from the observed inventory;
all later positions shift down by one. The original source file is preserved.

Run this from the repository root to reproduce the corrected span without changing
the source or outputs:

```sh
python3 - <<'PY'
import json
from pathlib import Path

tokens = Path('ciphertext.txt').read_text().split()
key = {e['token']: e['value']
       for e in json.loads(Path('working_key.json').read_text())['entries']}
assert tokens[156:158] == ['2', '~7']
reviewed = tokens[154:156] + ['~27'] + tokens[158:161]
result = ''.join(key[t] for t in reviewed)
assert result == 'doneralieu'
print(result)
PY
```

## D: “joindre” — stronger, still contextual

On the last cipher line, the two marks after `69` do not look identical: the first
has a different upper stroke and bowl from the second. The second resembles the
mark used in *tant* at position 103. The published transcription calls both `t`,
which forces the original decoder to produce `JONNDRE`.

A distinct first symbol with candidate value I would resolve this:

```text
Position:   195  196                  197  198  199
Published:  69   t                    t    f    ~28
Reviewed:   69   [distinct glyph?]    t    f    ~28
Candidate:  JO   [I?]                 N    D    RE
```

**The visual distinction and the I assignment are separate claims.** The image
supports reconsidering the transcription; I is inferred from *joindre*, with no
independent second occurrence identified. Handwriting variation remains another
possibility. This is therefore a stronger conjecture, not a confirmed key entry.
Changing every `t` to I would break *tant* and is not proposed.

The following `~42 ~53` are still unassigned. A completed sentence followed by
the cleartext *Je suis* makes terminal padding a possibility, but does not prove
either sign is a null. `~53` also occurs at position 55 and must be explained
consistently there.

## A: the Meuse clause — useful exclusions

The unchanged key gives the following at positions 59–69:

```text
"13  18  ~28  ~33  h-  y-   ~28  12   ~8  20  ~33
ES   T   RE   SE   I   [?]  RE   [?]  ME  U   SE
```

Neither **entre Sambre et Meuse** nor **entre Sembre et Meuse** fits this sequence
by assigning only the unknowns. The fixed prefix is `ESTRESEI`, not `ENTRESAM`
or `ENTRESEM`. Testing the longer conjectures *ils assemblent…* and *on assemble…*
against positions 53–69 likewise fails even when unknowns may expand to arbitrary
strings. This excludes these exact readings under the fixed key, not every
possible reconstruction of the clause.

Several separate issues would need evidence:

- At 59, `"13=ES` would need reconsideration to obtain EN; its other occurrences
  support ES in contexts read as *est*. The photograph does not clearly justify
  silently replacing this mark with `"12=EN`.
- At 63, the mark grouped with `h-` deserves comparison with positions 24 and 150.
  A local M could help a conjectural *Sembre*, but changing all `h-` values would
  break *point* and *faire*.
- `x-`, `y-`, bare `12`, and the longer group `"48` have no independently
  established expansions. A plausible place name cannot establish all of them.
- Interpreting `~53` as a syllable to complete *assemble* must also account for
  its occurrence after the proposed *joindre*. Declaring it a null only there
  would introduce an unsupported exception.

The earlier [Le Tellier–Colbert keys](https://cryptiana.web.fc2.com/code/louisxiv0.htm)
were also inspected. The November 1650 reconstruction shares several bare-number
syllables, including `47=DE` and `49=DO`, but uses different numbering later in the
syllabary. These comparisons support investigating related cipher material; they
do not supply a demonstrated matching key for the unresolved 1657 code groups.

## B: the other marching party — still unidentified

`"40` occurs only once, before *par la marche qu’il a ordre de faire*. Its position
supports a masculine singular referent, potentially a commander. There is no
internal repetition that distinguishes a particular name or title. No matching
codebook or parallel plaintext identifying this code was located in this pass.
Turenne and La Ferté remain historical suggestions, not deciphered values.

The best next evidence would be the accompanying royal instructions, a parallel
copy of this letter, or another letter using the same key. The source survey
reports that cleartext royal instructions accompanied the letter; their contents
were not available in the material inspected here.

## What changes in the reading

The supported improvement is **“leur donnera lieu de craindre pour Rocroi.”**
The ending **“pour l’y aller joindre”** is better motivated but retains a question
mark. The Meuse clause, the identity represented by `"40`, and the terminal symbols
remain unresolved. The baseline decoder and frozen key are unchanged so that the
published transcription and these reviewed alternatives can be compared directly.
