import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name="Slither"
    options={"build_exe":{"packages":["pygame"], "include_files":["snakehead.png"]}},

    description = "Slither Game",
    executables = executables
    )
