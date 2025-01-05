# Contract Generator Web Application

## Description

This project is a web application that allows users to input details for a contract, generate a professionally formatted contract using a chatbot API, and download the result as a `.docx` or `.pdf` file. The application is built to streamline contract creation by providing pre-defined input fields for various sections such as customer name, project scope, payment terms, risks, and legal considerations. Once the information is submitted, the chatbot API processes it into a well-structured contract.

Users can interact with the application via a browser-based interface or a standalone GUI application created with PySide6.

---

## Tech Stack

- **Frontend**: HTML, CSS (minimal for layout)
- **Backend**: Flask (Python)
- **AI Integration**: OpenAI GPT-based API with LangChain
- **Document Generation**: Python libraries: `python-docx` for `.docx` files and `reportlab` for `.pdf` files
- **GUI**: PySide6 for the standalone desktop version

---

## Features

1. **User Input Interface**:
   - Web form for entering contract details (customer name, project scope, deliverables, timelines, etc.).
   - Standalone GUI application for desktop users.

2. **AI-Powered Contract Generation**:
   - Integrates with an AI chatbot API to generate contracts based on user-provided details.

3. **Document Export**:
   - Save the generated contract as `.docx` or `.pdf` formats.

4. **Dynamic and Extendable Design**:
   - Easily adaptable to include additional sections or contract formats.

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Required Python libraries (install using `pip`):
  ```bash
  pip install flask python-docx reportlab langchain llama-index PySide6 python-dotenv
  ```

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     API_Key=your_openai_api_key
     ```

3. **Set Up Data**:
   - Place documents to train the vector store in a directory named `data`.

4. **Run the Web Application**:
   ```bash
   python web.py
   ```
   Access the application at `http://127.0.0.1:5000/`.

5. **Run the GUI Application**:
   ```bash
   python interface.py
   ```

---

## Challenges

The most challenging aspect of this project was integrating the AI chatbot API with the document generation pipeline while maintaining the professional formatting required for contracts. Overcoming this required extensive fine-tuning of prompts and testing different document libraries to ensure the output met the desired standards.

---

## How It Works

1. **Input Data**:
   - Users fill out a form specifying all the details for the contract.

2. **AI Processing**:
   - The backend uses a combination of LangChain and LlamaIndex to query the OpenAI GPT model for contract generation.

3. **Document Generation**:
   - The response is formatted and saved as `.docx` or `.pdf`.

4. **Result**:
   - Users can download the generated contract directly from the web interface or desktop application.

---

## Future Improvements

- Add user authentication and contract history.
- Enhance the interface with better design and UX features.
- Support additional languages for contract generation.
- Allow customization of contract templates.
