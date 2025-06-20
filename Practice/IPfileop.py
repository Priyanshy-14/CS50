'''4: Log File Analyzer Problem:
Given a simulated log file (text file), extract: All IP addresses (format: 192.168.0.1), All timestamps ([12/Jun/2024:10:30:00 +0530]), Use exception handling for: File not found, No pattern match (custom error)
'''
import re

class NoPatternMatch(Exception):
    pass

filename = "log.txt"

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
time_pattern = r"\[\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4}\]"

try:
    with open(filename, 'r') as file:
        content = file.read()

    ips = re.findall(ip_pattern, content)
    timestamps = re.findall(time_pattern, content)

    if not ips and not timestamps:
        raise NoPatternMatch(" No IP addresses or timestamps found in the log.")

    print(" IP Addresses Found:")
    for ip in ips:
        print(ip)

    print("\n Timestamps Found:")
    for time in timestamps:
        print(time)

except FileNotFoundError:
    print(" Error: Log file not found.")
except NoPatternMatch as e:
    print(e)

