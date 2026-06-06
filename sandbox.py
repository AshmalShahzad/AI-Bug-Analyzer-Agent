import subprocess
import sys
import tempfile
import os

def execute_student_code(code_string):
    """
    Executes a string of Python code safely in an isolated subprocess,
    capturing both standard output and runtime crash traces.
    """
    # 1. Create a temporary file to hold the code string securely
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as temp_file:
        temp_file.write(code_string)
        temp_file_path = temp_file.name

    try:
        # 2. Run the code dynamically using the system's python interpreter
        result = subprocess.run(
            [sys.executable, temp_file_path],
            capture_output=True,
            text=True,
            timeout=5  # Safeguard: kills the process after 5 seconds if there's an infinite loop
        )
        
        # 3. Evaluate the process exit code
        if result.returncode == 0:
            return {
                "is_buggy": False,
                "stdout": result.stdout,
                "error_trace": None
            }
        else:
            # Code crashed! Return the exact Traceback error message
            return {
                "is_buggy": True,
                "stdout": result.stdout,
                "error_trace": result.stderr
            }
            
    except subprocess.TimeoutExpired:
        return {
            "is_buggy": True,
            "stdout": "",
            "error_trace": "TimeoutError: Code execution exceeded 5 seconds. (Potential Infinite Loop detected)."
        }
        
    finally:
        # 4. Clean up: Always delete the temporary file from disk
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)