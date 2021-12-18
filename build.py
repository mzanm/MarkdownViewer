import shutil
import os
import PyInstaller.__main__ as pm


def cleanup(dist):
    shutil.rmtree("build", True)
    if dist:
        shutil.rmtree("dist", True)
    try:
        os.remove("MarkdownViewer.spec")
    except FileNotFoundError:
        pass
    shutil.rmtree("__pycache__", True)


cleanup(True)

pm.run(
    [
        "--windowed",
        "--clean",
        "mdviewer.py",
        "--exclude-module=_ssl",
        "--exclude-module=pyreadline",
        "--exclude-module=difflib",
        "--exclude-module=tcl",
        "--exclude-module=optparse",
        "--exclude-module=pickle",
        "--exclude-module=pdb",
        "--exclude-module=unittest",
        "--exclude-module=test",
        "--exclude-module=doctest",
        "--exclude-module=tkinter",
        "--name=MarkdownViewer",
    ]
)

cleanup(False)
