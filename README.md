Gets the Bitcoin, Ethereum and Solana prices in GBP, USD and EUR from the CoinGecko API
and saves each one to its own CSV file.

### Requirements

- Python 3.10 or later
- An internet connection (the script calls the CoinGecko API)

### Setup

1. Open a terminal in the project folder.

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

   Or install them directly:

   ```bash
   pip install requests pandas pydantic
   ```

### Run

```bash
python main.py
```

This creates `bitcoin.csv`, `ethereum.csv` and `solana.csv` in the project folder.

It then reads the three files back into one pandas DataFrame and prints the highest and
lowest priced coin in GBP, plus the average GBP price.
