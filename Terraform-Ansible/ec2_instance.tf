terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {
  region     = "ap-southeast-2"
  access_key = "AKIA3WERWNOMDLWKKEPC"
  secret_key = "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"
}
resource "tls_private_key" "rsa_4096" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
variable "key_name" {}
resource "aws_key_pair" "key_pair" {
  key_name   = var.key_name
  public_key = tls_private_key.rsa_4096.public_key_openssh
}
resource "local_file" "private_key" {
  content  = tls_private_key.rsa_4096.private_key_pem
  filename = var.key_name
}
resource "aws_instance" "public_instance" {
  ami           = "ami-0df4b2961410d4cff"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.key_pair.key_name
  tags = {
    Name = "public_instance1"
  }
}
