provider "aws" {
  region     = var.region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

provider "kubernetes" {
  host                   = module.eks.endpoint_name
  cluster_ca_certificate = module.eks.cluster_ca_certificate
  token                  = module.eks.eks_token
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.1"
    }
  }
  required_version = ">= 0.14"
}
