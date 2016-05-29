#! python3
# hub.py input name of something then what you want to do with it.
import pyperclip
import shelve
import sys


def add_entry(entry_name):
    entry_obj = shelve.open('saves')

    """Save the name and object to the file."""
    entry_obj[entry_name] = pyperclip.paste()
    print('%s successfully added to the database!' % entry_name)
    """Close the file"""
    entry_obj.close()


def delete_entry(entry_name):
    entry_obj = shelve.open('saves')

    """Delete the entry or raise an exception"""
    try:
        del entry_obj[entry_name]
    except KeyError:
        raise Exception("That entry does not exist and cannot be deleted")
    print('%s successfully deleted from the database!' % entry_name)
    """Close the file"""
    entry_obj.close()


def get_entry(entry_name):
    entry_obj = shelve.open('saves')

    """Retrieves the value associated with the name. If the value does not exist an error will be raised."""
    try:
        value = entry_obj[entry_name]
    except KeyError:
        raise Exception("That entry does not exist and cannot be retrieved.")

    """Close the file."""
    entry_obj.close()

    """Copies retrieved value to clipboard."""
    print('%s successfully retrieved and copied to keyboard!' % entry_name)
    pyperclip.copy(value)


def list_entries():
    entry_obj = shelve.open('saves')

    """Print out the name of every entry in the database."""
    if len(entry_obj.keys()) == 0:
        print('The database is empty!')

    else:
        print("The database contains:")
        for i in entry_obj.keys():
            print('\t', i)

    """Close the file."""
    entry_obj.close()


def rename_entry(entry_name, new_name):
    entry_obj = shelve.open('saves')

    """Get the entry and rename it."""
    val = entry_obj[entry_name]
    del entry_obj[entry_name]
    entry_obj[new_name] = val

    """Close the file."""
    entry_obj.close()


def command_help():
    print('\nrename entry_name new_name -- renames an entry (keeps same value)')
    print(
        'add entry_name -- add whatever is in your clipboard to '
        'the database, under the given entry name (will also replace value if given entry_name'
        'already exists)')
    print('del entry_name -- delete entry_name from database')
    print('get entry_name -- copy value associated with entry_name to clipboard')
    print('list -- see every key currently in the database.')
    print('quit -- exit the program\n')


def main():
    if len(sys.argv) == 1 or len(sys.argv) == 0:
        while True:
            command = str(input('\nPlease type a command: '))
            command = command.split()

            if len(command) == 1:
                if command[0] == 'help':
                    command_help()
                    continue

                elif command[0] == 'list' or command[0] == 'l' or command[0] == 'ls':
                    list_entries()
                    continue

                elif command[0] == 'quit':
                    quit()
                    continue

                else:
                    command_help()
                    continue
            elif len(command) == 2:
                if command[0] == 'a' or command[0] == 'add':
                    add_entry(command[1])
                    continue

                elif command[0] == 'remove' or command[0] == 'del' or command[0] == 'delete':
                    delete_entry(command[1])
                    continue

                elif command[0] == 'get':
                    get_entry(command[1])
                    continue

                else:
                    command_help()
                    continue
            elif len(command) == 3:
                if command[0] == 'rename':
                    rename_entry(command[1], command[2])
    """The following is the python argument integration. ***UNSTABLE***
    if sys.argv[0] == 'python3':
        operation = sys.argv[2]
        sys.argv.append(operation)

        name = sys.argv[1]
        sys.argv[2] = name

        sys.argv[1] = 'python3'

    if sys.argv[2] == 'help':
        command_help()

    elif sys.argv[2] == 'list' or sys.argv[2] == 'l':
        list_entries()

    elif sys.argv[3] == 'add' or sys.argv[3] == 'a' or sys.argv[3] == 'put':
        add_entry(sys.argv[2])

    elif sys.argv[3] == 'del' or sys.argv[3] == 'd' or sys.argv[3] == 'delete' or sys.argv[3] == 'remove':
        delete_entry(sys.argv[2])

    elif sys.argv[3] == 'get':
        get_entry(sys.argv[2])
    """


if __name__ == '__main__':
    main()
