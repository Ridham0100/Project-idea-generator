import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = ChatGroq(api_key=GROQ_API_KEY, model = 'openai/gpt-oss-20b', temperature=0.7)


def project_idea_generator(idea):
    prompt_template = PromptTemplate(
        input_variables=["idea"],
        template= "I want to make a GenAI project on {idea} . Suggest me one name for it."
    )



    name_chain = LLMChain(llm=client, prompt=prompt_template)
    

    prompt_template_items = PromptTemplate(
        input_variables=["text"],
        template="Give me 10 project ideas on {text} GenAI project."
    )

    items_chain = LLMChain(llm=client, prompt=prompt_template_items)
    

    pipeline = SimpleSequentialChain(chains=[name_chain, items_chain], verbose=True)
    result = pipeline.invoke({"input": idea})  # Changed from "idea" to "input"
    
    output = name_chain.run(idea=idea)
    menu_items = result['output']  # This contains the menu from second chain
    # Extract just the restaurant name by removing markdown and extra text
    return {
        'name': output,    # Clean restaurant name
        'items': menu_items    # Menu items
    }

