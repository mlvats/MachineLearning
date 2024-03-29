# Building Generative AI Applications Using Amazon Bedrock 
- Link - https://explore.skillbuilder.aws/learn/course/17904/play/94134/module-1-introduction-to-amazon-bedrock

- Amazon Bedrock Workshop : https://catalog.us-east-1.prod.workshops.aws/workshops/a4bdb007-5600-4368-81c5-ff5b4154f518/en-US
- Amazon Bedrock User Guide : https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- Amazon Bedrock API Reference : https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html
- Agents for Amazon Bedrock : https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html

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

# Optimizing LLM Performance

## LLM performance challenges
- Large language models (LLMs) are pretrained on large data collections, and they can perform multiple tasks, such as text generation, text summarization, question answering, and sentiment analysis.
- However, the models do not perform well when the task requires dealing with out-of-domain data or remembering conversational context.
- These challenges lead to hallucinations or inaccurate responses.
- A single prompt to the LLM might not always provide the expected result.
- It might require the chaining of requests to the model to produce accurate results.
- 
## Simplifying LLM development with LangChain
- LangChain provides the software building blocks to reduce the complexity of building functionality from scratch.
- You can use it to take full advantage of the power of the LLMs.
- 
 ![image](https://github.com/mlvats/MachineLearning/assets/32443900/e912bd76-6f68-4bff-89b5-99c3dda1b020)
-------------
- LLMs do not retain state between invocations, so the application must manage any context.
- For example, to give a chat experience, the LLM needs the conversation as part of the context to produce the correct results.
- Additionally, LLMs can develop reasoning to solve problems, such as multistep problems where the application needs to find information in steps to solve a problem.
- LangChain provides components to make it more efficient to perform the common tasks of managing context or the sequencing of steps when interacting with an LLM.

## Using LangChain components
- LangChain is open source and is currently available in three programming languages: Python, TypeScript, and JavaScript.
- LangChain consists of components such as schema, models, prompts, indexes, memory, chains, and agents.
- You can use these components to build applications, such as the Retrieval Augmented Generation (RAG) based question answering chatbots.
- You can also use these components for text summarization, code generation, and interacting with APIs.
- You can use LangChain components to connect LLMs with other sources of data to improve the accuracy of responses.
- Ref Link : https://python.langchain.com/docs/get_started/introduction

## Integrating AWS and LangChain
## Supported integrations for AWS
- LangChain supports integrations with numerous software providers, including Amazon.
- Some of the most important integrations related to Amazon include LLMs, prompt templates, chains, chat models, text embedding models, document loaders, retrievers, and agents.
-  For the current list of all supported Amazon Web Services (AWS) integrations, refer to - https://python.langchain.com/docs/integrations/platforms/aws
  
## Schema
- The schema provides the structure for the conversation to construct the prompts generated by LangChain that are sent to the LLM.
- For example, the ChatMessages schema describes how to construct chat prompts with human messages, artificial intelligence (AI) messages, examples, and documents.
- In the following lessons, you will learn about the most important AWS and LangChain integrations for models, prompt templates, indexes, memory, chains, and agents.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/05edcd91-44f1-4a9b-83de-dd719623df5d)
---------------
# Using Models with LangChain
- In this section, you will learn about the language models that are used in LangChain.
- These models include LLMs, chat models, and text embedding models.

## LLMs
- LLMs take text as input and generate text as output, and LangChain provides LLM components to interact with different language models.
- The LLM class is an abstraction for working across different providers and is used by LangChain to interact with an LLM model.

## Amazon Bedrock
- LangChain supports Amazon Bedrock as an LLM.
- Amazon Bedrock currently supports the following models: Amazon Titan Text, AI21 Labs Jurassic, Anthropic Claude, and Cohere Command.
- The following example demonstrates how to create an instance of the Amazon Bedrock class and invoke an Amazon Titan LLM from the LangChain LLM module.
- The model_id is the value of the selected model available in Amazon Bedrock.

  ```
    from langchain.llms import Bedrock
    inference_modifiers = {"temperature": 0.3, "maxTokenCount": 512}
    llm = Bedrock(
         client = boto3_bedrock,
         model_id="amazon.titan-tg1-large"
         model_kwargs =inference_modifiers
    )
    response = llm.predict("What is the largest city in Vermont?")
    print(response) 
----
## Chat models
- Conversational interfaces, such as chatbots and virtual assistants, can lower the cost of customer support, while improving customer experience.
- LangChain provides a chat models component to build conversational applications.
- This component accepts content in the form of messages that contain input text.
- Chat models example : The following example demonstrates how you can get a response from an LLM by passing a user request to the LLM.
### Input

```
  from langchain.chat_models.bedrock import BedrockChat
  from langchain.schema import HumanMessage
  chat = BedrockChat(model_id="anthropic.claude-v2", model_kwargs={"temperature":0.1})
  messages = [
      HumanMessage(
           content="I would like to try Indian food. Name three Indian vegetarian dishes for a meal."
      )
 ]
 chat(messages)
