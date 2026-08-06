class BackgroundJob:

    total_jobs = 0 

    PENDING="PENDDING"
    RUNNING="RUNNING"
    COMPLETED="COMPLETED"
    FAILED="FAILED"

    def __init__(self,job_id:str, created_by:str):
        #instance level variables
        self.job_id = job_id
        self.created_by = created_by 

        self._status = self.PENDING
        self._retry_count = 0
        self._error_message = None

        BackgroundJob.total_jobs+=1 # class level variables shared acroos all instances 