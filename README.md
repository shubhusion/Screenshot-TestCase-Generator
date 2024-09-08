# Screenshot Test Case Generator

This project uses a multimodal LLM to generate test cases based on screenshots of digital product features.

## Setup

### Backend

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

The backend server will start running on `http://localhost:5000`.

### Frontend

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

The frontend application will start running on `http://localhost:3000`.

## Usage

1. Open your web browser and go to `http://localhost:3000`.
2. (Optional) Enter any context information in the text box.
3. Upload screenshots of the digital product features you want to test.
4. Click the "Describe Testing Instructions" button.
5. The generated test cases will be displayed on the page.

## Note

This is a prototype implementation. The current version uses a simple image captioning model as a placeholder for the multimodal LLM. In a production environment, you would replace this with a more sophisticated model trained specifically for generating test cases from screenshots.
