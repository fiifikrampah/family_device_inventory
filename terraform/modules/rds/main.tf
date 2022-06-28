#Use EKS VPC and private subnets to put RDS in same private subnets

resource "aws_db_subnet_group" "fdi_subnet_grp" {
  name       = "${var.namespace}-vpc"
  subnet_ids = var.private_subnet_id

  tags = {
    Name = "fdi_Subnet_Group"
  }
}

resource "aws_db_parameter_group" "fdi_pgroup" {
  name   = "family-devices-param-grp"
  family = "postgres13"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "aws_db_instance" "fdi_db" {
  identifier             = "family-devices"
  allocated_storage      = 20
  storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "13"
  instance_class         = "db.t3.micro"
  db_name                = var.rds_db
  username               = var.rds_username
  password               = var.rds_password
  port                   = var.rds_port
  parameter_group_name   = aws_db_parameter_group.fdi_pgroup.name
  db_subnet_group_name   = aws_db_subnet_group.fdi_subnet_grp.name
  vpc_security_group_ids = [var.private_sg]
  skip_final_snapshot    = true
}
