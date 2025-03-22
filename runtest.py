# This is to be run with the body and text examples in Test_Inputs folder.
# For use in actual application, You need to take the input data and create 
# a body string that holds all review text.
#

import bert
import torch
from summarizer import Summarizer

body = '''
       This coffee had a wonderfully smooth flavor with just the right amount of boldness.
       I loved the rich aroma that filled my kitchen while it brewed. A fantastic way to start the day.
       The chocolatey undertones were a pleasant surprise, and it had no bitter aftertaste.
       This is one of the best medium roasts I’ve tried. Balanced and full of flavor.
       The freshness was noticeable from the first sip. You can really taste the quality.
       I enjoy drinking it black, and it’s still smooth and satisfying. Highly recommend.
       It has the perfect balance of acidity and richness. Definitely my new favorite.
       I tried it with a splash of cream, and it brought out even more of the nutty notes.
       Brews beautifully in a French press, giving it a full-bodied flavor.
       This coffee has a bold, robust flavor without being too harsh. Perfect for a morning pick-me-up.
       I was blown away by how smooth this coffee was. From the moment I opened the bag, the rich aroma promised something special. It brewed up beautifully, with a deep, full-bodied flavor that didn’t lean too bitter. I also picked up subtle notes of caramel and dark chocolate, adding a delightful complexity. Every cup felt like a treat, and it’s been my go-to for both relaxing weekends and busy mornings. Highly recommend this one!
       This coffee is the perfect balance of smooth and bold. I usually take my coffee black, and this one didn’t disappoint. It has a beautiful aroma, almost like fresh cocoa, and the taste followed through with a rich, nutty profile. The acidity was low, making it gentle on my stomach, but the flavor was still bright and complex. I’ve already ordered another bag!
       The moment I opened the bag, I knew I was in for a treat. The beans had a perfect glossy sheen, indicating freshness. I brewed a cup using my pour-over, and it was incredible. It had a silky texture with notes of hazelnut and a hint of dark chocolate. Even as it cooled, the flavors remained smooth and enjoyable. This is the kind of coffee I’ll proudly serve to friends and family.
       This coffee completely changed my morning routine. The flavor is so smooth and rich, with a perfect balance of sweet and nutty notes. It doesn’t leave a bitter aftertaste like some other brands I’ve tried. I’ve also noticed that the beans stay fresh for longer than most, which is a huge plus. It’s become a staple in my house, and I can’t recommend it enough.
       I’m in love with the bold, smooth flavor of this coffee. It has a deep, roasted aroma that makes waking up a little easier. The first sip was like a warm hug, with subtle notes of caramel and a lingering cocoa finish. I usually add a splash of oat milk, and it pairs perfectly. If you’re a fan of medium-dark roasts, this one is a must-try.
       This coffee is everything I hoped for. It has a beautiful balance of flavors with a subtle nuttiness and a hint of chocolate. I used it for both espresso and drip coffee, and it excelled in both methods. The crema on the espresso was thick and golden, and the flavor was rich without any bitterness. I’m already planning to buy another bag!
       I can’t believe how much I’m enjoying this coffee. It’s smooth, bold, and full of complex flavors. The hint of caramel on the finish is delightful, making every sip feel indulgent. I also appreciate that it’s ethically sourced. It’s rare to find a coffee that ticks all the boxes — this one does. Highly recommended!
       This coffee is fantastic. I brew it in my Chemex, and it produces a clean and crisp cup every time. It has a nice medium body with notes of cocoa and a little bit of toasted almond. The flavor is rich without being overwhelming, and it leaves a pleasant aftertaste. It’s easily one of the best coffees I’ve had at home.
       I’ve tried many different coffees, but this one stands out. The beans are clearly fresh, and the grind consistency works perfectly for my espresso machine. The shot pulled beautifully with a thick crema and a smooth, velvety taste. There’s a subtle hint of dark chocolate that lingers, making it perfect for sipping slowly. Definitely a repeat purchase.
       I was pleasantly surprised by how smooth this coffee is. No bitterness, just a clean, balanced cup.
       The caramel notes are subtle but delightful. It’s like a treat in a cup.
       I’m usually a tea drinker, but this coffee has me reconsidering. So flavorful!
       I love how rich and bold it tastes without any acidity. Exactly what I was looking for.
       This coffee is so smooth that I don’t even need to add sugar. Truly a premium experience.
       It makes my mornings so much better. The aroma alone is worth it.
       Perfect for cold brew! The flavor stays strong and doesn’t get watered down.
       I brought this to work, and now my coworkers won’t stop asking where I got it.
       There’s a beautiful complexity to the flavor. Every cup tastes like a small luxury.
       It’s the kind of coffee that makes you slow down and really enjoy it. Highly recommend.
       My house smells amazing every time I brew this. It’s like a café experience at home.
       The packaging was beautiful, and the coffee was even better. A total win.
       I usually get my coffee from local shops, but this beats most of them.
       Even as a casual coffee drinker, I can taste the difference. So much better than grocery store brands.
       This coffee has just the right amount of boldness. It’s rich without being overpowering.
       The nutty flavor really comes through, making it the perfect cup for a cozy morning.
       I brewed this in my AeroPress, and it brought out the chocolatey notes perfectly.
       I can’t stop raving about this coffee to my friends. Every cup is a joy.
       It’s rare to find a coffee that’s both bold and smooth, but this one nails it.
       My new go-to for weekend brunches. Everyone loves it!
       If you like medium roasts, this is a no-brainer. Absolutely delicious.
       Even my husband, who isn’t a big coffee fan, loved this one.
       A fantastic value for the quality. I’d happily pay more for something this good.
       I tried it iced, and it was just as flavorful. Definitely a versatile brew.
       This coffee has made my mornings so much better. I’ll never go back to my old brand.
'''

#print("Input text length:", len(body))
#print("Input text:", body)

print("Model Loading...")
bert_model = Summarizer()
print("Model Loaded...")


# Generate the summary
print("Summary Started...")
bert_summary = bert_model(body, min_length=10, max_length=45)
print("Summary Generated...")

# Ensure the summary is correctly converted to a string and printed
#print("Summary length:", len(bert_summary))
print("Summary:", bert_summary)
#print("Summary:", ''.join(bert_summary))