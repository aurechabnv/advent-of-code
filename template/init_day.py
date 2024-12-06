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
        content = content.replace(f"# Day", f"# Day {day}: {day_title}") # update comment
        content = content.replace(f"day=0", f"day={day}") # update request

        with open(target_folder / file_name, "w") as f:
            f.write(content)

# update table in README.md
with open(base_path / 'README.md', 'r') as f:
    content = f.read()
matches = re.compile(fr'(\| \[Day \d{int(day)-1}: (.*)].*\|)').search(content)
last_table_line = matches.group(1)
new_table_line = last_table_line.replace(matches.group(2), day_title).replace(str(int(day)-1), day).replace('⭐','')
content = content.replace(last_table_line, last_table_line + '\n' + new_table_line)
with open(base_path / 'README.md', 'w') as f:
    f.write(content)
