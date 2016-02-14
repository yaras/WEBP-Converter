from cx_Freeze import setup, Executable

includefiles = []
includes = []
excludes = []
packages = ["PIL.Image", "PIL.WebPImagePlugin"]

setup(
    name = "WEBP Converter",
    version = "0.1.0",
    description = "This is my program",
    options = {'build_exe': {'includes': includes, 'excludes': excludes, 'packages': packages, 'include_files': includefiles}},
    executables = [Executable("converter.py")]
    )
