#!/usr/bin/env python3


import sys

from lexicon import VERBS
from verbs import calculate_form


if len(sys.argv) == 2:
    lemma_filter = sys.argv[1]
else:
    lemma_filter = None

passed = 0
fails = []
with open("test.txt") as f:
    for line in f:
        record = line.strip().split("#")[0]
        if not record:
            continue
        lemma, parse, form = record.split()
        if lemma_filter and lemma_filter != lemma:
            continue

        prediction, rule = calculate_form(VERBS[lemma], parse)

        if prediction == form:
            passed += 1
        else:
            fails.append("{} != {} {}".format(record, prediction, rule))

print("{} passed".format(passed))
if fails:
    print("{} failed".format(len(fails)))
    print(fails[0])