```

Sample response

```
Response:
AIMessage(content=" Here is a list of Indian vegetarian dishes for a meal: aloo gobi, chana masala, and dal tadka.", additional_kwargs={}, example=False)
```
---------
## Text embedding models
- Text embedding models take text as input and then output numerical representations of the text in the form of a vector of floating-point numbers.
- The numerical representations are called word embeddings, and they capture the semantic meaning of the text.
- The embeddings are used in various natural language processing (NLP) tasks, such as sentiment analysis, text classification, and information retrieval. Y
- You can save the embeddings in a vector database to improve search accuracy and for faster retrieval.

### Embedding example
- The following example demonstrates how to call a BedrockEmbeddings client to send text to the Amazon Titan Embeddings model to get embeddings as a response.

```
from langchain.embeddings import BedrockEmbeddings

embeddings = BedrockEmbeddings(
      credentials_profile_name="bedrock-admin",
      region_name="us-east-1",
     model_id="amazon.titan-e1t-medium"
)

embeddings.embed_query("Cooper is a puppy that likes to eat beef.")
```

- It is important to understand that the embedding vector represents the semantics of the phrase, not of the string.
- This means that synonyms will result in vectors with more similarity, even if the string is quite different.
- 
  
# Constructing Prompts
- The prompt is a single text instruction given to the LLM as input to get a response.
- When building complex generative artificial intelligence (generative AI) applications, you might need to construct prompts in a specific way.
- You can include instructions, context, or examples, and dynamically populate input variables to guide the LLM to return output to meet your requirements.
- 
### Prompt templates in LangChain
- LangChain provides predefined prompt templates in the form of text strings that can take a set of parameters from the user and generate a prompt.
- Prompt templates make prompt engineering more efficient and make it possible to reuse prompts.

### Prompt example
- The following example demonstrates the creation of a prompt template, pass input variables, and templates as arguments.

 ```
from langchain import PromptTemplate

# Create a prompt template that has multiple input variables
multi_var_prompt = PromptTemplate(
     input_variables=["customerName", "feedbackFromCustomer"],
     template="""
     Human: Create an email to {customerName} in response to the following customer service feedback that was received from the customer: 
     <customer_feedback> 
          {feedbackFromCustomer}
     </customer_feedback>
     Assistant:"""
)
# Pass in values to the input variables
prompt = multi_var_prompt.format(customerName="John Doe",
          feedbackFromCustomer="""Hello AnyCompany, 
     I am very pleased with the recent experience I had when I called your customer support.
      I got an immediate call back, and the representative was very knowledgeable in fixing the problem. 
     We are very happy with the response provided and will consider recommending it to other businesses.
     """
)

```

# Structuring Documents with Indexes
- You can use indexes to structure documents and optimize how LLMs interact with them.
- In this section, you will learn about the important indexes that can help with AWS relevant integrations: document loaders, retrievers, and vectorstores.

### Document loaders
- When building generative AI applications using the RAG approach, documents must be loaded from different sources to the LLMs to generate embeddings.
- LangChain provides the document loaders component, which is responsible for loading documents from various sources.
- Sources can include a database, an online store, or a local store.
- You can index and use information from these sources for information retrieval.
- You can use the document loaders to load different types of documents, such as HTML, PDF, and code.
- ref : https://python.langchain.com/docs/modules/data_connection/document_loaders.html
- 
### Document loaders example
- The following example demonstrates the loading of a document from Amazon Simple Storage Service (Amazon S3) using the S3FileLoader module.

```
from langchain.document_loaders import S3FileLoader

loader = S3FileLoader("mysource_bucket","sample-file.docx")
data = loader.load()

