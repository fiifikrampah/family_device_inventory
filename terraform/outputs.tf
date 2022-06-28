output "rds_host" {
  description = "RDS instance hostname"
  value       = module.rds.rds_hostname
}

output "rds_user" {
  description = "RDS instance root username"
  value       = module.rds.rds_username
}

output "rds_pass" {
  description = "RDS instance password"
  value       = module.rds.rds_password
  sensitive   = true
}

output "rds_port" {
  description = "RDS instance port"
  value       = module.rds.rds_port
}

output "region" {
  description = "AWS Region"
  value       = var.region
}

output "cluster_name" {
  description = "The EKS cluster name"
  value       = module.eks.cluster_name
}