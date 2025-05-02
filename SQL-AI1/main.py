import streamlit as st
from Apollo_1 import get_few_shot_db_chain
import re

st.title("Chat with Apollo Pharmacy Database 👨🏼‍⚕️")

question = st.text_input("Question: ")

if question:
    try:
        chain = get_few_shot_db_chain()

        # Capture the output to extract the SQL query
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            # Now we can use run() since we fixed the chain to have only one output key
            response = chain.run(question)

        # Get the captured output
        output = f.getvalue()

        # Extract SQL query using regex
        sql_match = re.search(r'SQLQuery:(.*?)SQLResult:', output, re.DOTALL)
        if sql_match:
            sql_query = sql_match.group(1).strip()
            # Clean up the SQL query (remove markdown formatting and ANSI color codes)
            sql_query = re.sub(r'```sql|```', '', sql_query).strip()
            # Remove ANSI color codes
            sql_query = re.sub(r'\x1B\[[0-9;]*[mK]', '', sql_query)
            # Also try to remove color codes in the format [32;1m[1;3m and [0m
            sql_query = re.sub(r'\[\d+(?:;\d+)*m', '', sql_query)

            # Display the SQL query
            st.header("SQL Query")
            # Use st.write with a plain string to avoid any syntax highlighting
            st.write(sql_query)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        response = None

    st.header("Answer")
    if isinstance(response, list) and len(response) > 0 and isinstance(response[0], dict):
        # Extract column names from the first dictionary
        columns = list(response[0].keys())
        # Extract data rows
        data = [list(row.values()) for row in response]

        # Calculate the maximum width for each column
        col_widths = []
        for i, col in enumerate(columns):
            # Find the longest value in this column, including the column name
            max_width = max(len(str(col)), max(len(str(row[i])) for row in data))
            col_widths.append(max_width)

        # Format the header
        header = "    ".join([f"{col:<{col_widths[i]}}" for i, col in enumerate(columns)])

        # Format each row
        rows = ["    ".join([f"{str(value):<{col_widths[i]}}" for i, value in enumerate(row)]) for row in data]

        # Display the table
        st.write(header)
        for row in rows:
            st.write(row)
    else:
        # Fallback for unexpected response types
        st.write(response)