import os
import shutil

random_seeds = [1234,2345,3456,4567,5678]
input_template = ""
with open("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/input.dat","r") as f:
    input_template = f.read()

print("Copying {{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh to each of the run directories.")
for idx, _dir in enumerate("run1 run2 run3 run4 run5".split()):
    shutil.copy("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh",
                f"{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/{_dir}/")
    print(f"Copied to {_dir}")
    with open(f"{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/{_dir}/input.dat","w") as f:
        f.write(input_template.replace("{random_seed}",str(random_seeds[idx])))
    print(f"Copied input.dat2 to {_dir}")

os.remove("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh")
os.remove("{{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/input.dat")
print(f"Deleted {{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/slurm_compute_mae.sh")
print(f"Deleted {{cookiecutter.dataset}}_{{cookiecutter.strategy}}_{{cookiecutter.batchsize}}/input.dat")
