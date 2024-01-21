import os
import json
import AppOpener


current_directory = os.getcwd()
file_directory = f"{current_directory}/apps.json"
canUseCommands = True


def read():
    with open(file_directory, "r") as f:
        data = json.load(f)
        return data


def display(data):
    print()
    for i, v in enumerate(data):
        print(f"{i+1}. {v}")
    print()


def begin():
    if "apps.json" not in os.listdir():
        # print('not there')
        with open("apps.json", "w"):
            pass
    fileHandle()


def fileHandle():
    global canUseCommands
    size = os.path.getsize(file_directory)
    # print(size)
    if size == 0:
        print("No data. Please add.")
        canUseCommands = False
    userCommands()


def oa():
    data = {str: list}
    if canUseCommands:
        with open(file_directory, "r") as f:
            data = json.load(f)
            for i in data["apps"]:
                AppOpener.open(i, match_closest=True)
    else:
        print("No data. Please add first.")


def add():
    global canUseCommands
    jsonData = {}
    item = input(f"Enter App name: ")
    if canUseCommands:
        data = read()
        data["apps"].append(item)
        with open(file_directory, "w") as f:
            f.write(json.dumps(data))
    else:
        jsonData["apps"] = [item]
        with open(file_directory, "w") as f:
            f.write(json.dumps(jsonData, indent=4))
        canUseCommands = True


def remove():
    show()
    item = input(f"Enter app name to remove: ")
    data: list = read()["apps"]
    if item in data:
        data.remove(item)
        jsonData = {"apps": data}
        with open(file_directory, "w") as f:
            f.write(json.dumps(jsonData))
    else:
        print("Item doesn't exist.\n")


def show():
    print("Showing All:")
    if canUseCommands:
        data = read()
        data = data["apps"]
        display(data)
    else:
        print("No Data to show\n")


def userCommands():
    while True:
        print("=" * 10)
        query: str = input(
            "Open All (oa)\nAdd (a)\nRemove (r)\nShow All (s)\nClose (c)\n=> "
        ).lower()
        print("=" * 10, "\n")
        match query:
            case "open all" | "o":
                oa()
            case "add" | "a":
                add()
            case "remove" | "r":
                remove()
            case "show all" | "s":
                show()
            case "close" | "c":
                exit()
            case _:
                print("Invalid option.\n")
                continue
        print()


if __name__ == "__main__":
    begin()
