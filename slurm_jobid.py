#!/apps/easybuild/software/Python/3.10.8-GCCcore-12.2.0/bin/python

import subprocess
import sys

def check_slurm_job_details(job_id):
    command = f"sacct -j {job_id} --format=JobID,JobName,Partition,MaxRSS,Elapsed,CPUTime,State,Submit,User,NodeList,Workdir%-50,ReqCPUS"

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # The first command-line argument (sys.argv[0]) is the script name
        # The actual arguments start from sys.argv[1]
        job_id_to_check = sys.argv[1]
        print("Job ID is:", job_id_to_check)
    else:
        sys.exit("No arguments provided. Please specify the Slurm Job ID")
    # Specify your Slurm job ID
    
    check_slurm_job_details(job_id_to_check)
