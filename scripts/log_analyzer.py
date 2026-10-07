import re
from collections import Counter

LOG_FILE = "logs/sample-auth.log"

failed_attempts = []
successful_logins = []

with open(LOG_FILE, "r") as file:
    for line in file:

        # Detect failed login attempts
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip_address = match.group(1)
                failed_attempts.append(ip_address)

        # Detect successful logins
        elif "Accepted password" in line:
            match = re.search(
                r"Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)",
                line
            )

            if match:
                username = match.group(1)
                ip_address = match.group(2)
                successful_logins.append((username, ip_address))

ip_counts = Counter(failed_attempts)

print("SOC Log Analysis")
print("----------------")
print(f"Total failed login attempts: {len(failed_attempts)}")
print(f"Total successful login attempts: {len(successful_logins)}")

print("\nFailed attempts by IP:")

for ip, count in ip_counts.items():
    print(f"{ip}: {count} failed attempts")

print("\nSuspicious IPs:")

for ip, count in ip_counts.items():
    if count >= 3:
        print(f"{ip} -> {count} failed attempts")

print("\nSuccessful logins:")

for username, ip in successful_logins:
    print(f"{ip} -> user: {username}")
