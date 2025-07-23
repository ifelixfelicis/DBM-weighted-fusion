# DBM-weighted-fusion

This repository contains Python scripts for weighted fusion of multi-source Digital Bathymetric Models (DBMs). It includes two core fusion methods: a two-DBM fusion approach and a six-DBM fusion approach, which are implemented in the `fusion/` directory.

---

## 📁 Repository Structure
DBM-weighted-fusion/
├── fusion/
│ ├── 2_DBM_fusion.py # Two-DBM fusion script
│ └── 6_DBM_fusion.py # Six-DBM fusion script
├── data/
│ └── README_data.md # Description of DBM sources (not data itself)
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # Project introduction

---

## 🧠 Description

This code implements weighted fusion strategies for DBM accuracy enhancement in shallow-water areas. Six widely-used global DBMs were used as sources, and fusion weights were optimized using statistical metrics such as RMSE and correlation.

The six DBMs include:
- ETOPO 2022 (15″ and 30″)
- TOPO V25.1
- SRTM30_PLUS V11.0
- SRTM15_PLUS V2.6
- GEBCO_2024

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt

### 2. Run the script

# For two-DBM fusion
python fusion/2_DBM_fusion.py

# For six-DBM fusion
python fusion/6_DBM_fusion.py

Note: Modify the data paths in the script before running.

📄 Data Description
No raw DBM data are provided in this repository due to third-party data source policies. For descriptions and download links of the six DBMs used in the fusion experiments, please refer to data/README_data.md.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For questions or collaborations, feel free to contact:
📧 w15684143509@gmail.com
