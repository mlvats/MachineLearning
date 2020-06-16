# CT - CCB Risk and Finance Technology

1. Quant Model Deployment. (MDAS - Model Deployment as Service)
    - ML Model Implementation Platform.
      - CMDS : Batch Model Implementation platform.
      - Ninja : Real Time Model Implementation platform.
    - Regulatory - Card: Card Forecasting Model implementation for CECL, CCAR, BO, RWA etc.
    - Regulatory - Non Card: Non Card Forecasting Model Implementation for CECL, CCAR 
    - Price Elasticity - Implementation of Pricing elasticity model to maximize Shareholder Value Added (SVA) by Optimizing Deposit Pricing.
    - NEO (Card Risk ML & Analytics): A new ML & Analytics platform for Card Risk Models.
    - DragNet Customer Graph - Graph Database for New Model Development and Implementation
  
 2. RADAR (Risk Attributes, Decision & Reporting) 
    - XXXX360: A cross LOB data and analytics provider enabling better risk management and opportunities to deepen customer relationships using both on-us and off-us data.
    - Third Party Data Services : CUBE: Strategic Third Party Data ingestion and distribution services
    - FRIDA : Web-based platform that houses the Material Risk Inventory, providing a centralized repository where LOB can identify the risks they manage.
    - Analytics and Reporting : A generic reporting system that provides reporting across multiple systems.
    - Decision Engine Consolidation: Focus on supporting the strategic Risk, Card, MARS and Fraud roadmaps to utilize the Unified Risk Decision System.
    
 3. Model Governance &  Analytics Implementation.
    - Model Risk Governance Hub (MGR Hub) : Strategic system for Model change and workflow management.
    - SAS Control Uplift : remediating all the control issues involved with SAS environments.
    - RQMS : Risk Queuing management Systems.
 
 4. CCB Finance :
    - CARI: Strategic system for Model change and workflow management.
    - Capacity planning
    - BI Insights: Web-based dashboard to pull executive summary by providing wrapper for analytics assets.
  
 5. Data Services :
    - Everest platform services
    - Data Management Program
  
 6. XXXXXX Architecture :
    - Tech Control - Data Central Migration.
  
 MDAS: a fully managed, controlled and SR11-7 compliant production platform for Model execution with end to end data.
 
 MDAS - Batch Models Deployment Patterns.
 
 Model Training :     Model Serving   : Pattern Description
 
  `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ `
   
 -  SAS Sandbox   ==> Hadoop/AWS (Python/Scala & Spark)  ==>  Pattern 1:   Models trained in SAS can gain > 90% performance improvement when deployed on distribution compute using spark.
 
 - MT - Discovery (Python/Scala & Spark) ==> Hadoop/AWS (Python/Scala & Spark)  ==>  Pattern 2: 
 
  - MT - Discovery (Python/Scala & Spark) ==> AWS (Python/Scala & Spark on EMR/ SageMaker)  ==>  Pattern 3: 
 
 - MT - Discovery (single core (SKLearn) ) ==> GKP (CMDS Wrapper + Containerized code)  ==>  Pattern 4:  BYOM (Bring your own model). Suitable for single core processes. Based on data classification, internal or public cloud options can be leveraged.
 
 - AWS (Omni AI Notebook, Sagemaker) ==> - AWS (Omni AI Sagemaker)  ==>  Pattern 5:  BYOM (Bring your own model) &  BYOM (Bring your own data).   Quick migration from training to serving for models trained on Omni AI.
 
  -  SAS Sandbox   ==>  GKP (Python/java )  ==> Pattern 6: Model trained in SAS are being 
   
 
