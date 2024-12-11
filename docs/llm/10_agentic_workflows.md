# Agentic Workflows

## From Chatbot to Agent
A Chatbot talks. An Agent *does*.

## Core Pattern: ReAct (Reason + Act)
1.  **Thought**: User wants weather in NY. I should check the weather tool.
2.  **Action**: `WeatherAPI(city='New York')`.
3.  **Observation**: "25°C, Sunny".
4.  **Thought**: I have the answer.
5.  **Response**: "It is 25°C and sunny in New York."

## Planning
-   **Chain of Thought**: Step-by-step reasoning.
-   **Tree of Thoughts**: Explore multiple branches of reasoning, backtrack if dead end.

## Tool Use
-   **Function Calling**: OpenAI API structured output.
-   **Code Interpreter**: Agent writes Python code to solve math/data problems.

## Multi-Agent Systems
-   **CrewAI / AutoGen**: One agent researches, one writes, one critiques.

