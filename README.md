# azure-ai-translator

## Project Overview

This project demonstrates the use of Azure OpenAI services in a Python application. The `translator.py` script translates text using Azure's Cognitive Services, specifically leveraging the GPT model.

---

> ⚠ **Disclaimer**: This project uses Azure OpenAI services, which may incur costs. Please review Azure's pricing and terms to understand potential charges associated with the use of this service. ⚠

---

## Environment Setup

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/).

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Required Packages**:
    ```bash
    pip install os-sys
    pip install requests
    pip install beautifulsoup4
    pip install python-docx
    pip install python-dotenv
    ```

## Azure Setup

### Step 1: Create a Resource Group in Azure

1. Go to the [Azure Portal](https://portal.azure.com/).
2. In the left-hand menu, select **Resource groups**.
3. Click **Create**.
4. Enter the **Subscription** and **Resource group name** (e.g., `azure-ai-translator-rg`).
5. Choose a **Region** close to your target audience or application.
6. Click **Review + create**, then **Create**.

### Step 2: Create an Azure OpenAI Service

1. In the [Azure Portal](https://portal.azure.com/), go to **Create a resource**.
2. Search for **Azure OpenAI** and select **Azure OpenAI**.
3. Click **Create**.
4. Select the **Subscription** and **Resource group** created in the previous step.
5. Choose a **Region** and enter a **Name** for the service (e.g., `azure-openai-service`).
6. Review and create the service.

### Step 3: Deploy the GPT-4 Model

1. Go to the newly created Azure OpenAI resource.
2. In the left-hand menu, select **Deployments**.
3. Click **+ Create**.
4. Choose the **Model** (e.g., `gpt-4o-mini`) and give the **Deployment** a name (e.g., `gpt-4o-mini`).
5. Set any required configurations and limits as per your project needs.
6. Click **Create** to deploy the model.

### Step 4: Get the Endpoint and API Key

1. Go to the **Keys and Endpoint** section of your Azure OpenAI service.
2. Copy the **Endpoint URL** and **Key**.

## Project Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/frmpiccolo/azure-ai-translator.git
    cd azure-ai-translator
    ```

2. **Configure Environment Variables**:
    - Create a `.env` file in the root directory of the project.
    - Add the following content to the `.env` file, replacing `your_api_key` and `your_endpoint_url` with the endpoint and key obtained in the previous steps. Set `DEFAULT_TARGET_LANGUAGE` to the desired target language code:
    
    ```env
    AZURE_OPENAI_KEY=your_api_key
    AZURE_OPENAI_ENDPOINT=your_endpoint_url
    DEFAULT_TARGET_LANGUAGE=pt-br  # Set to your preferred target language (e.g., en for English, es for Spanish)    
    ```

## Running the Program

1. **Run the Script**:
    ```bash
    python translator.py
    ```

2. **Input Text**:
    - The program will prompt you to enter the text you want to translate.
    - Enter the text, and the script will send it to the Azure OpenAI service for translation.

## Program Information

The `translator.py` script performs the following tasks:

1. **Extracts Content from a Web Page**: Given a URL, the script fetches the page content and extracts all paragraphs.
2. **Translates Extracted Paragraphs**: Each paragraph obtained from the web page is translated to the target language specified by the user.
3. **Translates Microsoft Word Files**: The script can also translate a Microsoft Word (.docx) file to the target language.

This project demonstrates the integration of Azure OpenAI services into a Python application for web content extraction, document translation, and text processing.

---

> ⚠ **Disclaimer**: Using Azure OpenAI services may incur costs. Be sure to monitor usage and review pricing on the [Azure Portal](https://portal.azure.com/). ⚠
