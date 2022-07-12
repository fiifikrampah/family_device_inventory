packer {
  required_plugins {
    amazon = {
      version = ">= 1.0.0"
      source  = "github.com/hashicorp/amazon"
    }
  }
}

# Builder 
build {
  name = "jenkins-server"
  source "source.amazon-ebs.jenkinsserver" {
    ssh_username = "ec2-user"
  }
  provisioner "ansible" {
    playbook_file = "jenkins/ansible/playbook.yaml"
    user = "ec2-user"
  }

}

locals {
  timestamp = regex_replace(timestamp(), "[- TZ:]", "")
}

# Sources
source "amazon-ebs" "jenkinsserver" {
  region        = "${var.region}"
  ami_name      = "jenkins-server-${local.timestamp}"
  instance_type = "${var.instance_type}"
  source_ami_filter {
    filters = {
      name                = "amzn2-ami-kernel-5.10-hvm-2.0.*.1-x86_64-gp2"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["137112412989"]
  }
  associate_public_ip_address = true
}

# Variables
variable "region" {
  type    = string
  default = "us-east-1"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}