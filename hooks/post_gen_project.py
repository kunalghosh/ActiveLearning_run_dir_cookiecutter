import os
import shutil

print("Copying {{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh to each of the run directories.")
for _dir in "run1 run2 run3 run4 run5".split():
    shutil.copy("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh",
                f"{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/{_dir}/")
    print(f"Copied to {_dir}")

os.remove("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh")
print(f"Deleted {{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh")
