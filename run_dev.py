import subprocess

commands = [
    ["pip", "uninstall", "ui-finder", "-y"],
    ["pip", "install", "-e", "."],
    ["ui_finder"]
]

for cmd in commands:
    print(f"\n🔧 Running: {' '.join(cmd)}")
    subprocess.run(cmd)
