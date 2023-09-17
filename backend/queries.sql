-- Tabela de alertas
CREATE TABLE alerts_responses (
    alert_severity INTEGER NULL,
    alert_category VARCHAR (4000) NULL,
    alert_signature VARCHAR (4000) NULL,
    payload VARCHAR (4000) NULL,
    src_ip VARCHAR (4000) NULL,
    whois_dest_ip VARCHAR (4000) NOT NULL,
    src_port INTEGER NULL,
    dest_ip VARCHAR (4000) NULL,
    whois_dest_ip VARCHAR (4000) NOT NULL,
    dest_port INTEGER NULL,
    dest_port_open BOOL NOT NULL,
    incitent BOOL NOT NULL,
    timestamp TIMESTAMP NULL,
);

-- Relatório IPs que mais são atacados
SELECT dest_ip,
    alert_signature,
    dest_port,
    COUNT(*) AS access_count
FROM suricata_logs
GROUP BY dest_ip,
    alert_signature,
    dest_port
ORDER BY access_count DESC;

-- Relatório IPs que mais atacam
SELECT src_ip,
    alert_signature,
    dest_port,
    COUNT(*) AS connection_attempts
FROM suricata_logs
GROUP BY src_ip,
    alert_signature,
    dest_port
ORDER BY connection_attempts DESC;