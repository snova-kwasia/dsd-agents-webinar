#!/usr/bin/env python3
"""
Script to run Jupyter notebooks for all sessions and generate a test report.
Dynamically discovers all session notebooks in the notebooks directory.
"""

import subprocess
import sys
import os
import re
from datetime import datetime
from pathlib import Path

# Set up paths
NOTEBOOKS_DIR = Path("/workspace/dsd-agents-webinar/notebooks")
OUTPUT_DIR = Path("/workspace/dsd-agents-webinar/notebook_output")


def discover_session_notebooks() -> list[Path]:
    """Dynamically discover all session notebooks."""
    notebooks = []
    
    # Look for session directories (session_1, session_2, etc.)
    for session_dir in sorted(NOTEBOOKS_DIR.iterdir()):
        if session_dir.is_dir() and session_dir.name.startswith("session_"):
            # Find all .ipynb files in the session directory
            for notebook_file in sorted(session_dir.glob("*.ipynb")):
                notebooks.append(notebook_file)
    
    return notebooks


def run_notebook(notebook_path: Path, output_dir: Path) -> dict:
    """Run a Jupyter notebook and return the result."""
    print(f"\n{'='*60}")
    print(f"Running notebook: {notebook_path}")
    print(f"{'='*60}\n")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Output file for executed notebook
    output_file = output_dir / f"executed_{notebook_path.name}"
    
    # Command to execute notebook
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--ExecutePreprocessor.timeout=600",
        "--output", str(output_file),
        "--output-dir", str(output_dir),
        str(notebook_path)
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=900,  # 15 minutes timeout
            cwd=str(NOTEBOOKS_DIR.parent)
        )
        
        return {
            "notebook": str(notebook_path),
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "notebook": str(notebook_path),
            "success": False,
            "stdout": "",
            "stderr": "Notebook execution timed out after 15 minutes",
            "returncode": -1
        }
    except Exception as e:
        return {
            "notebook": str(notebook_path),
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }


def generate_report(results: list) -> str:
    """Generate a test report from the notebook execution results."""
    report = []
    report.append("=" * 70)
    report.append("NOTEBOOK EXECUTION TEST REPORT")
    report.append("=" * 70)
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    for result in results:
        report.append("-" * 70)
        report.append(f"Notebook: {result['notebook']}")
        report.append("-" * 70)
        report.append(f"Status: {'PASSED' if result['success'] else 'FAILED'}")
        report.append(f"Return Code: {result['returncode']}")
        
        if result['stderr']:
            report.append("")
            report.append("Errors/Stderr:")
            # Only show last 2000 chars of stderr to avoid too much output
            stderr = result['stderr']
            if len(stderr) > 2000:
                stderr = "...\n" + stderr[-2000:]
            report.append(stderr)
        
        if result['stdout']:
            report.append("")
            report.append("Output (stdout):")
            stdout = result['stdout']
            if len(stdout) > 2000:
                stdout = "...\n" + stdout[-2000:]
            report.append(stdout)
        
        report.append("")
    
    # Summary
    report.append("=" * 70)
    report.append("SUMMARY")
    report.append("=" * 70)
    passed = sum(1 for r in results if r['success'])
    failed = sum(1 for r in results if not r['success'])
    report.append(f"Total Notebooks: {len(results)}")
    report.append(f"Passed: {passed}")
    report.append(f"Failed: {failed}")
    report.append("")
    
    return "\n".join(report)


def main():
    """Main function to run notebooks and generate report."""
    print("Starting notebook execution test...")
    print(f"Working directory: {os.getcwd()}")
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv("/workspace/dsd-agents-webinar/.env", override=True)
    
    # Check API keys
    required_keys = ["SAMBANOVA_API_KEY", "TAVILY_API_KEY"]
    missing = [k for k in required_keys if not os.environ.get(k)]
    if missing:
        print(f"WARNING: Missing API keys: {missing}")
        print("Notebooks may fail without these keys.")
    else:
        print("API keys loaded successfully.")
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Dynamically discover all session notebooks
    notebooks = discover_session_notebooks()
    
    if not notebooks:
        print("No session notebooks found!")
        print(f"Looking in: {NOTEBOOKS_DIR}")
        return 1
    
    print(f"\nDiscovered {len(notebooks)} notebook(s):")
    for nb in notebooks:
        print(f"  - {nb}")
    
    # Run notebooks
    results = []
    
    for notebook_path in notebooks:
        result = run_notebook(notebook_path, OUTPUT_DIR)
        results.append(result)
    
    # Generate report
    report = generate_report(results)
    
    # Save report
    report_file = OUTPUT_DIR / "test_report.txt"
    with open(report_file, "w") as f:
        f.write(report)
    
    print(f"\nReport saved to: {report_file}")
    print("\n" + report)
    
    # Return exit code based on results
    if all(r['success'] for r in results):
        print("\n✓ All notebooks executed successfully!")
        return 0
    else:
        print("\n✗ Some notebooks failed to execute.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
