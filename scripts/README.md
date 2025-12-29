EBS Volume Cleanup Script
Overview
This Python script automates the identification and removal of unused AWS EBS (Elastic Block Store) volumes. It helps reduce cloud costs and maintains operational hygiene by cleaning up orphaned resources.

Prerequisites
Python 3.x 
boto3 library installed (pip install boto3)
AWS credentials configured via environment variables or AWS CLI

Usage Examples
Dry Run (Default/Safe Mode): To list volumes that would be deleted without actually performing the action:

python cleanup_volumes.py --dry-run

Execution Mode: To proceed with the deletion of identified unattached volumes:

python cleanup_volumes.py --execute

Features
Error Handling: Includes try-except blocks to manage API failures or permission issues.
Logging: Outputs detailed logs of all actions taken for audit purposes.
Configurability: Uses command-line arguments to toggle between dry-run and execution modes