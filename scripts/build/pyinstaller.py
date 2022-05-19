import PyInstaller.__main__

def main():
    PyInstaller.__main__.run([
        './genshinautocheckin/main.py',
        '--onefile',
        '--specpath',
        './build',
        '--distpath',
        './build'
    ])

if __name__ == '__main__':
    main()
