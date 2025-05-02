from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from urllib.parse import quote_plus
from langchain_google_genai import ChatGoogleGenerativeAI
from sqlalchemy import create_engine
import os

from few_shots import few_shots



# Database connection details
def get_few_shot_db_chain():

    os.environ["GOOGLE_API_KEY"] = "AIzaSyDs_WSLm63v1DdK-KotL-wBZfWMTQ9E4DQ"

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.5)

    db_user = "akash"
    db_password = "akash@123"
    server_name = "DESKTOP-46UHGHJ\\SQLEXPRESS"
    db_name = "Apollo_Pharmacy"
    db_driver = "ODBC Driver 17 for SQL Server"

    # Encode password and driver
    encoded_password = quote_plus(db_password)
    connection_string = (
        f"mssql+pyodbc://{db_user}:{encoded_password}@{server_name}/{db_name}"
        f"?driver={quote_plus(db_driver)}"
    )

    engine = create_engine(connection_string)

    # 🔥 Custom SQLDatabase with safe runner
    from langchain_community.utilities.sql_database import SQLDatabase as BaseSQLDatabase

    class SafeSQLDatabase(BaseSQLDatabase):
        def run(self, command, fetch="all", include_columns=True, parameters=None, execution_options=None):
            if isinstance(command, str):
                command = command.replace("```sql", "").replace("```", "").strip()
            return super().run(command, fetch=fetch, include_columns=include_columns, parameters=parameters, execution_options=execution_options)

    # Now use the SafeSQLDatabase
    db = SafeSQLDatabase(engine)

    # Chain setup
    from langchain_experimental.sql.base import SQLDatabaseChain

    # Define SafeSQLDatabaseChain as a subclass of SQLDatabaseChain
    class SafeSQLDatabaseChain(SQLDatabaseChain):
        @property
        def output_keys(self):
            return ["result"]

        def _call(self, inputs, run_manager=None):
            # Override to ensure SQL query is printed
            result = super()._call(inputs, run_manager)
            # Only return the result key to make run() work
            if isinstance(result, dict) and "result" in result:
                return {"result": result["result"]}
            return result

    db_chain = SafeSQLDatabaseChain.from_llm(
        llm,
        db,
        verbose=True,
        return_direct=True  # <<<<--- THIS is what was missing
    )


    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join([str(v) if not isinstance(v, str) else v for v in example.values()]) for example in few_shots]
    for shot in few_shots:
        if isinstance(shot['Answer'], list):
            shot['Answer'] = str(shot['Answer'])
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore,k=2,)

    mssql_prompt = """You are a Microsoft SQL Server expert. Given an input question, first create a syntactically correct Microsoft SQL Server query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP clause as per Microsoft SQL Server. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in square brackets ([]) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use GETDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """
    from langchain.prompts import PromptTemplate, FewShotPromptTemplate

    # Define the example prompt template
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="Question: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )

    # Define the few-shot prompt template
    few_shot_prompt = FewShotPromptTemplate(
        examples=few_shots,
        example_prompt=example_prompt,
        prefix=mssql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
        example_separator="\n\n"
    )
    # Define a custom output parser for the chain
    class CustomSQLDatabaseChain(SQLDatabaseChain):
        @property
        def output_keys(self):
            return ["result"]

        def _call(self, inputs, run_manager=None):
            result = super()._call(inputs, run_manager)
            # Only return the result key to make run() work
            if isinstance(result, dict) and "result" in result:
                return {"result": result["result"]}
            return result

    new_chain = CustomSQLDatabaseChain.from_llm(
        llm,
        db,
        verbose=True,
        prompt=few_shot_prompt,
        return_direct=True,
        use_query_checker=False
    )
    return new_chain