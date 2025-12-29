# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
}

# Create a VPC with public and private subnets across multiple AZs 
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "${var.project_name}-vpc"
  cidr = var.vpc_cidr

  azs             = ["${var.aws_region}a", "${var.aws_region}b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true # Cost optimization for assessment
}

# S3 Bucket for static assets with encryption 
resource "aws_s3_bucket" "static_assets" {
  bucket = "${var.project_name}-assets-${var.environment}"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "s3_enc" {
  bucket = aws_s3_bucket.static_assets.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# RDS Instance in a private subnet 
resource "aws_db_instance" "app_db" {
  allocated_storage      = 20
  db_name                = "appdb"
  engine                 = "postgres"
  engine_version         = "15.3"
  instance_class         = "db.t3.micro"
  username               = "dbadmin"
  password               = var.db_password
  db_subnet_group_name   = module.vpc.database_subnet_group
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  storage_encrypted      = true # Security best practice 
  skip_final_snapshot    = true
}

# Application Load Balancer 
resource "aws_lb" "app_alb" {
  name               = "${var.project_name}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = module.vpc.public_subnets
}

# Security Groups 
resource "aws_security_group" "alb_sg" {
  name   = "alb-sg"
  vpc_id = module.vpc.vpc_id
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "db_sg" {
  name   = "db-sg"
  vpc_id = module.vpc.vpc_id
  # Only allow access from application layer (Least Privilege) 
}