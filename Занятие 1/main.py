def is_palindrome(string):
    reversed_string = ""
    for i in range(len(string), 0, -1):
        reversed_string += string[i - 1]
        if string == reversed_string:
            print("True")
        else:
            print("False")



is_palindrome("radar")
is_palindrome("Python")
