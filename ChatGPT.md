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


# Alias

aws lambda create-alias --function-name YourFunctionName --function-version 2 --name YourAlias

aws lambda update-alias --function-name YourFunctionName --function-version 3 --name YourAlias

aws lambda delete-alias --function-name YourFunctionName --name YourAlias

aws lambda list-aliases --function-name YourFunctionName

Example Usage:
Let's say you have a Lambda function named "MyLambdaFunction," and you want to create an alias "prod" pointing to version 2:

aws lambda create-alias --function-name MyLambdaFunction --function-version 2 --name prod

Now, you can invoke your Lambda function using the "prod" alias:
aws lambda invoke --function-name MyLambdaFunction:prod --payload '{"key1": "value1", "key2": "value2"}' output.txt