```

### Retriever
- LangChain includes a retriever component for fetching relevant documents to combine with language models. When a user submits a query, the retriever searches through the document index to find the most relevant documents. It then sends the results to the application for further processing.
- When building RAG applications on AWS, you can use Amazon Kendra to index and query various data sources.
- Amazon Kendra is a fully managed service that provides semantic search capabilities for state-of-the-art ranking of documents and passages.
- Amazon Kendra also comes with pre-built connectors to popular data sources, such as Amazon S3, SharePoint, Confluence, and websites.
- It supports common document formats, such as HTML, Microsoft Word, PowerPoint, PDF, Excel, and PureText files.
- LangChain supports different retrieval algorithms.
- You can use the AmazonKendraRetriever method to retrieve documents from Amazon Kendra.
- For the complete list of supported retrievers, refer to Retrievers : https://python.langchain.com/docs/modules/data_connection/retrievers/

### Retriever example
The following example demonstrates the use of the AmazonKendraRetriever to query an Amazon Kendra index and pass the results from that call to an LLM as context along with a prompt.

```
from langchain.retrievers import AmazonKendraRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.llms.bedrock import Bedrock


llm = Bedrock(
     credentials_profile_name=credentials_profile_name,
     region_name = region,
     model_kwargs={"max_tokens_to_sample":300,"temperature":1,"top_k":250,"top_p":0.999,"anthropic_version":"bedrock-2023-05-31"},
     model_id="anthropic.claude-v2"
)

retriever = AmazonKendraRetriever(index_id=kendra_index_id,top_k=5,region_name=region)

prompt_template = """ Human: This is a friendly conversation between a human and an AI. 
     The AI is talkative and provides specific details from its context but limits it to 240 tokens.
     If the AI does not know the answer to a question, it truthfully says it does not know.

     Assistant: OK, got it, I'll be a talkative truthful AI assistant.

     Human: Here are a few documents in <documents> tags:
     <documents>
     {context}
</documents>
     Based on the above documents, provide a detailed answer for, {question} 
     Answer "do not know" if not present in the document. 

      Assistant:
     """

PROMPT = PromptTemplate(
     template=prompt_template, input_variables=["context", "question"]
     )

response = ConversationalRetrievalChain.from_llm(
     llm=llm, 
     retriever=retriever, 
     return_source_documents=True, 
     combine_docs_chain_kwargs={"prompt":PROMPT},
     verbose=True)

```
## Vector stores 
- When building generative AI applications, such as question answering bots, the LLMs produce accurate results when relevant company-specific or user-specific data is given as context.
- 

![image](https://github.com/mlvats/MachineLearning/assets/32443900/1fac748f-9ec6-4591-84b7-171281a6d3ed)
--------
- LangChain supports both open source and provider-specific vector stores.
- LangChain supports vector engine for Amazon OpenSearch Serverless and the pgvector extension available with Amazon Aurora PostgreSQL-Compatible Edition.
- LangChain provides the vector stores component to query the supported vector stores for relevant data.

## Vector store example
- The following example demonstrates how to create an instance of the VectorStore class and use OpenSearch Serverless as a vector store to query embeddings.
```
import os

from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import OpenSearchVectorSearch

index_name = os.environ["AOSS_INDEX_NAME"]
endpoint = os.environ["AOSS_COLLECTION_ENDPOINT"]

embeddings = BedrockEmbeddings(client=boto3_bedrock)

vector_store = OpenSearchVectorSearch(
          index_name=index_name,
          embedding_function=embeddings,
          opensearch_url=endpoint,
          http_auth=get_aws4_auth(),
          use_ssl=True,
          verify_certs=True,
          connection_class=RequestsHttpConnection,
     )
retriever = vector_store.as_retriever()

```

# Storing and Retrieving Data with Memory
- Memory plays a crucial role in building conversational interfaces like chatbots.
- The chatbots powered by language models can respond in a human-like manner if they can remember the previous interactions with the user.
- However, the LLMs themselves do not hold state. Hence, a prompt should include the context of the conversation.

## LangChain memory
- LangChain memory provides the mechanism to store and summarize (if needed) prior conversational elements that are included in the context on subsequent invocations.
- LangChain provides components in the form of helper utilities for managing and manipulating previous chat messages.
- These utilities are modular.
- You can chain them with other components and interact with different types of abstractions to build powerful chatbots.
- In LangChain, there are different ways you can implement conversational memory for a chatbot as follows:
    - ConversationBufferMemory: The ConversationBufferMemory is the most common type of memory in LangChain. It includes past conversations that happened between the user and the LLM.
    - ConversationChain: The ConversationBufferMemory is built on top of ConversationChain, which is designed for managing conversations. For a complete list of supported memory types, refer to - https://python.langchain.com/docs/modules/memory/types/
 
## Memory example
- The following example demonstrates the use of ConversationBufferMemory to store the previous conversation and have the LLM respond to subsequent questions by using the chat history.

```
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory

