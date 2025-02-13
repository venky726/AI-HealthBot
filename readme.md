# AI HealthCare Assistant

This project is an AI-powered healthcare assistant built using Streamlit and Google's Generative AI. The assistant provides concise and accurate medical information based on user queries.

## Project Structure

- `new/.env`: Contains environment variables, including the Google API key.
- `new/bot.py`: The main application script.
- `requirements.txt`: Lists the dependencies required for the project.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the `new` directory.
3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/2) file in the [new](http://_vscodecontentref_/3) directory with your Google API key:

    ```env
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

## Running the Application

To run the application, execute the following command in the [new](http://_vscodecontentref_/4) directory:

```sh
streamlit run bot.py
```
