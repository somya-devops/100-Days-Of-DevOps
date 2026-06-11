import os

# Core Logic: Simulated web server log entries
server_logs = [
    "2026-06-11 12:00:01 INFO User logged in successfully",
    "2026-06-11 12:01:15 ERROR 404 Page not found on /profile",
    "2026-06-11 12:02:42 INFO API call returned status 200",
    "2026-06-11 12:03:10 CRITICAL 500 Internal Server Error on database connection"
]

print("🔍 Scanning logs for critical errors (404/500)...")
print("-" * 50)

error_count = 0

# Iteration & String Matching
for log in server_logs:
    if "404" in log or "500" in log:
        print(f"🚨 ALERT: {log}")
        error_count += 1

print("-" * 50)
print(f"✅ Scan complete. Total critical errors found: {error_count}")