#File creator: Paul Boyer
#pauboyer@uat.edu
#CSC235 Python Programming 1
#WK 1 assignment 2

# intro varible to the program that will be called by the print command
intro = "Appropriate use of mayonnaise\n\n"+\
    "This is to demonstrate where mayonnaise belongs should you find it in your hosehold\n"+\
    "Be warned - this may incur the wrath of your significant other..\n"+\
    "and then she makes you dig through the trash and grab the mayo and you cry a little bit\n"+\
    "and possbily wet yourself out of fear.. \n\n"

# varible used to store the type of information
s1 = 'a'
# formatted strings
s1 = f's{1} Locate the nearest garbage\n'
s2 = f's{2} Search for mayonnaise within household\n'
s3 = f's{3} Take mayonnaise to garbage\n'
#s4 = f's{4} Throw it into the garbage with gusto anyways because that\'s where it belongs\n'
s5 = f's{5} Have no remorse for throwing it away even if others like it\n'

# print command calling the varibles to display information
print(intro)
print(s1)
print(s2)
print(s3)
# ask for user input
print("On a scale of 1-10 how scared are you for thorwing away the mayonnaise?")
# input function and fear_lvl is the varible
fear_lvl = input()
# print string with user input included in the sentance
print(f's{4} Throw it into the garbage with gusto anyways because that\'s where it belongs and be level {fear_lvl} afraid\n')    
print(s5)
#end of program