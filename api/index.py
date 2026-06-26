import subprocess

def handler(event, context):
    # Inicia o Streamlit como um subprocesso
    # Certifique-se de que 'app.py' está no mesmo diretório ou no PATH
    subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--server.headless", "true"])

    # Retorna uma resposta HTTP simples para o Vercel
    return {
        'statusCode': 200,
        'body': 'Streamlit app is starting...'
    }