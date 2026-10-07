# Suspicious Login Investigation

## 1. Investigation Overview

This investigation reviews authentication events to identify potentially suspicious login activity.

## 2. Observed Activity

The logs contain multiple failed login attempts from different source IP addresses.

The investigation focuses on identifying unusual authentication patterns and determining whether additional investigation is required.

## 3. Investigation Questions

The following questions were considered:

- Which IP addresses generated failed login attempts?
- Which usernames were targeted?
- Were there repeated attempts within a short period?
- Was a successful login observed after failed attempts?
- Was the successful login authorized?

## 4. Analysis

Repeated failed authentication attempts can indicate password guessing or brute-force activity.

However, failed login attempts alone do not prove that an attack occurred. Additional context such as user activity, source IP ownership, login location, and authentication history should be reviewed.

## 5. Recommended SOC Actions

- Verify the affected user's activity.
- Review authentication logs around the event.
- Investigate the source IP addresses.
- Check for additional failed or successful authentication events.
- Monitor the affected account for unusual activity.
- Escalate the incident if unauthorized access is suspected.

## 6. Conclusion

The observed authentication activity should be investigated further because unusual login patterns can be an early indicator of attempted unauthorized access.

Additional logs and contextual information would be required before confirming a security incident.
