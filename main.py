from sandbox import execute_student_code
from agent import analyze_bug

def main():
    print("--- 🚀 AI Bug Analysis Assistant Initialized ---\n")

    # 1. A sample piece of buggy Python code
    # Logical Error: An off-by-one error that will cause an IndexError
    sample_code = """
def calculate_average(numbers):
    total = 0
    # BUG: The loop goes one step too far, causing an IndexError
    for i in range(len(numbers) + 1):  
        total += numbers[i]
    return total / len(numbers)

scores = [85, 90, 92]
print("Average:", calculate_average(scores))
"""

    print("Testing the following student code:")
    print(sample_code)
    print("-" * 50)
    print("Running in sandbox...\n")

    # 2. Execute the code using your Perception Toolkit
    execution_result = execute_student_code(sample_code)

    # 3. Handle the output and trigger the Agentic Brain
    if execution_result["is_buggy"]:
        print("⚠️ BUG DETECTED! Traceback captured.")
        print("🧠 Sending data to Agentic Brain for analysis...\n")
        
        error_trace = execution_result["error_trace"]
        
        # 4. Generate the final educational report
        analysis_report = analyze_bug(sample_code, error_trace)
        
        print("=" * 10 + " AI BUG ANALYSIS REPORT " + "=" * 10)
        print(analysis_report)
        print("=" * 44)
    else:
        print("✅ Code executed successfully! Standard Output:")
        print(execution_result["stdout"])

if __name__ == "__main__":
    main()