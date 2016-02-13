#!/usr/bin/env python3

# We got some animals at home.
cats = 5
dogs = 2
print ("We have got %d cats and %d dogs." % (cats, dogs))

animals = cats + dogs
print ("So that would be %d animals." % animals)

# So how much food do we need?
cat_portion = 100
dog_portion = 300
print ("My cats portions are %d grams.\nMy dogs are %d grams." % 
        (cat_portion, dog_portion))

# Just the cats.
cats_total = cats * cat_portion
print ("To feed all my %d cats, I would need %d grams of food." % 
        (cats, cats_total))

# Just the dogs.
dogs_total = dogs * dog_portion
print ("My %d dogs, need %d grams in total." % (dogs, dogs_total))

# You can use arithmetic operators on strings too...
print ("-" * 80)

# Total amount of food
animals_total = cats_total + dogs_total
print ("That means that my animals will need %dg in total, per day." % 
        (animals_total))




