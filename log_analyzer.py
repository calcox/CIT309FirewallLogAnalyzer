from datetime import datetime
import re

class LogEntry:
    event_time: datetime
    internal_ip: int
    port_number: int
    protocol: int
    action: int
    rule_id: int
    source_ip: str
    country: int
    country_name: int
    
    @property
    def ipv4_class(self):
        ipv4_pattern = r'^(\d+)\.'
        match = re.match(ipv4_pattern, self.source_ip)
        if match:
            first_component = int(match.group(1))
            if 0 <= first_component <= 127:
                return "A"
            elif 128 <= first_component <= 191:
                return "B"
            elif 192 <= first_component <= 223:
                return "C"
            elif 224 <= first_component <= 239:
                return "D"
            else:
                return "Unknown"
        else:
            return "Invalid IP"

log_entry = LogEntry()
log_entry.source_ip = "11.177.69.220"
print(log_entry.ipv4_class)  # Output will be: "A"

log_entry.source_ip = "173.205.219.112"
print(log_entry.ipv4_class)  # Output will be: "C"
