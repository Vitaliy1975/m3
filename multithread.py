import concurrent.futures
from pathlib import Path
import shutil

def copy_sorter(source_directory,destination_directory="/dist"):
    destination_directory_path=Path(destination_directory)
    source_directory_path=Path(source_directory)
    try:
        Path.mkdir(destination_directory_path,mode=0o777,parents=False,exist_ok=True)
    except Exception as e:
        print(e)
    try:
        if source_directory_path.exists() and source_directory_path.is_dir():
            for sub in source_directory_path.rglob("*"):
                name=sub.name
                absolute_path=sub.absolute()
                suffix_dir=sub.suffix
                suffix_dir=suffix_dir.strip(".")
                full_destination_path=destination_directory_path / suffix_dir / name
                if suffix_dir=="":
                    continue
                else:
                    try:
                        Path.mkdir(destination_directory_path / suffix_dir,mode=0o777,parents=False,exist_ok=True)
                        shutil.copy2(absolute_path,full_destination_path,)
                    except Exception as e:
                        print(e)

        else:
            print(f"'{source_directory_path}' is not a directory or '{source_directory_path}' does not exist.")
    except Exception as e:
        print(e)



if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(copy_sorter("d:\goit\\test","d:\goit\sorted"))
    # copy_sorter("D:\\goit\\test","D:\\goit\\sort")