titan_llm = Bedrock(model_id="amazon.titan-tg1-large", client=boto3_bedrock)
memory = ConversationBufferMemory()

conversation = ConversationChain(
     llm=titan_llm, verbose=True, memory=memory
)

print(conversation.predict(input="Hi! I am in Los Angeles. What are some of the popular sightseeing places?")) 
```
- Ask a question without mentioning the city Los Angeles to find out how the model responds according to the previous conversation.
  ```
  print(conversation.predict(input="What is closest beach that I can go to?"))
  ```

  # Using Chains to Sequence Components
  - To build complex generative AI applications, you can chain LLMs with other LangChain components, such as memory and retrievers.
  - For example, you can chain two different tasks. First, ask the LLM to write a blog on a particular topic. Second, request the model to produce a blog title.
  - A chain can also run a set of chains, so you can create a more complex flow with multiple calls to an LLM. It uses the results of one call as the input to the next call.
  - 
## Chaining components
- At its core, a chain is a set of components that run together.
- The component can be a call to an LLM, an API, or a sequence of other chains.
- The component has an input format and an output.
- For example, the LLMChain takes in an LLM, a prompt template, and parameters to the prompt template.
- It returns the output of the LLM call.
- The chain can parse the output of the LLM to a specific format and return the data in a more structured way.
- A chain can also run a set of chains, so you can create a more complex flow with multiple calls to an LLM. It uses the results of one call as the input to the next call.

## Processing large amounts of data
- Chains are also helpful when processing more data than can be contained in the context.
- For example, you might do a document summarization against a very large document.
- The chain will chunk up the document and make multiple calls to the LLM to produce a single summary.
- There are different types of chains that LangChain supports, among which the LLMChain is a common one.
- For the complete list of supported chains, refer to Chains(opens in a new tab). https://python.langchain.com/docs/modules/chains/
- 
## Chain example
- The following example demonstrates how to use chains to call an LLM multiple times in a sequence.
```
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock

llm = Bedrock(
     credentials_profile_name=credentials_profile_name,
     region_name = region,
     model_kwargs=         
 {"max_tokens_to_sample":300,"temperature":1,"top_k":250,"top_p":0.999,"anthropic_version":"bedrock-2023-05-31"},
     model_id="anthropic.claude-v2"
)

prompt = PromptTemplate(
     input_variables=["company"],
     template="Create a list with the names of the main metrics tracked in the reports of {company}.",
)

chain = LLMChain(llm=llm, prompt=prompt)
answers = chain.run("Amazon")
print(answers)

answers = chain.run("AWS")
print(answers)

```
# Managing External Resources with LangChain Agents
- The LLMs are pretrained on a vast amount of text data and learn from a wide range of patterns.
- Hence, they can generate effective text responses.
- However, they lack the capability when it comes to solving rule-based mathematical, logic, and reasoning types of requests.
- 
## Using LangChain agents
- LangChain agents can interact with external sources, such as search engines, calculators, APIs, or databases.
- The agents can also run code to perform actions to assist the LLMs in generating accurate responses.
- LangChain provides the chain interface to sequence multiple components to build an application.
- An LLMChain is an example of a basic chain.
- The following mechanisms use basic chains:
- A RAG application can use an LLMChain to return a response. The response is based on two pieces of information: the user query and a context supplied as a set of documents retrieved from a vector store.
- A RouterChain is an example of a complex chain. For example, you can use a RouterChain to select one prompt template from the available prompt templates based on user input.
- The LangChain agents act as reasoning engines for the LLMs to decide the actions to take and the order in which to take the actions. An action can be a tool that uses the results from a search engine or a math calculator.

 ## LangChain agent features
 -  The LangChain agent follows a sequence of actions :
![image](https://github.com/mlvats/MachineLearning/assets/32443900/90259f3e-5d2d-4bb8-a091-777b9350a18e)
----
- For more information, refer to ReAct : https://python.langchain.com/docs/modules/agents/agent_types/react
- For a complete list of agents, refer to Agents : https://python.langchain.com/docs/modules/agents/
- 
## Agent example
- The following example demonstrates how to initialize an agent, a tool, and an LLM to form a chain.

```
from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms.bedrock import Bedrock
from langchain import LLMMathChain

llm = Bedrock(model_id="anthropic.claude-instant-v1", client=boto3_bedrock, model_kwargs=model_parameter)

