\# Runtime Truth



Don't trust the tool response. Verify the state.



Runtime Truth is a minimal experiment for detecting execution-state divergence in agent-driven web actions.



\## Demo



An agent calls a reservation tool.



The tool reports:



SUCCESS



But Runtime Truth independently checks the authoritative application state.



The reservation does not exist.



Result:



DIVERGENCE DETECTED



\## Core idea



Declared tool result != actual application state.



Instead of trusting the tool response, verify the post-action state independently.



\## WebMCP Challenge



Prototype built for the OpenAI WebMCP Challenge.

