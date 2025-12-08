# Level 1 Practical Exam: Certified Agent Developer

| | |
|--|--|
| **Duration** | 2 hours |
| **Passing Score** | 70% (automated) + manual review |

## Scenario: TechSupport Inc.

**TechSupport Inc.** needs a voice AI agent for their customer support line. Customers call to:

1. Get help with common technical issues
2. Check the status of support tickets
3. Create new support tickets

## Requirements

### Part 1: Basic Agent Setup (25 points)

Create `solution/techsupport_agent.py` with:

- [ ] Appropriate agent name
- [ ] Professional prompt with clear role definition
- [ ] At least 3 prompt sections (Role, Guidelines, Process)
- [ ] Voice configuration with appropriate TTS voice
- [ ] Speech and function filler phrases

### Part 2: SWAIG Functions (40 points)

#### Function 1: `check_ticket_status` (20 points)

```text
Parameter: ticket_id (string)
```

Requirements:
- Accept ticket ID as parameter
- Return status for valid tickets
- Handle invalid ticket IDs gracefully

Use this mock data:

```python
TICKETS = {
    "T-1001": {"status": "open", "issue": "Login problems", "created": "Monday"},
    "T-1002": {"status": "in_progress", "issue": "Slow performance", "created": "Tuesday"},
    "T-1003": {"status": "resolved", "issue": "Password reset", "created": "Last week"},
}
```

#### Function 2: `create_ticket` (20 points)

```text
Parameters:
  - issue_type (string, enum: ["login", "performance", "billing", "other"])
  - description (string)
```

Requirements:
- Accept issue type and description
- Generate a ticket number (can be mock, e.g., "T-2001")
- Return confirmation with ticket number

### Part 3: Voice Configuration (20 points)

- [ ] Language configured (English, en-US)
- [ ] TTS voice selected
- [ ] Speech fillers configured
- [ ] Function fillers configured

### Part 4: Live Demonstration (15 points)

Record a demo showing:
- Agent greeting and conversation
- Checking a ticket status
- Creating a new ticket

Submit your recording (wav, mp3, or mp4) in the repository.

## Testing Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Check agent loads
swaig-test solution/techsupport_agent.py --list-tools

# Verify SWML output
swaig-test solution/techsupport_agent.py --dump-swml

# Test check_ticket_status
swaig-test solution/techsupport_agent.py --exec check_ticket_status --ticket_id "T-1001"

# Test create_ticket
swaig-test solution/techsupport_agent.py --exec create_ticket \
  --issue_type "login" --description "Cannot access account"
```

## Submission

1. Implement your solution in `solution/techsupport_agent.py`
2. Add your demo recording to the repository
3. Push to trigger auto-grading
4. Check the "Grading Results" issue for automated feedback

**Note:** After automated checks pass, your submission will be tagged for manual review by an instructor.

## Grading Breakdown

| Component | Points | Type |
|-----------|--------|------|
| Agent loads correctly | 10 | Automated |
| Valid SWML generation | 10 | Automated |
| Prompt configuration | 5 | Automated |
| check_ticket_status exists | 10 | Automated |
| create_ticket exists | 10 | Automated |
| Valid ticket lookup works | 10 | Automated |
| Invalid ticket handled | 5 | Automated |
| Ticket creation works | 5 | Automated |
| Language configured | 10 | Automated |
| Fillers configured | 10 | Automated |
| Code quality | 10 | Manual |
| Live demonstration | 5 | Manual |
| **Total** | **100** | |

---

## Next Assignment

Congratulations on completing Level 1! Ready for Level 2? [**Start Lab 2.1: Function Results & Actions**](https://classroom.github.com/a/4Vcg0Jxl)

---

*SignalWire AI Agents Certification - Level 1 Practical Exam*
