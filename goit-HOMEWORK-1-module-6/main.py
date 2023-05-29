# Сортування файлів у папці
# Хз як


from pathlib import Path
from shutil import copyfile
import argparse


parser = argparse.ArgumentParser(description="Sorting folder")

parser.add_argument("--source", "-s", help="source folder")  # ім'я змінної

parser.add_argument("--output", "-o", default="dist", help="output folder")  # результат

args = vars(parser.parse_args())  # parser.parse_args() парсер, vars - поверне словник

source = args.get("source")
output = args.get("output")

# print(f"args is {args}")

# print(source, output)


def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            ext = element.suffix
            new_path = output_folder / ext
            new_path.mkdir(exist_ok=True, parents=True)
            copyfile(element, new_path / element.name)


# def copy_file_handler(file: Path):
# ext = file.suffix
# new_path = output_folder / ext
# new_path.mkdir(exist_ok=True, parents=True)
# copyfile(file, new_path / file.name)


# begin
# print(Path(output))
# print(Path(source))


output_folder = Path(output)  # dist = > Path(folder`s_Name_destination)
read_folder(Path(source))  # source => Path(namr_folder_dor_pictures)
