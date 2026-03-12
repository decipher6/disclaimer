#!/usr/bin/env python
"""
Simple FastAPI server to run CrewAI and display results
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import sys
import shutil
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Add backend/src to path
backend_path = Path(__file__).parent / "backend" / "src"
sys.path.insert(0, str(backend_path))

from full_marketing_materials_reviewer.crew import FullMarketingMaterialsReviewerCrew

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if it doesn't exist
UPLOADS_DIR = Path(__file__).parent / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the simple HTML frontend"""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ComplianceAI - Review Results</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: #1e3a8a;
            color: white;
            padding: 20px 0;
            margin-bottom: 30px;
        }
        
        header h1 {
            font-size: 28px;
            margin-left: 20px;
        }
        
        .upload-section {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        .upload-box {
            border: 2px dashed #cbd5e1;
            border-radius: 8px;
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 20px;
        }
        
        .upload-box:hover {
            border-color: #3b82f6;
            background: #f8fafc;
        }
        
        .upload-box.dragover {
            border-color: #3b82f6;
            background: #eff6ff;
        }
        
        .upload-icon {
            font-size: 48px;
            margin-bottom: 10px;
        }
        
        input[type="file"] {
            display: none;
        }
        
        .jurisdictions {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 20px;
            background: #f8fafc;
            padding: 15px;
            border-radius: 8px;
        }
        
        .jurisdiction-checkbox {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px;
            cursor: pointer;
        }
        
        .jurisdiction-checkbox input[type="checkbox"] {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }
        
        .agent-list {
            margin-top: 30px;
            display: none;
        }
        
        .agent-list.active {
            display: block;
        }
        
        .agent-item {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 15px;
            border-left: 4px solid #e5e7eb;
        }
        
        .agent-item.loading {
            border-left-color: #3b82f6;
        }
        
        .agent-item.complete {
            border-left-color: #10b981;
        }
        
        .agent-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .agent-name {
            font-weight: 600;
            color: #1e3a8a;
            font-size: 16px;
        }
        
        .agent-status {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
        }
        
        .spinner {
            border: 2px solid #f3f4f6;
            border-top: 2px solid #3b82f6;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .agent-content {
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid #e5e7eb;
            display: none;
        }
        
        .agent-item.complete .agent-content {
            display: block;
        }
        
        .agent-content-text {
            background: #f8fafc;
            padding: 15px;
            border-radius: 6px;
            font-size: 14px;
            line-height: 1.8;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .agent-content-text h1,
        .agent-content-text h2,
        .agent-content-text h3 {
            color: #1e3a8a;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        .agent-content-text h1 {
            font-size: 24px;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }
        
        .agent-content-text h2 {
            font-size: 20px;
        }
        
        .agent-content-text h3 {
            font-size: 18px;
        }
        
        .agent-content-text p {
            margin-bottom: 12px;
        }
        
        .agent-content-text ul,
        .agent-content-text ol {
            margin-left: 20px;
            margin-bottom: 12px;
        }
        
        .agent-content-text li {
            margin-bottom: 6px;
        }
        
        .agent-content-text code {
            background: #e5e7eb;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
        }
        
        .agent-content-text pre {
            background: #1f2937;
            color: #f9fafb;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            margin-bottom: 12px;
        }
        
        .agent-content-text pre code {
            background: transparent;
            padding: 0;
            color: inherit;
        }
        
        .agent-content-text blockquote {
            border-left: 4px solid #3b82f6;
            padding-left: 15px;
            margin-left: 0;
            color: #6b7280;
            font-style: italic;
        }
        
        .agent-content-text table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 12px;
        }
        
        .agent-content-text table th,
        .agent-content-text table td {
            border: 1px solid #e5e7eb;
            padding: 8px 12px;
            text-align: left;
        }
        
        .agent-content-text table th {
            background: #f3f4f6;
            font-weight: 600;
        }
        
        .agent-content-text strong {
            font-weight: 600;
            color: #1f2937;
        }
        
        .agent-content-text em {
            font-style: italic;
        }
        
        button {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #2563eb;
        }
        
        button:disabled {
            background: #9ca3af;
            cursor: not-allowed;
        }
        
        .progress {
            display: none;
            margin-top: 20px;
        }
        
        .progress.active {
            display: block;
        }
        
        .progress-steps {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        
        .step {
            flex: 1;
            text-align: center;
            padding: 10px;
            position: relative;
        }
        
        .step::after {
            content: '';
            position: absolute;
            top: 20px;
            left: 50%;
            width: 100%;
            height: 2px;
            background: #e5e7eb;
            z-index: -1;
        }
        
        .step:last-child::after {
            display: none;
        }
        
        .step.active::after {
            background: #3b82f6;
        }
        
        .step-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 10px;
            font-size: 20px;
        }
        
        .step.active .step-icon {
            background: #3b82f6;
            color: white;
        }
        
        .step.complete .step-icon {
            background: #10b981;
            color: white;
        }
        
        .results {
            display: none;
            margin-top: 30px;
        }
        
        .results.active {
            display: block;
        }
        
        .result-section {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        
        .result-section h2 {
            color: #1e3a8a;
            margin-bottom: 15px;
            font-size: 20px;
        }
        
        .compliance-status {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 15px;
        }
        
        .status-compliant {
            background: #d1fae5;
            color: #065f46;
        }
        
        .status-non-compliant {
            background: #fee2e2;
            color: #991b1b;
        }
        
        .status-needs-review {
            background: #fef3c7;
            color: #92400e;
        }
        
        .result-content {
            background: #f8fafc;
            padding: 15px;
            border-radius: 6px;
            font-size: 14px;
            line-height: 1.8;
            max-height: 500px;
            overflow-y: auto;
        }
        
        .result-content h1,
        .result-content h2,
        .result-content h3 {
            color: #1e3a8a;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        .result-content h1 {
            font-size: 24px;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }
        
        .result-content h2 {
            font-size: 20px;
        }
        
        .result-content h3 {
            font-size: 18px;
        }
        
        .result-content p {
            margin-bottom: 12px;
        }
        
        .result-content ul,
        .result-content ol {
            margin-left: 20px;
            margin-bottom: 12px;
        }
        
        .result-content li {
            margin-bottom: 6px;
        }
        
        .result-content code {
            background: #e5e7eb;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
        }
        
        .result-content pre {
            background: #1f2937;
            color: #f9fafb;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            margin-bottom: 12px;
        }
        
        .result-content pre code {
            background: transparent;
            padding: 0;
            color: inherit;
        }
        
        .result-content blockquote {
            border-left: 4px solid #3b82f6;
            padding-left: 15px;
            margin-left: 0;
            color: #6b7280;
            font-style: italic;
        }
        
        .result-content table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 12px;
        }
        
        .result-content table th,
        .result-content table td {
            border: 1px solid #e5e7eb;
            padding: 8px 12px;
            text-align: left;
        }
        
        .result-content table th {
            background: #f3f4f6;
            font-weight: 600;
        }
        
        .result-content strong {
            font-weight: 600;
            color: #1f2937;
        }
        
        .result-content em {
            font-style: italic;
        }
        
        .error {
            background: #fee2e2;
            color: #991b1b;
            padding: 15px;
            border-radius: 6px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🛡️ ComplianceAI</h1>
        </div>
    </header>
    
    <div class="container">
        <div class="upload-section">
            <h2 style="margin-bottom: 20px;">Review Marketing Material</h2>
            
            <div class="upload-box" id="uploadBox">
                <div class="upload-icon">📄</div>
                <p>Click to upload PDF or drag and drop</p>
                <input type="file" id="fileInput" accept=".pdf">
            </div>
            
            <div class="jurisdictions">
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="difc" checked> Dubai International Financial Centre
                </label>
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="ksa" checked> Kingdom of Saudi Arabia
                </label>
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="kuwait" checked> State of Kuwait
                </label>
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="qatar"> State of Qatar
                </label>
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="oman"> Sultanate of Oman
                </label>
                <label class="jurisdiction-checkbox">
                    <input type="checkbox" value="uae" checked> United Arab Emirates
                </label>
            </div>
            
            <button id="submitBtn" onclick="submitReview()">Submit for Review</button>
            
            <div class="progress" id="progress">
                <div class="progress-steps">
                    <div class="step active" id="step1">
                        <div class="step-icon">1</div>
                        <div>Extracting Content</div>
                    </div>
                    <div class="step" id="step2">
                        <div class="step-icon">2</div>
                        <div>Checking Compliance</div>
                    </div>
                    <div class="step" id="step3">
                        <div class="step-icon">3</div>
                        <div>Generating Summary</div>
                    </div>
                    <div class="step" id="step4">
                        <div class="step-icon">✓</div>
                        <div>Complete</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="agent-list" id="agentList"></div>
        <div class="results" id="results"></div>
        <div class="error" id="error" style="display: none;"></div>
    </div>
    
    <script>
        const uploadBox = document.getElementById('uploadBox');
        const fileInput = document.getElementById('fileInput');
        let selectedFile = null;
        
        uploadBox.addEventListener('click', () => fileInput.click());
        
        uploadBox.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadBox.classList.add('dragover');
        });
        
        uploadBox.addEventListener('dragleave', () => {
            uploadBox.classList.remove('dragover');
        });
        
        uploadBox.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadBox.classList.remove('dragover');
            const file = e.dataTransfer.files[0];
            if (file && file.type === 'application/pdf') {
                fileInput.files = e.dataTransfer.files;
                handleFileSelect(file);
            }
        });
        
        fileInput.addEventListener('change', (e) => {
            if (e.target.files[0]) {
                handleFileSelect(e.target.files[0]);
            }
        });
        
        function handleFileSelect(file) {
            selectedFile = file;
            uploadBox.innerHTML = `
                <div class="upload-icon">✓</div>
                <p><strong>${file.name}</strong></p>
                <p style="color: #6b7280; font-size: 14px;">Click to change file</p>
            `;
        }
        
        async function submitReview() {
            if (!selectedFile) {
                alert('Please select a PDF file');
                return;
            }
            
            const jurisdictions = Array.from(document.querySelectorAll('.jurisdictions input:checked'))
                .map(cb => cb.value);
            
            if (jurisdictions.length === 0) {
                alert('Please select at least one jurisdiction');
                return;
            }
            
            const formData = new FormData();
            formData.append('file', selectedFile);
            formData.append('jurisdictions', JSON.stringify(jurisdictions));
            
            // Store selected jurisdictions for filtering results
            sessionStorage.setItem('selectedJurisdictions', JSON.stringify(jurisdictions));
            
            // Show progress
            document.getElementById('progress').classList.add('active');
            document.getElementById('results').classList.remove('active');
            document.getElementById('agentList').classList.remove('active');
            document.getElementById('error').style.display = 'none';
            document.getElementById('submitBtn').disabled = true;
            
            // Initialize agent list
            initializeAgentList(jurisdictions);
            
            // Update progress steps
            updateProgress(1);
            
            try {
                const response = await fetch('/api/review', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error('Review failed');
                }
                
                updateProgress(2);
                const data = await response.json();
                updateProgress(3);
                
                // Update agent results as they come in
                if (data.agent_results) {
                    for (const [agentId, result] of Object.entries(data.agent_results)) {
                        updateAgentResult(agentId, result);
                    }
                }
                
                setTimeout(() => {
                    updateProgress(4);
                    displayResults(data);
                    document.getElementById('progress').classList.remove('active');
                    document.getElementById('submitBtn').disabled = false;
                }, 500);
                
            } catch (error) {
                document.getElementById('error').style.display = 'block';
                document.getElementById('error').textContent = 'Error: ' + error.message;
                document.getElementById('progress').classList.remove('active');
                document.getElementById('submitBtn').disabled = false;
            }
        }
        
        function updateProgress(step) {
            for (let i = 1; i <= 4; i++) {
                const stepEl = document.getElementById('step' + i);
                stepEl.classList.remove('active', 'complete');
                if (i < step) {
                    stepEl.classList.add('complete');
                } else if (i === step) {
                    stepEl.classList.add('active');
                }
            }
        }
        
        function displayResults(data) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.classList.add('active');
            
            let html = '';
            
            // Summary section
            if (data.summary) {
                const statusClass = `status-${data.compliance_status}`;
                const summaryHtml = typeof marked !== 'undefined' ? marked.parse(data.summary) : escapeHtml(data.summary);
                html += `
                    <div class="result-section">
                        <h2>Summary</h2>
                        <span class="compliance-status ${statusClass}">${data.compliance_status.toUpperCase()}</span>
                        <div class="result-content">${summaryHtml}</div>
                    </div>
                `;
            }
            
            // Individual jurisdiction results - only show selected jurisdictions
            const selectedJurisdictions = JSON.parse(sessionStorage.getItem('selectedJurisdictions') || '[]');
            const jurisdictionNames = {
                'uae': 'UAE',
                'ksa': 'KSA',
                'kuwait': 'Kuwait',
                'difc': 'DIFC',
                'qatar': 'Qatar',
                'oman': 'Oman'
            };
            
            if (data.results) {
                for (const [key, value] of Object.entries(data.results)) {
                    // Only show if it's a selected jurisdiction or general/summary
                    if (key === 'summary' || key === 'general') {
                        continue; // Already shown above
                    }
                    if (value && selectedJurisdictions.includes(key)) {
                        const title = (jurisdictionNames[key] || key.charAt(0).toUpperCase() + key.slice(1)) + ' Compliance Review';
                        const contentHtml = typeof marked !== 'undefined' ? marked.parse(value) : escapeHtml(value);
                        html += `
                            <div class="result-section">
                                <h2>${title}</h2>
                                <div class="result-content">${contentHtml}</div>
                            </div>
                        `;
                    }
                }
            }
            
            resultsDiv.innerHTML = html;
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function initializeAgentList(jurisdictions) {
            const agentList = document.getElementById('agentList');
            agentList.classList.add('active');
            
            const agents = [
                { id: 'pdf_document_coordinator', name: 'PDF Document Coordinator' },
                { id: 'general_compliance_checker', name: 'General Compliance Checker' }
            ];
            
            // Add jurisdiction agents (Qatar and Oman use general compliance - no separate agents)
            const jurisdictionMap = {
                'uae': 'UAE Compliance Specialist',
                'ksa': 'KSA Compliance Specialist',
                'kuwait': 'Kuwait Compliance Specialist',
                'difc': 'DIFC Compliance Specialist'
            };
            
            jurisdictions.forEach(j => {
                if (jurisdictionMap[j]) {
                    agents.push({ id: `${j}_compliance_specialist`, name: jurisdictionMap[j] });
                }
            });
            
            agents.push({ id: 'compliance_report_compiler', name: 'Compliance Report Compiler' });
            
            let html = '';
            agents.forEach(agent => {
                html += `
                    <div class="agent-item loading" id="agent-${agent.id}">
                        <div class="agent-header">
                            <div class="agent-name">${agent.name}</div>
                            <div class="agent-status">
                                <div class="spinner"></div>
                                <span>Processing...</span>
                            </div>
                        </div>
                        <div class="agent-content">
                            <div class="agent-content-text" id="agent-content-${agent.id}"></div>
                        </div>
                    </div>
                `;
            });
            
            agentList.innerHTML = html;
        }
        
        function updateAgentResult(agentId, result) {
            const agentEl = document.getElementById(`agent-${agentId}`);
            const contentEl = document.getElementById(`agent-content-${agentId}`);
            
            if (agentEl && contentEl) {
                agentEl.classList.remove('loading');
                agentEl.classList.add('complete');
                agentEl.querySelector('.agent-status').innerHTML = '<span style="color: #10b981;">✓ Complete</span>';
                // Render markdown to HTML
                if (typeof marked !== 'undefined') {
                    contentEl.innerHTML = marked.parse(result);
                } else {
                    contentEl.textContent = result;
                }
            }
        }
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content)

