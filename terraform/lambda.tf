data "archive_file" "lambda" {
  type        = "zip"
  source_file = "../src/ingestion_lambda_function_raw/ingestion-raw.py"
  output_path = "../src/ingestion_lambda_function_raw/ingestion-raw.zip"
}
resource "aws_lambda_function" "lambda-source-raw" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename         = data.archive_file.lambda.output_path
  function_name    = "ingest-mvlens-raw"
  role             = aws_iam_role.iam_for_lambda.arn
  handler          = "ingestion-raw.lambda_handler"
  source_code_hash = data.archive_file.lambda.output_base64sha256
  timeout          = 900
  runtime          = "python3.10"
  ephemeral_storage {
    size = 512 # min 512 MB and the max 10240 MB
  }

  environment {
    variables = {
      codebucket = "indl-data-ingestion-code"
    }
  }

}
