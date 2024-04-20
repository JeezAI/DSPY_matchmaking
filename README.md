# 🔍Internship Finder

## 📝Project Overview

JeezAI Internship Finder is an AI-powered web application that connects students with the most compatible internship opportunities. It leverages advanced natural language processing techniques and the power of DSPy framework by Stanford NLP (Omar Khattab, Herumb Shandilya, Arnav Singhvi) to analyze resumes, generate search queries, and provide detailed match analyses between students' credentials and internship requirements.

![image](https://github.com/JeezAI/DSPy_matchmaking/assets/114735073/50934dc0-0b03-4fc2-946d-21794d1a489a)


## 🔑Key Features

- **Resume Parsing:** Automated extraction of pertinent information from resumes.
- **Keyword-Based Search Queries:** Generates dynamic queries to find the best internships.
- **Match Analysis:** Compares student profiles with internship requirements for precise matches.
- **Scalable Data Storage:** Uses Weaviate, a vector database for efficient data storage and retrieval.
- **Streamlit Web Interface:** Provides an easy-to-navigate interface for users to upload resumes and explore internship opportunities.

## 🖥️Technical Architecture

The Internship Finder is built with a stack that includes DSPy for structured AI programming, Cohere for text processing, and Streamlit for the front-end, encapsulated within a modular architectural framework.

### Core Technologies

- **DSPy:** A framework for declarative structured programming in AI. It enables the modularization of NLP tasks into reusable components, enhancing both development efficiency and system scalability. DSPy allows defining declarative language model calls that get compiled into self-improving pipelines. This shifts the focus from manual prompt engineering to treating LMs as devices. It introduces concepts like natural language type signatures, modules, and optimizers to specify transformations, encapsulate prompting techniques, and update LM weights to achieve target metrics. DSPy can be used to build complex pipelines, like multi-hop question answering systems that break down questions, retrieve relevant passages, and synthesize answers. The DSPy compiler enables systematic optimization of prompts by running inputs through the pipeline, analyzing traces, and treating prompt engineering as a discrete AI optimization problem.
 ![image](https://github.com/JeezAI/DSPy_matchmaking/assets/114735073/59ebbbdb-d382-4422-a530-361b112b8eb5)


Some exciting applications mentioned include:
- Generating structured outputs with type predictors, JSON templates, and retry logic
- Building self-correcting pipelines with DSPy assertions and custom guard rails
- Optimizing Chain-of-Thought reasoning for complex question answering
- Integrating with retrieval systems and APIs for grounded language modeling

  You can learn more about the DSPy framework by visiting Stanford NLP GitHub Repo here [https://github.com/stanfordnlp/dspy].

Overall, DSPy provides an impressive framework for building reliable, optimized and complex language model applications in a more automated and scalable way compared to manual prompt engineering. We're excited to try it out for our mathmaking projects.

We also use;
- **Cohere:** Utilized for its newest and most powerful model, Commard R+ in generating search queries and performing deep linguistic analyses. [https://docs.cohere.com/docs/command-r-plus]
- **Weaviate:** Chosen for its vector search capabilities, allowing quick retrieval of internship opportunities from large datasets.We used Weaviate Hybrid search to combine multiple search algorithms to improve the accuracy and relevance of search results. This hybrid query involves both keyword matching and semantic vector search to return the most relevant internship opportunities from the database. [https://weaviate.io/]
- **Streamlit:** Facilitates rapid development of interactive web apps, used here to craft the user interface. 

### 📚Directory Structure

- `main.py` - Orchestrates the user interaction and integrates various modules.
- `tools.py` - Contains utility functions and custom methods for data processing.
- `resume_temp.json` - Template for standardizing resume data format.

## 🤖DSPy Integration

The Internship Finder leverages the power of DSPy to create reusable and modular components for various AI tasks. 

### Modules and Agents

1. **`Internship_finder` (Module):
   - Inherits from `dspy.Module` and encapsulates the core logic for finding relevant internships based on a student's resume.
   - Utilizes a Chain of Thought approach with multiple instances of the `generate_query` signature to generate search queries iteratively.
   - Employs the `generate_analysis` signature to perform a detailed match analysis between the student's background and internship requirements.

2. `generate_query` (Signature):
   - Defines the structure and behavior of the query generation process.
   - Analyzes the resume, extracts keywords from skills, education, experience, and projects.
   - Generates keyword-based queries to search for the best internships in the Weaviate database.

3. `generate_analysis` (Signature):
   - Defines the structure and behavior of the match analysis process.
   - Takes the student's resume and a list of potential internship opportunities as input.
   - Performs a detailed match analysis based on educational background, skill and experience match, and project relevance.
   - Provides a summary of the match analysis for each internship in a structured JSON format.
    

## 📊Data Extraction with Crew AI

Crew AI enhances our data extraction capabilities by automatically pulling structured insights from unstructured internship descriptions. This enriched data supports improved matching accuracy and created JSON file for each database records.

## 🚀Getting Started

### Installation

**Clone the repository:**

   ```bash
   git clone https://github.com/JeezAI/DSPy_matchmaking.git
   ```

# Environment Setup

Set environment variables for API keys:

bash
-export CO_API_KEY="Your_Cohere_API_Key"
-export WCS_API_KEY="Your_Weaviate_API_Key"
-export OPENAI_API_KEY="Your_OpenAI_API_Key"

#Running the Application
Launch the application with Streamlit:

```bash
streamlit run main.py
```
Visit http://localhost:8501 in your web browser to interact with the application.


### Future Enhancements
- Data Source Expansion: Link to more databases for a broader internship selection.
- Personalized Recommendations: Adapt search results based on individual career aspirations and feedback.
- Interactive User Feedback: Use collaborative filtering to refine matching algorithms based on user interactions.
- Real-time Notifications: Implement a system to notify users of new opportunities.
- Integrate with LinkedIn Analyzer and Career Roadmap Planner [https://github.com/JeezAI/careerbuilder_Linkedin2CareerRoadmap]

### 📝Conclusion
The Internship Finder exemplifies the powerful combination of DSPy for structured AI development and Cohere for sophisticated text analysis, providing a robust solution for internship matching. This platform not only streamlines the search process but also offers a scalable framework for future enhancements.

### 🤝Contribution Guidelines
We welcome contributions from the community. Please read our contribution guidelines to learn how you can help improve the Internship Finder.