```
- A ZERO_SHOT ReAct agent calls the in-built tool LLMMathChain to do math calculations separately and pass the result to the LLM for the final response.

```
llm_math = LLMMathChain(llm=llm)

maths_tool = Tool(
     name='Calculator',
     func=llm_math.run,
     description='Calculator you need to solve math problems.'
)

tools = load_tools(
          ['llm-math'],
          llm=llm
     )

llm_agent = initialize_agent(
     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
     tools=tools,
     llm=llm,
     verbose=True
)

llm_agent.run(" What is the distance between San Francisco and Los Angeles? If I travel from San Francisco to Los Angeles with the speed of 40 , how long will it take?")

```
- LLMs perform multiple tasks, such as text generation, text summarization, question answering, and sentiment analysis.
- However, the models do not perform well when the task requires dealing with out-of-domain data or remembering conversational context.
- These challenges lead to hallucinations or inaccurate responses.

- LangChain agents can interact with external sources, like search engines, calculators, APIs, or databases.
- Agents can also run code to perform actions to assist the LLMs in generating accurate responses.
- The memory component provides the mechanism to store and summarize prior conversational elements that are included in the context on subsequent invocations.
- The retriever is the component for fetching relevant documents to combine with language models.
- The document loaders component is responsible for loading documents from various sources.
- 
  
# Architecture Patterns
## Introduction to Architecture Patterns

- Architecture patterns:  In this module, you will learn about various architecture patterns that can be implemented with Amazon Bedrock for building useful generative AI applications such as the following: 

![image](https://github.com/mlvats/MachineLearning/assets/32443900/991b6376-d36e-49fd-84f7-037692de15d5)
-----

## Text Generation and Text Summarization
####  Text generation
- The architecture pattern for text generation using Amazon Bedrock is illustrated in the following image.
- You can pass the Amazon Bedrock foundation model a prompt using an Amazon Bedrock playground or an Amazon Bedrock API call.
- The model will generate text based on the input prompt you provide. You will learn how to do this in Module 6: Hands on Labs. 
![image](https://github.com/mlvats/MachineLearning/assets/32443900/bea608d8-3bce-4b8a-8df9-944b05513e78)
-----
###  Text generation with LangChain
- For text generation, you can also use a LangChain layer to add a conversation chain to specific text generation use cases.
- LangChain is a powerful open source library.
- It pairs well with some of the strongest text generation FMs on Amazon Bedrock to efficiently create conversations, text generation, and more.
- The architecture pattern for text generation with LangChain is illustrated in the following figure.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/236e02d2-250f-45ab-a61f-ff9833dc2a21)
-----

###  Text summarization
- There are two main types of text summarization techniques:
- Extractive Summarization : This technique involves identifying and selecting the most important words, phrases, or sentences from source a document and then concatenating them to form a summary. The selected elements are usually the most informative and representative parts of the text.
- Abstractive Summarization: This technique involves generating new text that is not a rephrasing of the source document. It consists of creating new text summaries that capture the key ideas and elements of the source text. Abstractive methods should produce coherent text that is similar to human-generated summaries.

### Application of text summarization
- Text summarization can help reduce information overload by synthesizing and surfacing important information that is more digestible and actionable by users. It has a wide range of applications
- 
![image](https://github.com/mlvats/MachineLearning/assets/32443900/fe0ff1de-ab9a-47df-a948-bf90a0508c78)
---

### Architecture patterns for text summarization applications

![image](https://github.com/mlvats/MachineLearning/assets/32443900/20b99536-6db3-4dce-98db-e446daff4f10)
-----
![image](https://github.com/mlvats/MachineLearning/assets/32443900/59d2d9dc-3006-44e2-a2b7-6be61030aed7)
----

### Question answering architecture
- Question answering is an important task that involves extracting answers to factual queries posed in natural language.
- Typically, a question answering system processes a query against a knowledge base containing structured or unstructured data and generates a response with accurate information.
- Ensuring high accuracy is key to developing a useful, reliable, and trustworthy question answering system, especially for enterprise use cases.
- 
![image](https://github.com/mlvats/MachineLearning/assets/32443900/8caca60c-7fff-480d-8289-10a8adc0809b)
----
![image](https://github.com/mlvats/MachineLearning/assets/32443900/32b7d7c1-8204-4e91-ad63-8a09a6e86012)
---
- One of the challenges in question answering is a limited number of tokens in the context.
- It is resolved by using RAG.
- The architecture pattern for personalized and specific use cases results in reliable and accurate responses.

# Chatbots

### Conversational interfaces 
- A basic architectural pattern of a chatbot use case with Amazon Bedrock is illustrated in the following diagram.
- In this basic use case, the user might enter a specific prompt, such as a question to Amazon Bedrock.
- The FM stores the chat, or the questions and responses generated, in a chat history.
- Based on the history of the chat and the current prompt from the user, Amazon Bedrock provides an accurate and helpful response.

  ![image](https://github.com/mlvats/MachineLearning/assets/32443900/a0b9d4c9-ce37-4a3f-8805-95d412c009a4)
-------------
![image](https://github.com/mlvats/MachineLearning/assets/32443900/00ba98c8-8c5a-4644-bfb6-b90c4b2a8d83)
----
### Architecture for a context-aware chatbot
![image](https://github.com/mlvats/MachineLearning/assets/32443900/e6181327-2f63-41e7-80f7-1209c7734a05)
-------------
![image](https://github.com/mlvats/MachineLearning/assets/32443900/0814af64-7449-43b7-aa25-8d5874038ce7)
---------

# Code Generation
##  Coding and programming tasks
- You can also use the foundation models in Amazon Bedrock for various coding and programming related tasks.
- Examples include code and SQL query generation, code explanation and translation, bug fixing, code optimization, and so forth.
- Using foundation models for coding related tasks helps developers and data scientists rapidly prototype their ideas and use cases.
- The following architecture pattern illustrates the use case of using the FMs in Amazon Bedrock for coding and programming. 

![image](https://github.com/mlvats/MachineLearning/assets/32443900/73bbbfe9-e377-478b-954f-4eafb5be71bb)

- In this pattern, you provide a prompt in plain text to the foundation model.
- The prompt includes an instruction telling the model what to generate and, in some cases, a few code examples.
- You can use this architecture for several use cases, such as SQL query generation, completing certain tasks requiring specific code instructions, and so forth. 

## LangChain and Agents for Amazon Bedrock
- Foundation models undergo extensive training on vast amounts of data.
- Despite their substantial natural language understanding capabilities, they cannot independently perform tasks like processing insurance claims or making flight reservations.
- This limitation arises from the necessity for access to the latest company or industry-specific data, which foundation models cannot obtain from up-to-date knowledge sources by default.
- Additionally, FMs cannot take specific actions to fulfill requests without a great deal of manual programming.
- Certain applications demand an adaptable sequence of calls to language models and various utilities depending on user input.
- The agent interface provides flexibility for these applications.
- An agent has availability to a range of resources and selects which ones to use based on the user input.
- Agents can use multiple tools, and they can use the output of one tool as the input for the next.
  
![image](https://github.com/mlvats/MachineLearning/assets/32443900/57f4669a-11c0-4bad-be02-0ad66034fdf0)
----

## Using ReAct to run agents on LangChain
- You can run agents on LangChain by using one of two techniques: plan and execute or ReAct, which stands for reasoning and acting.
- The ReAct technique will evaluate the prompt and determine the next step in solving the problem.
- It will then run that step and then repeat the process until the LLM can answer the question.
- Plan and execute works a little differently in that it determines the steps needed ahead of time and performs them sequentially.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/2d75495d-d831-4412-bc44-b469630f0312)
-----
## Agents for Amazon Bedrock 
- Amazon Bedrock is a fully managed offering that makes it more efficient for developers to automate tasks.
- With agents for Amazon Bedrock, FMs can understand user requests, break down complex tasks into multiple steps, and take necessary actions to fulfill requests. D
- evelopers can use agents for Amazon Bedrock to create an orchestration plan without any manual coding.
- For example, an agent-powered generative AI restaurant application can provide a basic response to the question,
- “Do we have sufficient amounts of dough to sustain this week?” However, it can also help you with the task of updating your inventory.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/71bec0db-4a36-4ba4-a1db-d08da062bf51)
---
- Example: Connecting foundation models to your company data sources with agents for Amazon Bedrock
- Now, you will take a closer look at using agents for Amazon Bedrock with an example.
- Sometimes, you want your foundation models to have access to additional data to help the model generate more relevant, context-specific responses without regularly retraining your foundation model.
- The following steps provide agents access to a knowledge base in Amazon Bedrock. To learn about each step, expand each of the following four categories.

![image](https://github.com/mlvats/MachineLearning/assets/32443900/0956b282-5360-481c-9078-239c3f3ca8d3)
----
![image](https://github.com/mlvats/MachineLearning/assets/32443900/a5cb1a32-63af-4809-9feb-aee55c6f557d)
---














