import subprocess

roots_output = subprocess.check_output(["pants", "roots"], text=True)
print(roots_output)
