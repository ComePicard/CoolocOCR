import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        reload_dirs=["app"],  # surveille les changements dans le dossier app/
        log_level="info"
    )
