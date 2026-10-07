# Security Incident Report

## 1. Incident Summary

Multiple failed SSH authentication attempts were observed from the same source IP address, followed by a successful login.

The activity was reviewed as a potential brute-force or password-guessing attempt.

## 2. Incident Details

| Field | Details |
|---|---|
| Incident Type | Suspicious Authentication Activity |
| Protocol | SSH |
| Source IP | 192.168.1.105 |
| Target Account | admin |
| Failed Attempts | 4 |
| Successful Login | Yes |
| Severity | Medium |
| Status | Requires Further Investigation |

## 3. Timeline

| Time | Event |
|---|---|
| 09:41:12 | Failed login attempt |
| 09:41:18 | Failed login attempt |
| 09:41:25 | Failed login attempt |
| 09:41:31 | Failed login attempt |
| 09:41:39 | Successful login |

## 4. Analysis

Four failed authentication attempts were observed within a short period from the same source IP address.

A successful login occurred shortly afterward from the same IP.

This pattern is suspicious and may indicate password guessing or brute-force activity. However, the available logs are not sufficient to confirm unauthorized access.

## 5. Recommended Response

1. Verify whether the successful login was authorized.
2. Review additional authentication and system logs.
3. Investigate the source IP address.
4. Check for unusual activity after the successful login.
5. Monitor the affected account.
6. Reset credentials if unauthorized access is confirmed.

## 6. Indicators of Interest

- Source IP: `192.168.1.105`
- Protocol: `SSH`
- Target account: `admin`
- Multiple failed authentication attempts
- Successful authentication following failures

## 7. Conclusion

The activity should be treated as suspicious until additional evidence confirms whether the successful login was legitimate.

Further log analysis and user verification are recommended before determining whether the event represents a confirmed security incident.

## 8. Analyst Learning

This investigation provided practice in:

- Authentication log analysis
- Identifying suspicious login patterns
- Building an incident timeline
- Extracting indicators
- Assessing potential security incidents
- Writing basic incident reports
