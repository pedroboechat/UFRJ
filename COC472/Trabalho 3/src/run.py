# Imports
import subprocess
from os import makedirs
makedirs("./data", exist_ok=True)

# Constant definitions
MAX_THREADS = 16
COMPILED_FILE = "./laplace"

# Compile the code with specified flags
def compile_laplace(o3, openmp):
    flags = []
    if openmp:
        file = "./laplace_omp.cxx"
        flags.append("-fopenmp")
    else:
        file = "./laplace.cxx"
    if o3: flags.append("-O3")
    print("Compiling with flags:", flags)
    result = subprocess.run(["g++", file, "-o", "laplace"] + flags, stdout=subprocess.PIPE)
    if result.returncode != 0: raise RuntimeError("Compilation Error with flags:", flags)

with open("./data/run.csv", mode="w") as out:
    out.write("flags;n_threads;nx;result;elapsed\n")
    # Run without OMP
    ## Run without flags
    compile_laplace(o3=False, openmp=False)
    for nx in [512, 1024, 2048]:
        print(f"No flags and nx = {nx}")
        result = subprocess.run([COMPILED_FILE, str(nx)], stdout=subprocess.PIPE).stdout.decode('utf-8')
        out.write(f"None;1;{nx};{result}")
    ## Run with -O3
    compile_laplace(o3=True, openmp=False)
    for nx in [512, 1024, 2048]:
        print(f"O3 and nx = {nx}")
        result = subprocess.run([COMPILED_FILE, str(nx)], stdout=subprocess.PIPE).stdout.decode('utf-8')
        out.write(f"O3;1;{nx};{result}")

    # Run with OMP
    ## Run without O3
    compile_laplace(o3=False, openmp=True)
    for n_threads in range(1, MAX_THREADS+1):
        for nx in [512, 1024, 2048]:
            print(f"fopenmp, threads = {n_threads} and nx = {nx}")
            result = subprocess.run([COMPILED_FILE, str(nx)], stdout=subprocess.PIPE, env={"OMP_NUM_THREADS": str(n_threads)}).stdout.decode('utf-8')
            out.write(f"fopenmp;{n_threads};{nx};{result}")
    ## Run with O3
    compile_laplace(o3=True, openmp=True)
    for n_threads in range(1, MAX_THREADS+1):
        for nx in [512, 1024, 2048]:
            print(f"fopenmp + O3, threads = {n_threads} and nx = {nx}")
            result = subprocess.run([COMPILED_FILE, str(nx)], stdout=subprocess.PIPE, env={"OMP_NUM_THREADS": str(n_threads)}).stdout.decode('utf-8')
            out.write(f"fopenmp+O3;{n_threads};{nx};{result}")