# Hello, world!

### Microsservices
- **Alerts:** Receives alerts from the other services and sends them to the user
```plaintext
Timestamp: 08/15/2023–21:46:27.168562
Alert ID: 1:2100498:7
Alert Type: GPL ATTACK_RESPONSE
Classification: Potentially Bad Traffic
Priority: 2
Protocol: TCP
Source IP: 108.138.128.54
Source Port: 80
Destination IP: 10.5.0.2
Destination Port: 55312
```
Receive JSON in this format:
```json
{
  "timestamp": "08/15/2023–21:46:27.168562",
  "alert_id": "1:2100498:7",
  "alert_type": "GPL ATTACK_RESPONSE",
  "classification": "Potentially Bad Traffic",
  "priority": 2,
  "protocol": "TCP",
  "source_ip": "108.138.128.54",
  "source_port": 80,
  "destination_ip": "10.5.0.2",
  "destination_port": 55312
}
```
And treat `alert_id` before uploading to the database.
```json
"alert_id": {
    "signature_id": 1,
    "rule_id": "2100498",
    "detection_count": 7
}
```

In the Alert ID we have:

1: signature ID that triggered the alert. In this case, the signature is SURICATA Applayer Detect protocol only one direction.
2100498: rule ID. It is an internal identifier used by Suricata to track its rules.
7: detection count. It indicates how many times this signature has been triggered in the current session.

src https://medium.com/@rubenszimbres/install-a-real-time-intrusion-detection-system-ids-with-suricata-and-python-7ce7ae78c5a3

https://realpython.com/python-microservices-grpc/#why-microservices