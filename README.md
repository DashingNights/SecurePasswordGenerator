# SecurePasswordGenerator
click and run python console script that generates some of the most secure passwords in existence

Visualised code execution :
https://pythontutor.com/render.html#code=from%20math%20import%20factorial%0Aimport%20random%0Aimport%20string%0A%0Aalphabets%20%3D%20list%28string.ascii_letters%29%0Adigits%20%3D%20list%28string.digits%29%0Aspecial_characters%20%3D%20list%28%22!%40%23%24%25%5E%26*%28%29~-%22%29%0A%0A%0A%23%20custom%20pw%20length%0Adef%20custom%28%29%3A%0A%20%20%20%20abc1%20%3D%20%5B%5D%0A%20%20%20%20digi1%20%3D%20%5B%5D%0A%20%20%20%20specichar1%20%3D%20%5B%5D%0A%20%20%20%20customlength1%20%3D%20int%28input%28%22please%20enter%20custom%20password%20length%3A%5Cn%22%29%29%0A%20%20%20%20for%20i%20in%20range%28customlength1%29%3A%0A%20%20%20%20%20%20%20%20abc1.append%28random.choice%28alphabets%29%29%0A%20%20%20%20%20%20%20%20digi1.append%28random.choice%28digits%29%29%0A%20%20%20%20%20%20%20%20specichar1.append%28random.choice%28special_characters%29%29%0A%20%20%20%20generatedpw1%20%3D%20''.join%28%0A%20%20%20%20%20%20%20%20random.sample%28''.join%28random.sample%28abc1%20%2B%20digi1%20%2B%20specichar1,%20customlength1%29%29,%20customlength1%29%29%0A%20%20%20%20print%28%22length%3A%20%22%20%2B%20str%28len%28generatedpw1%29%29%29%0A%20%20%20%20print%28%22Number%20of%20possiblities%3A%20%22,%20int%28possiblities%28generatedpw1%29%29%29%0A%20%20%20%20print%28generatedpw1%29%0A%20%20%20%20input%28%22%22%29%0A%0A%0A%23%20defined%20password%20length%0Adef%20static%28%29%3A%0A%20%20%20%20lengthstatic%20%3D%20int%28'17'%29%0A%20%20%20%20abc%20%3D%20%5B%5D%0A%20%20%20%20digi%20%3D%20%5B%5D%0A%20%20%20%20specichar%20%3D%20%5B%5D%0A%20%20%20%20for%20i%20in%20range%28lengthstatic%29%3A%0A%20%20%20%20%20%20%20%20abc.append%28random.choice%28alphabets%29%29%0A%20%20%20%20%20%20%20%20digi.append%28random.choice%28digits%29%29%0A%20%20%20%20%20%20%20%20specichar.append%28random.choice%28special_characters%29%29%0A%20%20%20%20generatedpw%20%3D%20''.join%28%0A%20%20%20%20%20%20%20%20random.sample%28''.join%28random.sample%28abc%20%2B%20digi%20%2B%20specichar,%20lengthstatic%29%29,%20lengthstatic%29%29%0A%20%20%20%20for%20i%20in%20range%28len%28generatedpw%29%29%3A%0A%20%20%20%20%20%20%20%20random.sample%28generatedpw,%20lengthstatic%29%0A%0A%20%20%20%20print%28%22length%3A%20%22%20%2B%20str%28len%28generatedpw%29%29%29%0A%20%20%20%20print%28%22Number%20of%20possiblities%3A%20%22,%20int%28possiblities%28generatedpw%29%29%29%0A%20%20%20%20print%28generatedpw%29%0A%20%20%20%20input%28%22%22%29%0A%0A%0A%23%20Calculate%20possiblities%20using%20factorial%20formulas%0Adef%20possiblities%28password%29%3A%0A%20%20%20%20raw_amount%20%3D%20factorial%28len%28password%29%29%0A%20%20%20%20for%20i%20in%20password%3A%0A%20%20%20%20%20%20%20%20if%20password.count%28i%29%20!%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raw_amount%20/%3D%20factorial%28password.count%28i%29%29%0A%20%20%20%20return%20raw_amount%0A%0A%0A%23%20ask%20for%20user%20input%0Achoice%20%3D%20str%28input%28%22custom%20length,%20input%20y,%20generic%20length,%20input%20n%3A%5Cn%22%29%29%0Aif%20choice.lower%28%29%20%3D%3D%20%22y%22%3A%0A%20%20%20%20custom%28%29%0Aelif%20choice.lower%28%29%20%3D%3D%20%22n%22%3A%0A%20%20%20%20static%28%29%0Aelse%3A%0A%20%20%20%20print%28%22Please%20enter%20a%20NUMBER.%5Cn%22%29&cumulative=false&curInstr=84&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22n%22%5D&textReferences=false
