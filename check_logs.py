from database import read_log

for name in ["warren", "george", "ray", "cathie"]:
    print(f"\n{'='*50}")
    print(f"{name.upper()} LOGS (Last 20)")
    print(f"{'='*50}")
    logs = read_log(name, last_n=20)
    if logs:
        for timestamp, log_type, message in logs:
            print(f"[{log_type}] {timestamp}: {message}")
    else:
        print("No logs found")