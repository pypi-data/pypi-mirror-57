######################################################
######Call the function: help with the parameter######
######e, of any exception thrown that is not in ######
######the "errors.ignore" file to immediately go######
######to a stack overflow search of your error. ######
######################################################

def help(e):
    e = type(e).__name__
    with open("errors.ignore", "r") as myfile:
        for i in myfile:
            if i in e.lower():
                return
    import webbrowser
    webbrowser.open("https://stackoverflow.com/search?q="+ e)
    quit()