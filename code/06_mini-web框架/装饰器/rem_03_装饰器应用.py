




#"<h1>hahaha</h1>

def add_privilige(function):
    def set_privilige():
        ret = function()
        ret = "<h1>" + ret + "</h1>"
        return ret
    return set_privilige

@add_privilige
def func():
    return "hahaha"

print(func())