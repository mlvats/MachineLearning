# Building Generative AI Applications Using Amazon Bedrock 
- Link - https://explore.skillbuilder.aws/learn/course/17904/play/94134/module-1-introduction-to-amazon-bedrock

------

 ## Amazon Bedrock offers several natural language processing (NLP) capabilities that can assist data scientists in their work.
- Text summarization
- Text generation
- Question answering systems
- Agents : Agents for Amazon Bedrock understand natural language user requests, break down complex tasks into API calls and data lookups, maintain conversation context, and take actions to fulfill requests.
          The service orchestrates prompt engineering with company-specific or domain-specific information and provides natural language responses.
          Agents for Amazon Bedrock handle infrastructure, monitoring, encryption, permissions, and invocation management without custom code.
  
- By using generative AI, data scientists can focus on architecting innovative solutions, such as
  - AI assistants,
  - Supply chain optimizers,
  - Personalized recommendation systems
 
- Generative AI for every business : https://aws.amazon.com/generative-ai/
- Top generative AI use cases : https://aws.amazon.com/generative-ai/use-cases/
- Generative AI Customer Stories : https://aws.amazon.com/generative-ai/customers/
- Amazon Bedrock : https://aws.amazon.com/bedrock/

  # Typical components of a generative AI application

  - A foundation model (FM) is in the center surrounded by components.
  - These include frontend web application or mobile app,
  - FM interface,
  - machine learning (ML) environment,
  - model training,
  - enterprise datasets,
  - vector database,
  -  text and image embeddings, and
  -  long-term memory store.
  -  Governance and security are integrated into all components.

  ![image](https://github.com/mlvats/MachineLearning/assets/32443900/9b07660e-b0b1-4c94-a831-0f7c330f92b1)


  # Foundation Models and the FM Interface
  - At the heart of a generative AI application is the foundation model that powers it.
  - Foundation models are models trained on broad data at scale that can be adapted to various downstream tasks.
  - As a result of their training, you can deploy foundation models to perform a variety of tasks.
  - Here’s where they differ from traditional machine learning models, which you can only use for the tasks they are trained on.
  - Foundation models provide the base on which you can build various generative AI applications.
  - Large language models (LLMs) are a subset of foundation models that are trained on a large corpus of text data.
  - 
  ![image](https://github.com/mlvats/MachineLearning/assets/32443900/58b98ef4-3a45-4fe6-acd1-0c723712731c)

# Interface and prompts
- To use a foundation model, you need an interface that provides access to it.
-  The interface is generally an API that is managed, or it can be self-hosted using an open source or proprietary model.
-  Using the API call, you can pass prompts to the foundation model and receive inference responses back.

# Inference parameters 
- Along with supplying prompts, using effective inference parameters can strongly influence the output from a foundation model.
- You can pass the parameters along with the prompts to the foundation model interface APIs.
- LLMs operate on tokens, which can be words, letters, or partial word units. (One thousand tokens is equivalent to approximately 750 words.)
- The LLM takes a sequence of input tokens and predicts the next token.
- The inference parameters help provide guidance to the LLM to produce the output or a sequence of tokens that are relevant for your use case.
## some inference parameters
 - Top P. : This technique controls choosing from the smallest possibility of tokens where the combined probability exceeds the parameter Top P. A higher value of Top P, such as 0.9, means the output is more deterministic and predictable because it chooses the most probable next tokens. Lower values can increase diversity, but output can become incoherent. It’s essential that you balance creativity and coherence.
 - Top K : Whereas Top P works based on probabilities, Top K reduces the sample size to the next k probable tokens. Typical k values are from 10 to 100. A k value of 1 is called a greedy strategy because the most probable token is always chosen.
 - Temperature parameter : Whereas Top P and Top K control which tokens are chosen based on the model’s output, the temperature parameter affects the model’s output directly. The higher the temperature, the flatter the probability distribution, which means it will be uniform across tokens. The generated tokens will be more creative and random. Lower temperature will polarize the distribution, which make deterministic outputs possible.
 - 

# Working with Datasets and Embeddings
 - Ingesting and using enterprise data sources provide the foundation model with domain-specific knowledge to generate tailored, highly relevant outputs that align with the needs of the enterprise.
 - You can supply enterprise data to the foundation models as context along with the prompt, which will help the model to return more accurate outputs.
 -  How do you figure out the context to pass? For that, you need a way to search the enterprise datasets using the prompt text that is passed.
 -  This is where vector embeddings help.

# Vector embeddings
- Embedding is the process by which text, images, and audio are given numerical representation in a vector space.
- Embedding is usually performed by a machine learning model.
- The following diagram provides more details about embedding. 

![image](https://github.com/mlvats/MachineLearning/assets/32443900/64d7f900-d857-4000-880f-59a53c25a30d)

- Enterprise datasets, such as documents, images and audio, are passed to ML models as tokens and are vectorized.
- These vectors in an n-dimensional space, along with the metadata about them, are stored in purpose-built vector databases for faster retrieval.
- For this example, consider only the text modality.
- The goal of generating embeddings is to capture semantic similarities between text so that text with similar meanings is mapped to nearby points in the vector space.
- Embeddings are often multi-dimensional vectors.
- Embedding helps when searching for similar words to find relevant information based on the user’s prompts.
- Amazon Bedrock provides the Amazon Titan Embeddings G1 - Text model that can convert text into embeddings.
- These embeddings are stored in a vector database. For more information, refer  :  https://docs.aws.amazon.com/bedrock/latest/userguide/embeddings.html

# Vector databases
- The core function of vector databases is to compactly store billions of high-dimensional vectors representing words and entities.
- Vector databases provide ultra-fast similarity search across these billions of vectors in real time.
- The most common algorithms used to perform the similarity search are k-nearest neighbors (k-NN) or cosine similarity.
- AWS also offers Pinecone in the AWS Marketplace, and there are open source, in-memory options, like Facebook AI Similarity Search (FAISS), Chroma, and many more.
- Link :  https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk

![image](https://github.com/mlvats/MachineLearning/assets/32443900/3004ed0d-8703-4fc2-808d-39db8057deed)

# Amazon Web Services (AWS) offers the following as viable vector database options:
- Amazon OpenSearch Service (provisioned)
- Amazon OpenSearch Serverless
- pgvector extension in Amazon Relational Database Service (Amazon RDS) for PostgreSQL
- pgvector extension in Amazon Aurora PostgreSQL - Compatible Edition
- 

# Vectorized enterprise data
- After enterprise data is vectorized, you can search the given prompt in a vector database.
- You can supply the relevant chunks of information as context to improve the output of the generative AI model.
- This can reduce hallucinations, a phenomenon in which an LLM confidently generates plausible sounding but false information.
- Vector databases and context are used in Retrieval Augmented Generation (RAG).

# Additional Application Components
## Prompt history store 
- A prompt history store is another essential component in a generative AI application, particularly applications used for conversational AI, like chatbots.
- A prompt history store helps with contextually aware conversations that are both relevant and coherent.
- Many foundation models have a limited context window, which means you can only pass so much data as input to them.
- Storing state information in a multiple-turn conversation becomes difficult, which is why a prompt history store is needed.
- It can persist the state and make it possible to have long-term memory of the conversation.
- By storing the history of prompts and responses, you can look up prompts from a previous conversation and avoid repetitive requests to the foundation model.
- This helps with requests from your audit and compliance teams about adherence to company policy and regulations.
- You can also debug prompt requests and responses to diagnose errors and warnings from your applications.

# Frontend web applications and mobile apps
- Often, you need to build a frontend application or app that acts as an interface for your users to use generative AI capabilities from the foundation model.
- The application or app is responsible for constructing prompts and calling the foundation model API.
- The responses from the foundation model are sanitized and filtered by the application or app before the users see them on their screens.
- The application or app should also handle failures and other unintended consequences in a seamless manner so the user experience is not affected.
- 
# RAG (Retrieval Augmented Generation)
- RAG is a framework for building generative AI applications that can make use of enterprise data sources and vector databases to overcome knowledge limitations.
- RAG works by using a retriever module to find relevant information from an external data store in response to a user's prompt.
- This retrieved data is used as context, combined with the original prompt, to create an expanded prompt that is passed to the language model.
- The language model then generates a completion that incorporates the enterprise knowledge.
- With RAG, language models can go beyond their original training data to use up-to-date, real-world information.
- RAG addresses the challenge of frequent data changes because it retrieves updated and relevant information instead of relying on potentially outdated sets of data.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/e54d0118-95cb-4fb8-b450-e41aa16aeaa5)


- There are two distinct stages when using the RAG pattern.
- The lower portion of the diagram explains converting the existing knowledge documents into vector embeddings and storing them in a vector database.
- This phase is typically performed by a batch job.
- After it is complete, you can augment the user’s query with relevant information or documents using semantic search.
- You can then pass the user’s query and retrieved information into an LLM for completion.

# Model Fine-Tuning
## Limitations of RAG and how fine-tuning can address them
- RAG is useful for enterprise use cases, but relying solely on RAG has some limitations.
- For example, the retrieval is limited to the enterprise datasets that are embedded into the vector stores at the time of the retrieval.
- The model remains static.
- The retrieval can add latency, and, for some use cases, that latency can be a problem.
- Also, the retrieval is based on pattern matching instead of a complex understanding of the context.
- Model fine-tuning can change the underlying foundation model as little or as much as you want.
- The model can learn the enterprise nomenclature, proprietary datasets, terminologies, and so on.
- Think of this as a permanent change to the underlying model.
-  By comparison, RAG makes the model intelligent only temporarily by supplying context from relevant document chunks.
- 
 
## There are two broad categories of fine-tuning:
-  prompt-based learning and
-  domain adaptation.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/9fe93812-d42b-4535-83a3-357c3b67385c)
-------------
![image](https://github.com/mlvats/MachineLearning/assets/32443900/bcb02099-ca09-4430-982a-c2cf7a49b92b)
--------------

# Comparing RAG and fine-tuning
- Both RAG and fine-tuning are suitable for customizing a foundation model for serving enterprise use cases.
- The choice ultimately depends on users as they consider a host of parameters, such as complexity, cost, and so forth.

# Securing Generative AI Applications
## Governance and security
- Governance and security are of paramount importance when building generative AI applications.
- Governance and security must be in place to make sure that you mitigate risks, maintain oversight, ensure accountability, and earn trust with your customers.
  
## Consider the following points when building generative AI applications:
- Manage and audit who can access each part of the generative AI application, such the foundation models, API methods, and so on.
- Monitor, log, and report on access to the underlying foundation model either directly or through customized approaches.
- Log requests to and responses from the foundation model to stay compliant with regulations and to ensure explainability of your actions.
- Periodically audit foundation models with test data and simulate prompt injection attacks to ensure that there are no unintended consequences.
- Document the complete process of the various facets of the application and keep them up to date.

 # Generative AI Application Architecture
 
##  Phase 1
- The focus of this phase is to convert the enterprise data used to augment input prompts into a compatible format to perform a relevancy search.
- This is done using an embeddings machine learning model.
- The batch job calls the model to convert existing knowledge documents into its numerical representations.
- The batch job then stores the data in a vector database using the approach described in the following three steps.

## Phase 2
- Phase 2 comprises seven steps. To learn more, choose each of the following seven numbered markers.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/d834b78d-ba84-49bf-83a3-ba46c2f895f0)


# Introduction to Amazon Bedrock Foundation Models

-  Each of these FMs cater to different generative artificial intelligence (generative AI) use cases, such as summarization, language translation, coding, and image generation.
-  
![image](https://github.com/mlvats/MachineLearning/assets/32443900/10c4ee6d-c540-4f49-993d-506e18b5fff5)

-----------------

## Inference parameters
 - When interacting with an FM, you can configure the inference parameters to customize the FM’s response.
 - Generally, you should only adjust one parameter at a time, and the results can vary depending on the FM.
 - The following parameters can be used to modify the output from the LLMs. Not all parameters are available with all LLMs.
 - 
### Randomness and diversity
![image](https://github.com/mlvats/MachineLearning/assets/32443900/c7cc24c3-e604-457f-9a63-6f37bb517d0c)

### Length
- Foundation models typically support the following parameters to control the length of the generated response.
![image](https://github.com/mlvats/MachineLearning/assets/32443900/52989555-3941-4254-a9db-a6810cf10281)
------------------

# Using Amazon Bedrock FMs for Inference

- Some inference parameters are common across most models, such as temperature, Top P, Top K, and response length.
- You will dive deep into unique model-specific parameters and I/O configuration you can tune to achieve the desired output based on the use case.
- 
## Amazon Titan
 - Amazon Titan models are Amazon foundation models. Amazon offers the Amazon Titan Text model and the Amazon Titan Embeddings model through Amazon Bedrock.

## AI21 Jurassic-2 (Mid and Ultra)

## Anthropic Claude 2
- Anthropic Claude 2 is another model available for text generation on Amazon Bedrock.
- Claude is a generative AI model by Anthropic. It is purpose built for conversations, summarization, question answering, workflow automation, coding, and more.
- It supports everything from sophisticated dialogue and creative content generation to detailed instruction

## Stability AI (SDXL)
- This is a text-to-image model used to generate detailed images. SDXL includes support for the following types of image creation:
-  Image-to-image prompting: This involves inputting one image to get variations of that image.
-  Inpainting: This involves reconstructing the missing parts of an image.
-  Outpainting: This involves constructing a seamless extension of an existing image.

## Cohere Command
- Command is the flagship text generation model by Cohere.
- It is trained to follow user commands and be useful instantly in practical business applications, such as summarization, copywriting, dialogue, extraction, and question answering.
- Optimized for business priorities, Cohere is System and Organizations Control (SOC) 2 compliant and emphasizes security, privacy, and responsible AI.

# Amazon Bedrock Methods
- Amazon Bedrock provides a list of APIs you can access in your respective notebooks and AWS Lambda functions to access Amazon Bedrock.
- There are Amazon Bedrock configuration related APIs and runtime-related APIs.

## Amazon Bedrock set up and configuration related APIs
- ListFoundationModels
## Amazon Bedrock runtime-related APIs
- InvokeModel
- InvokeModelWithResponseStream

# Data Protection and Auditability

## Comprehensive data protection and privacy
 -  Your data used with Amazon Bedrock is not used for service improvement and is not shared with third-party model providers.
 -  You can use AWS PrivateLink with Amazon Bedrock to establish private connectivity between your FMs and your virtual private cloud (VPC) without exposing your traffic to the internet.
 -  Your data is encrypted in transit and at rest.
 -  You can customize FMs privately so you can control how your data is used and encrypted.
 -  Amazon Bedrock makes a separate copy of the base foundation model and trains the private copy of the model.

## Secure your generative AI applications

- Link - https://docs.aws.amazon.com/bedrock/latest/userguide/security.html

![image](https://github.com/mlvats/MachineLearning/assets/32443900/c857895a-d625-497c-b62a-f6caf63706d3)

----------
## Support for governance and auditability

![image](https://github.com/mlvats/MachineLearning/assets/32443900/7938943b-90b5-47da-8459-22ed6583e600)


 - Monitor Amazon Bedrock : https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html

Ref Link 
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/security.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html
----


 

- 


 


