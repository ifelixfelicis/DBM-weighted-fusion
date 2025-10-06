# DBM-weighted-fusion

This repository contains Python scripts for weighted fusion of multi-source Digital Bathymetric Models (DBMs). It includes two core fusion methods: a two-DBM fusion approach and a six-DBM fusion approach, which are implemented in the `fusion/` directory.

---

## 📁 Repository Structure

```
DBM-weighted-fusion/
├── fusion/                    # Python scripts for DBM fusion
│   ├── 2_DBM_fusion.py        # Two-DBM fusion script
│   └── 6_DBM_fusion.py        # Six-DBM fusion script
├── data/                      # Directory for dataset descriptions (not data itself)
│   └── README_data.md         # Descriptions of DBM sources and access links
├── requirements.txt           # Python dependencies
├── LICENSE                    # CC0 1.0 License file
└── README.md                  # Project documentation (this file)
```

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
```

### 2. Run the script

```bash
# For two-DBM fusion
python fusion/2_DBM_fusion.py

# For six-DBM fusion
python fusion/6_DBM_fusion.py
```

> 🔧 **Note:** Modify the data paths in the scripts before running.

---

## 📄 Data Description

No raw DBM data are included in this repository because the data sources are third-party global DBM products. For descriptions and download links, please refer to [data/README_data.md](data/README_data.md).

---

## 📝 License

This dataset and code are licensed under the Creative Commons Zero v1.0 Universal (CC0 1.0) Public Domain Dedication.  
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.  

Full license text: [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 📬 Contact

For questions or collaborations, feel free to contact:  
📧 w15684143509@gmail.com
