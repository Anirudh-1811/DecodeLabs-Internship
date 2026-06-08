# Rule-Based AI Chatbot Logic Engine
## Project 1 Documentation | DecodeLabs AI Engineering Track

Welcome to the foundation phase documentation for the DecodeLabs AI Engineering track. This repository establishes clear, predictable control flow and deterministic logic before moving into probabilistic models. This transparent framework is built entirely on strict programmatic decision-making to guarantee absolute execution predictability and zero hallucination risk. 

The system design is explicitly engineered to simulate human interaction through hard-coded programmatic logic blocks rather than deep learning architectures.

---

##  Architectural Blueprint
The framework relies strictly on the classic **Input-Process-Output (IPO)** model to handle user queries both safely and instantaneously:

*   **Input Stage:** Handles the continuous, real-time capture of text directly from the user terminal. This utilizes an infinite loop control structure wrapped cleanly within an interrupt safety block.
*   **Process Stage:** Handles data normalization, string cleansing, and deterministic pattern matching. The raw string is passed through automated whitespace stripping and lowercase conversion operations combined with a high-efficiency lookup strategy.
*   **Output Stage:** Delivers an immediate response back to the user or gracefully terminates the execution engine through a single-cycle atomic execution backed by a hard-coded fallback safety mechanism.

---

##  Engineering Highlights & Optimization

### Avoiding the `if-elif` Ladder Anti-Pattern
Chaining endless conditional evaluation rules together creates fragile code structures prone to high technical debt and cascading failures during system updates. Furthermore, an `if-elif` ladder forces the machine to scan every single condition sequentially line-by-line, inducing an inefficient linear runtime complexity of $O(n)$ that bogs down performance as the rule scale grows.

### Hash Map Lookup Strategy
To resolve this operational bottleneck, this architecture utilizes a native Python dictionary to act as an industrial hash map lookup structure. Because input keys map directly to specific output values, the engine performs instant lookups in **$O(1)$ constant time**, ensuring the chatbot responds just as fast with thousands of rules as it does with a few.

### Continuous Runtime Safety
To guarantee stability, the framework rejects standard direct dictionary bracket indexing, which can trigger a fatal application crash if a user enters an unmapped term. Instead, the engine leverages the dictionary `.get()` method to process lookups safely. 

> **Key Feature:** This approach allows the system to evaluate key matching and issue a hard-coded default fallback message simultaneously in a single, safe, atomic operation cycle whenever a query falls outside the known rule set.

---

##  Vocabulary & Input Triggers
The hard-coded dictionary vocabulary is fully optimized to recognize a robust set of deterministic input triggers:

| Category | Input Triggers | Expected Behavior |
| :--- | :--- | :--- |
| **Greetings** | `hello`, `hi`, `hey` | Returns standard automated greetings. |
| **Navigation** | `help` | Provides instant user navigation assistance. |
| **System Metrics** | `status`, `about`, `blueprint`, `credits` | Returns system configuration metrics and project tracking details. |
| **Curated Data** | `fact`, `quote` | Delivers pre-determined informational strings. |
| **Termination** | `exit`, `bye`, `quit`, `goodbye` | Triggers a clean break from the loop and safely closes the application. |

---

##  Environment & Execution
Validating and running the script requires a basic **Python 3** environment without any external dependencies or heavy deep learning frameworks. 

### Input Sanitization Layer
Users do not need to worry about accidental capitalization typos or erratic spacing during evaluation. The normalization layer sanitizes inputs automatically:
* Entering an irregularly spaced or capitalized greeting (e.g., `"  HeLlO "`) is instantly rectified to lowercase format (`"hello"`) to serve the matching response.
* Any completely unrecognized phrase safely routes to the default fallback statement without breaking the execution loop.

### Running the Program
Execute the script directly from your terminal using standard system execution commands:
```bash
python chatbot_engine.py
