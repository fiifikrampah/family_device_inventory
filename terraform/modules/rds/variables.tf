variable "namespace" {
  type    = string
  default = "fdi"
}

variable "rds_password" {
  type        = string
  description = "POSTGRES_PASSWORD"
  default     = "password"
  sensitive   = true
}

variable "rds_username" {
  type        = string
  description = "POSTGRES_USER"
  default     = "postgres"
}

variable "rds_db" {
  type        = string
  description = "POSTGRES_DB"
  default     = "familydevices"
}

variable "rds_port" {
  description = "POSTGRES_PORT"
  default     = "5432"
}

variable "private_subnet_id" {
  description = "The VPC private subnet"
  type        = list(any)
}

variable "private_sg" {}
