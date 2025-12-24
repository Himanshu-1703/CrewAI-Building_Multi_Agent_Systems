from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from typing import List

# define the pdf knowledge source
research_paper_source = PDFKnowledgeSource(
    file_paths=["survey_on_icl.pdf"],
    chunk_size=1500,
    chunk_overlap=250
)

@CrewBase
class KnowledgeCrew():
    """KnowledgeCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # define the path for config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # define our agent
    @agent
    def research_summarization(self) -> Agent:
        return Agent(
            config=self.agents_config["research_summarization"],
            verbose=True
        )
        
    # define the task
    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarization_task"]
        )
        
    # define the crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[research_paper_source]
        )