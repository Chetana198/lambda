output "source_bucket" {
  value = aws_s3_bucket.source.bucket
}

output "destination_bucket" {
  value = aws_s3_bucket.destination.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.move_s3_objects.function_name
}
