# 🏥 Apollo Pharmacy Database Chat 👨🏼‍⚕️

Welcome to the Apollo Pharmacy Database Chat project! This interactive Streamlit application allows users to query a pharmacy database using natural language. Powered by LangChain and Google's Generative AI, it translates your questions into SQL queries and retrieves the answers from the database. No SQL knowledge required! 🚀

## 🌟 Features

- **Natural Language Queries:** Ask questions in plain English, and the app will handle the SQL for you.
- **Few-Shot Learning:** Uses predefined examples to guide the language model in generating accurate SQL queries.
- **Semantic Similarity Search:** Selects the most relevant examples using embeddings and a vector store.
- **Interactive Interface:** Built with Streamlit for an easy and intuitive user experience.
- **SQL Query Display:** Shows the generated SQL query along with the query results.

## 🛠️ Technologies Used

- **LangChain:** Framework for building applications with large language models.
- **Google Generative AI:** Provides the language model (`gemini-1.5-pro-latest`) for generating SQL queries.
- **HuggingFace Embeddings:** For creating vector representations of text.
- **Chroma Vector Store:** For storing and searching vector embeddings.
- **SQLAlchemy & pyodbc:** For database connection and querying.
- **Streamlit:** For building the web interface.

## 🚀 Setup and Installation

### Clone the Repository:
```bash
git clone https://github.com/yourusername/apollo-pharmacy-chat.git
cd apollo-pharmacy-chat
```
### Install Dependencies:

```
pip install -r requirements.txt
```
### Set Up Environment Variables:

1. Create a `.env` file in the root directory.

2. Add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```
### Database Configuration:

- Ensure you have a Microsoft SQL Server database set up with the name `Apollo_Pharmacy`.

- Update the database connection details in `Apollo_1`.py if necessary.

# Run the Application:
```
streamlit run main.py
```
### 🎯 Usage
1. **Open the Application:** Navigate to http://localhost:8501 in your browser.

2. **Ask a Question:** Enter a question about the pharmacy database, such as `"How many medicines do we have left for Paracetamol?"`

3. **View Results:** The application will display the generated SQL query and the query results in a formatted table.

### 📝 Example Queries

* "How many medicines do we have left for Paracetamol"

* "List all medicines with stock less than 100 units"

* "Find medicines priced above ₹3"

* "Show medicines that are expired"

* "List medicine names with their discount percentage"

* "Count how many medicines are manufactured by each manufacturer"
