output "rds_hostname" {
  description = "RDS instance hostname"
  value       = aws_db_instance.fdi_db.address
}

output "rds_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.fdi_db.username
}

output "rds_password" {
  description = "RDS instance password"
  value       = aws_db_instance.fdi_db.password
  sensitive   = true
}

output "rds_port" {
  description = "RDS instance port"
  value       = aws_db_instance.fdi_db.port
}

output "rds_db" {
  description = "RDS DB Name"
  value       = aws_db_instance.fdi_db.db_name
}