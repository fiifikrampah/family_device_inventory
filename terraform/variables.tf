variable "namespace" {
  description = "The namespace to use for unique resource naming"
  default     = "fdi"
  type        = string
}

variable "region" {
  description = "AWS region"
  default     = "us-east-1"
  type        = string
}

variable "aws_access_key" {}

variable "aws_secret_key" {}
