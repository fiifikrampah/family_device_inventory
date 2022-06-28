module "networking" {
  source    = "./modules/networking"
  namespace = var.namespace
}

module "rds" {
  source            = "./modules/rds"
  namespace         = var.namespace
  private_subnet_id = module.networking.private_subnet_id
  private_sg        = module.networking.private_sg_id
}

module "eks" {
  source                 = "./modules/eks"
  private_subnet_id      = module.networking.private_subnet_id
  private_sg             = module.networking.private_sg_id
  vpc_id                 = module.networking.vpc_id
  endpoint               = module.eks.endpoint_name
  cluster_ca_certificate = module.eks.cluster_ca_certificate
  eks_token              = module.eks.eks_token
}

module "helm" {
  source   = "./modules/helm"
  rds_host = module.rds.rds_hostname
  rds_port = module.rds.rds_port
  rds_db   = module.rds.rds_db
}