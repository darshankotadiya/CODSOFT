import time

# =================================================================
# PROJECT: NEURAL-LOGIC RULE-BASED CHATBOT
# ORGANIZATION: CODSOFT INTERNSHIP (TASK 1)
# DEVELOPER: DARSHAN (MERN STACK & AI ENTHUSIAST)
# =================================================================

class CodSoftAssistant:
    def __init__(self):
        # Professional identity mapping
        self.bot_name = "Nexus-AI"
        self.developer = "Darshan"

    def process_request(self, user_query):
        """Processes incoming strings and matches them with pre-defined logic patterns."""
        data = user_query.lower().strip()

        # Phase 1: Greeting Patterns
        if any(word in data for word in ["hi", "hello", "hey", "greetings"]):
            return f"System Online. Hello! I am {self.bot_name}. How may I assist your workflow today?"

        # Phase 2: Identity & Source Validation (CodSoft Highlight)
        elif "identity" in data or "who are you" in data or "name" in data:
            return f"I am {self.bot_name}, a rule-based engine developed by {self.developer} for the CodSoft Artificial Intelligence Internship."

        # Phase 3: Technical Capabilities
        elif "tasks" in data or "what can you do" in data:
            return "Currently, I can execute rule-based NLP, pattern recognition, and provide internship-specific metadata."

        # Phase 4: Status & Performance
        elif "status" in data or "how are you" in data:
            return "All modules are functional. Latency: Minimal. System Status: Healthy."

        # Phase 5: Termination Signal
        elif "exit" in data or "bye" in data or "quit" in data:
            return "Deactivating session. Thank you for the interaction. Goodbye!"

        # Fallback for undefined logic
        else:
            return "Query unrecognized. My current logic-gate is limited to pre-defined internship parameters. Please rephrase."

def run_interface():
    assistant = CodSoftAssistant()
    
    print(f"\n[BOOTING] {assistant.bot_name} v1.0.4 Initialized...")
    time.sleep(1) # Adding a professional delay
    print("-------------------------------------------------------")
    print(f"COMMAND CENTER: ACTIVE | DEVELOPER: {assistant.developer}")
    print("-------------------------------------------------------")

    while True:
        user_input = input("\nPROMPT >> ")
        
        if not user_input:
            continue
            
        # Processing response
        response = assistant.process_request(user_input)
        
        # Displaying with a 'typing' feel
        print(f"[{assistant.bot_name}]: ", end="")
        for char in response:
            print(char, end="", flush=True)
            time.sleep(0.01)
        print()

        if user_input.lower() in ["exit", "bye", "quit"]:
            break

if __name__ == "__main__":
    run_interface()