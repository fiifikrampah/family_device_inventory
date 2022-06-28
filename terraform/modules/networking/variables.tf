variable "namespace" {
  type    = string
  default = "fdi"
}

variable "public_subnets_list" {
  type    = list(any)
  default = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "private_subnets_list" {
  type    = list(any)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

variable "postgres_port" {
  description = "POSTGRES_PORT"
  default     = "5432"
}