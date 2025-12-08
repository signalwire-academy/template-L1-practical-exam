#!/usr/bin/env python3
"""
TechSupport Agent - Level 1 Practical Exam Reference Solution

This is the instructor reference solution. Students should implement
their own version in solution/techsupport_agent.py
"""

from signalwire_agents import AgentBase, SwaigFunctionResult

# Mock ticket database
TICKETS = {
    "T-1001": {"status": "open", "issue": "Login problems", "created": "Monday"},
    "T-1002": {"status": "in_progress", "issue": "Slow performance", "created": "Tuesday"},
    "T-1003": {"status": "resolved", "issue": "Password reset", "created": "Last week"},
}

# Counter for new tickets
_ticket_counter = 2000


class TechSupportAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="techsupport-agent",
            route="/support"
        )

        # Configure prompts
        self.prompt_add_section(
            "Role",
            "You are a friendly technical support agent for TechSupport Inc. "
            "Help customers check ticket status and create new support tickets."
        )

        self.prompt_add_section(
            "Guidelines",
            bullets=[
                "Be professional and helpful",
                "Always confirm ticket IDs before looking them up",
                "For new tickets, collect issue type and description",
                "Provide clear next steps after each action"
            ]
        )

        self.prompt_add_section(
            "Process",
            bullets=[
                "Greet the customer warmly",
                "Ask how you can help today",
                "Use check_ticket_status for existing tickets",
                "Use create_ticket for new issues"
            ]
        )

        # Configure language with fillers
        self.add_language(
            "English",
            "en-US",
            "rime.spore",
            speech_fillers=["Um", "Uh", "Well", "Let me see"],
            function_fillers=[
                "Let me check that for you...",
                "One moment please...",
                "Looking that up now..."
            ]
        )

        # Register functions
        self._setup_functions()

    def _setup_functions(self):
        @self.tool(
            description="Check the status of an existing support ticket",
            parameters={
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "string",
                        "description": "The ticket ID to look up (e.g., T-1001)"
                    }
                },
                "required": ["ticket_id"]
            }
        )
        def check_ticket_status(args: dict, raw_data: dict = None) -> SwaigFunctionResult:
            ticket_id = args.get("ticket_id", "").upper()

            if ticket_id in TICKETS:
                ticket = TICKETS[ticket_id]
                return SwaigFunctionResult(
                    f"Ticket {ticket_id} is currently {ticket['status']}. "
                    f"Issue: {ticket['issue']}. Created: {ticket['created']}."
                )
            else:
                return SwaigFunctionResult(
                    f"Ticket {ticket_id} was not found. Please verify the ticket "
                    "number and try again, or I can help you create a new ticket."
                )

        @self.tool(
            description="Create a new support ticket",
            parameters={
                "type": "object",
                "properties": {
                    "issue_type": {
                        "type": "string",
                        "description": "Type of issue",
                        "enum": ["login", "performance", "billing", "other"]
                    },
                    "description": {
                        "type": "string",
                        "description": "Description of the issue"
                    }
                },
                "required": ["issue_type", "description"]
            }
        )
        def create_ticket(args: dict, raw_data: dict = None) -> SwaigFunctionResult:
            global _ticket_counter
            issue_type = args.get("issue_type", "other")
            description = args.get("description", "No description provided")

            _ticket_counter += 1
            ticket_id = f"T-{_ticket_counter}"

            # In a real system, this would save to a database
            TICKETS[ticket_id] = {
                "status": "open",
                "issue": f"{issue_type}: {description}",
                "created": "Just now"
            }

            return SwaigFunctionResult(
                f"I've created ticket {ticket_id} for your {issue_type} issue. "
                "A support specialist will review it shortly. Is there anything "
                "else I can help you with?"
            )


# Create and run the agent
agent = TechSupportAgent()

if __name__ == "__main__":
    agent.run()
