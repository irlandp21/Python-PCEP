# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

print("Step 2:", beatles)

# step 3
members = ['Stu Sutcliff','Pete Best']
for i in members:
    add = input("Add "+i+" to band? Type 'y'")
    if add == 'y':
        beatles.append(i)
    else: continue

print("Step 3:", beatles)

# step 4
if 'Stu Sutcliff' in beatles: del beatles[beatles.index('Stu Sutcliff')]
if 'Pete Best' in beatles: del beatles[beatles.index('Pete Best')]

print("Step 4:", beatles)

# step 5
beatles.insert(0,'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))