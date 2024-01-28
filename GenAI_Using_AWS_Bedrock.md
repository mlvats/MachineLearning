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


