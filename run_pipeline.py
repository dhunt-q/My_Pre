import os
import subprocess

def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        result = subprocess.run(
            ["python", script_name], capture_output=True, text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"Error while running {script_name}:\n{result.stderr}")
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")

if __name__ == "__main__":
    scripts = [
        "scripts/fetch_data.py",
        "scripts/preprocess_data.py",
        "scripts/train_model.py",
        "scripts/predict_stats.py",
    ]
    
    for script in scripts:
        run_script(script)
    print("All scripts executed successfully!")
