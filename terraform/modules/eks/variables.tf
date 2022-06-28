variable "cluster_name" {
  default = "fdi-eks-cluster"
}

variable "private_subnet_id" {
  description = "The VPC private subnet"
  type        = list(any)
}

variable "vpc_id" {
  description = "The VPC ID"
}

variable "private_sg" {}

variable "endpoint" {
  description = "The EKS endpoint"
}

variable "cluster_ca_certificate" {
  description = "The EKS CA certificate"
}

variable "eks_token" {
  description = "The EKS auth token"
}
