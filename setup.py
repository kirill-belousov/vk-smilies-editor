from cx_Freeze import setup, Executable

setup(
    name = "vk-smilies-editor",
    version = "0.2",
    description = "editing the vk smilies reader dictionaries",
    executables = [Executable("main.py")]
)