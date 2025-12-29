# Exercise 1: Infrastructure as Code (AWS)

## Overview
This Terraform configuration provisions a highly available, secure 3-tier web architecture on AWS.

## Deployment Instructions
1. **Prerequisites**: Ensure Terraform and AWS CLI are installed and configured with appropriate credentials.
2. **Initialize**: Run `terraform init` to download the AWS provider and necessary modules.
3. **Configuration**: Review `variables.tf`. You can override defaults using a `terraform.tfvars` file or environment variables.
4. **Plan**: Run `terraform plan` to preview the infrastructure changes.
5. **Apply**: Run `terraform apply` to provision the resources.

## Security Features
- **Encryption**: RDS and S3 resources are encrypted at rest.
- **Network Isolation**: Application and Database tiers are placed in private subnets.
- **IAM Roles**: EC2 instances use IAM roles with minimal permissions for S3 access.