# AWS-Security-Automation-Project.
"Automating AWS security audits with Python and Boto3. Focused on catching common misconfigurations like public S3 buckets and missing MFA before they become actual problems."


# AWS-Security-Automation-Project

I built this project to stop doing boring manual security checks in my AWS environment. Instead of clicking around the console, I use these Python scripts to find risks instantly.

### What it actually does:
*   **Public S3 Hunter:** Scans all buckets and flags any that are accidentally set to public.
*   **MFA Police:** Checks all IAM users and lists exactly who hasn't turned on Multi-Factor Authentication yet.

### How to use it:
1.  Make sure you have `boto3` installed: `pip install boto3`
2.  Set up your AWS credentials locally (never upload them here!).
3.  Run the script: `python security_audit.py`

### Why I'm working on this:
Manual audits are slow and I usually miss things. This repo is where I'll keep adding automation scripts as I learn more about cloud security.

