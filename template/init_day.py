import re
from datetime import datetime
from pathlib import Path
import shutil

cur_year = datetime.today().year
cur_day = datetime.today().day

# user inputs
year = input(f"Year (default {cur_year}) : ") or str(cur_year)
day = input(f"Day (default {cur_day}) : ") or str(cur_day)
day_title = ''
while not day_title:
    day_title = input(f"Day Title (required) : ").title()

base_path = Path(__file__).resolve().parent.parent
template_folder = base_path / 'template' / 'day_00'
target_folder = base_path / year / f"day_{day.zfill(2)}"

target_folder.mkdir(parents=True, exist_ok=True)

# copy template files to target folder
for child in template_folder.iterdir():
    if child.suffix == '.py':
        file_name = child.name.replace('00', day.zfill(2))
        shutil.copy(child, target_folder / file_name)

        # load file for update
        with open(target_folder / file_name, 'r') as f:
            content = f.read()

        content = content.replace(f"day_00", f"day_{day.zfill(2)}") # update import
        content = content.replace(f"# Day", f"# Day {day}: {day_title}") # update comment
        content = content.replace(f"day=0", f"day={day}") # update request

        with open(target_folder / file_name, "w") as f:
            f.write(content)

# update table in README.md
with open(base_path / 'README.md', 'r') as f:
    content = f.read()
matches = re.compile(fr'(\| \[Day ({str(int(day)-1).zfill(2)}): (.*)].*\|)').search(content)
last_table_line = matches.group(1)
new_table_line = ((last_table_line.replace(matches.group(2), day.zfill(2))
                                  .replace(matches.group(3), day_title))
                                  .replace('⭐',''))
content = content.replace(last_table_line, last_table_line + '\n' + new_table_line)
with open(base_path / 'README.md', 'w') as f:
    f.write(content)
