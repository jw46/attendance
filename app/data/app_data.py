import pandas as pd
import app.apputil.util as util

groups: list[str] = None
selected_group_index: int = -1
selected_group: str = None
selected_student = None
group_list = []
selected_date = util.get_today()
students_df: pd.DataFrame = None
class_df: pd.DataFrame = None
current_ui: str = 'Select a different group'
waiting = False
