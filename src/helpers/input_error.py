"""F"""
def input_error(func):
    """"Function for errors messages"""
    messages = ["The phone number must be 10 digits.", "Name is required field.", "Invalid email.", "Invalid date format. Use DD.MM.YYYY"]
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) in messages:
                return(e)
            return "Enter the argument for the command"
        except KeyError:
            return "Not found."
        except IndexError:
            return "Enter user name."
        # except Exception as e:
        #     return e
    return inner
