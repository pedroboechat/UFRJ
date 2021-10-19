import subprocess
import re
import os
os.chdir(os.path.dirname(__file__))
os.makedirs("./data", exist_ok=True)

MAX_CPU = 16
COMMAND = ["mpiexec", "-n", str(MAX_CPU), "./xhpl"]

with open("./data/run.csv", mode="w") as out:
    out.write("T/V;N;NB;P;Q;time;gflops\n")
    for ns in [5040, 10000]:
        for nbs in [32, 64, 128, 256]:
            for p, q in [(1,16), (2,8), (4,4), (8,8), (16,1)]:
                print(f"Running for Ns={ns}, NBs={nbs}, p={p}, q={q}")
                with open("HPL.dat", mode="w") as HPL:
                    HPL.write(f"""HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
{ns}       Ns
1            # of NBs
{nbs}          NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
{p}            Ps
{q}            Qs
16.0         threshold
1            # of panel fact
2            PFACTs (0=left, 1=Crout, 2=Right)
1            # of recursive stopping criterium
4            NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
1            # of recursive panel fact.
1            RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
1            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1            # of lookahead depth
1            DEPTHs (>=0)
2            SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0            L1 in (0=transposed,1=no-transposed) form
0            U  in (0=transposed,1=no-transposed) form
1            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)""")
                result = subprocess.run(COMMAND, stdout=subprocess.PIPE).stdout.decode('utf-8')
                print(result)
                try:
                    result = result[result.index("WR11C2R4"):]
                    result = result[:result.index("\n")]
                    result = re.sub(" +", ";", result)
                except:
                    pass
                out.write(result)
                out.write("\n")
    for ns in [20000, 40000, 60000]:
        print(f"Running for Ns={ns}, NBs={nbs}, p={p}, q={q}")
        with open("HPL.dat", mode="w") as HPL:
            HPL.write(f"""HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
{ns}       Ns
1            # of NBs
256          NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
1            Ps
16           Qs
16.0         threshold
1            # of panel fact
2            PFACTs (0=left, 1=Crout, 2=Right)
1            # of recursive stopping criterium
4            NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
1            # of recursive panel fact.
1            RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
1            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1            # of lookahead depth
1            DEPTHs (>=0)
2            SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0            L1 in (0=transposed,1=no-transposed) form
0            U  in (0=transposed,1=no-transposed) form
1            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)""")
        result = subprocess.run(COMMAND, stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        try:
            result = result[result.index("WR11C2R4"):]
            result = result[:result.index("\n")]
            result = re.sub(" +", ";", result)
        except:
            pass
        out.write(result)
        out.write("\n")