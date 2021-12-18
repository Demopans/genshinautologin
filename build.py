# in progress
import sys, os
if sys.platform.startswith('freebsd'):
    pass
elif sys.platform.startswith('linux'):
    pass
elif sys.platform.startswith('aix'):
    pass
elif sys.platform.startswith('win32'):
    os.system(r'.\venv\Scripts\pyinstaller --onefile --paths '
              r'.\venv\Lib\site-packages '
              r'.\main.py --distpath ./dd')
elif sys.platform.startswith('cygwin'):
    os.system(r'.\venv\Scripts\pyinstaller --onefile --paths '
              r'.\venv\Lib\site-packages '
              r'.\main.py --distpath ./dd')
elif sys.platform.startswith('darwin'):
    pass

