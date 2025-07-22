# PyResVol – Volumetric & Material‑Balance Reserves Estimator

🛢️ **PyResVol** is a Python-based tool designed for petroleum reservoir engineers to estimate hydrocarbon reserves using three core industry techniques:
- Volumetric Method
- Material Balance Equation (MBE)
- Decline Curve Analysis (DCA)

This project is meant to serve as a resume-level, real-world solution for petroleum engineering students and professionals.

---

## 📁 Project Structure

```
PyResVol/
│
├── data/
│   ├── sample_volumetric_data.csv
│   ├── mbe_input_data.csv
│   └── dca_production_data.csv
│
├── volumetric.py        # Contains OOIP calculation (Volumetric method)
├── mbe.py               # Material Balance model and plotting
├── dca.py               # Decline Curve Analysis models and plotting
├── main.py              # Executes the full pipeline: Volumetric → MBE → DCA
└── README.md            # This documentation
```

---

## 📊 Features

### ✅ Volumetric Estimation
Calculates Original Oil in Place (OOIP) using:
- Reservoir Area (acres)
- Thickness (ft)
- Porosity
- Water Saturation
- Formation Volume Factor (Bo)

### ✅ Material Balance Equation (MBE)
- Implements linear MBE formulation
- Estimates recoverable reserves by regression
- Plots F vs Eo trend for visual evaluation

### ✅ Decline Curve Analysis (DCA)
- Fits production data to:
  - Exponential decline
  - Harmonic decline
  - Hyperbolic decline
- Predicts future production trends
- Visualizes and prints model parameters

---

## 🚀 How to Run

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/PyResVol.git
cd PyResVol
```

### 2. Install Required Libraries

```bash
pip install numpy pandas matplotlib scipy
```

### 3. Run the Main Script

```bash
python main.py
```

This will:
- Print OOIP results for each reservoir
- Plot the MBE line
- Plot DCA curves (Exponential, Harmonic, Hyperbolic)

---

## 📂 Data Format

### `sample_volumetric_data.csv`

| area_acres | thickness_ft | porosity | water_saturation | Bo |
|------------|--------------|----------|------------------|----|
| 160        | 30           | 0.15     | 0.25             | 1.2 |

---

### `mbe_input_data.csv`

| F     | Eo    |
|-------|-------|
| 10000 | 5.5   |
| 20000 | 10.9  |
| ...   | ...   |

---

### `dca_production_data.csv`

| time_days | production_rate |
|-----------|-----------------|
| 0         | 1000            |
| 30        | 950             |
| ...       | ...             |

---

## 📌 Key Learnings

- Python implementation of core reservoir engineering principles
- Curve fitting with `scipy.optimize.curve_fit`
- Modular coding practices and clean plotting with Matplotlib
- End-to-end petroleum data science pipeline

---

## 📄 License

This project is for educational and portfolio purposes. For any commercial use, please seek proper approvals.

---

## 👨‍💻 Author

**Rudra Prasad Rath**  
B.Tech Petroleum Engineering, IIT (ISM) Dhanbad  
[LinkedIn](https://www.linkedin.com/in/rudra-prasad-rath-11b63b287/) | [GitHub](https://github.com/rudra03rath)
