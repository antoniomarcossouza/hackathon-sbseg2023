# Hello, world!

### Microsservices
---
### Alerts

Receives alerts from the other services and sends them to the user
```
Timestamp: 08/15/2023 21:46:27.168562
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
  "signature": 1,
  "rule_id": 2100498,
  "detection_count": 7,
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

```sql
CREATE TABLE alerts (
    id VARCHAR PRIMARY KEY,
    timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    signature_id INTEGER NOT NULL,
    rule_id INTEGER NOT NULL,
    detection_count INTEGER NOT NULL,
    alert_type VARCHAR NOT NULL,
    classification VARCHAR NOT NULL,
    priority INTEGER NOT NULL,
    protocol VARCHAR NOT NULL,
    source_ip VARCHAR NOT NULL,
    source_port INTEGER NOT NULL,
    destination_ip VARCHAR NOT NULL,
    destination_port INTEGER NOT NULL
);

```

```sql
INSERT INTO alerts (
        id,
        timestamp,
        signature_id,
        rule_id,
        detection_count,
        alert_type,
        classification,
        priority,
        protocol,
        source_ip,
        source_port,
        destination_ip,
        destination_port
    )
VALUES (
        '08/15/2023 21:46:27.168562_108.138.128.54_2100498',
        '08/15/2023 21:46:27.168562',
        1,
        2100498,
        7,
        'GPL ATTACK_RESPONSE',
        'Potentially Bad Traffic',
        2,
        'TCP',
        '108.138.128.54',
        80,
        '10.5.0.2',
        55312
    );

```