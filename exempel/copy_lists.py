from os import system, name
from time import sleep


def clear_screen():
    # clears screen
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def new_page():
    print()
    # Clears screen, tells user to press enter and wait for the enter key press
    print("--We will continue on the next page, press enter to continue")
    input()
    print()
    clear_screen()


clear_screen()

print("Hello.\nLet's look at how Python handles copied lists")
print("As you know, lists are a mutable data type, so it's important to know how they work")
print("")
print("Let's first create a list called example_list that contains three elements - 'one', 'two', and 'three'. "
      "The syntax for that is as follows: ")
print("")
print("example_list = ['one', 'two', 'three']")
example_list = ['one', 'two', 'three']
print("")
print("After that, let's make a copy called copied list. The syntax is simple:\ncopied_list = example_list")
print("")

copied_list = example_list
print("")

new_page()

print("We now have two lists that are copies of each other. Let's take a look at where in memory those lists are "
      "stored, first example_list:\nprint(id(example_list))")
print("")
print(id(example_list))
print("")

print("And then, copied_list: print(id(copied_list))")
print("")
print(id(copied_list))
print("")

print("Are those the same? It's not easy to be sure just at a glance."
      "\nInstead of comparing ourselves, let's have python do it for us")
print("")

print("print(id(example_list) == id(copied_list))")
print("")
print("result:", id(example_list) == id(copied_list))
print("")
print("The memory address is the same! This means that they aren't two separate entities, but rather two different "
      "labels for the same data!")

new_page()

print("This should mean that if we change one, the change is reflected in the other. Let's verify!")
print("Both our list contain the elements 'one, 'two', and 'three'. Let's add 'banana' to the copied list only")
print("")
print("copied_list.append('banana')")
copied_list.append('banana')
print("")
print("Now let's have a look at the original list: \nprint(example_list)")
print(example_list)
print("")
print("The banana showed up in the original list as well! We have confirmed that changing one will change the other. "
      "Let's see if we can make a truly independent copy")

new_page()

print("Let's make a third list and see if we can decouple it from the first two: \nthird_list = list(example_list[:])")
print("")
third_list = list(example_list[:])

print("What exactly does the above line of code do? Let's have a look: First, the 'example_list[:]'-part is a slice."
      "It returns the _values_ of the first list. This is key. If I hadn't use a slice I would "
      "have returned the list object, which is what happened with copied_list. Ok, let's look at the rest of the"
      " syntax, I had just returned the values and assigned them to a label, I would have made a tuple. Why? "
      "Well, let's try to imagine what the equivalent line would be? First, Python would evaluate the values from the"
      "list slice. Then it would assign the values to third_list. The line would therefore look like this\n"
      "third_list = 'one', two', 'three', 'banana'\n That is the exact syntax for making a tuple, but we want a list. "
      "In order for Python make third_list an actual list, we need to use the list() function. This will return the "
      "values in the form of a list, which is exactly what has been done when assigning third_list.")

print("")
print('Now we have our, hopefully independent, list. The next step is to validate everything again')
print("")
new_page()

print("Let's use the same method as last, first we look at memory addresses, then we add something to one of the lists")
print("print(id(example_list) == id(third_list))")
print("")
print("result:", id(example_list) == id(third_list))
print("")
print("The memory addresses are different now, this looks promising. Will everything work as we intended now?")
print("")
print("example_list.append('split')")
example_list.append('split')
print("")
print("Now let's have a look at the third list: \nprint(third_list)")
print(third_list)
print("")
print("There is no banana split in our third list just the banana, which was already in example_list when we created"
      "third_list. We have thus confirmed that it is truly a different entity than example_list")

