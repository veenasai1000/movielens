variable "aws_region" {
  description = "AWS_Region"
  type        = string
  default     = "us-east-2"
}

variable "vpc_cidr_block" {
  description = "VPC CIDR BLOCK"
  type        = string
  default     = "192.168.0.0/20"
}

variable "public_subnet_cidr_block" {
  description = "PUBLIC SUBNET CIDR BLOCK"
  type        = string
  default     = "192.168.0.0/26"
}

variable "private_subnet_cidr_block" {
  description = "PRIVATE SUBNET CIDR BLOCK"
  type        = string
  default     = "192.168.0.64/26"
}

variable "public_availability_zone" {
  description = "PUBLIC AVAILABILITY ZONE"
  type        = string
  default     = "us-east-2a"
}

variable "private_availability_zone" {
  description = "PRIVATE AVAILABILITY ZONE"
  type        = string
  default     = "us-east-2a"
}
