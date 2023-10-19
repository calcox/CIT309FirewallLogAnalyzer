import unittest
from datetime import datetime
from log_analyzer import LogEntry

class TestLogEntry(unittest.TestCase):

    def test_event_time_conversion(self):
        log_entry = LogEntry()
        event_time_str = "2022-01-01 08:29:25 UTC"
        log_entry.event_time = datetime.strptime(event_time_str, "%Y-%m-%d %H:%M:%S %Z")
        self.assertEqual(log_entry.event_time.month, 1)  #month is 1?
        self.assertEqual(log_entry.event_time.hour, 8)  #hour is 8?

    def test_ipv4_class(self):
        log_entry = LogEntry()

        log_entry.source_ip = "11.177.69.220"
        self.assertEqual(log_entry.ipv4_class, "A")  #class A

        log_entry.source_ip = "173.205.219.112"
        self.assertEqual(log_entry.ipv4_class, "C")  #class C

    def test_invalid_ip(self):
        log_entry = LogEntry()
        log_entry.source_ip = "256.0.0.0" 
        self.assertEqual(log_entry.ipv4_class, "Invalid IP")  #INVALID IP

if __name__ == '__main__':
    unittest.main()
