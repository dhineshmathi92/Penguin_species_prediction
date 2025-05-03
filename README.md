# Penguin Species Prediction

A web application to predict the species of a penguin based on user-provided biological measurements. The project leverages a machine learning model for prediction and offers an intuitive and visually appealing UI built with Streamlit.

## Features

* User-friendly interface for entering penguin attributes.
* Dropdown menus for categorical data (`island`, `sex`) and numerical inputs for measurements.
* Predicts the species of a penguin based on provided data.
* Real-time communication between the frontend and backend.

---

## Tech Stack

### Frontend:

* **Streamlit**: For building the web interface with a focus on simplicity and aesthetics.

### Backend:

* **Flask**: For handling API requests and serving predictions.
* **Python**: Core programming language used to integrate various libraries and frameworks.

### Machine Learning:

* A pre-trained model used for predicting penguin species (can be extended to train your own model).

---

## How It Works

1. **Input Fields**:

   * Select the island from a dropdown (`Biscoe`, `Torgersen`, `Dream`).
   * Input numerical values for `Bill Length`, `Bill Depth`, `Flipper Length`, and `Body Mass`.
   * Select the penguin's sex from a dropdown (`Male`, `Female`).

2. **Submit the Data**:

   * Click the "Submit" button to send the input to the backend.

3. **Prediction**:

   * The backend processes the input and returns the predicted penguin species, displayed in the UI.

---

## Setup Instructions

### Prerequisites

* Python 3.7+
* Pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/penguin-species-prediction.git
   cd penguin-species-prediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the backend server:

   ```bash
   python backend.py
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser:

   * Go to `http://localhost:8501` (Streamlit default URL).

---

## Example Input

| Field               | Example Value |
| ------------------- | ------------- |
| Island              | `Biscoe`      |
| Bill Length (mm)    | `45.5`        |
| Bill Depth (mm)     | `15.3`        |
| Flipper Length (mm) | `200`         |
| Body Mass (g)       | `4500`        |
| Sex                 | `Male`        |

### Example Output

```
Predicted Penguin Species: Chinstrap
```

---

## Future Enhancements

* Add additional penguin attributes for prediction.
* Integrate more machine learning models.
* Host the application on a cloud platform like AWS, Azure, or Heroku.
* Implement logging and monitoring for backend requests.

---

