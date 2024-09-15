from secret_key import API_TOKEN, REPO_ID
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import SequentialChain, LLMChain



def generate_name_and_items(selected_cusine):
    """This method invokes the LLMChain to generate a restaurant name and items> Pass the cuisine as input to the chain."""

    # Create an endpoint for the Hugging Face model
    llm = HuggingFaceEndpoint(
        repo_id=REPO_ID,
        max_length=128,
        temperature=0.5,
        huggingfacehub_api_token=API_TOKEN,
    )

    # Create a template for the LLMChain to generate a fancy restaurant name
    name_template = PromptTemplate(
        input_variables=["selected_cusine"],
        template="""Generate one fancy restaurant name for {selected_cusine} cuisine. Only return the name. Do not include explanations, descriptions, or any additional context.""",
    )
    name_chain = LLMChain(llm = llm, prompt = name_template, output_key = "restaurant_name")

    # Create a template for the LLMChain to generate a fancy menu item
    menu_item_template = PromptTemplate(
        input_variables=["selected_cusine"],
        template="""Generate 5 fancy menu items for {selected_cusine} cuisine in a clean JSON format.
    Each item should have a 'name' and 'description' field only. Do not include extra text, headings, or additional information beyond the JSON structure.""",
    )
    menu_chain = LLMChain(llm = llm, prompt = menu_item_template, output_key = "menu_items")

    # Create a SequentialChain to generate a restaurant name and menu item
    sequential_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["selected_cusine"],
        output_variables=["restaurant_name", "menu_items"],
    )
    response = sequential_chain.invoke({"selected_cusine":selected_cusine})
    return response


if __name__ == "__main__":
    print(generate_name_and_items("Italian"))