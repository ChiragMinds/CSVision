import pandas as pd
import tempfile

def load_csv(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        path = tmp.name
    return pd.read_csv(path)
