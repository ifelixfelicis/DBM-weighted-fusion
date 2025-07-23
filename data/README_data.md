# Data Folder Information

This folder does **not** contain any raw Digital Bathymetric Model (DBM) data, as the input datasets are sourced from third-party global DBM products.  
All data used in the fusion experiments are publicly available and can be downloaded from the official sources listed below.

## Expected Input Format

To run the provided fusion scripts, you need a `.csv` file containing the following columns:

- `MSL` — Mean Sea Level (reference or ground truth value)
- `etopo15` — ETOPO 2022 (15″)
- `etopo30` — ETOPO 2022 (30″, resampled to 15″)
- `topo_25_1` — TOPO V25.1 (1′, resampled to 15″)
- `srtm30_v11` — SRTM30_PLUS V11.0 (30″, resampled to 15″)
- `srtm15` — SRTM15_PLUS V2.6 (15″)
- `g24` — GEBCO_2024 (15″)

## How to Get the Data

You may:
- Use your own bathymetric/topographic data formatted to match the structure above
- Download global DEM/DBM products (e.g., ETOPO2022, SRTM, GEBCO) from their respective official sources
- Contact the authors if you wish to obtain compatible input samples for academic use
