#!/usr/bin/env python3
"""Decode the frozen published transcription with the partial working key.

Python 3.9+; standard library only. No network access or external packages.
Unknown entries and unproven boundary/null hypotheses remain visible.
This reproduces a proposed reading; it is not a proof that every key entry is correct.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

EXPECTED_CORE = (
    'ilfaudraquevousregliezvostremarcheensortequevousdoniezjalousie'
    'tantarocroyquauxplacesduhainaut'
)
EXPECTED_UNKNOWN = {'"48':[53], '~53':[55,201], 'x-':[57], 'y-':[64],
                    '12':[66], '"40':[133], '2':[157], '~42':[200]}

def run(cipher_path: Path, key_path: Path, output_dir: Path) -> None:
    source = cipher_path.read_bytes()
    doc = json.loads(key_path.read_text(encoding='utf-8'))
    if hashlib.sha256(source).hexdigest() != doc['ciphertext_sha256']:
        raise ValueError('Ciphertext hash mismatch: the frozen source has changed.')
    tokens = source.decode('utf-8').split()
    if len(tokens) != 202 or len(set(tokens)) != 95:
        raise ValueError('Unexpected token inventory.')
    key = {entry['token']:entry for entry in doc['entries']}
    if len(key) != len(doc['entries']) or set(tokens) != set(key):
        raise ValueError('Key must contain exactly one entry per observed token form.')
    rows = []
    fragments = []
    unknown = {}
    for pos, token in enumerate(tokens, 1):
        entry = key[token]
        if entry['status'] == 'boundary_hypothesis':
            rendered = f'[[BOUNDARY_OR_NULL?:{token}]]'
        elif entry['value'] is None:
            rendered = f'[[UNRESOLVED:{token}]]'
            unknown.setdefault(token, []).append(pos)
        else:
            if not isinstance(entry['value'], str) or not entry['value']:
                raise ValueError(f'Invalid non-boundary value for {token!r}.')
            rendered = entry['value']
        fragments.append(rendered)
        rows.append({'position':pos, 'cipher_token':token,
                     'candidate_expansion':entry['value'] or '',
                     'status':entry['status'], 'strict_rendering':rendered,
                     'note':entry['note']})
    if unknown != EXPECTED_UNKNOWN:
        raise ValueError(f'Unexpected unresolved inventory: {unknown!r}.')
    core = ''.join(key[t]['value'] or '' for t in tokens[69:123])
    if core != EXPECTED_CORE:
        raise ValueError('The documented 54-token core no longer matches the fixed key.')
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir/'strict_decoding.txt').write_text(''.join(fragments)+'\n', encoding='utf-8')
    with (output_dir/'token_alignment.tsv').open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    summary = {'ciphertext_sha256':doc['ciphertext_sha256'], 'token_count':len(tokens),
               'distinct_forms':len(key), 'key_status_counts':dict(Counter(e['status'] for e in key.values())),
               'unresolved_positions':unknown,
               'boundary_or_null_hypotheses':{'71':[1], '72':[202]},
               'coherent_core_positions':[70,123], 'coherent_core_tokens':54,
               'coherent_core_letters':len(core), 'coherent_core':core,
               'checks_passed':['source SHA-256','202 tokens / 95 forms','one fixed entry per form',
                                'exact unresolved inventory','54-token core reproduced'],
               'limitation':'These are reproducibility/consistency checks, not independent validation of the cryptanalytic solution.'}
    (output_dir/'audit_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ciphertext',type=Path,default=base/'ciphertext.txt')
    parser.add_argument('--key',type=Path,default=base/'working_key.json')
    parser.add_argument('--output-dir',type=Path,default=base/'output')
    args = parser.parse_args()
    try:
        run(args.ciphertext,args.key,args.output_dir)
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
