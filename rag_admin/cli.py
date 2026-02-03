import json
import typer

from rag_core.config import load_yaml, build_admin_pipeline
from rag_core.policy import (
    LOADER_POLICY,
    EMBEDDER_POLICY,
    STORE_WRITE_POLICY,
    validate_caps,
)
from rag_core.pipeline import index_all

app = typer.Typer(add_completion=False)

@app.command()
def sync(config: str, json_out: bool = False):
    cfg = load_yaml(config)
    loader, chunker, embedder, store = build_admin_pipeline(cfg)

    # Validate per-component capabilities (admin pipeline)
    validate_caps(loader, LOADER_POLICY, "loader")
    validate_caps(embedder, EMBEDDER_POLICY, "embedder")
    validate_caps(store, STORE_WRITE_POLICY, "store")

    out = index_all(loader, chunker, embedder, store)
    if json_out:
        typer.echo(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        typer.echo(f"Indexed docs={out['docs']} chunks={out['chunks']} dim={out['dim']}")

if __name__ == "__main__":
    app()
