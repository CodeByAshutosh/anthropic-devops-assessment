Pipeline Flow Overview
The pipeline is designed as a multi-stage workflow using GitHub Actions to ensure code quality and secure deployment.

Build & Test Stage:


Trigger: Initiated by a push to main or staging branches.


Unit Testing: Runs pytest to ensure application logic is sound before building artifacts.

Security Scan Stage:


Docker Build: Creates a container image of the Python application.


Vulnerability Scanning: Uses Trivy to scan the image layers for known CVEs (Common Vulnerabilities and Exposures).

Deployment Stage:


Staging: Automated deployment occurs when code is pushed to the staging branch.


Production: Deployment to the production cluster is restricted to the main branch.

Decision Points

Failure Termination: If tests or security scans fail, the pipeline terminates immediately, preventing faulty or insecure code from reaching any environment.


Production Approval Gate: Deployment to production requires a manual sign-off within GitHub Actions "Environments," ensuring a "human-in-the-loop" check for high-stakes releases.

2. Strategy for Handling Secrets and Credentials
This section outlines the security posture for managing sensitive data like AWS keys and Kubernetes configs.


GitHub Actions Secrets: All sensitive credentials (e.g., AWS_ACCESS_KEY_ID, KUBECONFIG) are stored as encrypted Repository Secrets.


Environment Isolation: Secrets are scoped to specific environments (Staging vs. Production) to prevent accidental cross-environment access.


Runtime Injection: Secrets are never hardcoded in the source code; they are injected as environment variables only during the execution of the specific pipeline job.


Least Privilege: The CI/CD service account is granted only the permissions necessary to push images to the registry and update Kubernetes manifests.