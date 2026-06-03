# Student Performance Predictor

An end-to-end Machine Learning application and web simulator that forecasts student final exam scores based on key academic indicators: **Attendance**, **Previous Assessment Marks**, and **Daily Study Hours**.

The application features a machine learning training pipeline alongside an interactive, premium glassmorphic web dashboard that supports dynamic transitions, hardware-accelerated score counters, benchmark comparisons, and model evaluation charts.

---

## 🎨 Web Dashboard Features

The web frontend has been redesigned into a responsive, simulator-style single-page experience:
- **Futuristic Glassmorphic Theme**: Sleek, frosted-glass container styling featuring vibrant neon purple and cyan gradients overlaid on an academic workspace backdrop.
- **Single-Page Panel Transitions**: Smoothly shifts between input sliders and analytics results without full page reloads.
- **60FPS Score Counter**: Animates the predicted exam score from `0.00` to the output value over `1.2s` using a hardware-accelerated ease-out cubic animation.
- **Personalized Academic Benchmarks**: Visual progress meters that compare the student's entered inputs against standard targets:
  - *Attendance*: User % vs. **90%** Recommended target.
  - *Previous Marks*: User score vs. **80/100** Standard target.
  - *Study Hours*: User hours/day vs. **8 hrs/day** Study target.
- **Interactive Model Validation Tabs**: Toggle between correlation heatmaps and scatter plots directly within a tabbed glass card container.
- **Full-Screen Loading Overlay**: Displays a sleek computation screen while the backend calculates predictions.
- **Responsive Layout**: Designed using CSS Flexbox and Grid, fully optimized for both desktop and mobile devices.

---

## 📂 Project Structure

```text
StudentPerformancePredictor/
│
├── app.py                     # Main Flask web application entrypoint
├── main.py                    # Runs training, generates graphs, and logs evaluation metrics
├── requirements.txt           # Python library dependencies
├── student_model.pkl          # Serialized, trained scikit-learn model file
│
├── src/                       # Core python model pipeline modules
│   ├── data_preprocessing.py  # Loads and cleans the dataset
│   ├── train_model.py         # Trains the machine learning model
│   ├── evaluate_model.py      # Evaluates performance metrics (R², MSE, MAE)
│   └── predict.py             # Computes predictions using student_model.pkl
│
├── data/                      # Data storage
│   └── students.csv           # Student training and evaluation dataset
│
├── images/                    # Output folder for main pipeline charts
│   ├── heatmap.png            # Correlation Heatmap plot
│   └── scatter_plot.png       # Study Hours vs. Exam Score Scatter plot
│
├── templates/                 # Jinja HTML templates
│   └── index.html             # Redesigned dashboard layout and client scripts
│
└── static/                    # Frontend style and static assets
    ├── style.css              # Custom variables, transitions, animations, and styling rules
    ├── academic_bg.png        # Blended high-quality tech backdrop image
    ├── heatmap.png            # Copied graph file for front-end tab rendering
    └── scatter_plot.png       # Copied graph file for front-end tab rendering
```

---

## ⚙️ Getting Started & Installation

### 1. Set Up Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate
```

### 2. Install Dependencies
Install all required libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Run the Machine Learning Pipeline (Optional)
Run the pipeline to preprocess data, generate validation plots in `images/`, train the model, serialize `student_model.pkl`, and log testing predictions:
```bash
python main.py
```

### 4. Launch the Web UI
Launch the local web server:
```bash
python app.py
```

Once running, open your web browser and navigate to:
```text
http://127.0.0.1:5000/
```
