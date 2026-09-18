from pathlib import Path


art_folder = Path("../../fart")

def moveFile(path):
    for f in path.glob("*.kra"):
        f.move_into(f"{path}/kra")
    for directory in path.iterdir():
        if directory.is_dir() and "kra" not in directory.stem:
            moveFile(directory)
            for f in directory.glob("*.kra"):
                f.move_into(f"{directory}/kra")
                print(f"placed in {directory}!")


moveFile(art_folder)
