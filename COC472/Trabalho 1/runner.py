# Imports
import subprocess
import os

os.makedirs("./output", exist_ok=True)

# For 100 GB of RAM
MEM_START = 10000
MEM_END = 110000
MEM_STEP = 10000

# C ij
print("="*20)
print("C Program (ij loop)")
print("="*20)
elapsed_c_ij = {}
for i in range(MEM_START, MEM_END + 1, MEM_STEP):
    e = float(subprocess.run(["./c/main", str(i), "0"], capture_output=True, text=True).stdout)
    elapsed_c_ij[i] = e
    print(f"{i}/110000 >> {e}")
with open("./output/output_c_ij.csv", "w") as f:
    f.write("n,elapsed\n")
    for index, value in elapsed_c_ij.items():
        f.write(f"{index},{value}\n")

# C ji
print("="*20)
print("C Program (ji loop)")
print("="*20)
elapsed_c_ji = {}
for i in range(MEM_START, MEM_END + 1, MEM_STEP):
    e = float(subprocess.run(["./c/main", str(i), "1"], capture_output=True, text=True).stdout)
    elapsed_c_ji[i] = e
    print(f"{i}/110000 >> {e}")
with open("./output/output_c_ji.csv", "w") as f:
    f.write("n,elapsed\n")
    for index, value in elapsed_c_ji.items():
        f.write(f"{index},{value}\n")

# Fortran ij
print("="*20)
print("Fortran Program (ij loop)")
print("="*20)
elapsed_fortran_ij = {}
for i in range(MEM_START, MEM_END + 1, MEM_STEP):
    e = float(subprocess.run(["./fortran/main", str(i), "0"], capture_output=True, text=True).stdout)
    elapsed_fortran_ij[i] = e
    print(f"{i}/110000 >> {e}")
with open("./output/output_fortran_ij.csv", "w") as f:
    f.write("n,elapsed\n")
    for index, value in elapsed_fortran_ij.items():
        f.write(f"{index},{value}\n")

# Fortran ji
print("="*20)
print("Fortran Program (ji loop)")
print("="*20)
elapsed_fortran_ji = {}
for i in range(MEM_START, MEM_END + 1, MEM_STEP):
    e = float(subprocess.run(["./fortran/main", str(i), "1"], capture_output=True, text=True).stdout)
    elapsed_fortran_ji[i] = e
    print(f"{i}/110000 >> {e}")
with open("./output/output_fortran_ji.csv", "w") as f:
    f.write("n,elapsed\n")
    for index, value in elapsed_fortran_ji.items():
        f.write(f"{index},{value}\n")