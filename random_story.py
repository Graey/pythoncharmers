import random
when = ['A long long time ago','A few years ago', 'Yesterday', 'Last night', 'A long time ago','Once upon a time','One fine morning']
who = ['a rabbit','a donkey', 'an elephant','a lion', 'a mouse', 'a turtle','a jackal','a hen']
name = ['Ali','Ollie','Oscar','Rosie','Lola','Archie','Miriam', 'Max', 'Luke']
residence = ['Barcelona', 'Germany', 'Venice', 'England','Afghanistan','Brazil','Argentina','Canada']
went = ['cinema', 'university', 'school', 'laundry','library','store','party','restaurant','concert','police station','ocean','garden']
happened = ['made a lot of friends', 'went to sleep','found a secret key', 'solved a mistery', 'wrote a book','wrote a code','ate some fancy food','saw his childhood friend','damced the night away']
print( random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
