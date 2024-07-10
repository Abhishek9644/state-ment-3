
analyze a web server log file for common patterns such as 404 errors, most requested pages, and IP addresses with the most requests, 


import re
from collections import Counter

# Function to parse Apache/Nginx log file
def parse_log_file(log_file):
    ip_addresses = []
    requested_pages = []
    status_codes = []
    
    with open(log_file, 'r') as file:
        for line in file:
            # Example log format: 127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /page HTTP/1.1" 404
            parts = re.split(r'\s+', line)
            
            if len(parts) > 3:
                ip_addresses.append(parts[0])
                requested_pages.append(parts[6])
                status_codes.append(parts[8])
    
    return ip_addresses, requested_pages, status_codes

# Function to analyze log data and generate report
def generate_report(ip_addresses, requested_pages, status_codes):
    total_requests = len(ip_addresses)
    count_404_errors = status_codes.count('404')
    
    most_requested_pages = Counter(requested_pages).most_common(5)
    top_ip_addresses = Counter(ip_addresses).most_common(5)
    
    report = f"Log Analysis Report\n\n"
    report += f"Total requests: {total_requests}\n"
    report += f"Number of 404 errors: {count_404_errors}\n\n"
    
    report += f"Top 5 requested pages:\n"
    for page, count in most_requested_pages:
        report += f"{page}: {count} requests\n"
    
    report += f"\nTop 5 IP addresses with the most requests:\n"
    for ip, count in top_ip_addresses:
        report += f"{ip}: {count} requests\n"
    
    return report

# Example usage:
log_file = '/path/to/your/access.log'  # Replace with your log file path
ip_addresses, requested_pages, status_codes = parse_log_file(log_file)
report = generate_report(ip_addresses, requested_pages, status_codes)

# Print or save the report
print(report)

# Optionally, save report to a file
report_file = 'log_analysis_report.txt'
with open(report_file, 'w') as file:
    file.write(report)

print(f"Report generated and saved to {report_file}")
