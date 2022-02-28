"""
Fix the code below
"""


def helloFactory(greeting_type):
    my_dict = {"polite": "Hello", "other": "hey"}
    return my_dict[greeting_type]


my_greeting = helloFactory("polite")
print(my_greeting)  # Should print "Hello"
