import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ContextualAIParseTool,
	FileReadTool
)





@CrewBase
class FullMarketingMaterialsReviewerCrew:
    """FullMarketingMaterialsReviewer crew"""

    
    @agent
    def pdf_document_coordinator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["pdf_document_coordinator"],
            
            
            tools=[				ContextualAIParseTool(api_key="key-783Ajwtdmr3OnbubdJLYsyJS-bwyxrgryLFkp4D1ndIsxZmm0")],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def general_compliance_checker(self) -> Agent:
        
        return Agent(
            config=self.agents_config["general_compliance_checker"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def uae_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["uae_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def ksa_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["ksa_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def kuwait_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["kuwait_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def difc_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["difc_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def qatar_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["qatar_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def oman_compliance_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["oman_compliance_specialist"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    
    @agent
    def compliance_report_compiler(self) -> Agent:
        
        return Agent(
            config=self.agents_config["compliance_report_compiler"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
                temperature=0.7,
                
            ),
            
        )
    

    
    @task
    def parse_pdf_document(self) -> Task:
        return Task(
            config=self.tasks_config["parse_pdf_document"],
            markdown=False,
            
            
        )
    
    @task
    def general_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["general_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def uae_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["uae_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def ksa_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["ksa_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def kuwait_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["kuwait_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def difc_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["difc_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def qatar_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["qatar_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def oman_compliance_review(self) -> Task:
        return Task(
            config=self.tasks_config["oman_compliance_review"],
            markdown=False,
            
            
        )
    
    @task
    def compile_final_compliance_report(self) -> Task:
        return Task(
            config=self.tasks_config["compile_final_compliance_report"],
            markdown=False,
            
            
        )
    

    def create_crew(self, selected_jurisdictions: list[str] = None) -> Crew:
        """Creates the FullMarketingMaterialsReviewer crew with selected jurisdictions"""
        # Filter agents and tasks based on selected jurisdictions
        if selected_jurisdictions is None:
            selected_jurisdictions = ['uae', 'ksa', 'kuwait', 'difc']
        
        # Always include these agents
        active_agents = [
            self.pdf_document_coordinator(),
            self.general_compliance_checker(),
            self.compliance_report_compiler(),
        ]
        
        # Map jurisdiction codes to agent methods
        jurisdiction_agents = {
            'uae': self.uae_compliance_specialist,
            'ksa': self.ksa_compliance_specialist,
            'kuwait': self.kuwait_compliance_specialist,
            'difc': self.difc_compliance_specialist,
            'qatar': self.qatar_compliance_specialist,
            'oman': self.oman_compliance_specialist,
        }
        
        # Add selected jurisdiction agents
        for jurisdiction in selected_jurisdictions:
            if jurisdiction in jurisdiction_agents:
                active_agents.append(jurisdiction_agents[jurisdiction]())
        
        # Filter tasks similarly
        active_tasks = [
            self.parse_pdf_document(),
            self.general_compliance_review(),
        ]
        
        # Map jurisdiction codes to task methods
        jurisdiction_tasks = {
            'uae': self.uae_compliance_review,
            'ksa': self.ksa_compliance_review,
            'kuwait': self.kuwait_compliance_review,
            'difc': self.difc_compliance_review,
            'qatar': self.qatar_compliance_review,
            'oman': self.oman_compliance_review,
        }
        
        # Add selected jurisdiction tasks
        for jurisdiction in selected_jurisdictions:
            if jurisdiction in jurisdiction_tasks:
                active_tasks.append(jurisdiction_tasks[jurisdiction]())
        
        # Always add the final compilation task
        active_tasks.append(self.compile_final_compliance_report())
        
        return Crew(
            agents=active_agents,
            tasks=active_tasks,
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="gemini/gemini-3-flash-preview"),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FullMarketingMaterialsReviewer crew (default - all jurisdictions)"""
        return self.create_crew()


