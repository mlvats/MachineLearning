aws lambda publish-version --function-name YourFunctionName

AWS CLI Commands:
Publishing a Version:
bash
Copy code
aws lambda publish-version --function-name YourFunctionName
Invoking a Specific Version:
bash
Copy code
aws lambda invoke --function-name YourFunctionName:1 output.txt
Invoking the Latest Version:
bash
Copy code
aws lambda invoke --function-name YourFunctionName:latest output.txt


# Create version 2
aws lambda publish-version --function-name MyLambdaFunction

# Invoke version 2
aws lambda invoke --function-name MyLambdaFunction:2 output.txt
