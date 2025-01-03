from tabnanny import verbose
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables from .env file
load_dotenv()  

# Configure the genai library with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create an instance of the ChatGoogleGenerativeAI model with Gemini-Pro and temperature 0.3
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

def generate_answer(question: str, context: str) -> str:
    print("Generating answer...")  # Print a message to indicate answer generation

    # Define the prompt template
    prompt_template = """
    Answer the question as detailed as possible based on the provided context.
    If the answer is not found in the context, simply state "Answer not available in the context."
    Context: {context}
    Question: {question}
    Answer: """

    # Create a PromptTemplate instance with the template and input variables
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # Create an LLMChain instance with the language model, prompt, and verbose output
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    # Invoke the chain with the question and context as input
    response = chain.invoke(input={"question": question, "context": context})

    # Return the generated answer text
    return response["text"]