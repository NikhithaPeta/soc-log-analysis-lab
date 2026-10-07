# SOC Log Analysis Lab

A beginner-friendly cybersecurity project focused on analyzing authentication logs, identifying suspicious login activity, and documenting investigation findings.

## Objective

The objective of this project is to practice basic Security Operations Center (SOC) investigation techniques using authentication logs.

## Scenario

The authentication logs contain multiple failed SSH login attempts followed by a successful login from the same source IP address.

The activity is investigated to determine whether it may represent a possible brute-force or password-guessing attempt.

## Tools & Technologies

- Linux authentication logs
- SSH
- Log analysis
- Basic incident investigation
- GitHub

## Investigation Performed

The investigation focused on:

- Identifying repeated failed login attempts
- Identifying the source IP address
- Reviewing timestamps
- Identifying the targeted username
- Checking for a successful login after repeated failures
- Documenting indicators and recommended actions

## Key Finding

Four failed login attempts were observed from `192.168.1.105`, followed shortly by a successful login from the same IP address.

This activity is considered suspicious and requires further investigation to determine whether the successful login was authorized.

## Indicators

| Indicator | Value |
|---|---|
| Source IP | `192.168.1.105` |
| Protocol | SSH |
| Target username | `admin` |
| Failed attempts | 4 |
| Successful login | Yes |

## Recommended Actions

- Verify whether the successful login was authorized.
- Review additional authentication logs.
- Investigate the source IP.
- Monitor for additional suspicious activity.
- Consider rate limiting or account lockout controls.

## What I Learned

Through this project, I practiced:

- Reading authentication logs
- Identifying suspicious login patterns
- Basic brute-force detection
- Extracting indicators from logs
- Documenting security findings
- Writing a basic SOC investigation report

## Project Structure

```text
soc-log-analysis-lab/
│
├── logs/
│   └── sample-auth.log
│
├── investigations/
│   └── brute-force-investigation.md
│
└── README.md
