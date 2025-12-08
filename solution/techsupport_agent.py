#!/usr/bin/env python3
"""
TechSupport Agent - Level 1 Practical Exam

Implement your solution here.

Requirements:
1. Create an agent for TechSupport Inc.
2. Implement check_ticket_status function
3. Implement create_ticket function
4. Configure voice and fillers

See README.md for full requirements.
"""

from signalwire_agents import AgentBase, SwaigFunctionResult

# Mock ticket database - use this data
TICKETS = {
    "T-1001": {"status": "open", "issue": "Login problems", "created": "Monday"},
    "T-1002": {"status": "in_progress", "issue": "Slow performance", "created": "Tuesday"},
    "T-1003": {"status": "resolved", "issue": "Password reset", "created": "Last week"},
}

# Your implementation here...
