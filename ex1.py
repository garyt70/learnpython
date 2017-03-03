print( "Hello World!")
print ("Hello Again")
print ("I like type this.")
print ("Yay!")

print ("Test math", 25+30/6)
print ("Roosters", 100-25*3%4)
print ("Now a bigger formula")
print (3+2+1-5+4%2-1/4+6)

#tutorial working with variables
cars = 100
space_in_a_car=4.0
drivers=30
passengers=90
carsNotDriven= cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * space_in_a_car
averagePassangersPerCar = passengers/carsDriven

print ("There are %d cars available, and %d drivers" % (cars, drivers))

formatter = "%r %r %r %r"
print ("Test formatting varible formatter", formatter % (1,2,3,4))

#test text input
age = input("How old are you?")
print ("your age is %r" % age)

#test opening file in different modes
with open("test_doc.txt","r+") as file1:
    print ("====  \n\n\n\n")
    print ( file1.read() )
    file1.write("54321\n")
    file1.write("end of file\n")
    file1.seek(0)
    for line in file1:
        print( line )
        print("---\n")

print ("Files is closed, correct?", file1.closed)
