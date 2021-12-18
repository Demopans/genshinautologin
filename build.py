# in progress
import platform, os
if platform.system() == 'Windows':
    os.system(r'.\venv\Scripts\pyinstaller --onefile --paths E:\JetBrains\IntelljProjects\genshinautologin\venv\Lib\site-packages E:\JetBrains\IntelljProjects\genshinautologin\main.py --distpath ./dd')

