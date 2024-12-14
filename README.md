
# Expert Agent Backend (FastAPI)

This repository contains the backend for the **Expert Agent Chat Bot**, implemented using Python FastAPI and the Google Gemini API. The backend processes user prompts, engages sub-agents based on specific fields and prompt titles, and delivers expert-level responses.

## Features
- **Prompt Handling**: Accepts user prompts and processes them dynamically.
- **Sub-Agent Communication**: Routes queries to relevant sub-agents based on the prompt field and title for domain-specific expertise.
- **AI-Powered Responses**: Leverages the Google Gemini API for generating responses.
- **FastAPI Framework**: Ensures a lightweight, high-performance backend.

## Installation

### Prerequisites

- Python 3.10 or higher: [Download here](https://www.python.org/downloads/)
- Virtual Environment (recommended): Ensure `venv` is installed.

### Steps

1. Clone the repository:
   ```bash
   git clone <backend-repo-url>
   cd <backend-repo-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and define the following variables:
   ```env
   GOOGLE_GEMINI_API_KEY=<your_google_gemini_api_key>
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API at `http://127.0.0.1:8090`.



### Sub-Agent Communication

- Dynamically engages sub-agents to handle domain-specific queries. The backend routes queries to the appropriate sub-agent based on the field and title of the prompt.


## Testing

1. Install testing dependencies:
   ```bash
   pip install pytest
   ```

2. Run tests:
   ```bash
   pytest
   ```

## Future Enhancements

- Add caching for frequently accessed responses.
- Integrate advanced sub-agent selection algorithms.
- Enhance user activity logging and analytics.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m "Add feature-name"`.
4. Push to your branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Thank you for using the **Expert Agent Backend**!

