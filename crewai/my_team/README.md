# Create an engineering team of agents using CrewAI

### The crew _my_team_ consists of multiple AI agents, each with unique roles, goals, and tools:

1. Engineering Lead
2. Backend Engineer
3. Frontend Engineer
4. Test Engineer

These agents collaborate on a series of tasks, defined in `src/my_team/config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `src/my_team/config/agents.yaml` file outlines the capabilities and configurations of each agent in the crew.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system.

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/my_team/config/agents.yaml` to define your agents
- Modify `src/my_team/config/tasks.yaml` to define your tasks
- Modify `src/my_team/crew.py` to add your own logic, tools and specific args
- Modify `src/my_team/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the my_team Crew, assembling the agents and assigning them tasks as defined in your configuration.

The crew will come up with an output that can be found at `output/`
