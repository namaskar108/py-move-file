import os


def move_file(command: str) -> None:
    files = command.split()
    file_1 = files[1]
    file_2 = files[2]
    if not os.path.basename(file_2):
        file_2 += file_1
    new_path = os.path.dirname(file_2)
    if new_path:
        os.makedirs(new_path, exist_ok=True)

    with open(file_1, "r") as file, open(file_2, "w") as new_file:
        new_file.write(file.read())
    os.remove(file_1)
