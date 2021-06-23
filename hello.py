# import os


# def make_new_address(path: str):
#     build_up = os.path.dirname(path)
#     file_name = os.path.basename(path)
#     new_path = os.path.join(build_up, file_name + ".old")
#     print(new_path)


# current_working_directory = os.getcwd()
# path_to_test = os.path.join(current_working_directory, "test.log")
# make_new_address(path_to_test)

from pathlib import Path


def make_new_address(path: Path):
    parent = path.parent
    file = path.name
    print(parent.joinpath(file + ".old"))


p = Path.cwd()
p = p / "test.log"
make_new_address(p)
