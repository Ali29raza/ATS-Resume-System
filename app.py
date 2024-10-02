from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os 
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64
import PyPDF2


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# setting genai model
def get_gemini_response(input , pdf_text , prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input , pdf_text , prompt])
    return response.text

# getting input from pdf file
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:   
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
   


        # convert image to pdf
        #images = pdf2image.convert_from_bytes(uploaded_file.read())
        #first_page = images[0]

        # convert to bytes
        #image_byte_arr = io.BytesIO()
        #first_page.save(image_byte_arr , format="JPEG")
        #image_byte_arr = image_byte_arr.getvalue()

        #pdf_parts = [
          #  {
          #      "mime_type":"image/jpeg",
           #     "data":base64.b64decode(image_byte_arr)
           # }
        #]
        #return pdf_parts
        
    else:
        raise FileNotFoundError("No file uploaded")
    
## streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# job description input
input_text = st.text_area("Job Description: " , key="input")

# resume uploading option
uploaded_file = st.file_uploader("Upload your resume(PDF)..." , type=["pdf"])

# setting conditions
if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell Me About The Resume")
prompt_1 = """
You are an AI specialized in analyzing resumes for technical roles such as Data Scientist, 
Machine Learning Engineer, Software Developer, and DevOps Engineer. Your task is to compare a resume 
with a job description for one of these roles. Evaluate how well the resume fits the job requirements 
by identifying matching skills, qualifications, and experiences. Additionally, highlight any missing 
or underrepresented skills, certifications, or qualifications that could enhance the resume's alignment
with the job description for better ATS optimization."""
submit2 = st.button("Resume Match Percentage")

prompt_2 = """
You are an AI specialized in comparing resumes with job descriptions for technical roles 
like Data Scientist, Machine Learning Engineer, Software Developer, or DevOps Engineer. Your task is to 
calculate the matching percentage between the provided resume and job description. Based on the comparison,
 explain whether the candidate is a strong fit for the role or not, and provide specific reasons for your 
 assessment, focusing on relevant skills, experience, and qualifications. Do not offer suggestions for improvement.

"""
submit3 = st.button("Contact Details")

prompt_3 = """
You are an AI trained to extract contact details from resumes. Your task is to analyze the provided 
resume and extract the following contact information: full name, phone number, email address, and 
LinkedIn profile (if available). Ensure that all details are accurately identified and presented clearly
"""

if submit1:
    if uploaded_file is not None:
        # getting pdf content
        pdf_content = input_pdf_setup(uploaded_file)
        # getting response from genai
        response = get_gemini_response(prompt_1 , pdf_content, input_text ) # input_text = job description
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload a file")

elif submit2:
    if uploaded_file is not None:
        # getting pdf content
        pdf_content = input_pdf_setup(uploaded_file)
        # getting response from genai
        response = get_gemini_response(prompt_2 , pdf_content, input_text ) # input_text = job description
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload a file")

elif submit3:
    if uploaded_file is not None:
        # getting pdf content
        pdf_content = input_pdf_setup(uploaded_file)
        # getting response from genai
        response = get_gemini_response(prompt_3 , pdf_content, input_text ) # input_text = job description
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload a file")
