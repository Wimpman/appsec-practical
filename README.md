# Application Security Engineer Skills Assessment

## Objective

The purpose of this assessment is to evaluate your ability to identify, understand, and propose remediations for security vulnerabilities in a segment of code. This will test your knowledge in application security best practices and your ability to apply this knowledge practically.

## Instructions

You are provided with a Python code snippet for a simple Flask web application. Your task is to review the code critically and identify any security vulnerabilities present. For each vulnerability you find, we would like you to:

1. Describe the vulnerability, including its name and how it occurs in the code.  
2. Assess the impact of the vulnerability and classify its severity.  
3. Explain how the vulnerability could potentially be exploited.  
4. Suggest a detailed remediation to address the vulnerability.  

Please document your findings clearly, providing explanations for your assessments and remediation steps. You can assume that the code is part of a real‑world web application and consider the broader implications of each vulnerability.

## Timeframe for Completion

Please allocate no more than 1 hour to complete this assessment. This time constraint is intended to focus on your initial analysis and recommendations rather than a comprehensive audit.

We respect that your time is valuable and understand you may have existing professional and personal commitments. Therefore, we are providing a two‑day window to complete this assessment.

Please submit your completed assessment within 48 hours from the receipt of this assignment. This should give you the flexibility to choose a time that best fits your schedule within this period.

If for any reason you require additional time or need to negotiate a different submission window, please let us know as soon as possible so we can accommodate your request.

---

### Getting Started (optional)

Running the application **is not required** to complete the assessment. The steps below are provided only if you would like to test vulnerabilities directly or validate your proposed remediations.

1. Make sure Python 3.9 or 3.10 is installed.  
2. Create and activate a virtual environment, then install dependencies:

   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On macOS / Linux:
   source venv/bin/activate
   pip install -r requirements.txt

3. Start the application:
   ```bash
   python app.py

4. Visit http://127.0.0.1:5000/ in your browser.
