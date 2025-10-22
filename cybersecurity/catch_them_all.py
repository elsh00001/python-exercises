def error_handler(function: callable) -> str:
    try:
        function()
        return "No errors :)"
    except ZeroDivisionError:
        return "You made a black hole!"
    except IndexError:
        return "You shouldn't be here!"
    except Exception as e:
        # errors and exceptions python doc
        return f'{type(e)}: {str(e)}'