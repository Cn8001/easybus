import uvicorn
import os

def main():
    host = "0.0.0.0"
    port = 8080
    if os.environ.get("EASYBUS_HOST"):
        host = os.environ.get("EASYBUS_HOST")
    if os.environ.get("EASYBUS_PORT"):
        port = int(os.environ.get("EASYBUS_PORT"))
    
    uvicorn.run("easybus.controller:app", host=host, port=port, reload=True)

if __name__ == "__main__":
    main()