import dspy
import os
from dspy.retrieve.weaviate_rm import WeaviateRM
import weaviate
import json
import streamlit as st
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl
from tools import resume_into_json

gpt4 = dspy.OpenAI(model="gpt-3.5-turbo-1106")

url = "https://internships-hc3oiv0y.weaviate.network"
apikey = os.getenv("WCS_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate
weaviate_client = weaviate.connect_to_wcs(
    cluster_url=url,  
    auth_credentials=weaviate.auth.AuthApiKey(apikey
    ),
        headers={
        "X-OpenAI-Api-Key": openai_api_key  
    }  
    
)


retriever_model = WeaviateRM("Internship", weaviate_client=weaviate_client)
questions = weaviate_client.collections.get("Internship")

dspy.settings.configure(lm=gpt4,rm=retriever_model)
# Weaviate client configuration


class JobListing(BaseModel):
    city: str
    date_published: datetime  # Assuming the date can be parsed into a datetime object
    apply_link: HttpUrl  # Pydantic will validate this is a valid URL
    company: str
    location: Optional[str]  # Assuming 'location' could be a string or None
    country: str
    name: str

class Out_Internship(BaseModel):
    output: list[JobListing] = Field(description="list of internships")  

def search_datbase(query):
    response = questions.query.hybrid(
        query=query,
        limit=3
    )

    interns = []

    # adding internships to list
    for item in response.objects:
        interns.append(item.properties) 
    

    context = json.dumps(interns)
    return json.loads(context)




class Internship_finder(dspy.Module):
    lm = dspy.OpenAI(model='gpt-3.5-turbo', temperature=0.3)

    dspy.settings.configure(lm=lm, rm=weaviate_client)

    def __init__(self):
        super().__init__()
        self.generate_query = [dspy.ChainOfThought(generate_query) for _ in range(3)]
        self.generate_analysis = dspy.Predict(generate_analysis,max_tokens=4000) 

    def forward(self, resume):
        #resume to pass as context 
        
        passages = []

        for hop in range(3):
            query = self.generate_query[hop](context=str(resume)).query
            info=search_datbase(query)
            passages.append(info)

        context = deduplicate(passages)    
        context.append(resume)
        
            
        analysis = self.generate_analysis(resume=str(resume), context=context).output
              
        # """ engaging_question = "Is the Analysis correct check internships to find match with resume skills, experience, projects and education? reply with either yes or no"
        # engaging_assessment = dspy.Predict("context, assessed_text, assessment_question -> assessment_answer")(
        #         context=context, assessed_text=analysis, assessment_question=engaging_question)
        # msg = st.toast("Analysis Test  1 Completed")
        # dspy.Suggest(check_answer(engaging_assessment.assessment_answer), "Please revise to make it more captivating.")

        # check_question = "Is the output as desired ? reply with either yes or no"    
        # final_check = dspy.Predict("context, assessed_text, assessment_question -> assessment_answer")(
        #     context=context, assessed_text=analysis, assessment_question=check_question)
        #  """
        msg = st.toast("Final Check Completed")
        #dspy.Suggest(check_answer(final_check.assessment_answer), "The analysis is not good. Retry the function")
        return analysis

def deduplicate(context):
        """
        Removes duplicate elements from the context list while preserving the order.
        
        Parameters:
        context (list): List containing context elements.
        
        Returns:
        list: List with duplicates removed.
        """
        json_strings = [json.dumps(d, sort_keys=True) for d in context]
    
        # Use a set to remove duplicate JSON strings
        unique_json_strings = set(json_strings)
    
        # Convert JSON strings back to dictionaries
        unique_dicts = [json.loads(s) for s in unique_json_strings]
        return unique_dicts

def check_answer(assessment_answer):
    if assessment_answer == "no":
        return False
    return True

def get_resume():
    with open('resume.json', 'r') as file: 
        resume = json.load(file)
     
    return resume


class generate_analysis(dspy.Signature):
    """
    Act as a ATS Tool and Find Best internships from context for resume by analyzing resume and internship.
    output of list of internships in below format: 
    {
    "name": "",
    "company": "",
    "apply_link": "",
    "match_analysis": ""
    }
    """
    
    context = dspy.InputField(desc="Internships")
    resume = dspy.InputField(desc="resume")
    output = dspy.OutputField(desc="list of listings",type=list[JobListing])

class generate_query(dspy.Signature):
    """
    Generate query to search in the weaviate database hybrid search by following below rules:
    1. Analyze the resume, extract keywords from skills, education, experience, projects
    2. then use the keywords to generate query to search in the weaviate database
    3. query should be keyword based to find the best internships for the resume
    """

    context = dspy.InputField(desc="Resume")
    query = dspy.OutputField(desc="query in simple string format")


def main():
    
    st.title("Internship Finder")
        
    file = st.file_uploader("Upload Resume to get started", type=["pdf"])
    
    
    col_company, col_url, col_analysis = st.columns([2,6,2])

    

    if file is not None:
        msg = st.toast("Resume Uploaded")
        resume = resume_into_json(file)
        analysis = Internship_finder()
        generate_analysis = analysis(resume)
        
        msg.toast("Analysis Completed")
        interns = json.loads(generate_analysis)
        with col_company:
            st.subheader("Companies")
            for intern in interns:
                st.link_button(intern["company"], intern["apply_link"])
        
        with col_url:
            st.subheader("Internships")
            for intern in interns:
                st.link_button(intern["name"], intern["apply_link"])
        
        with col_analysis:
            st.subheader("Analysis")
            for intern in interns:
                with st.expander("More Details"):
                    st.write(intern["match_analysis"])

        if interns is None:
            msg.toast("No Internships Found")    
        msg.toast("Internships Found !!")
    


if __name__ == "__main__":
    main()