@app.post("/api/review")
async def review_pdf(file: UploadFile = File(...), jurisdictions: str = None):
    """Process PDF for compliance review"""
    try:
        # Save uploaded file
        file_path = UPLOADS_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Parse jurisdictions
        import json
        selected_jurisdictions = json.loads(jurisdictions) if jurisdictions else ['uae', 'ksa', 'kuwait', 'difc']
        
        # Create crew
        crew_instance = FullMarketingMaterialsReviewerCrew()
        crew = crew_instance.create_crew(selected_jurisdictions=selected_jurisdictions)
        
        # Prepare inputs
        inputs = {
            'pdf_file_path': str(file_path),
            'general_checklist': 'General compliance checklist requirements',
        }
        
        # Add jurisdiction checklists
        jurisdiction_checklists = {
            'uae': 'UAE compliance checklist requirements',
            'ksa': 'KSA compliance checklist requirements',
            'kuwait': 'Kuwait compliance checklist requirements',
            'difc': 'DIFC compliance checklist requirements',
            'qatar': 'Qatar compliance checklist requirements',
            'oman': 'Oman compliance checklist requirements',
        }
        
        for jurisdiction in selected_jurisdictions:
            if jurisdiction in jurisdiction_checklists:
                inputs[f'{jurisdiction}_checklist'] = jurisdiction_checklists[jurisdiction]
        
        # Execute crew
        result = crew.kickoff(inputs=inputs)
        
        # Extract results
        results = {}
        agent_results = {}
        summary = None
        
        # Map task names to agent IDs
        task_to_agent = {
            'parse_pdf_document': 'pdf_document_coordinator',
            'general_compliance_review': 'general_compliance_checker',
            'uae_compliance_review': 'uae_compliance_specialist',
            'ksa_compliance_review': 'ksa_compliance_specialist',
            'kuwait_compliance_review': 'kuwait_compliance_specialist',
            'difc_compliance_review': 'difc_compliance_specialist',
            'qatar_compliance_review': 'qatar_compliance_specialist',
            'oman_compliance_review': 'oman_compliance_specialist',
            'compile_final_compliance_report': 'compliance_report_compiler'
        }
        
        # Get the final result
        if hasattr(result, 'tasks_output') and result.tasks_output:
            for task_output in result.tasks_output:
                task_name = task_output.name if hasattr(task_output, 'name') else str(task_output)
                task_output_raw = task_output.raw if hasattr(task_output, 'raw') else str(task_output)
                
                # Map to agent
                agent_id = None
                for task_key, agent_key in task_to_agent.items():
                    if task_key in task_name.lower():
                        agent_id = agent_key
                        break
                
                if agent_id:
                    agent_results[agent_id] = task_output_raw
                
                # Also populate results dict - only for selected jurisdictions
                if 'general' in task_name.lower():
                    results['general'] = task_output_raw
                elif 'uae' in task_name.lower() and 'uae' in selected_jurisdictions:
                    results['uae'] = task_output_raw
                elif 'ksa' in task_name.lower() and 'ksa' in selected_jurisdictions:
                    results['ksa'] = task_output_raw
                elif 'kuwait' in task_name.lower() and 'kuwait' in selected_jurisdictions:
                    results['kuwait'] = task_output_raw
                elif 'difc' in task_name.lower() and 'difc' in selected_jurisdictions:
                    results['difc'] = task_output_raw
                elif 'compile' in task_name.lower() or 'summary' in task_name.lower():
                    summary = task_output_raw
                    results['summary'] = summary
        
        # Qatar and Oman use the general compliance result (no separate agents)
        if 'qatar' in selected_jurisdictions and results.get('general'):
            results['qatar'] = results['general']
        if 'oman' in selected_jurisdictions and results.get('general'):
            results['oman'] = results['general']
        
        # If no summary extracted, use the raw result
        if not summary and hasattr(result, 'raw'):
            summary = result.raw
            results['summary'] = summary
            if 'compliance_report_compiler' not in agent_results:
                agent_results['compliance_report_compiler'] = summary
        
        # Determine compliance status
        compliance_status = 'needs_review'
        if summary:
            summary_lower = summary.lower()
            if 'compliant' in summary_lower and 'non' not in summary_lower and 'non_compliant' not in summary_lower:
                compliance_status = 'compliant'
            elif 'non_compliant' in summary_lower or 'non-compliant' in summary_lower:
                compliance_status = 'non_compliant'
        
        return {
            "compliance_status": compliance_status,
            "results": results,
            "summary": summary,
            "agent_results": agent_results
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
