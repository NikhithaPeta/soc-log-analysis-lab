# Brute-Force Login Investigation

## 1. Investigation Overview

This investigation analyzes authentication logs to identify suspicious login activity.

## 2. Suspicious Activity

The logs show multiple failed SSH login attempts from the same IP address:

- Source IP: 192.168.1.105
- Target username: admin
- Failed attempts: 4
- Time range: 09:41:12 – 09:41:31

A successful login occurred from the same IP address shortly after the failed attempts.

## 3. Analysis

The repeated failed login attempts from the same source IP may indicate a possible brute-force or password-guessing attempt.

The successful login following the failed attempts requires further investigation to determine whether the login was legitimate.

## 4. Indicators

| Indicator | Value |
|---|---|
| Source IP | 192.168.1.105 |
| Protocol | SSH |
| Target username | admin |
| Failed attempts | 4 |
| Successful login | Yes |

## 5. Recommended Actions

- Verify whether the successful login was authorized.
- Review additional authentication logs around the same time.
- Check whether the source IP belongs to a legitimate user or system.
- Consider implementing account lockout or rate-limiting controls.
- Monitor the source IP for additional suspicious activity.

## 6. Conclusion

The observed pattern is suspicious because multiple failed login attempts were followed by a successful login from the same source IP. Further investigation is required to determine whether the activity represents an unauthorized access attempt.
