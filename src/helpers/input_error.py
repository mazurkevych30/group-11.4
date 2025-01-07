"""F"""
def input_error(func):
    """"F"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return e
    return inner
