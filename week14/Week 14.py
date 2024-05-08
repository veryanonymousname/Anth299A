# Significant parts of this script won't work on your computers.

import AnthroTools as at
import re
import pandas as pd

seq1 = '/users/nick/desktop/anth299a/W6c.txt'
seq2 = '/users/nick/desktop/anth299a/rsrs.txt'

alignment = str(at.pairwise(seq1, seq2))
print(alignment)

tpatt = "^target\s+\d+\s+([NACGT-]+)"
qpatt = "^query\s+\d+\s+([NACGT-]+)"
mpatt = "^\s+\d+\s+([|.-]+)"


tmatches = re.findall(tpatt, alignment, re.MULTILINE)
target = "".join(tmatches)
# print(target)

qmatches = re.findall(qpatt, alignment, re.MULTILINE)
query = "".join(qmatches)
# print(query)

mmatches = re.findall(mpatt, alignment, re.MULTILINE)
middle = "".join(mmatches)
# print(middle)

# print(len(target), len(query), len(middle))
length = len(target)

df = pd.DataFrame(columns=['position', 'target', 'query', 'comp'])
for i in range(length):
    position = i + 1
    t = target[i]
    q = query[i]
    m = middle[i]
    df.loc[i, ['position', 'target', 'query', 'comp']] = [position, t, q, m]

# pd.set_option('display.max_rows', None)
# print(df)

print("the following positions have mismatched base pairs:\n", df[df['comp']=='.']['position'].to_string(index=False))

print('________________________\n________________________\n________________________\n________________________\n')

print("And these positions have gaps, in one sequence or the other:\n", df[df['comp']=='-']['position'].to_string(index=False))
# or
print("These are the items with gaps:,\n", df[(df['target']=='-') | (df['query']=='-')])
