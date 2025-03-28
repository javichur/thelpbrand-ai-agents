from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Defining specific LLM for those Agents. 
    # Put "openai/"" in front of your model name, so litellm knows you're trying to call an openai /chat/completions endpoint.
    # Via https://docs.litellm.ai/docs/providers/openai_compatible 
    llm = LLM(
        model="openai/my-openai-compatible-model",
        api_key="not-required-in-lm-studio",
        base_url="http://localhost:1234/v1" # I use LM Studio application to serve LLMs during development locally.
    )

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher_lps(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_lps'],
            llm=self.llm
        )

    @agent
    def researcher_trends(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_trends'],
            llm=self.llm
        )
    
    @agent
    def creative_director(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_director'],
            llm=self.llm
        )

    @agent
    def potential_user(self) -> Agent:
        return Agent(
            config=self.agents_config['potential_user'],
            llm=self.llm
        )

    @agent
    def prompt_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_designer'],
            llm=self.llm
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_lps_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_lps_task'],
        )

    @task
    def research_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_trends_task'],
        )
    
    @task
    def creative_director_task(self) -> Task:
        return Task(
            config=self.tasks_config['creative_director_task'],
        )
    
    @task
    def potential_user_task(self) -> Task:
        return Task(
            config=self.tasks_config['potential_user_task'],
        )
    
    @task
    def prompt_designer_task(self) -> Task:
        return Task(
            config=self.tasks_config['prompt_designer_task'],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
