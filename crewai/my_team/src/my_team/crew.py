from pyexpat import model
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
# from crewai.project.annotations import agent, crew, task
# from crewai.project.crew_base import CrewBase

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MyTeam():
    """MyTeam crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml" 

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            model=os.getenv("MODEL"),
            api_key=os.getenv("OPENAI_API_KEY"),
            config=self.agents_config['backend_engineer'],
            verbose=True,
            #allow_code_execution=True,
            #code_execution_mode="safe", # Use Docker for safety
            max_execution_time=500,
            max_retry_limit=3
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyTeam crew"""

        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            #process=Process.hierarchical, # In case you want to use hierarchical instead https://docs.crewai.com/how-to/Hierarchical/
            verbose=True,
        )
