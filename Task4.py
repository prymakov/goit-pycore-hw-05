
def main():
    phone_book = {}

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Error. Could not find contact."
            except ValueError:
                return "Give me name and phone please."
            except IndexError:
                return "Enter user name."
        return inner

    @input_error
    def add_contact(args):
        name, phone = args
        phone_book[name] = phone
        return "Contact added."

    @input_error
    def change_contact(args):
        name, phone = args
        if name in phone_book:
            phone_book[name] = phone
            return "Contact updated."
        else:
            raise KeyError

    @input_error
    def show_all():
        if phone_book:
            return "\n".join(f"{name}: {phone}" for name, phone in phone_book.items())
        else:
            return "No contacts found."

    @input_error
    def show(args):
        return phone_book[args[0]]

    def parse_input(user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    print("Welcome to the assistant bot!")
    print("Enter a command:")

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(show_all())
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "show":
            print(show(args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()