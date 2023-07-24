import re

for s in range(int(input())):
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", lambda x: ['or', 'and'][x.group() == '&&'], input()))
