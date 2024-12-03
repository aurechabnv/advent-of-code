from datetime import datetime
from pathlib import Path
import shutil

cur_year = datetime.today().year
cur_day = datetime.today().day

# user inputs
year = input(f"Year (default {cur_year}) : ") or str(cur_year)
day = input(f"Day (default {cur_day}) : ") or str(cur_day)

base_path = Path(__file__).resolve().parent.parent
template_folder = base_path / 'template' / 'day_0'
target_folder = base_path / year / f"day_{day}"

target_folder.mkdir(parents=True, exist_ok=True)

# copy template files to target folder
for child in template_folder.iterdir():
    if child.suffix == '.py':
        file_name = child.name.replace('0', day)
        shutil.copy(child, target_folder / file_name)

        # load file for update
        with open(target_folder / file_name, 'r') as f:
            content = f.read()

        content = content.replace(f"day_0", f"day_{day}") # update import
        content = content.replace(f"# Day", f"# Day {day}") # update comment
        content = content.replace(f"day=0", f"day={day}") # update request

        with open(target_folder / file_name, "w") as f:
            f.write(content)
