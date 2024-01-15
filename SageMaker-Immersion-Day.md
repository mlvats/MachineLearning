# SageMaker Immersion Day

Workshop Link -  https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US

Learning more about SageMaker 
-  https://aws.amazon.com/blogs/machine-learning/part-1-how-natwest-group-built-a-scalable-secure-and-sustainable-mlops-platform/
-  https://aws.amazon.com/sagemaker/pipelines/

![image](https://github.com/mlvats/MachineLearning/assets/32443900/66ea7f3d-5c96-4ec7-b171-5e38fe0f70cf)
---

![image](https://github.com/mlvats/MachineLearning/assets/32443900/36f16742-5a57-42a8-8aeb-399a0648ead7)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/521fdb4a-cf49-4b80-8483-74be449ec839)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/e846f84c-123d-4184-b052-e42efc6da8bd)

![image](https://github.com/mlvats/MachineLearning/assets/32443900/5d6e65f4-d272-4edf-9880-9c3175188958)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/f3765f09-f9f2-4752-927f-602e6eda9f0f)

![image](https://github.com/mlvats/MachineLearning/assets/32443900/5e9fd25b-0b07-402a-9575-aef54b41ffb6)

![image](https://github.com/mlvats/MachineLearning/assets/32443900/13aa26b8-752f-41c2-9d06-3feea159006b)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/4c133380-e864-49c9-99bc-ff34d298fad4)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/1ce38cd7-d951-4063-970f-497f7b979d19)  

![image](https://github.com/mlvats/MachineLearning/assets/32443900/e3c2ea2e-630e-4947-9728-340b94cf9d60)  

Deugger is for Tesorflow (Neural Network ) or XGBoost jobs
![image](https://github.com/mlvats/MachineLearning/assets/32443900/86f0fbd1-09aa-400d-97cd-cf5471dec37b)

![image](https://github.com/mlvats/MachineLearning/assets/32443900/d3f4d003-8ec8-4d7a-9054-20e141ffbc66)

![image](https://github.com/mlvats/MachineLearning/assets/32443900/a1eda7b2-ee51-4b88-92a1-dea068aa4b2a)

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

# Amazon SageMaker Pipelines 
- You can automate the entire model build workflow, including data preparation, feature engineering, model training, model tuning, and model validation, and catalog it in the model registry.  
- You can configure pipelines to run automatically at regular intervals or when certain events are triggered, or you can run them manually as needed.  
- SageMaker Pipelines is a native workflow orchestration tool  for building ML pipelines that take advantage of direct Amazon SageMaker  integration.
-   

# SageMaker Workflows
- As you scale your machine learning (ML) operations, you can use Amazon SageMaker fully managed workflow services to implement continuous integration and deployment (CI/CD) practices for your ML lifecycle.
- For Kubernetes based architectures, you can install SageMaker Operators on your Kubernetes cluster to create SageMaker jobs natively using the Kubernetes API and command-line Kubernetes tools such as kubectl.
- 

##  SageMaker offers the following workflow technologies:
- Amazon SageMaker Model Building Pipelines: Tool for building and managing ML pipelines. 
- Kubernetes Orchestration: SageMaker custom operators for your Kubernetes cluster and components for Kubeflow Pipelines. 
- SageMaker Notebook Jobs: On demand or scheduled non-interactive batch runs of your Jupyter notebook.

### You can also leverage other services that integrate with SageMaker to build your workflow. Options include the following services:
-  Airflow Workflows: SageMaker APIs to export configurations for creating and managing Airflow workflows.
-  AWS Step Functions: Multi-step ML workflows in Python that orchestrate SageMaker infrastructure without having to provision your resources separately.

## Three components improve the operational resilience and reproducibility of your ML workflows: 
 - pipelines
 - model registry, and
 - projects.

# SageMaker projects
- SageMaker projects introduce MLOps templates that automatically provision the underlying resources needed to enable CI/CD capabilities for your ML development lifecycle.
- The following screenshot shows how the three components of SageMaker Pipelines can work together in an example SageMaker project.
![image](https://github.com/mlvats/MachineLearning/assets/32443900/d264f27c-917a-4d61-ba59-165b978ca65f)
-----------------
-----------------
![image](https://github.com/mlvats/MachineLearning/assets/32443900/16da05df-510d-4040-b4bb-6bc1e32dbd9a)

- The MLOps templates that are made available through SageMaker projects are provided via an AWS Service Catalog  portfolio that automatically gets imported when a user enables projects on the Studio domain.
- Two repositories are added to AWS CodeCommit :
- The first repository provides scaffolding code to create a multi-step model building pipeline including the following steps:
     - data processing,
     - model training,
     - model evaluation, and
     - conditional model registration based on accuracy.
- As you can see in the pipeline.py file, this pipeline trains a linear regression model using the XGBoost algorithm on the well-known UCI Abalone dataset .
- This repository also includes a build specification file , used by AWS CodePipeline  and AWS CodeBuild  to run the pipeline automatically.
- The second repository contains code and configuration files for model deployment, as well as test scripts required to pass the quality gate.
    - This repo also uses CodePipeline and CodeBuild, which run an AWS CloudFormation  template to create model endpoints for staging and production.

- Two CodePipeline pipelines:
    -   The ModelBuild pipeline automatically triggers and runs the pipeline from end to end whenever a new commit is made to the ModelBuild CodeCommit repository.
    -   The ModelDeploy pipeline automatically triggers whenever a new model version is added to the model registry and the status is marked as Approved. Models that are registered with Pending or Rejected statuses aren’t deployed.
 
    -   







