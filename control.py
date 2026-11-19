class ProcessControl:

    def start(self, job_name):
        print(f"Iniciando {job_name}")
        return 123

    def success(self, execution_id):
        print(f"Sucesso {execution_id}")

    def error(self, execution_id, error):
        print(f"Erro {execution_id}: {error}")