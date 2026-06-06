import streamlit as st
from sandbox import execute_student_code
from agent import analyze_bug

# Set up the visual page configuration
st.set_page_config(page_title="AI Bug Analyzer", page_icon="🐞", layout="wide")

st.title("🐞 AI-Driven Bug Analysis Assistant")
st.markdown("""
Welcome to the AI Debugger. Paste your buggy Python code below. 
The system will run it in a secure sandbox, catch the exact error trace, and provide an educational fix!
""")

# 1. Create a large text box for the user to paste code
user_code = st.text_area("Paste your Python code here:", height=300, placeholder="def my_function():\n    pass")

# 2. Create an "Analyze" button
if st.button("🚀 Analyze Code"):
    if user_code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        # Show a loading spinner while the sandbox runs
        with st.spinner("Running code in sandbox..."):
            execution_result = execute_student_code(user_code)
        
        # If the code crashes
        if execution_result["is_buggy"]:
            st.error("⚠️ BUG DETECTED! Traceback captured. Sending to Agentic Brain...")
            
            # Show a loading spinner while Gemini thinks
            with st.spinner("🧠 AI Brain is diagnosing the logic error..."):
                error_trace = execution_result["error_trace"]
                analysis_report = analyze_bug(user_code, error_trace)
            
            st.success("Analysis Complete!")
            
            # Display the beautiful markdown report
            st.markdown("---")
            st.markdown(analysis_report)
            
        # If the code actually works perfectly
        else:
            st.success("✅ Code executed successfully! No bugs detected.")
            st.markdown("### Standard Output:")
            st.code(execution_result["stdout"], language="python")