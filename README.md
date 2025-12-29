# DevOps Engineer Assessment - Ashutosh Shukla

## Overview
This repository contains my solutions for the Anthropic Remote DevOps Engineer Assessment Test. It demonstrates my proficiency in Infrastructure as Code (IaC), CI/CD pipeline design, Kubernetes orchestration, and automation scripting.

## Project Structure
- **/terraform**: AWS infrastructure definitions using Terraform.
- **/.github/workflows**: CI/CD pipeline definition for GitHub Actions.
- **/docs**: Incident post-mortem documentation.
- **/scripts**: Python automation script for EBS cleanup.
- **/k8s**: Kubernetes manifests for a multi-tier application.

## Time Spent per Exercise
| Exercise | Task | Time Spent |
| :--- | :--- | :--- |
| Part 1-3 | Professional Background & Theory | 1.5 Hours |
| Exercise 1 | Infrastructure as Code (Terraform) | 1.0 Hour |
| Exercise 2 | CI/CD Pipeline Design | 0.5 Hours |
| Exercise 3 | Monitoring & Post-Mortem | 0.5 Hours |
| Exercise 4 | Scripting & Automation | 0.5 Hours |
| Exercise 5 | Kubernetes Challenge | 1.0 Hour |
| **Total** | | **5.0 Hours** |

## Assumptions Made
1. **AWS as Primary Provider:** Exercise 1 and 4 assume an AWS environment.
2. **Standard Kubernetes:** Manifests in Exercise 5 are designed for any standard K8s cluster (minikube, EKS, GKE).
3. **Python Environment:** The automation script assumes a Python 3.x environment with `boto3` installed.

## Instructions to Run
- **Terraform:** Run `terraform init` followed by `terraform plan` in the `/terraform` folder.
- **Kubernetes:** Deploy using `kubectl apply -f ./k8s`.
- **Script:** Run `python ./scripts/cleanup_volumes.py`.