import os
from pathlib import Path

name = Path("./{}".format(input()))
new_name = input()


if name.is_file():
    os.rename(name, new_name)
    print("Done")
else:
    print("Error 404")
