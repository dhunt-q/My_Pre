import subprocess

def run_script(script_path, script_name):
    try:
        print(f"\n=== Running {script_name} ===\n")
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error in {script_name}:\n{result.stderr}")
            exit(1)  # Exit if any script fails
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")
        exit(1)

if __name__ == "__main__":
    print("Starting automated NBA player stats prediction pipeline...")

    # Step 1: Fetch Data
    run_script("scripts/fetch_data.py", "Fetch Data")

    # Step 2: Preprocess Data
    run_script("scripts/preprocess_data.py", "Preprocess Data")

    # Step 3: Train the Model
    run_script("scripts/train_model.py", "Train Model")

    # Step 4: Predict Stats
    run_script("scripts/predict_stats.py", "Predict Stats")

    print("\n=== Pipeline completed successfully! ===\n")
