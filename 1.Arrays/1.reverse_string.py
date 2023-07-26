def reverse(str):
    if str == "":
        return ""
    reversed = ""
    for i in range(len(str) - 1, -1, -1):
        reversed += str[i]
    return reversed

def reverse_recursive(str):
    if str == "":
        return ""
    return reverse(str[1:]) + str[0]