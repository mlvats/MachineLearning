Senior Application Engineer - AI/ML Model Governance

About Us:

Join our dynamic team at Vanguard's Chief Data and Analytics Office (CDAO) - Enterprise Data Office (EDO) and play a pivotal role in building and enhancing our AI/ML models governance application. As a Senior Application Engineer, you will contribute to shaping the technical culture of our team and mentor junior developers.

Key Responsibilities:

Utilize your hands-on knowledge of Vanguard's AWS services, including Lambda, DynamoDB, S3, Glue, IAM, CloudFormation, and other relevant services.
Demonstrate strong Python coding and development skills, emphasizing unit testing and end-to-end testing.
Showcase proficiency in JavaScript and React UI for effective application development.
Contribute to API development to enhance the functionality of our AI/ML models governance application.
What You'll Learn:

Gain expertise in the latest tools and practices for AI/ML/LLM model governance.
Collaborate with passionate experts and thought leaders in the AI/ML model Ops and governance space.
Acquire experience in scaling and rolling out an application that will be leveraged across multiple Lines of Business (LOBs).

-----------------

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


Alias Instead of Version:
While versions are a way to reference specific snapshots, using aliases is often recommended for managing invocations in a more flexible manner. Aliases can be updated to point to different versions, allowing you to promote changes through different environments without modifying the invoking code.

Keep in mind that using aliases for version management is often more flexible and recommended in real-world scenarios.

