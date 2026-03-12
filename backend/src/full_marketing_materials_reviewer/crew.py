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
        """Creates the FullMarketingMaterialsReviewer crew with selected jurisdictions.
        Qatar and Oman use the general compliance result (no separate agents)."""
        # Filter agents and tasks based on selected jurisdictions
        if selected_jurisdictions is None:
            selected_jurisdictions = ['uae', 'ksa', 'kuwait', 'difc']
        
        # Only UAE, KSA, Kuwait, DIFC have dedicated agents; Qatar and Oman use general compliance
        crew_jurisdictions = [j for j in selected_jurisdictions if j in ('uae', 'ksa', 'kuwait', 'difc')]
        
        # Always include these agents
        active_agents = [
            self.pdf_document_coordinator(),
            self.general_compliance_checker(),
            self.compliance_report_compiler(),
        ]
        
        # Map jurisdiction codes to agent methods (no qatar/oman - they use general)
        jurisdiction_agents = {
            'uae': self.uae_compliance_specialist,
            'ksa': self.ksa_compliance_specialist,
            'kuwait': self.kuwait_compliance_specialist,
            'difc': self.difc_compliance_specialist,
        }
        
        # Add selected jurisdiction agents (only those with dedicated agents)
        for jurisdiction in crew_jurisdictions:
            active_agents.append(jurisdiction_agents[jurisdiction]())
        
        # Build tasks: parse, general, then jurisdiction-specific (only uae/ksa/kuwait/difc)
        general_task = self.general_compliance_review()
        jurisdiction_tasks_map = {
            'uae': self.uae_compliance_review,
            'ksa': self.ksa_compliance_review,
            'kuwait': self.kuwait_compliance_review,
            'difc': self.difc_compliance_review,
        }
        jurisdiction_tasks_list = [jurisdiction_tasks_map[j]() for j in crew_jurisdictions]
        
        active_tasks = [
            self.parse_pdf_document(),
            general_task,
        ] + jurisdiction_tasks_list
        
        # Compile task with context = only the tasks we're actually running
        compile_task = Task(
            config=self.tasks_config["compile_final_compliance_report"],
            context=[general_task] + jurisdiction_tasks_list,
            markdown=False,
        )
        active_tasks.append(compile_task)
        
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


