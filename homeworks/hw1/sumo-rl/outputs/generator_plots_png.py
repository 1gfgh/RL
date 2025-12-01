import subprocess
import os
from tqdm import tqdm

os.makedirs("plots", exist_ok=True)

runs = int(input("Runs cnt: "))
is_mine = (input("Is mine model? y/n\n")) == 'y'
episodes = 4

for run in range(1, runs + 1):
    for episode in tqdm(range(1, episodes + 1)):
        cmd = [
            "python", "plot.py",
            "-f", f"my_ql-4x4grid_run{run}_conn0_ep{episode}.csv",
            "-l", f"My QLAgent (run {run}, ep {episode})",
            "-t", f"My QLAgent - Run {run}, Episode {episode}",
            "-yaxis", "system_total_waiting_time",
            "-ma", "10",
            "-output", f"plots/my_ql_run{run}_ep{episode}.png"
        ]
        if not is_mine:
            cmd = [
                "python", "plot.py",
                "-f", f"baseline_ql-4x4grid_run{run}_conn0_ep{episode}.csv",
                "-l", f"Base QLAgent (run {run}, ep {episode})",
                "-t", f"Base QLAgent - Run {run}, Episode {episode}",
                "-yaxis", "system_total_waiting_time",
                "-ma", "10",
                "-output", f"plots/base_ql_run{run}_ep{episode}.png"
            ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print("Ошибка для")
                print(f"Run {run} ep {episode}\n\n")
        except Exception as e:
            print(f"{e}")
