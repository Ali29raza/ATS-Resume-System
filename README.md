# ATS Resume Expert

**ATS Resume Expert** is a web application designed to help HR professionals by analyzing resumes and comparing them to job descriptions for technical roles such as Data Scientist, Machine Learning Engineer, Software Developer, and DevOps Engineer. This app uses Google Generative AI (Gemini) to provide resume analysis, match percentage calculations, and extraction of contact details.

## Features

- **Resume Analysis**: Compares the resume with the job description, identifying matching skills, qualifications, and experiences.
- **Resume Match Percentage**: Calculates the percentage of how well the resume aligns with the job description and provides specific feedback based on skills and qualifications.
- **Contact Details Extraction**: Extracts essential contact information (full name, phone number, email address, LinkedIn profile) from the uploaded resume.

## How It Works

1. **Input**: 
   - HR professionals provide a job description and upload a resume in PDF format.
   
2. **AI-Powered Analysis**: 
   - The app uses Google Generative AI to process the resume and job description, performing three key functions:
     - Analyzing how well the resume matches the job description.
     - Calculating a match percentage to determine resume fit.
     - Extracting contact details from the resume.

3. **Output**: 
   - The app displays AI-generated results, including resume analysis, match percentage, or extracted contact information, depending on the selected action.

## Model Details

This application uses **Google's Gemini Model (gemini-1.5-flash)** to power the resume analysis and matching process. The **Generative AI Model** is configured using the provided API key, and it helps perform the following tasks:

- **Content Generation**: Generates text responses based on the provided resume and job description.
- **Comparative Analysis**: Compares job descriptions and resumes to identify key matching and missing elements.
- **Contact Extraction**: Automatically identifies and extracts contact details such as the candidate’s name, email, phone number, and LinkedIn profile.

The model is particularly useful for HR professionals managing large-scale resume screenings by automating time-consuming tasks such as assessing resume fit for specific technical roles.

## Application Flow

1. Input the job description into the provided text area.
2. Upload the resume (in PDF format).
3. Select one of the following actions:
   - Analyze the resume against the job description.
   - Calculate the resume match percentage.
   - Extract contact details from the resume.
   
4. View the results based on the selected action.

## Key Benefits

- **Tailored for Technical Roles**: Focuses on roles like Data Scientist, Machine Learning Engineer, Software Developer, and DevOps Engineer.
- **Optimized for ATS**: Helps HR professionals refine resumes to better match job descriptions for improved performance in Applicant Tracking Systems (ATS).
- **Automatic Contact Extraction**: Extracts critical contact details (name, phone number, email, LinkedIn) directly from the resume.

## License

This project is licensed under the MIT License.
