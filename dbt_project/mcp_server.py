from fastapi import FastAPI
import json
from pathlib import Path

# Paths to dbt artifacts
dbt_target = Path("C:/Users/AnuragSundar/Desktop/mcp_dbt_project/dbt_project/target")
manifest_path = dbt_target / "manifest.json"
catalog_path = dbt_target / "catalog.json"

# Load artifacts
with open(manifest_path) as f:
    manifest = json.load(f)

with open(catalog_path) as f:
    catalog = json.load(f)

app = FastAPI(title="MCP Demo Server")

# List all models
@app.get("/models")
def list_models():
    return list(manifest.get("nodes", {}).keys())

# Get columns for a model
@app.get("/columns/{model_name}")
def get_columns(model_name: str):
    node_key = f"model.dbt_project.{model_name}"
    if node_key in catalog["nodes"]:
        return list(catalog["nodes"][node_key]["columns"].keys())
    return {"error": "Model not found"}

# Demo metric
@app.get("/metrics/total_revenue")
def total_revenue():
    return {
        "name": "total_revenue",
        "sql": "SELECT SUM(amount) AS total_revenue FROM MCP_DATA.orders"
    }
