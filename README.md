# Internship Finder

## Project Overview

JeezAI Internship Finder is an AI-powered web application that connects students with the most compatible internship opportunities. It leverages advanced natural language processing techniques and the power of DSPy (Declarative Structured Programming for AI) to analyze resumes, generate search queries, and provide detailed match analyses between students' credentials and internship requirements.

## Key Features

- **Resume Parsing:** Automated extraction of pertinent information from resumes.
- **Keyword-Based Search Queries:** Generates dynamic queries to find the best internships.
- **Match Analysis:** Compares student profiles with internship requirements for precise matches.
- **Scalable Data Storage:** Uses Weaviate, a vector database for efficient data storage and retrieval.
- **Streamlit Web Interface:** Provides an easy-to-navigate interface for users to upload resumes and explore internship opportunities.

## Technical Architecture

The Internship Finder is built with a stack that includes DSPy for structured AI programming, Cohere for text processing, and Streamlit for the front-end, encapsulated within a modular architectural framework.

### Core Technologies

- **DSPy:** A framework for declarative structured programming in AI. It enables the modularization of NLP tasks into reusable components, enhancing both development efficiency and system scalability. DSPy allows defining declarative language model calls that get compiled into self-improving pipelines. This shifts the focus from manual prompt engineering to treating LMs as devices. It introduces concepts like natural language type signatures, modules, and optimizers to specify transformations, encapsulate prompting techniques, and update LM weights to achieve target metrics. DSPy can be used to build complex pipelines, like multi-hop question answering systems that break down questions, retrieve relevant passages, and synthesize answers. The DSPy compiler enables systematic optimization of prompts by running inputs through the pipeline, analyzing traces, and treating prompt engineering as a discrete AI optimization problem.This declarative approach leads to significant quality improvements over few-shot prompting and can match the performance of powerful models like GPT-3.5 through optimized prompts.

Some exciting applications mentioned include:
- Generating structured outputs with type predictors, JSON templates, and retry logic
- Building self-correcting pipelines with DSPi assertions and custom guard rails
- Optimizing Chain-of-Thought reasoning for complex question answering
- Integrating with retrieval systems and APIs for grounded language modeling

  You can learn more about the DSPy framework by visiting Stanford NLP GitHub Repo here [https://github.com/stanfordnlp/dspy].

Overall, DSPy provides an impressive framework for building reliable, optimized and complex language model applications in a more automated and scalable way compared to manual prompt engineering. We're excited to try it out for our mathmaking projects.

We also use;
- **Cohere:** Utilized for its newest and most powerful model, Commard R+ in generating search queries and performing deep linguistic analyses. [https://docs.cohere.com/docs/command-r-plus]
- **Weaviate:** Chosen for its vector search capabilities, allowing quick retrieval of internship opportunities from large datasets. [https://weaviate.io/]
- **Streamlit:** Facilitates rapid development of interactive web apps, used here to craft the user interface. 

### Directory Structure

- `main.py` - Orchestrates the user interaction and integrates various modules.
- `tools.py` - Contains utility functions and custom methods for data processing.
- `resume_temp.json` - Template for standardizing resume data format.

## DSPy Integration

Internship Finder leverages DSPy's structured programming capabilities to create well-defined, isolated modules that perform specific AI tasks. This section details the key DSPy components:

### Modules and Agents

- **Internship_finder Module:** Core module handling the logic for querying internships.
  - Inherits from `dspy.Module`.
  - Uses `generate_query` and `generate_analysis` signatures to iterate through query generation and match analysis.
  
- **generate_query Signature:**
  - Responsible for parsing the resume data to extract skills, experiences, and education.
  - Generates targeted search queries for internships using extracted keywords.
  
- **generate_analysis Signature:**
  - Takes resume data and potential internship matches as inputs.
  - Conducts thorough compatibility analyses, outputting a structured match analysis in JSON format.

## Data Extraction with Crew AI

Crew AI enhances our data extraction capabilities by automatically pulling structured insights from unstructured internship descriptions. This enriched data supports improved matching accuracy and created JSON file for each database records.

## Getting Started

### Installation

# Environment Setup

Set environment variables for API keys:

bash
export CO_API_KEY="Your_Cohere_API_Key"
export WCS_API_KEY="Your_Weaviate_API_Key"
export OPENAI_API_KEY="Your_OpenAI_API_Key"
Running the Application
Launch the application with Streamlit:

bash
Copy code
streamlit run main.py
Visit http://localhost:8501 in your web browser to interact with the application.


### Future Enhancements
- Data Source Expansion: Link to more databases for a broader internship selection.
- Personalized Recommendations: Adapt search results based on individual career aspirations and feedback.
- Interactive User Feedback: Use collaborative filtering to refine matching algorithms based on user interactions.
- Real-time Notifications: Implement a system to notify users of new opportunities.

### Conclusion
The Internship Finder exemplifies the powerful combination of DSPy for structured AI development and Cohere for sophisticated text analysis, providing a robust solution for internship matching. This platform not only streamlines the search process but also offers a scalable framework for future enhancements.

### Contribution Guidelines
We welcome contributions from the community. Please read our contribution guidelines to learn how you can help improve the Internship Finder.
