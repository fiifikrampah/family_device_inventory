output "public_subnet_id" {
  description = "The VPC public subnet"
  value       = module.vpc.public_subnets
}

output "private_subnet_id" {
  description = "The VPC private subnet"
  value       = module.vpc.private_subnets
}

output "private_sg_id" {
  description = "The private subnet security group"
  value       = aws_security_group.private.id
}

output "public_sg_id" {
  description = "The public subnet security group"
  value       = aws_security_group.public.id
}

output "vpc_id" {
  description = "The VPC ID"
  value       = module.vpc.vpc_id
}
