resource "local_file" "helm_values" {
  content = templatefile("${path.module}/values_template.yaml", {
    postgres_host = var.rds_host
    postgres_port = var.rds_port
    postgres_db   = var.rds_db
    }
  )
  filename = "${path.module}/../../../kubernetes/values.yaml"
}
