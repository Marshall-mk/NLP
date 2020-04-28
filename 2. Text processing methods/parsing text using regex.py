# parsing text using regex

import re

pattern = '\s+'
string = 'i like you'
la = re.split(pattern,string)

# extracting email IDs
doc = 'For more details please mail us at: xyz@abc.com, pqr@mno.com'
pattern_1 = r'[\w\.-]+@[\w\.-]+'
addresses = re.findall(pattern_1,doc)
for address in addresses:
	print(address)

# replacing email IDs
 doc_1 = 'For more details please mail us at xyz@abc.com'
 new_email_address = re.sub(pattern_1,r'marshall@gmail.com',doc_1)
 print(new_email_address)


