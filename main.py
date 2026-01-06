import os
import glob
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from colorama import Fore, Style, init

# 1. Setup
init(autoreset=True) # Colors for terminal
load_dotenv()

# Verify API Key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print(Fore.RED + "❌ ERROR: GROQ_API_KEY not found in .env")
    exit()

llm = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile")

# 2. The Security Analyst Prompt
audit_prompt = ChatPromptTemplate.from_template("""
You are a Senior Cyber Security Auditor. 
Analyze the following Python code for security vulnerabilities.

Focus on:
1. Hardcoded Secrets (API Keys, Passwords).
2. SQL Injection flaws.
3. Command Injection / RCE.
4. Insecure Imports.

CODE TO ANALYZE:
{code_content}

OUTPUT FORMAT:
If Safe: Return only the word "SAFE".
If Unsafe:
[RISK DETECTED]: (Name of vulnerability)
[SEVERITY]: (High/Medium/Low)
[EXPLANATION]: (One sentence why it is bad)
[FIX]: (Provide the corrected code snippet)
""")

# 3. The Scanner
def scan_directory(target_folder="test_files"):
    print(Fore.CYAN + f"🔎 STARTING CYBER-SENTINEL SCAN ON: {target_folder}...")
    
    # Find all Python files
    files = glob.glob(f"{target_folder}/*.py")
    
    if not files:
        print(Fore.YELLOW + "⚠️ No Python files found to scan.")
        return

    for file_path in files:
        print(Fore.WHITE + "-" * 50)
        print(Fore.BLUE + f"📂 Scanning File: {file_path}")
        
        with open(file_path, "r") as f:
            code_content = f.read()
            
        # 4. The Audit (Send to AI)
        print(Fore.YELLOW + "   ⚡ Analyzing logic...")
        chain = audit_prompt | llm
        result = chain.invoke({"code_content": code_content})
        
        # 5. The Report
        if "SAFE" in result.content and len(result.content) < 10:
            print(Fore.GREEN + "   ✅ STATUS: SECURE")
        else:
            print(Fore.RED + "   🚨 VULNERABILITIES DETECTED!")
            print(Fore.WHITE + result.content)

if __name__ == "__main__":
    # Create a dummy .env file if it doesn't exist just to prevent crashes
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("GROQ_API_KEY=your_key_here")
            
    scan_directory()