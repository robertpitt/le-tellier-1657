# Le Tellier–Castelnau cipher, 12 May 1657

A reproducible **partial decipherment** of a letter from Le Tellier to the
Marquis de Castelnau: the ciphertext, proposed key, literal output, and readable
solution. The reading is substantial but incomplete. A [targeted manuscript-image
review](MANUSCRIPT_REVIEW.md) resolves the transcription problem in *donnera lieu*
and strengthens *joindre*. The complete transcription and key remain unverified.

## Input, key, and output

| File | Purpose |
| --- | --- |
| [ciphertext.txt](ciphertext.txt) | Unchanged supplied transcription: 202 tokens, 95 distinct forms. |
| [working_key.json](working_key.json) | All 95 observed forms, with candidate values, status, occurrence positions, and uncertainty notes. |
| [decode.py](decode.py) | Applies the fixed working key using only the Python standard library. |
| [output/strict_decoding.txt](output/strict_decoding.txt) | Literal output, retaining unknowns and possible boundary symbols. |
| [output/token_alignment.tsv](output/token_alignment.tsv) | Each input token aligned with its proposed expansion and evidence status. |
| [output/audit_summary.json](output/audit_summary.json) | Input hash, inventory, unresolved positions, and consistency checks. |
| [MANUSCRIPT_REVIEW.md](MANUSCRIPT_REVIEW.md) | Follow-up image inspection, one supported transcription correction, and remaining hypotheses. |

## Readable solution

This is an editorial reconstruction of the encrypted passage. Word divisions,
punctuation, accents, and modern spellings are supplied; brackets mark gaps or
conjectures. The already-readable introduction is not part of this recovery.

> d’obliger, s’il est possible, les ennemis à ne point dégarnir Rocroi ni à faire
> monter les troupes que **[A : passage non résolu, se terminant par « Meuse »]**.
>
> Il faudra que vous régliez votre marche en sorte que vous donniez jalousie tant
> à Rocroi qu’aux places du Hainaut, et qu’en **[même ?]** temps que **[B : sujet
> non identifié]**, par la marche qu’il a ordre de faire, leur **donnera lieu**
> de craindre pour Rocroi, vous leur fassiez croire que la vôtre est
> pour l’y aller **[joindre ?] [D : fin non résolue]**.

*Donnera lieu* incorporates the image-supported correction C below. The checked-in
input, key, and decoder output retain the original published transcription.

The passage appears to direct a diversion: threaten Rocroi and the towns of
Hainaut, discourage the enemy from withdrawing troops, and mislead them about
the destination of Castelnau’s march. This interpretation comes from the partial
reading; the identity of the other marching party remains unknown.

## How the key works

The working model combines **letters, syllables, and longer code groups**.
Different symbols can represent the same letter. A token is a whitespace-delimited
source form: marks such as `~`, `-`, `=`, and `"` are significant. For example,
`5~` is preserved exactly as supplied, rather than rewritten as `~5`.

Several number families follow an ordered vowel pattern. These examples are
observed assignments, not a recovered historical codebook:

| Family | Proposed values |
| --- | --- |
| Bare numbers | `47=DE`, `49=DO`, `50=DU`, `51=FA`, `56=GA`, `57=GE` |
| L syllables | `~2=LA`, `~3=LE`, `~4=LI`, `5~=LO` |
| M syllables | `~7=MA`, `~8=ME`, `~9=MI`, `~10=MO` |
| N syllables | `~12=NA`, `~13=NE`, `~14=NI` |
| QU syllables | `~22=QUA`, `~23=QUE`, `~24=QUI` |
| Longer groups | `"33=VOUS`, `"32=VOSTRE`; `"25=MESME` is contextual. |

For example, positions 76–86 decode with one fixed value per form:

```text
"33   ~28  z-  ~4  c  31  "32     ~7  3  l  62
VOUS  RE   G   LI  E  Z   VOSTRE  MA  R  C  HE
```

Positions 70–123 form a continuous 54-token passage yielding 93 letters:

```text
ilfaudraquevousregliezvostremarcheensortequevousdoniezjalousietantarocroyquauxplacesduhainaut
```

The key contains 78 working assignments, 7 contextual hypotheses, 8 unresolved
forms, and 2 boundary/null hypotheses. The seven contextual values are `33=Y`,
`"34=TER`, `J-=M`, `35=ET`, `"25=MESME`, `o=P`, and `"14=EUR`; their individual
limitations are recorded in the key. Unobserved syllabary cells are omitted.

## Unresolved text and editorial changes

| Span (1-based, inclusive) | Remaining issue |
| --- | --- |
| A: 53–69 | The clause ending in `MEUSE` is unresolved; `"48`, `~53`, `x-`, `y-`, and `12` have no assigned value. |
| B: 133 | `"40` may represent the subject of the following clause; no name is established. |
| C: 155–161 | Image-supported correction: read original positions 157–158 (`2 ~7`) as one barred `27`. The existing key gives `DONERALIEU`, modernized as *donnera lieu*. |
| D: 195–201 | The image suggests that the two marks transcribed `t t` differ. Assigning the first a conjectural I gives *joindre*; `~42` and `~53` remain unknown. |
| 1 and 202 | `71` and `72` are possible boundary/null symbols, not established nulls. |

In the frozen published transcription, eight unknown forms occur at nine positions:
`"48` (53), `~53` (55, 201),
`x-` (57), `y-` (64), `12` (66), `"40` (133), `2` (157), and `~42` (200).

The readable solution restores *est*, *possible*, *donniez*, *fassiez*, and
*aller* from literal `ES`, `POSIBLE`, `DONIEZ`, `FASIEZ`, and `ALER` in the
corresponding clear contexts. It modernizes `VOSTRE`, `QUAN`, `LI`, and `ROCROY`
to *votre/vôtre*, *qu’en*, *l’y*, and *Rocroi*. The provisional Y in `ROCROY`
cannot be distinguished from I by these occurrences alone. Candidate `MESME`
becomes *même ?*. Opening `71` and closing `72` are omitted only in the editorial
reading; all gaps and boundary hypotheses remain visible in the literal output.

The remaining discrepancies could reflect spelling, transcription, original
encipherment, or an incorrect assignment. The follow-up review establishes neither
a complete decipherment nor a general resolution of these problems.

## Reproduce

With Python 3.9 or later, run from the repository directory:

```sh
python3 decode.py
```

This regenerates the three files in `output/`. No dependencies or network access
are required. To write results elsewhere, use `python3 decode.py --output-dir /tmp/le-tellier-output`.

The decoder checks the source SHA-256, token inventory, one entry per observed
form, exact unresolved inventory, and continuous core above. These checks establish
reproducibility and consistency, **not independent historical verification**.
The script applies the supplied key; it does not rediscover it automatically.

Frozen input SHA-256:

```text
3618959aec3ceafc0e604f6bb34eb1eaaf120cf3675383081dbc0c64c3321459
```

## Source and license

Prepared from `le_tellier_1657_working_decipherment.zip` (analysis dated
14 September 2026). The supplied report attributes the transcription to
[Satoshi Tomokiyo’s Cryptiana post](https://cryptiana.blogspot.com/2025/10/an-undeciphered-letter-of-le-tellier-to.html),
published 20 October 2025, with a correction noted on 7 December 2025. The archive
provides the working analysis; this repository packages it without claiming a
new or complete decipherment. The manuscript photograph and website HTML are
not included.

Released under [CC0 1.0 Universal](LICENSE): the repository’s original code,
analysis, and documentation are dedicated to the public domain to the extent
permitted by law. Source attribution is retained; this dedication does not claim
rights over third-party material.
