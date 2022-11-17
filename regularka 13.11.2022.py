import re, csv

people_cont = []
people_cont_phone = []
phone = {}
contacts_list_fixed = []

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  list = list(rows)

for i in list:
  pattern = r"(\+7|8)?(\s+)?\(?(\d{3})\)?-?(\s+)?(\d{3})-?(\d{2})-?(\d{2})(\s)?\(?(доб.\s\d{4})?\)?"
  result = re.sub(pattern, r"+7(\3)\5-\6-\7\8\9,", ','.join(i))
  people_cont += [result]

for b in people_cont:
  pattern1 = r"^(\w+)(,|\s)(\w+)(,|\s)(\w+)*(,{1,3})(\w+)*(,)?(position|\w*\s+.*[^\d][^,])?(,)"
  result_1 = re.sub(pattern1, r"\1,\3,\5,\7,\9,", b)
  people_cont_phone += [result_1.split(',')]

for ii in people_cont_phone:
  for t in ii:
      keys = t.split(',')
  if (ii[0],ii[1]) not in phone:
      phone[ii[0],ii[1]] = ii[2:]
  else:
        for z in ii[2:]:
           if z not in phone[ii[0],ii[1]]:
             phone[ii[0],ii[1]] += [z]

for k,v in phone.items():
    contacts_list_fixed += [[k[0],k[1]] + v]
    print(contacts_list_fixed)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f)
  datawriter.writerows(contacts_list_fixed)