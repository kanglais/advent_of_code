import re

count_valid = 0

required_fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: 150 <= int(x[:len(x)-2]) <= 193 if "cm" in x else 59 <= int(x[:len(x)-2]) <= 76 if re.search('in|cm', x) != None else False,
    "hcl": lambda x: re.search('^#[0-9a-f]{6}$', x) is not None,
    "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda x: re.search('^[0-9]{9}$', x) is not None
}

# def validate(doc):
#     valid = []
#     try:
#         if int(doc['byr']) >= 1920 and int(doc['byr']) <= 2002:
#             valid.append(1)
#         if int(doc['iyr']) >= 2010 and int(doc['iyr']) <= 2020:
#             valid.append(1)
#         if int(doc['eyr']) >= 2020 and int(doc['eyr']) <= 2030:
#             valid.append(1)
#         if 'cm' in doc['hgt']:
#             if int(doc['hgt'][:3]) >= 150 and int(doc['hgt'][:3]) <= 193:
#                 valid.append(1)
#         if 'in' in doc['hgt']:
#             if int(doc['hgt'][:2]) >= 59 and int(doc['hgt'][:2]) <= 76:
#                 valid.append(1)
#         if re.search('^#[0-9a-f]{6}$', doc['hcl']) is not None:
#             valid.append(1)
#         if doc['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
#             valid.append(1)
#         if re.search('^[0-9]{9}$', doc['pid'].lstrip("0")) is not None:
#             valid.append(1)
#         if len(valid) == 7:
#             return True
#     except:
#         return False

def validate(doc):
    for field in required_fields.keys():
        if field not in doc or not required_fields[field](doc[field]):
            if len(doc) == 8:
                print(doc)
            return False
    return True


documents = []
with open('day4_input.txt', 'r') as f:
    document = {}
    for line in f.readlines():
        i = line.split(' ')

        if line == '\n':
            document = {}
        else:
            for x in i:
                temp = x.split(':')
                document.update({temp[0]:temp[1].strip('\n')})
            documents.append(document)

docs = [dict(s) for s in set(frozenset(doc.items()) for doc in documents)]

for d in docs:
    # keys = list(set(d.keys()))
    if validate(d):
        count_valid+=1

print(count_valid)
