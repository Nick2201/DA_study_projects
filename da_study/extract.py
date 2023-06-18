from pathlib import Path
from dataclasses import dataclass,field

@dataclass
class DataSet:
    tasks_path_input:str
    TASKS_PATH: str = field(init=False,repr=False)

    def extension_change(self):
        old_f_name = Path(self.tasks_path_input)
        new_f_name = old_f_name.with_name('TASKS')
        self.TASKS_PATH= old_f_name.rename(new_f_name.with_suffix('.md'))
        print('TASKS.md have created')

